from django.contrib import admin

# Register your models here.
# all models must be imported before they can be used as urls
from .models import profile


class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile, profileAdmin)
