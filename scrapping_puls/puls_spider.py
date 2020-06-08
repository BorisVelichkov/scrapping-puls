import scrapy
from bs4 import BeautifulSoup

class PulsSpider(scrapy.Spider):
    name = 'puls_spider'
    start_urls = (['https://www.puls.bg/illnes/anatomy/'] +
                  ['https://www.puls.bg/illnes/a-z/letter_{}.html'.format(index) for index in range(28)])

    def parse(self, response):
        data = {}
        articles = response.css('ul.list_green_backgound')
        for article in articles:
            data['title'] = article.css('a::attr(title)').getall()
            urls = article.css('a::attr(href)').getall()
            for url in urls:
                if 'cat' not in url:
                    # processing category in the anatomy page
                    yield response.follow(url, self.parse_article)
                else:
                    yield response.follow(url, self.parse)

    def parse_article(self, response):
        item = {}

        item['title'] = response.css("h1.title-h1::text").get()
        item['author'] = response.css("div.issue_author a::text").get('').strip()
        item['url'] = response.url

        item['published'] = response.css("time.time::text").getall()[0]
        item['last_edited'] = response.css("time.time::text").getall()[1]
        item['number_of_read'] = response.css("div.cell.small-12.medium-6.article-subtitle b::text").getall()[-1]

        article_text = BeautifulSoup(response.css("div.article-text").extract()[0], 'lxml').text
        item['article_text'] = [article_text.replace('\xa0', '').strip('\n')]

        yield item

        next_page = response.css('li.arrow.next a::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(next_page, self.parse_article)

"""
Example how to run the script:
>>> scrapy runspider quotes_spider.py -o quotes.json

Another way to test is like:
>>> scrapy crawl puls_spider

Open interactive shell:
>>> scrapy shell "https://www.puls.bg/illnes/issue_499/part_1.html" --nolog
"""
