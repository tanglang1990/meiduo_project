import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()  # 让接下来的代码处在一个Django的环境中

from users.models import User

user = User.objects.get(pk=5)
user1 = User.objects.get(pk=5)

user.first_name = 'tanglang'
user.save()

# 其他地方修改数据库的数据的时候，已经加载的模型实例，不会自动修改
print(dir(user1))
# 1. dir的内置函数可以看一个对象的所有属性和方法
# 2. 懂英文
user1.refresh_from_db()
print(user1.first_name) # tanglang