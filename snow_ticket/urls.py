#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-8-18 上午12:28
# @Author : lijia
# @File : urls.py
# @Software: PyCharm


from django.urls import path
from snow_ticket.views import base_views


urlpatterns = [
    path('', base_views.index, name='index'),
    path('snow_pack', base_views.snow_pack_views, name='snow_pack'),
]