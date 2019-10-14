# 递归
# 什么是递归？
# 函数自己调用自己

# def fo(n):
#     print(n)
#     n += 1
#     fo(n)
#
# fo(1)


import sys

# 递归的最大层数  1000
# 由于解释器自己存在一些函数的调用，我们看不到递归递归了1000次
# recursionlimit = sys.getrecursionlimit()
# print(recursionlimit)
#
# # 可以设置递归的层数
# sys.setrecursionlimit(10)
#
#
# def fo(n):
#     print(n)
#     n += 1
#     fo(n)
#
# fo(1)

# 找到文件夹下所有的文件
# import os
#
# def find_all_file_in_the_path(path):
#    dirs = os.listdir(path)
#    # 遍历当前的文件或文件夹
#    for dir in dirs:
#        dir_real_path = os.path.join(path, dir)
#        #if os.path.isfile(dir_real_path):
#        if not os.path.isdir(dir_real_path):
#            print(dir_real_path)
#        else:
#            find_all_file_in_the_path(dir_real_path)
#
#
#    # 判断是否是文件
#    # 如果是文件的话就直接打印出来
#    # 如果是文件夹的话继续遍历
#
#
#
# find_all_file_in_the_path(r'C:\Users\a\Desktop\test')
# #
#
# print(os.path.isdir(r'C:\Users\a\Desktop\test\B\E\F'))

[{'id': 1, 'name': '手机',
  "sub_cats": [
      {
          "id": 38,
          "name": "手机通讯",
          "sub_cats": [
              {"id": 115, "name": "手机"},
              {"id": 116, "name": "游戏手机"}
          ]
      },
      {
          "id": 39,
          "name": "手机配件",
          "sub_cats": [
              {"id": 119, "name": "手机壳"},
              {"id": 120, "name": "贴膜"}
          ]
      }
  ]
  # ...
  }]

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()

from goods.models import GoodsCategory
from django.forms import model_to_dict

cat_list = []
cat1_list = GoodsCategory.objects.filter(parent__isnull=True)

def cat_to_dict(cat):
    parent_dict = model_to_dict(cat, ['id', 'name'])
    # 判断一下当前类别是否有子
    # 如果没有子，直接返回
    # 如果有子，继续遍历，
    if cat.subs.count():
        sub_cats = []
        for cat_child in cat.subs.all():
            child_dict = cat_to_dict(cat_child)
            sub_cats.append(child_dict)
        parent_dict['sub_cats'] = sub_cats
    return parent_dict

for cat1 in cat1_list:
    cat_list.append(cat_to_dict(cat1))

# print(cat_list)
import json

# ensure_ascii 一定要知道：阻止把中文等其他非ascii的字符转换为 unicode的编码
json_str = json.dumps(cat_list, ensure_ascii=False)
print(json_str)



# for cat1 in cat1_list:
#     d = model_to_dict(cat1, ['id', 'name'])
#     sub_cats = []
#     for cat2 in cat1.subs.all():
#         d2 = model_to_dict(cat2, ['id', 'name'])
#         sub_cats2 = []
#         for cat3 in cat2.subs.all():
#             sub_cats2.append(model_to_dict(cat3, ['id', 'name']))
#         d2['sub_cats'] = sub_cats2
#         sub_cats.append(d2)
#     d['sub_cats'] = sub_cats
#     print(d)


