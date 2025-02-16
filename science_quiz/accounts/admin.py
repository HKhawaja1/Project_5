from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")  # Columns in the list view
    list_filter = ("created_at",)  # Filter by creation date
    search_fields = ("name", "email", "phone")  # Search bar functionality
    readonly_fields = ("created_at",)  # Prevent editing the timestamp
    ordering = ("-created_at",)  # Order by newest messages first
    list_per_page = 20  # Number of messages per page

    # Remove add and edit permissions
    def has_add_permission(self, request):
        return False  # Disable "Add" button

    def has_change_permission(self, request, obj=None):
        return False  # Disable editing

    def has_delete_permission(self, request, obj=None):
        return False  # Disable deletion (optional)
    
    fieldsets = (
        ("Contact Information", {
            "fields": ("name", "email", "phone"),
            "classes": ("wide",)
        }),
        ("Message", {
            "fields": ("message",),
            "classes": ("collapse",)
        }),
        ("Metadata", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )

admin.site.register(ContactMessage, ContactMessageAdmin)
