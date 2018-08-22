#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-8-18 上午12:26
# @Author : lijia
# @File : base_views.py
# @Software: PyCharm

from django.http import HttpResponse
from django.shortcuts import render
from snow_ticket.models import *


def index(request):
    return render(request, 'index.html')


def snow_pack_views(request):
    snow_pack_id = request.GET.get('id', 1)
    # 雪票类型
    snow_ticket_type_map = dict()
    all_snow_ticket_type = SnowTicketType.objects.all()
    for one_type in all_snow_ticket_type:
        snow_ticket_type_map[one_type.id] = one_type.type_name
    # 雪场
    snow_pack_desc = SnowPack.objects.get(id=snow_pack_id).name

    # 雪票
    snow_ticket = list()
    all_ticket = SnowTicket.objects.filter(snow_pack_id=snow_pack_id)
    for one_snow_ticket in all_ticket:
        one_snow_ticket.product_desc = snow_ticket_type_map.get(one_snow_ticket.product_type, '')

    data = dict()
    data['snow_pack_desc'] = snow_pack_desc
    data['all_ticket'] = all_ticket

    return render(request, 'table_static.html', context=data)
