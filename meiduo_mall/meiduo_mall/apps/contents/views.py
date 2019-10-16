from django.shortcuts import render
from django.views import View
from collections import OrderedDict

from goods.models import GoodsChannelGroup, GoodsChannel, GoodsCategory
from contents.models import ContentCategory, Content


# Create your views here.


class IndexView(View):
    """首页广告"""

    def get(self, request):
        """提供首页广告页面"""
        # 查询并展示商品分类
        # 准备商品分类对应的字典
        categories = OrderedDict()    #  {}
        # 查询所有的商品频道:37个一级类别
        channels = GoodsChannel.objects.order_by('group_id', 'sequence')
        # 遍历所有频道
        for channel in channels:  #  100手机（1）  101相机（1）  102电脑（2）
            # 获取当前频道所在的组
            group_id = channel.group_id    # 2
            # 构造基本的数据框架:只有11个组
            if group_id not in categories:
                categories[group_id] = {'channels': [], 'sub_cats': []}
                # { '1': {'channels': [], 'sub_cats': [] }

            # 查询当前频道对应的一级类别
            cat1 = channel.category
            # 将cat1添加到channels
            categories[group_id]['channels'].append({
                'id': cat1.id,
                'name': cat1.name,
                'url': channel.url
            })
            #
            # { '1': {'channels': [ { 'id': 100, 'name': '手机','url': url}
            #  ， 'id': 101, 'name': '相机','url': url}  ],
            #  'sub_cats': []
            #   '2' : {'channels': [  { 'id': 102, 'name': '电脑','url': url} ], 'sub_cats': []}
            # }

            # 查询二级和三级类别
            for cat2 in cat1.subs.all():  # 从一级类别找二级类别
                cat2.sub_cats = []  # 给二级类别添加一个保存三级类别的列表
                for cat3 in cat2.subs.all():  # 从二级类别找三级类别
                    cat2.sub_cats.append(cat3)  # 将三级类别添加到二级sub_cats

                # 将二级类别添加到一级类别的sub_cats
                categories[group_id]['sub_cats'].append(cat2)

        # 查询首页广告数据
        # 查询所有的广告类别
        contents = OrderedDict()
        content_categories = ContentCategory.objects.all()
        for content_category in content_categories:
            # 使用广告类别查询出该类别对应的所有的广告内容
            contents[content_category.key] = content_category.content_set.filter(
                status=True).order_by('sequence')  # 查询出未下架的广告并排序
            # 链式查询  QuerySet.filter()    QuerySet

        # 构造上下文
        # from contents.utils import get_categories
        # categories = get_categories()
        context = {
            'categories': categories,
            'contents': contents
        }

        return render(request, 'index.html', context)
