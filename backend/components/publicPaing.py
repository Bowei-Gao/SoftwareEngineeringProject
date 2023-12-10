# -*- coding: utf-8 -*-

"""
@author: 猿小天

@contact: QQ:1638245306

@Created on: 2020/7/17 017 18:58
"""
from rest_framework.pagination import PageNumberPagination


class publicPagination(PageNumberPagination):
    """
    公共分页配置
    """
    page_query_param = 'pageIndex'  # 当前页
    page_size_query_param = 'pageSize'  # 当前页数量
    page_size = 10  # 默认当前页数量
    max_page_size = 100  # 前端最大当前页数量
