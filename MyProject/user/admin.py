from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email','message')
admin.site.register(contactus,contactusAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','headlines','slider_dec','slider_picture')
admin.site.register(slider,sliderAdmin)

class newbatchesAdmin(admin.ModelAdmin):
    list_display = ('id','name','batch_pic','starting_date')
admin.site.register(newbatches,newbatchesAdmin)

class collegeAdmin(admin.ModelAdmin):
    list_display = ('id','college_name','college_picture')
admin.site.register(college,collegeAdmin)

class session_yearAdmin(admin.ModelAdmin):
    list_display = ('id','session')
admin.site.register(session_year,session_yearAdmin)

class batchAdmin(admin.ModelAdmin):
    list_display = ('id','batch_name')
admin.site.register(batch,batchAdmin)

class placementAdmin(admin.ModelAdmin):
    list_display = ('id','student_picture','student_name','college','session','batch','company_name','company_logo')
admin.site.register(placement,placementAdmin)


class registrationAdmin(admin.ModelAdmin):
    list_display = ('name','email','passwd','mobile','profile','course','pyear','college','batch','status','batchid')
admin.site.register(registration,registrationAdmin)

