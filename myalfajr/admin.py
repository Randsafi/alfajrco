from django.contrib import admin
from .models import seeds # استورد النماذج التي تريد التسجيل بها

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name_s', 'catgory', 'classification','descript')  # الحقول الظاهرة في القائمة
    # list_filter = ('field1',)                     # إضافة فلتر جانبي
    #search_fields = ('field1', 'field2')          # إضافة بحث

admin.site.register(seeds, YourModelAdmin)
#admin.site.register(seeds) # تسجيل نموذج المنتج

