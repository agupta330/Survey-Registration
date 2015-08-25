from django.contrib import admin
from Survey.models import UserProfile
from Survey.models import Survey, SurveyFields


class ChoiceInline(admin.TabularInline):
    model = SurveyFields
    extra = 1


class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['survey_name']}),
        ('Date information', {'fields': ['end_date'], 'classes': ['collapse']}),
        ('Survey information', {'fields': ['survey_description'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['survey_name','survey_description','end_date']

# Register your models here.
admin.site.register(Survey, SurveyAdmin)
admin.site.register(UserProfile)
