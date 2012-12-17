# Scrapy settings for android_apps_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'android_apps_crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['android_apps_crawler.spiders']
NEWSPIDER_MODULE = 'android_apps_crawler.spiders'
DEFAULT_ITEM_CLASS = 'android_apps_crawler.items.AppItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
    'android_apps_crawler.pipelines.AppPipeline',
    'android_apps_crawler.pipelines.SQLitePipeline'
]
LOG_LEVEL = 'INFO'