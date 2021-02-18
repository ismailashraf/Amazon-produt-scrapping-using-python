import scrapy
from ..items import AmazonproductscraperItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.de/-/en/V%C3%ADvoactive-Waterproof-Training-Animated-Exercises/dp/B07XLDZWYP']

    def parse(self, response):
        items = AmazonproductscraperItem()
        product_name = response.css('#productTitle::text').get().strip()

        items['product_name'] = product_name
        yield items
        pass
