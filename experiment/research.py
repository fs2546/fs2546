# -*- coding: utf-8 -*-
import json
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
items = []
def parse(response):
    for info in response.xpath('//div[@class="block-research-list__content__item"]'):
    	item = dict(
    		url = info.xpath('.//a[@class="research--title"]/@href').extract_first(),
    		name = info.xpath('.//text()').re_first('\n\s*(.*)'),
    		title = info.xpath('.//@about').extract_first()[10:],
    		time = info.xpath('.//time/text()').extract_first(),
    		journal = info.xpath('.//span/i/text()').extract_first()
    )
    	items.append(item)

def has_next_page(response):
    classes = response.xpath('//li[contains(@class, "pager__item pager__item--next")]/@class').extract_first()
    return 'disabled' not in classes

def goto_next_page(driver):
    next_page_btn = driver.find_element_by_xpath('//li[contains(@class, "pager__item pager__item--next")]')
    next_page_btn.click()

def wait_page_return(driver, page):
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//li[@class="pager__item is-active"]'),
        str(page)
        )
    )

def spider():
    driver = webdriver.PhantomJS()
    url =  'https://www.marshall.usc.edu/faculty-research/recent-publications'
    driver.get(url)
    page = 1
    while True:
        wait_page_return(driver, page)
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf8'))
        parse(response)
        if not has_next_page(response):
            break
        page += 1
        goto_next_page(driver)
        with open('research.json','w') as f:
            f.write(json.dumps(items))

if __name__ == '__main__':
    spider()
