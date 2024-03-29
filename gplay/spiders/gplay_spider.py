import scrapy
from ..items import GplayItem


class GplaySpider(scrapy.Spider):
    name = 'gplay_spider'
    start_urls = ['http://gplay.bg/']

    def parse(self, response):
        categories = response.xpath("//div[@class='nav-menu']/ul/li[./a[contains(@title, 'Периферия') or contains ("
                                    "@title, 'Хардуер')]]//a[not(contains(@title,'Периферия') or contains (@title, "
                                    "'Хардуер'))]/@href").getall()
        for category in categories:
            category += '?flag%5B%5D=available&perPage=30&sort=price_asc'
            yield response.follow(category, callback=self.parse_products)

    def parse_products(self, response):
        products = response.xpath("//div[@class='product-item']/a[@class='product-name']/@href").getall()
        for product in products:
            yield scrapy.Request(product, callback=self.parse_single_product)

        next_page = response.xpath("(//ul[@role='navigation']/li[@class='page-item'])[last()]/a/@href").get()
        if next_page is not None:
            yield scrapy.Request(url=next_page, callback=self.parse_products)

    def parse_single_product(self, response):
        price = response.xpath("//div[@class='price']/div[contains(@class, 'normal-price')]/price/@*").get()
        price_format = "{:.1f}".format(float(price))
        final_price = float(price_format)
        
        item = GplayItem()
        item['product_number'] = response.xpath("//div[@class='col-md-6 product-ref-number']/strong/text()").get()
        item['category'] = response.xpath("(//div[@class='path py-3']/a)[2]/text()").get()
        item['subcategory'] = response.xpath("(//div[@class='path py-3']/a)[3]/text()").get()
        item['title'] = response.xpath("//h1[@class='large-title']/text()").get()
        item['subtitle'] = response.xpath("//h2[@class='product-subtitle ']/text()").get()
        item['price'] = final_price

        yield item
