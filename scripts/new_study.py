#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-8-18 上午1:46
# @Author : lijia
# @File : new_study.py
# @Software: PyCharm

#!/usr/bin/env python
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

    from datetime import datetime

    from snow_ticket.models import SnowTicketType

    aa = SnowTicketType(include_board=1, create_time=datetime.date(datetime.now()), day_or_hour=1, duration=2, use_time=23,
                        create_operator=1)

    print(aa)
    aa.save()
    print(123)
    print(aa.id)

    print(SnowTicketType.objects.all())