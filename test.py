import sys
from time import sleep
from os.path import dirname,abspath
from page import BiliBili


sys.path.insert(0,dirname(dirname(abspath(__file__))))

class Test:
    def test_search(self,browser,url):
        page=Page(browser)
        page.get(url)
        page.input="自动化测试"
        page.button.click()


