import openpyxl
from datetime import datetime


def write_snow_pack_info(file_name):
    wb = openpyxl.load_workbook(file_name)
    type_set = set()
    for sheet in wb:
        if '张家口' in sheet.title:
            continue

        snow_pick_name = sheet.title.replace('雪票价格', '')
        # 产品编号 产品类型 门市价 优惠价
        # Y01 平日周末4小时（自带板）    400 320

        print(snow_pick_name)
        # if '滑雪场' in snow_pick_name:
        #     one_pack = SnowPack(name=snow_pick_name, create_time=datetime.now())
        #     one_pack.save()
        #     print(one_pack.id)

        i = 3
        snow_pick_obj = SnowPack.objects.get(name=snow_pick_name)
        print(snow_pick_obj.id)
        while i <= sheet.max_row:
            product_code = sheet['A'+str(i)].value
            market_price = sheet['C'+str(i)].value
            perfer_price = sheet['D'+str(i)].value
            product_type = sheet['B'+str(i)].value
            product_type_obj = SnowTicketType.objects.get(type_name=product_type)
            print(product_type_obj.id)
            one_snow_ticket = SnowTicket(product_code=product_code,
                                         market_price=market_price,
                                         prefer_price=perfer_price,
                                         snow_pack_id=snow_pick_obj.id,
                                         product_type=product_type_obj.id,
                                         is_online=1,
                                         create_time=datetime.now()
                                         )
            one_snow_ticket.save()
            print('one_snow_ticket', one_snow_ticket.id)
            # 需要先创建类型表，然后取id， 类型表添加类型名字
            i += 1
    #
    # print(type_set)
    # print(len(type_set))
    # for item in type_set:
    #     print(item)
    #     one_type = SnowTicketType(type_name=item, create_time=datetime.now())
    #     one_type.save()
    #     print(one_type.id)
    # print(len(
    #     SnowTicketType.objects.all()
    # ))


if __name__ == '__main__':
    # !/usr/bin/env python
    import os

    import sys

    if __name__ == '__main__':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chongli_tour.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)
    from snow_ticket.models import SnowTicketType, SnowPack, SnowTicket
    write_snow_pack_info(file_name='snow_pack_info.xlsx')