from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin
from .models import Item
from .models import Item1

# Register your models here.
class mysoftwareAdmin(admin.ModelAdmin):
    list_display = ('id','software_title','software_description','software_picture','software_date')
admin.site.register(mysoftware,mysoftwareAdmin)


class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','category_picture','category_date')
admin.site.register(category,categoryAdmin)

class studentbatchAdmin(admin.ModelAdmin):
    list_display = ('id','batch_name')
admin.site.register(studentbatch,studentbatchAdmin)

class mylecturesAdmin(admin.ModelAdmin):
    list_display = ('id','video_category','video_batch','vlink','thumbnail','video_description','added_date')
admin.site.register(mylectures,mylecturesAdmin)

class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Item,MyModelAdmin)

class MyAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Item1,MyAdmin)



class batchtimingAdmin(admin.ModelAdmin):
    list_display = ('id','batch','clink','timing','start_date')
admin.site.register(batchtiming,batchtimingAdmin)















