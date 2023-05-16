import scrapy


class SellerLinksSpider(scrapy.Spider):
    name = "seller_links"
    allowed_domains = ["amazon"]
    start_urls = ["https://amazon"]

    def parse(self, response):
        pass
        for amazon_category in amazon_categories;
              yield scrapy.Request(
                  url=”https://www.amazon.de/mn/search/other?_encoding=UTF8&language=en_
                  GB&page-l&pickerToList=enc-merchantbin&rh=n%3A+amazon_category,callback
                  =self.parse_next”
        method = “GET”,
        meta = {‘amazon_category’ :amazon_category}
        )

    def seller_link_extract(self,response);

        item = AmazonSellerLinkitem()
        item[‘seller_category’] = “_” .join(response.xpath(‘//*@class=”a-row-a-spacing-base”]//a
        /text().extract())
        sellers = responsive.xpath(‘//[@class=”s-see-all-indexbar-column”]//a’)

        for seller in sellers:
        item[‘seller_name’] = seller.xpath(‘,/@title’).extract_first()
        item[‘sellers_page_url’] = “https://www.amazon.de/sp?_encoding=UTF&asian=&isCBA
        =&marketplaceID=&orderID=&seller=” +str(seller.xpath(‘,/@href’).re(‘6%3A(.*?)&’)[0])
        yielditem