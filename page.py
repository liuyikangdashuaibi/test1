from page_objects import Page,PageElement,PageElements

class BiliBili(Page):

    #根据html元素找到输入关键字的元素
    input=PageElement(class_name="nav-search-keyword",describe="搜索")

    #根据html元素找到点击的按钮
    button=PageElement(class_name="bilifont.bili-icon",describe="按钮")


