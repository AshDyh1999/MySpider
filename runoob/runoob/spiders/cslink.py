# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from runoob.items import RunoobItem


class CslinkSpider(scrapy.Spider):
    name = 'cslink'
    # allowed_domains = ['runoob.com']
    # start_urls = ['http://runoob.com/']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url = 'http://runoob.com/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = RunoobItem()
    
        alist = response.xpath('/html/body/div[4]/div/div[2]/div')
        for each in alist:
            div = each.xpath('.//a')
            for a in div:
                item['name'] = a.xpath('.//h4/text()').extract()[0]
                item['introduce'] = a.xpath('.//strong/text()').extract()[0]
                item['link'] = each.xpath('.//@href').extract()[0]
                yield item
        
        # next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        # if next_url:
        #     next_url = 'https://movie.douban.com/top250' + next_url[0]
        #     yield Request(next_url, headers=self.headers)
        # pass
