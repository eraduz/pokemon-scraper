from gc import callbacks
import scrapy

class DetailsSpider(scrapy.Spider):
    name = 'details'
    start_urls = ['https://scrapeme.live/shop/']

    def parse(self, response):
        links = response.css('a.woocommerce-LoopProduct-link::attr(href)')
        for link in links:
            yield response.follow(link.get(), callback=self.getDetails)

        next_page = response.css('a.next.page-numbers').attrib['href']

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def getDetails(self, response):
        wrapper = response.css('div.entry-summary')
        for item in wrapper:
            yield {
                'name': item.css('h1.entry-title::text').get(),
                'price': item.css('span.woocommerce-Price-amount::text').get(),
                'desc': item.css('.woocommerce-product-details__short-description > p:nth-child(1)::text').get(),
                'sku': item.css('span.sku::text').get(),
                'categories': item.css('.posted_in > a::text').getall(),
                'tags': item.css('.tagged_as > a::text').getall()
            }

