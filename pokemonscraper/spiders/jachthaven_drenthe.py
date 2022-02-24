import scrapy


class JachthavenDrentheSpider(scrapy.Spider):
    name = 'jachthaven_drenthe'
    allowed_domains = ['waterkaart.net/gids/jachthavens-Drenthe.php']
    start_urls = ['http://waterkaart.net/gids/jachthavens-Drenthe.php/']

    def parse(self, response):
        pass
