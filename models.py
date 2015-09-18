from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group, User
import datetime

# class Role(Group):
# Source:
# http://stackoverflow.com/a/2182418
#     rank = models.IntegerField(default=1)
#     description = models.TextField(default='')

#     def __str__(self):
#         return self.name
# Source:
# http://stackoverflow.com/a/2182418


class CampaignUser(models.Model):

    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
    is_approved = models.BooleanField(default=False)
    is_agreed = models.BooleanField(default=False)

    class Meta:

        db_table = 'campaign_user'


class Organization(Group):

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'organization'


class Role(Group):
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    note = models.TextField(null=True)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')
    last_accessed = models.DateTimeField(default=timezone.now())

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    organization = models.ForeignKey(Organization, null=True)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.title
