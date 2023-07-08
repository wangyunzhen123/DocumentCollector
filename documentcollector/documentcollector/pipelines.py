# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class DocumentcollectorPipeline:

    def open_spider(self, spider):  # 在爬虫开启的时候仅执行一次
        self.writer = csv.writer(open('data.csv', 'a+', encoding='utf-8',newline=''))
        header = ['uid','doi','title']
        self.writer.writerow(header)

    def process_item(self, item, spider):
        self.writer.writerow([item['uid'], item['doi'], item['title']])
        print("write")
        return item
