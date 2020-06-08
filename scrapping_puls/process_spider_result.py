import argparse
import json
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(("PostProcess the result from 'puls_spider'. "
                                      "It will save the result with the prexis 'processed_' + input_file name"))
    parser.add_argument('--input_file', '-i', help='Absolute path to result JSON file from the spider')

    args = parser.parse_args()

    print("INPUT:", args.input_file)
    with open(args.input_file, 'r') as f:
        data = json.load(f)

    first_urls = [el for el in data if el['url'].endswith('/')]

    for record in data:
        for uniq in first_urls:
            if uniq['url'] in record['url'] and uniq['url'] != record['url']:
                uniq['article_text'].extend(record['article_text'])

    dirname, basename = os.path.split(args.input_file)
    output_file = os.path.join(dirname, 'processed_' + basename)
    with open(output_file, 'w') as f:
        json.dump(first_urls, f, ensure_ascii=False)


"""
Example Usage:
>>> python post_process_spider_result.py --input_file "puls_spider.json"
OUTPUT: "processed_puls_spider.json"
"""
