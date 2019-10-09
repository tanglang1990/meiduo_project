import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()

from django.conf import settings
from django.core.mail import send_mail

def send_verify_email(to_email, verify_url):
    """
    发送验证邮箱邮件
    :param to_email: 收件人邮箱
    :param verify_url: 验证链接
    :return: None
    """
    subject = "美多商城邮箱验证"
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用美多商城。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
    try:
        # message是普通内容，就是你发什么，对应的邮箱就收到什么
        # html_message 是html的内容，你发的内容会被渲染html的页面展示出去
        # 二者选其一
        send_mail(subject, "", '美多商城<dailyfreshzxc@yeah.net>', [to_email], html_message=html_message)
    except Exception as e:
        print(e)

send_verify_email('782555894@qq.com', '链接')