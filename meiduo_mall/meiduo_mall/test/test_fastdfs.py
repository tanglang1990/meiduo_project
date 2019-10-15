import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()

# 1. 导入FastDFS客户端扩展
from fdfs_client.client import Fdfs_client

# 2. 创建FastDFS客户端实例
# 绝对路径

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
client_config_path = os.path.join(BASE_DIR, 'utils', 'fastdfs', 'client.conf')
print(client_config_path)

client = Fdfs_client(client_config_path)  # 最好使用绝对路径，永远不会出问题
# 3. 调用FastDFS客户端上传文件方法
ret = client.upload_by_filename('../static/images/adv011.jpg')
print(ret)
