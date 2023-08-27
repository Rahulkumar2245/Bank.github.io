from django.contrib import admin
from bank_api.models import Branch,Bank

# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display=['name']

    search_fields=('name',)  


class BranchAdmin(admin.ModelAdmin):
    list_display=('branch','ifsc')

    list_filter=['branch']   



admin.site.register(Branch,BranchAdmin)
admin.site.register(Bank,BankAdmin)
