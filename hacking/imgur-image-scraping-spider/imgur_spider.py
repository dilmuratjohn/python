import scrapy
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor

class ImgurItem(scrapy.Item):
	title = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()

BOT_NAME = 'imgur'

SPIDER_MODULES = ['imgur.spiders']
NEWSPIDER_MODULE = 'imgur.spiders'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = '/home/ubuntu/imgurFront/'

class ImgurSpider(CrawlSpider):
	name = 'imgur'
	allowed_domains = ['imgur.com']
	start_urls = ['http://www.imgur.com']
	rules = [Rule(LinkExtractor(allow=['/gallery/.*']), 'parse_imgur')]

	def parse_imgur(self, response):
		image = ImgurItem()
		image['title'] = response.xpath(\
			"//h2[@id='image-title']/text()").extract()
		rel = response.xpath(//img/@src").extract()
		image['image_urls'] = ['http:'+rel[0]]
		return image
