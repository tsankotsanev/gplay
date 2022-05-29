# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_jsonschema.item import JsonSchemaItem


class GplayItem(JsonSchemaItem):
    jsonschema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Product",
        "description": "A product from gplay website",
        "type": "object",
        "properties": {
            "category": {
                "description": "The main category of a product",
                "type": "string"
            },
            "subcategory": {
                "description": "The subcategory of a product",
                "type": "string"
            },
            "title": {
                "description": "The title of a product",
                "type": "string"
            },
            "subtitle": {
                "description": "The subtitle of a product",
                "type": "string"
            },
            "product_number": {
                "description": "The product serial number",
                "type": "string"
            },
            "price": {
                "description": "The price of a product",
                "type": "number",
                "maximum": 200,
                "exclusiveMaximum": True
            }
        },
        "required": [
            "category",
            "subcategory",
            "title",
            "subtitle",
            "product_number",
            "price"
        ]
    }
