from page_objects import Page,PageElement,PageElements

class BiliBili(Page):
    input=PageElement(class_name="nav-search-keyword",describe="搜索")
    button=PageElement(class_name="bilifont.bili-icon",describe="按钮")


