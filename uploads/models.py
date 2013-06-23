from django.db import models

# Create your models here.
class Upload(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	caption = models.TextField()
	image = models.ImageField(upload_to='uploads/%Y/%m/%d')
	uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
	approved = models.BooleanField(default=False)

	class Meta:
		ordering = ["-uploaded_at", "name"]

	def __unicode__(self):
		return self.name

	def admin_image(self):
		return '<a href="/media/' + str(self.image) +\
			'"><img src="/media/' + str(self.image) +\
			'" height="100"/></a>'
	admin_image.short_description = 'Image'
	admin_image.allow_tags = True