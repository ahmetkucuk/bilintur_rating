from django.contrib import admin
from listofmenu.models import Menu

# Register your models here.

class MenuAdmin( admin.ModelAdmin):
	fieldsets = [
		('Meal',	{'fields': ['meal']}),
		('Date',	{'fields': ['date_meal']}),
	]
admin.site.register( Menu, MenuAdmin)
