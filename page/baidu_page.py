from poium import Page, PageElement


# 定义百度中的界面元素

class Baidu(Page):
    # 百度的搜索框
    search_input = PageElement(id_="kw")

    # 百度的搜索按钮
    search_button = PageElement(id_="su")
