import requests
import re

class DiscountInfo:
    #优惠信息网址
    def __init__(self):
        self.urls = ['https://www.3k8.com']
        self.page = 1

    def fetch(self,url):
        resp = requests.get(url+"{}".format(self.page))
        self.page += 1
        resp.encoding = 'utf-8'
        text =  resp.text







discount = DiscountInfo()
for url in len(discount.urls):
    discount.fetch(url)