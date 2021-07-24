# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class SimplePipeline:
    def process_item(self, item, spider):
        #!注意这里调用item的属性时要用item['attr']而不是item.attr
        if not os.path.exists('./videos'):
          os.mkdir('./videos')
        with open('./videos/'+item['pic'],'wb') as fp:
            fp.write(item['data'])
        return item
