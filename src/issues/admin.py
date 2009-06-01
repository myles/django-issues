from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.comments.models import Comment

from issues.models import Category, Version, Issue

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'assigned',)
	list_filter = ('assigned',)
	search_field = ['^name',]
	prepopulated_fields = {'slug': ('name',)}

class VersionAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')
	list_filter = ('date',)
	search_field = ['^name',]
	prepopulated_fields = {'slug': ('name',)}

class CommentInline(generic.GenericStackedInline):
	model = Comment
	ct_fk_field = 'object_pk'

class IssueAdmin(admin.ModelAdmin):
	inlines = [
		CommentInline,
	]
	
	list_display = ('subject',)
	list_filter = ('status', 'priority', 'assigned')
	search_field = ['^subject',]
	
	def save_model(self, request, obj, form, change):
		if not change:
			obj.created = request.user
		
		if obj.category and not obj.assigned:
			obj.assigned = obj.category.assigned
		
		obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Issue, IssueAdmin)