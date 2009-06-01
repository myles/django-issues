from django.db import models
from django.conf import settings
from django.db.models import permalink
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.generic import GenericRelation

class Version(models.Model):
	name = models.CharField(_('name'), max_length=200)
	slug = models.SlugField(_('slug'), max_length=50, unique=True)
	description = models.TextField(_('description'), blank=True, null=True)
	url = models.URLField(_('url'), blank=True, null=True)
	date = models.DateField(_('date'), blank=True, null=True)
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		db_table = 'issue_versions'
		ordering = ('date',)
		verbose_name = _('version')
		verbose_name_plural = _('versions')
	
	def __unicode__(self):
		return u"%s" % (self.name)
	
	@permalink
	def get_absolute_url(self):
		return ('issues_version_detail', None, {
			'slug': self.slug,
		})

class Category(models.Model):
	name = models.CharField(_('name'), max_length=200)
	slug = models.SlugField(_('slug'), max_length=50, unique=True)
	assigned = models.ForeignKey(User, blank=True, null=True,
		related_name='category_assigned')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		db_table = 'issue_categories'
		ordering = ('name',)
		verbose_name = _('category')
		verbose_name_plural = _('categories')
	
	def __unicode__(self):
		return u"%s" % (self.name)
	
	@permalink
	def get_absolute_url(self):
		return ('issue_category_detail', None, {
			'slug': self.slug,
		})

ISSUE_STATUSES = (
	(1, _('New')),
	(2, _('Assigned')),
	(3, _('Resolved')),
	(4, _('Feedback')),
	(5, _('Closed')),
	(6, _('Rejected')),
)

ISSUE_PRIORITIES = (
	(1, _('Low')),
	(2, _('Normal')),
	(3, _('High')),
	(4, _('Urgent')),
	(5, _('Immediate')),
)

# TODO I want this it first check the `settings.py` file for customization.
ISSUE_STATUS_CHOICES = ISSUE_STATUSES
ISSUE_PRIORITIY_CHOICES = ISSUE_PRIORITIES

class Issue(models.Model):
	subject = models.CharField(_('subject'), max_length=200)
	description = models.TextField(_('description'), blank=True, null=True)
	
	version = models.ForeignKey(Version, blank=True, null=True)
	category = models.ForeignKey(Category, blank=True, null=True)
	
	created = models.ForeignKey(User, related_name='created')
	assigned = models.ForeignKey(User, blank=True, null=True,
		related_name='issue_assigned')
	watcher = models.ManyToManyField(User, blank=True, null=True,
		related_name='watchers')
	
	start_date = models.DateField(_('start'), blank=True, null=True,
		help_text=_('The date to start working on the issue.'))
	due_date = models.DateField(_('due date'), blank=True, null=True,
		help_text=_('The date the issue is due.'))
	
	status = models.IntegerField(_('status'), choices=ISSUE_STATUS_CHOICES,
		default=1)
	priority = models.IntegerField(_('priority'),
		choices=ISSUE_PRIORITIY_CHOICES, default=2)
	
	comment = GenericRelation(Comment, object_id_field='object_pk')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		db_table = 'issues'
		ordering = ('due_date', 'priority',)
		verbose_name = _('issue')
		verbose_name_plural = _('issues')
	
	def __unicode__(self):
		return u"[%s] %s" % (self.pk, self.subject)
	
	@permalink
	def get_absolute_url(self):
		return ('issues_issue_detail', None, {
			'pk': self.pk,
		})
