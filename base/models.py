from django.db import models
from django.utils.text import slugify

# Create your models here.
class Topic(models.Model):
    subject_choices = (
        ("chemistry","chemistry"),
        ("fauna", "fauna"),
        ("flora", "flora"),
        ("biology","biology"),
        ("astronomy","astronomy"),
        ("machinery","machinery"),
        ("default","default")
    )
    headline = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(max_length=200)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images")
    slug = models.SlugField(null=True, blank=True)
    key = models.CharField(max_length=50, null=True,blank=True)
    entry=models.CharField(max_length=200,null=True,blank=True)
    subject=models.CharField(max_length=200, choices=subject_choices, default='default')

    def __str__(self):
        return self.headline

    def save(self,*args,**kwargs) :
        if self.slug==None:
            slug = slugify(self.headline)
            has_slug = Topic.objects.filter(slug =slug).exists()
            count = 1
            while has_slug:
                count+=1
                # slugify(self.headline) += '-' + str(count)
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Topic.objects.filter(slug =slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)
