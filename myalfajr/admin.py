from django.contrib import admin
from .models import Fertilizers,seeds # استورد النماذج التي تريد التسجيل بها

admin.site.register(seeds) # تسجيل نموذج المنتج
admin.site.register(Fertilizers) # تسجيل نموذج التصنيف
