# Gplay spider
Scrapy project, that collects data from `gplay.bg` source. We are targeting products from the following categories:  
* Периферия
* Хардуер

Every category has several subcategories. Our goal is to crawl (navigate) through all of them, and scrape all of the products, that meet the following criteria:
* it has to be available (has status – “наличен”)
* it costs less than 200 leva (doesn’t matter if the product is in promotion or not) 

For each we have to collect the information listed below:
* category
* subcategory
* title 
* subtitle
* product number
* price

## Installation
For this project we are gonna be using [Pip](https://pip.pypa.io/en/stable/installation/) to install the packages we need
1. Clone the project  
`git clone https://github.com/tsankotsanev/gplay`
2. Activate virtual environment through the [terminal](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) or if you're using [PyCharm](https://www.jetbrains.com/pycharm/) he can do this for you
3. Install the project packages

Install scrapy:

`pip3 install scrapy`

Install [JSON Schema](https://github.com/scrapy-plugins/scrapy-jsonschema) which we're gonna be using to validate our data:

`pip3 install scrapy-jsonschema`

## Pipelines
* `scrapy_jsonschema.JsonSchemaValidatePipeline` - validate the entire item based on the given [JSON Schema](https://github.com/scrapy-plugins/scrapy-jsonschema)
* `gplay.pipelines.GplayPipeline` - stores the output data in [SQLite](https://www.sqlite.org/index.html) database

## Usage
* `scrapy crawl <spider_name>` - runs the spider

