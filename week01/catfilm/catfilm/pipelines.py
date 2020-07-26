# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class CatfilmPipeline:
    def process_item(self, item, spider):
        result_list = item['result_list']
        movie_df = pd.DataFrame(data=result_list)
        movie_df.to_csv('./result2.csv', encoding='utf8', index=False, header=False)
