from django.db import models
from django.contrib.auth.models import User
from categories.models import models as categoryModels

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    category = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    # add in catalogue

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    def get_cat_list(self):           #for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]