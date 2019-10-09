from django.shortcuts import render
from django.views import View

from django import http
import logging

from areas.models import Area
from meiduo_mall.utils.response_code import RETCODE

logger = logging.getLogger('django')


class AreasView(View):
    """省市区三级联动"""

    def get(self, request):
        # 判断当前是要查询省份数据还是市区数据
        area_id = request.GET.get('area_id')
        if not area_id:
            # 查询省级数据
            # Area.objects.filter(属性名__条件表达式=值)
            try:
                province_model_list = Area.objects.filter(parent__isnull=True)

                # 需要将模型列表转成字典列表
                province_list = []
                for province_model in province_model_list:
                    province_dict = {
                        "id": province_model.id,
                        "name": province_model.name
                    }
                    province_list.append(province_dict)
                # 响应省级JSON数据
                return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'province_list': province_list})
            except Exception as e:
                logger.error(e)
                return http.JsonResponse({'code': RETCODE.DBERR, 'errmsg': '查询省份数据错误'})
        else:
            # 查询城市或区县数据
            pass
