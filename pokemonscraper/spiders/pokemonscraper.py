from msilib.schema import Error
import scrapy

class PokemonScraper(scrapy.Spider):
    name = 'pokemon'
    start_urls = ['https://scrapeme.live/shop/']

    def parse(self, response):
        products = response.css('li.type-product')

        for product in products:
            try:
                yield {
                    'name': product.css('h2.woocommerce-loop-product__title::text').get(),
                    'price': product.css('span.woocommerce-Price-amount::text').get(),
                    'link': product.css('a.woocommerce-LoopProduct-link').attrib['href']
                }
            except:
                print("Something went wrong")

        next_page = response.css('a.next.page-numbers').attrib['href']

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
