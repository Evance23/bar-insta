from django.contrib import admin

# Register your models here.
from .models import Profile,Images,Comments,Follow
admin.site.register(Profile)
admin.site.register(Images)
admin.site.register(Comments)
admin.site.register(Follow)
