import hashlib
import re
import scrapy
from documentcollector.items import DocumentcollectorItem
from documentcollector.log import lg


class GeosicenceworldSpider(scrapy.Spider):
    name = 'GeosicenceWorld'
    allowed_domains = ['pubs.geoscienceworld.org/journals/search-results']
    start_urls = ['http://pubs.geoscienceworld.org/journals/search-results']
    url = start_urls[0] + '?q={paleosol}'

    num = 0
    first = True
    res = 0
    page = 1

    def start_requests(self):
        yield scrapy.Request(url=self.url)


    def parse(self, response):
        #print(response.text)
        if(self.first == True):
           self.num = self.__getTaskNum(response)
           self.first = False

        journal_pattern = '<strong>Journal:</strong> <a href="(.*?)">(.*?)</a>'
        publisher_pattern = '<strong>Publisher:</strong> <a href="(.*?)">(.*?)</a>'
        doi_pattern = '<div class="sri-doi">DOI: <a href="(.*?)">(.*?)</a></div>'
        title_pattern = '<a class="js-result-link" href="(.*?)">(.*?)</a>'

        for txt in response.text.split('<div class="sr-list al-article-box al-normal clearfix">')[1:]:
            self.res = self.res + 1

            item = DocumentcollectorItem()
            try:
                doi = re.findall(doi_pattern, txt)[0][0]
                doi = self.__foramtDoi(doi)
                item['doi'] = doi

                uid = self.__gen_uuid_of_doi(doi)
                item['uid'] = uid
            except Exception as e:
                lg.info("no doi")
                pass

            try:
                title_pre = re.findall(title_pattern, txt)[0][1].replace("<b>", "").replace("</b>", "")
                pattern = r'<span class="search-highlight">(.*?)</span>'
                title = re.sub(pattern, r'\1', title_pre)
                item['title'] = title
            except Exception as e:
                lg.info('no title')

            yield item

        lg.info(f"There are {self.task_nums - self.res} left")
        self.page = self.page + 1
        url = self.url + "&fl_SiteID=9&" + f"page={self.page}"
        yield scrapy.Request(url=url, callback=self.parse, method="GET",dont_filter=True)



    def __getTaskNum(self,response):
        div = response.xpath("//div[@class='sr-statistics']").extract_first()
        self.task_nums = int(re.findall(pattern='OF(.*?)RESULTS FOR', string=div)[0].strip().replace(',', ''))
        print("Search results: {} nums.".format(self.task_nums))

    def __foramtDoi(self, doi: str) -> str:
        #如果 doi 值为 'https://doi.org/10.1785/0120030046'，则经过这些替换后，doi 的值将变为 '10.1234/foo'
        doi = doi.replace('https://doi.org/', '').replace('/doi/', '').replace('full/', '').replace('book/', '')
        return doi

    def __gen_uuid_of_doi(self, doi: str) -> str:
        # self.uuid[doi] = str(uuid.uuid3(uuid.NAMESPACE_OID, doi))
        md5 = hashlib.md5()
        md5.update(doi.encode('utf-8'))
        res = md5.hexdigest()
        return res
