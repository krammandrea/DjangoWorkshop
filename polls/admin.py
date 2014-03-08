from django.contrib import admin
from polls.models import Poll, Choice, Author

# another option is StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 

class PollAdmin(admin.ModelAdmin):
    # group the form fields 
    fieldsets = [
        (None, {"fields": ['question']}),
        ('Information', {"fields": ['pub_date', 'author']})
        ]
    inlines = [ChoiceInline] # create Choices at the same time as creating a new Poll 

    # display all the entries/rows in the change_list page in this format 
    list_display = ('question', 'author', 'pub_date', 'was_published_recently')
    # list_display = ('question')

    # adds filters on the sidebar 
    # filters depend on the field type
    list_filter = ['pub_date']   #date 
    search_fields = ['question'] #char


# Edit, remove and add data in the admin page /admin/polls
admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice) #removed because of added inlines  = [ChoiceInline]
admin.site.register(Author) 