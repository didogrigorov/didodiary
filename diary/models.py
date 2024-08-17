from datetime import timezone

from django.core.exceptions import ValidationError
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    date_posted = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('single-blog', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

class About(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def clean(self):
        if not self.pk and About.objects.exists():
            raise ValidationError('There can only be one About Us Content!')

    def save(self, *args, **kwargs):
        # Call the clean method to ensure that the validation error is raised
        self.clean()
        super(About, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.title