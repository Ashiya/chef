from django.contrib import admin
from chef.models import Chef, Recipe

class ChefAdmin(admin.ModelAdmin):

    list_display = ('email', 'name','specialized_in' , 'created_at')


class RecipeAdmin(admin.ModelAdmin):

    list_display = ('chef', 'name', 'steps_to_make', 'created_at')

admin.site.register(Chef, ChefAdmin)
admin.site.register(Recipe, RecipeAdmin)
