# 递归 recursion


# 1. 什么是递归？
# def foo(n):
#     print(n)
#     n += 1
#     foo(n)
#
# foo(1)

# 2. 递归的最大层数
# import sys
#
# recursionlimit = sys.getrecursionlimit()
# print(recursionlimit)

# 3. 限制递归层数
# sys.setrecursionlimit(10)
# def foo(n):
#     print(n)
#     n += 1
#     foo(n)
#
# foo(1)

# 4. 递归有什么用？
# 举例
# 1. 遍历得到文件夹下所有的文件
# import os
#
#
# def print_all_files_in_path(path):
#     for child_dir_or_file in os.listdir(path):
#         child_path = os.path.join(path, child_dir_or_file)
#         if os.path.isfile(child_path):
#             print(child_path)
#         else:
#             print_all_files_in_path(child_path)
#
#
# print_all_files_in_path(r'C:\Users\a\Desktop\test')


# 2. 遍历导航栏
import json

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

cat1_list = GoodsCategory.objects.filter(parent__isnull=True)
def cat_to_dict(cat):
    dict = model_to_dict(cat, ['id', 'name'])
    print(dict)
    if cat.subs.count():
        sub_cats = []
        for cat in cat.subs.all():
            sub_cats.append(cat_to_dict(cat))
        dict['sub_cats'] = sub_cats
    return dict


all_cat = []
for cat1 in cat1_list:
    model_dict = cat_to_dict(cat1)
    all_cat.append(model_dict)

print(json.dumps(all_cat, ensure_ascii=False))
