from QQLoginTool.QQtool import OAuthQQ
from django.views import View
from django.conf import settings
from django import http

from meiduo_mall.utils.response_code import RETCODE


class QQAuthURLView(View):
    """提供QQ登录扫码页面"""

    def get(self, request):
        # 接收next
        next = request.GET.get('next')

        # 创建工具对象
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI, state=next)

        # 生成QQ登录扫码链接地址
        login_url = oauth.get_qq_url()

        # 响应
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'login_url': login_url})
