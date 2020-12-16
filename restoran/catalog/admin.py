from django.contrib import admin

# Register your models here.
from .models import  Type, Food, TableInstance, Drink, Table

#admin.site.register(Food)
admin.site.register(Type)
#admin.site.register(TableInstance)
#admin.site.register(Drink)
#admin.site.register(Table)

# Define the admin class
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    fields = ['name', 'Cost', 'Type', 'summary']
    list_display = ('name', 'Cost', 'Type')

# Register the Admin classes for Book using the decorator

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    fields = ['name', 'Cost', 'Type', 'summary']
    list_display = ('name', 'Cost', 'Type')

class TableInstanceInline(admin.TabularInline):
    model = TableInstance

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    inlines = [TableInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(TableInstance)
class TableInstanceAdmin(admin.ModelAdmin):
    list_display = ('table', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')
fieldsets = (
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )