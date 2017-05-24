from scrapy.spiders import Spider
from scrapy.selector import Selector
from MobileSpider.items import MobilespiderItem

class JDSpider(Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = []
    
    def parser(self, response):
        
        pass

