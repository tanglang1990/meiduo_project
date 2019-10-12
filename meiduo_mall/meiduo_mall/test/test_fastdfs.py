import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()

# 1. 导入FastDFS客户端扩展
from fdfs_client.client import Fdfs_client

# 2. 创建FastDFS客户端实例
client = Fdfs_client('../utils/fastdfs/client.conf')
# 3. 调用FastDFS客户端上传文件方法
ret = client.upload_by_filename('../static/images/adv01.jpg')
print(ret)
