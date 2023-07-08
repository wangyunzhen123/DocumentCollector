import json

import scrapy


class ElesevierSpider(scrapy.Spider):
    name = 'Elesevier'
    allowed_domains = ['www.sciencedirect.com/search']
    start_urls = ['http://www.sciencedirect.com/search']

    keyword = 'paleosol'
    base_url = f'https://www.sciencedirect.com/search/api?qs={keyword}'
    offset = 0
    articleTypes = ''
    token = 'Ea3ZhS4jrwwfpDvrntwxmztJs6VmCxmiS2ayBWCGnFxuMqMpA1CiH6bTygysCvgmJPTOYn6KsmsBMMpDAxxu6xzfZ%2BIiSoQKYPoNSoz63xP85ejvxSPW7zBMkTUekyc8vKdDbfVcomCzYflUlyb3MA%3D%3D'

    url = base_url + f"&show=100&offset={offset}&lastSelectedFacet=articleTypes&articleTypes={articleTypes}&t=" + \
          token + "&hostname=www.sciencedirect.com"

    #print(f"url={url}")


    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, meta={'use_cloudscraper': True})

    def parse(self, response):
        print(response.text)
        #print("="*30)
        #data = json.loads(response.body)
        #print(data)
        #print("="*30)


