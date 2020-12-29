# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import sqlite3
class QuotesPipeline:

#     def __init__(self):
#         self.create_connection()
#         self.create_table()

#     def create_connection(self):
        
#         self.conn = sqlite3.connect("quotes.db")
#         # To open sql file 
#         self.curr = self.conn.cursor()

#         pass
#     def create_table(self):
#         self.curr.execute("""drop table if exists quotes_db""")
#         self.curr.execute("""create table quotes_db(
#     title text,
#     author text,
#     tag text)""")

    
    def process_item(self, item, spider):
        # self.store_db(item)
        # print("Pipeline: " + item["quote"][0])
        return item

#     def store_db(self,item):
#         self.curr.execute("""insert into quotes_db values (?,?,?)""",(item["quote"][0],item["author"][0],item["tags"][0]))
#         self.conn.commit()