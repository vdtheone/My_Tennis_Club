from django.contrib import admin
from .models import ContactUs, Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'joined_date')
    prepopulated_fields = {"slug": ("first_name", "last_name")}

admin.site.register(Member, MemberAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(ContactUs, ContactUsAdmin)
