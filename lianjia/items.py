# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 标题
    sub_title = scrapy.Field()  # 子标题
    follow = scrapy.Field()  # 关注
    looked = scrapy.Field()  # 看过
    price = scrapy.Field()  # 价格
    unit_price = scrapy.Field()  # 单价
    room_num = scrapy.Field()  # 房间数
    drawing_num = scrapy.Field()  # 客厅数
    acreage = scrapy.Field()  # 面积
    district = scrapy.Field()  # 小区名称
    area = scrapy.Field()  # 区域
    year = scrapy.Field()  # 年份
    prefix = scrapy.Field() #城市简称
