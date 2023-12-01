import scrapy
import csv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class spider_one(scrapy.Spider):
## First Read through our dataset and select the url's
    name = 'tres'
    def start_requests(self):
        csv_file_path = 'datasets/phishing_dataset.csv'
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                url = row[0]
                yield scrapy.Request(url=url, callback=self.parse)

## Scrape the URL IP address
    def parse(self, response):
        ip_address = response.json().get('origin')
        return ip_address


def run_spider_three(self):
    process = CrawlerProcess(get_project_settings())
    process.crawl(self)
    process.start()