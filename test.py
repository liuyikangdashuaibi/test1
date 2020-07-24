import sys
from time import sleep
from os.path import dirname,abspath
from page import BiliBili


sys.path.insert(0,dirname(dirname(abspath(__file__))))

class Test:
      
        #检测网址中的搜索功能是否存在问题
    def test_search(self,browser,url):

        #初始化page
        page=Page(browser)

        #将对应的网址赋给page
        page.get(url)

        #再搜索框中输入“自动化测试”
        page.input="自动化测试"

        #点击搜索按钮
        page.button.click()


