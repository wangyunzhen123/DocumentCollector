# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import cloudscraper
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class DocumentcollectorSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DocumentcollectorDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



import cloudscraper
from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest

class CloudScraperMiddleware:
    def __init__(self, settings):
        self.scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
            'Referer': 'https://www.sciencedirect.com/search?qs=paleosol',
            "Connection": 'keep-alive',
            'Cookie':'search_traffic=%7B%227%22%3A26%7D; EUID=c03e8140-e305-4d8d-b6a6-125495c48a8c; mboxes=%7B%22sd%3Aaccessbanner-button-patientaccess%22%3A%7B%22variation%22%3A%22B%22%7D%7D; __gads=ID=1d065c2fcc16f94f:T=1688444233:RT=1688444233:S=ALNI_MbIBXzZT3bYRUz9MT8cu8k2O9uJvQ; mbox=session%23b6ca3f886c344bd0ac1b4d16a5d2ed40%231688484036%7CPC%23c95b0f043c5641e4ac65b8b11e62e4c9.34_0%231751726976; id_ab=IDP; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..rOtV9kresBh2MyIcv_HbFw.TmUANK_JPGapp0esS7umtsBI5eUtvdJibn_o1bT8XrNDcsW0JWfNKJKrat5pPf4dH9wArGC5h86qPhugjq76H-COOdu2EmfGDeZZTBB9bKIMLcpcX7m0WytbKprNNhnF4HvcKU5yYE12-bCSUCoNog.hatPx-6MIjRIUBEr2SKYAQ; sd_session_id=ce46b05b60bd2144d29aac6-acfc963fbb05gxrqa; has_multiple_organizations=false; __cf_bm=WzH.EYGritfTMcOrR78xGLX3PL_UAERcjoW0BXTTbkQ-1688724450-0-AeYFJR65lGBAC0wLZoasgHVCPnYV0gNat5QCDSzNv4ZBHkZOorvVJdGuKDwNhJz8i8YZ8QyglWBArYq40gukhwJ3M6Gqbjb3B/0nMzO6GZ2u+MrLT/kfhDQh3MEU1P0ONg==; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=179643557%7CMCIDTS%7C19546%7CMCMID%7C08981173887321356500279601772033232853%7CMCAAMLH-1689329251%7C11%7CMCAAMB-1689329251%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1688731651s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C702990746%7CvVersion%7C5.5.0; s_pers=%20v8%3D1688724451059%7C1783332451059%3B%20v8_s%3DLess%2520than%25201%2520day%7C1688726251059%3B%20c19%3Dsd%253Asearch%253Aresults%253Aguest%7C1688726251061%3B%20v68%3D1688724449759%7C1688726251067%3B; s_sess=%20s_ppvl%3D%3B%20s_cpc%3D1%3B%20s_cc%3Dtrue%3B%20c21%3Dqs%253Dpaleosol%3B%20e13%3Dqs%253Dpaleosol%253A1%3B%20c13%3Drelevance-desc%3B%20e41%3D1%3B%20s_ppv%3Dsd%25253Asearch%25253Aresults%25253Aguest%252C6%252C6%252C975%252C1050%252C975%252C1920%252C1080%252C1%252CP%3B; MIAMISESSION=654205e6-4401-4141-8d82-99f5caa14ae8:3866177504',
            'Sec-Ch-Ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': 'Windows',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9'
        }

        self.scraper.headers.update(headers)

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls(crawler.settings)
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        # 忽略那些不需要使用cloudscraper的请求
        if not request.meta.get('use_cloudscraper', False):
            return None

        try:
            response = self.scraper.get(request.url)
            return HtmlResponse(request.url, body=response.content, encoding='utf-8', request=request)
        except Exception as e:
            raise IgnoreRequest(f'CloudScraperMiddleware error: {e}')

    def spider_closed(self, spider):
        self.scraper.close()
