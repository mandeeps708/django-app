from django.contrib import admin

# Register your models here.
from .models import roll

class rollAdmin(admin.ModelAdmin):
	list_display=['name', 'college_Rollno', 'age', 'email','timestamp', 'updated']
	class Meta:
		model = roll

admin.site.register(roll, rollAdmin)