# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import LianjiaItem
import json
import pymysql


class LianJia(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ["lianjia.com"]
    start_urls = [
        # "http://wh.lianjia.com/ershoufang/pg1/",
        # "http://gz.lianjia.com/ershoufang/pg1/",
        # "http://cs.lianjia.com/ershoufang/pg1/",
        # "http://fs.lianjia.com/ershoufang/pg1/"
        "http://cd.lianjia.com/ershoufang/pg1/",
        "http://cq.lianjia.com/ershoufang/pg1/"
    ]

    def __init__(self, **kwargs):
        super(LianJia, self).__init__(**kwargs)
        # self.file = open('./items.tet', 'wb')
        self.conn = pymysql.connect(host='192.168.33.11', port=3306, user='root', passwd='123456', db='lianjia')

    def parse(self, response):
        selector = Selector(response)
        lis = selector.xpath('//ul[@class="sellListContent"]/li')
        for li in lis:
            detail_url = li.xpath('div/div[@class="title"]/a/@href').extract()[0]
            # print li.xpath('div/div[@class="title"]/a/text()').extract()[0]
            # print detail_url
            yield Request(detail_url, callback=self.parse_detail)

        if len(lis) > 0:
            next_page = int(response.url.split('/')[-2][2:]) + 1
            base_url = response.url.split('pg')[0] + 'pg'
            next_url = base_url + str(next_page) + '/'
            print next_url
            yield Request(next_url, callback=self.parse, dont_filter=True)

    def parse_detail(self, response):
        selector = Selector(response)
        item = LianjiaItem()
        item['title'] = selector.xpath('//div[@class="sellDetailHeader"]//div[@class="title"]/h1/text()').extract()[0]
        item['sub_title'] = \
            selector.xpath('//div[@class="sellDetailHeader"]//div[@class="title"]/div[@class="sub"]/text()').extract()[
                0]
        item['follow'] = selector.xpath('//div[@class="btnContainer "]//span[@id="favCount"]/text()').extract()[0]
        item['looked'] = selector.xpath('//div[@class="btnContainer "]//span[@id="cartCount"]/text()').extract()[0]
        item['price'] = selector.xpath('//div[@class="price "]//span[@class="total"]/text()').extract()[0]
        item['unit_price'] = selector.xpath('//span[@class="unitPriceValue"]/text()').extract()[0]
        item['room_num'] = selector.xpath('//div[@class="room"]//div[@class="mainInfo"]/text()').extract()[0][0:1]
        item['drawing_num'] = selector.xpath('//div[@class="room"]//div[@class="mainInfo"]/text()').extract()[0][2:3]
        item['acreage'] = \
            selector.xpath('//div[@class="houseInfo"]//div[@class="area"]/div[@class="mainInfo"]/text()').extract()[0][
            :-2]
        item['district'] = selector.xpath('//div[@class="communityName"]/a[@class="info"]/text()').extract()[0]
        item['area'] = selector.xpath('//div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract()[0]
        item['year'] = \
            selector.xpath('//div[@class="houseInfo"]/div[@class="area"]/div[@class="subInfo"]/text()').extract()[0][:4]
        item['prefix'] = response.url.split('.')[0][7:]
        # print item
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # yield item
        # pass
        cur = self.conn.cursor()
        sql = "insert into room VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute('set names utf8')
        cur.execute(sql,
                    (item['title'].encode("utf-8"), item['sub_title'].encode("utf-8"), item['follow'].encode("utf-8"),
                     item['looked'].encode("utf-8"), item['price'].encode("utf-8"),
                     item['unit_price'].encode("utf-8"), item['room_num'].encode("utf-8"),
                     item['drawing_num'].encode("utf-8"), item['acreage'].encode("utf-8"),
                     item['district'].encode("utf-8"),
                     item['area'].encode("utf-8"),
                     item['year'].encode("utf-8"), item['prefix'].encode("utf-8")))
        cur.close()
        self.conn.commit()
