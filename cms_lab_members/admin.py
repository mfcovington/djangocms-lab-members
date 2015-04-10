from django.contrib import admin

from lab_members.models import Scientist
from lab_members.admin import ScientistAdmin

class CMSScientistAdmin(ScientistAdmin):
    fieldsets = [
        ScientistAdmin.fieldset_basic,
        ScientistAdmin.fieldset_advanced,
    ]

admin.site.unregister(Scientist)
admin.site.register(Scientist, CMSScientistAdmin)
