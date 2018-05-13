from django.db import models
from django.utils import timezone
from .forms import BlogPostForm
from django.conf import settings

class Post(models.Model):
	"""
	Here we'll define our Post model
	"""

	# author is linked to a registered
	# user in the 'auth_user' table.
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateTimeField(blank=True, null=True)
	views = models.IntegerField(default=0) # Record how often a post is seen
	tag = models.CharField(max_length=30, blank=True, null=True)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title

	def new_post(request):
    		form = BlogPostForm()
    		return render(request, 'blogpostform.html', {'form': form})