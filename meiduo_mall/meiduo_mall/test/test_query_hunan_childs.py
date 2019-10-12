import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()

from areas.models import Area

# hunan_province = Area.objects.get(name='湖南省')
# print(hunan_province.id)

citys = Area.objects.filter(parent__id=430000)

# citys = hunan_province.subs.all()
# print(type(citys))
print(list(citys))
