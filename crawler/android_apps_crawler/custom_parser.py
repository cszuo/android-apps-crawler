import re

from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from android_apps_crawler.items import AppItem

def parse_anzhi(response):
    xpath = "//div[@class='detail_down']/a/@onclick"
    appItemList = []
    sel = Selector(response)
    for script in sel.xpath(xpath).extract():
        id = re.search(r"\d+", script).group()
        url = "http://www.anzhi.com/dl_app.php?s=%s&n=5" % (id,)
        appItem = AppItem()
        appItem['url'] = url
        appItemList.append(appItem)
    return appItemList

def parse_zhushou(response):
    xpath = "//script/text()"
    appItemList = []
    print response
    sel = Selector(response)
    for script in sel.xpath(xpath).extract():
        url = re.search(r"downurl':'[^']*", script)
        if url==None: continue
        url = url.group()
        appItem = AppItem()
        appItem['url'] = url[url.rfind("'")+1:]
        appItemList.append(appItem)
    return appItemList


