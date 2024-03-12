import scrapy

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']

    def parse(self, response):
        for ad in response.css('.c-offerBox'):
            title = ad.css('.c-offerBox__title::text').get()
            image = ad.css('.c-offerBox__image img::attr(src)').get()
            url = ad.css('.c-offerBox__title a::attr(href)').get()
            yield {
                'title': title,
                'image': image,
                'url': url,
            }
