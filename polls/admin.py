from django.contrib import admin
from polls.models import Poll, Choice, Author

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Author)
# Register your models here.
