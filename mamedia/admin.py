from django.contrib import admin
from post.models import *
from user.models import *


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comments)