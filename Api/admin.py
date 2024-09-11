from django.contrib import admin
from .models import (Testimonal,WorkExperience,Work,Skill,About,Contact,Brand,Experience)
# Register your models here.
class AdminTestmonies(admin.ModelAdmin):
    list_display=["name","campany"]
admin.site.register(Testimonal,AdminTestmonies)

class AdminWorkExperience(admin.ModelAdmin):
    list_display=["name","campany"]
admin.site.register(WorkExperience,AdminWorkExperience)

class AdminWorks(admin.ModelAdmin):
    list_display=["title","projectLink"]
admin.site.register(Work,AdminWorks)

class AdminBrands(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Brand,AdminBrands)

class AdminAbouts(admin.ModelAdmin):
    list_display=["title"]
admin.site.register(About,AdminAbouts)

class AdminContacts(admin.ModelAdmin):
    list_display =['name',"email"]
admin.site.register(Contact,AdminContacts)

class AdminSkills(admin.ModelAdmin):
    list_display=["name","bgColor"]
admin.site.register(Skill,AdminSkills)

class AdminExperiences(admin.ModelAdmin):
    list_display=["year"]
admin.site.register(Experience,AdminExperiences)



