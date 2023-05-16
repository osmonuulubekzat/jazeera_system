from django.contrib import admin
from .models import *


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ('FirstName', 'LastName', 'Email',)
    # add filtering by date
    list_filter = ('date',)
    # add search field
    search_fields = ['FirstName']
    readonly_fields = ['date','FirstName', 'LastName', 'Email', 'PhoneNumber', "Region"]

admin.site.register(OurСlints, CommentAdmin)


