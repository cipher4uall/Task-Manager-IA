from django.contrib import admin
from users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_photo')
    search_fields = ('user__username',)

admin.site.register(Profile, ProfileAdmin)
