from django.shortcuts import render
from django.views import View

from areas.models import Area


# Create your views here.


class AreasView(View):
    """省市区三级联动"""

    def get(self, request):
        # 判断当前是要查询省份数据还是市区数据
        area_id = request.GET.get('area_id')
        if not area_id:
            # 查询省级数据
            # Area.objects.filter(属性名__条件表达式=值)
            province_model_list = Area.objects.filter(parent__isnull=True)

            # return http.JsonResponse({'code': '', 'errmsg': '', 'province_list': province_model_list})
            pass
        else:
            # 查询城市或区县数据
            pass
