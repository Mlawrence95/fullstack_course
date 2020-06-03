from django.contrib import admin

from videos.models import Movie, Customer
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    # change order
    fields = ['release_year','title', 'length']

    # can search by these in admin panel
    search_fields = ['title', 'release_year']

    # filter by these in the admin panel
    list_filter = ['release_year', 'length']

    # which metadata to show for each model
    list_display = ['title', 'length', 'release_year']

    # these fields can be changed in the list view
    list_editable = ['length']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Customer)
