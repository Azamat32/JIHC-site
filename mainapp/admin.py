from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class clubImageAdmin(admin.StackedInline):
    model = clubImage
 
@admin.register(clubs_page_form)
class clubAdmin(admin.ModelAdmin):
    inlines = [clubImageAdmin]
 
    class Meta:
       model = clubs_page_form

class NewsAdmin(TranslationAdmin):
    prepopulated_fields = {'slug':('title',)}  
@admin.register(clubImage)
class clubImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ValounterVideo)
admin.site.register(clubs_page_video)
admin.site.register(students_life_img)
admin.site.register(For_parents)
admin.site.register(students_life_description)
admin.site.register(SwiperImg)
admin.site.register(TalapkerPost)
admin.site.register(NewsBigPost)
admin.site.register(NewsLongPost)
admin.site.register(NewsShortPost)
admin.site.register(NavList)
admin.site.register(NewsPostForm,NewsAdmin)

admin.site.register(Gallery)
admin.site.register(TalapkerPageTable)
admin.site.register(StudentPageForm)