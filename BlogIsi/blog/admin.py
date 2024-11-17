from django.contrib import admin
from blog.models import Form
# Register your models here.

admin.site.site_title = "صفحه ادمین "
admin.site.site_header = "بخش ادمین ها"
admin.site.index_title = "Site Administration"
class FormAdmin(admin.ModelAdmin):
    list_display = ('last_name',
                    'field',
                    'degree', "subject",
                    'phone_number', 'is_done', 'created_on')
    search_fields = ('last_name', 'field', 'degree', "subject", 'phone_number',)
    list_filter = ("is_done", "created_on",)


admin.site.register(Form, FormAdmin)