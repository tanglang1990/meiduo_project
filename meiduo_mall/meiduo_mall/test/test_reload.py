import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.dev")
django.setup()

from users.models import User

user1 = User.objects.get(id=5)
user2 = User.objects.get(id=5)

user1.first_name += 'tang'
user1.save()
print(user1.first_name)

print(user2.first_name)
print(dir(user2))
user2.refresh_from_db()
print(user2.first_name)
