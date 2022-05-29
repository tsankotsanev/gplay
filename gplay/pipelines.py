# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class GplayPipeline:
    def __init__(self):
        self.con = sqlite3.connect('gplay.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(
        product_number TEXT PRIMARY KEY,
        category TEXT,
        subcategory TEXT,
        title TEXT,
        subtitle TEXT,
        price REAL
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES (?,?,?,?,?,?)""", (
            item['product_number'],
            item['category'],
            item['subcategory'],
            item['title'],
            item['subtitle'],
            item['price']
        ))
        self.con.commit()
        return item
