# Scrapping puls

This project contains the code for scrapping the well known bulgarian medical website - www.puls.bg.
The purpose of this project is scrape illness and anatomy articles in bulgarian language so we can expand our dataset.
With the data we are going to train a model in NLP Machine Learning tasks.

Pages that were scrapped are:

* Illnesses section - https://www.puls.bg/illnes/a-z/
* Anatomy section - https://www.puls.bg/illnes/anatomy/

## To run the code:

1. Trigger the scrapper:
    ```
    >>> scrapy runspider puls_spider.py -o puls_spider_results.json
    ```
2. Process the data from the spider
    ```
    >>> python process_spider_result.py --input_file "puls_spider_results.json"\
    OUTPUT: "processed_puls_spider_results.json"
    ```

ENJOY!