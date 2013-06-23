from django.contrib import admin
from .models import Upload

class UploadAdmin(admin.ModelAdmin):
	date_hierarchy = "uploaded_at"
	list_display = ["approved", "name", "email", "caption", "admin_image"]
	list_display_links = ["name"]
	list_editable = ["approved"]
	list_filter = ["approved", "name", "email", "uploaded_at"]
	search_fields = ["name", "email"]

admin.site.register(Upload, UploadAdmin)