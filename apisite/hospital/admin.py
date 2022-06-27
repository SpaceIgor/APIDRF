from django.contrib import admin
from .models import Doctor, Direction


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name_direction')
    list_display_links = ('id', 'name_direction')
    list_filter = ('id', 'slug', 'name_direction')
    search_fields = ('id', 'slug', 'name_direction')

    prepopulated_fields = {'slug': ('name_direction', )}


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_doctor', 'directions', 'slug', 'date_of_birth', 'experience', 'description')
    list_display_links = ('id', 'name_doctor')
    ordering = ('id', 'name_doctor', 'slug', 'date_of_birth', 'experience', 'description')
    list_filter = ('id', 'name_doctor', 'slug', 'date_of_birth', 'experience', 'description')
    search_fields = ('id', 'name_doctor', 'directions', 'slug', 'date_of_birth', 'experience', 'description')
    prepopulated_fields = {'slug': ('name_doctor', )}

    def directions(self, obj):
        return "\n".join([item.name_direction for item in obj.direction.all()])


admin.site.register(Direction, DirectionAdmin)
admin.site.register(Doctor, DoctorAdmin)


