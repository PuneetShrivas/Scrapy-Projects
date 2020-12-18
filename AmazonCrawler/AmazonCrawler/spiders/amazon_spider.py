import scrapy

from ..items import AmazoncrawlerItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 1
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1608281035&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        items = AmazoncrawlerItem()

        all_products = response.css('div.sg-col-inner')

        for products in all_products:
            product_name = products.css('.a-color-base.a-text-normal::text').extract()
            product_author = products.css('.sg-col-12-of-20 .sg-col-12-of-20 .a-size-base+ .a-size-base').css('::text').extract()
            product_price = products.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
            product_imglink = products.css('.s-image::attr(src) ').extract()

            items['product_name'] = product_name
            items['product_author'] = product_author
            items['product_price'] = product_price
            items['product_imglink'] = product_imglink

            if len(product_name) > 0:
                if len(product_author) > 0:
                    yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(AmazonSpiderSpider.page_number) + '&fst=as%3Aoff&qid=1608284107&rnid=1250225011&ref=sr_pg_' + str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number <= 75:
            AmazonSpiderSpider.page_number += 1
            print('PPPPPPPPage Number accessed : '+ str(AmazonSpiderSpider.page_number))
            yield response.follow(next_page, callback = self.parse)
