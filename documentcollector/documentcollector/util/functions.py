import hashlib
import re


def __getTaskNum(response):
    div = response.xpath("//div[@class='sr-statistics']").extract_first()
    task_nums = int(re.findall(pattern='OF(.*?)RESULTS FOR', string=div)[0].strip().replace(',', ''))
    print("Search results: {} nums.".format(task_nums))


def __foramtDoi(doi: str) -> str:
    # 如果 doi 值为 'https://doi.org/10.1785/0120030046'，则经过这些替换后，doi 的值将变为 '10.1234/foo'
    doi = doi.replace('https://doi.org/', '').replace('/doi/', '').replace('full/', '').replace('book/', '')
    return doi


def __gen_uuid_of_doi(doi: str) -> str:
    # self.uuid[doi] = str(uuid.uuid3(uuid.NAMESPACE_OID, doi))
    md5 = hashlib.md5()
    md5.update(doi.encode('utf-8'))
    res = md5.hexdigest()
    return res