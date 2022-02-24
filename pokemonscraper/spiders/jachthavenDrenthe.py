import scrapy


class JachthavendrentheSpider(scrapy.Spider):
    name = 'jachthavenDrenthe'
    allowed_domains = ['waterkaart.net/gids/jachthavens-Drenthe.php']
    start_urls = ['http://waterkaart.net/gids/jachthavens-Drenthe.php/']

    def parse(self, response):
        pass
