import os
import django

from datetime import date, datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()  # 让接下来的代码处在一个Django的环境中

from goods.models import GoodsVisitCount


#
# GoodsVisitCount.objects.create(category_id=3, count=1)


# 当前时间：   2019-10-19 11:02:07
# 数据库的时间：2019-10-19 03:02:44  慢了8个小时

# 会带来时间混乱的问题？
# 怎么办？
# 1. TIME_ZONE 改成 'Asia/Shanghai'
# 2. USE_TZ = False  (推荐大家使用第二种方法)


# goods_v =    GoodsVisitCount.objects.get(id =12)
# print(type(goods_v.date))
#
# from datetime import date, datetime
# # datetime 实际上date的子类
# print(type(datetime.today()))


# print(date.today() )
# print(datetime.today())

GoodsVisitCount.objects.create(category_id=115, count=1)
