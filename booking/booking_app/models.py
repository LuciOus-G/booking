from django.db import models
from django.utils.text import slugify
from datetime import date as dt

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(blank=True, editable=False, max_length=255)
    desc = models.TextField(default='')
    date = models.DateField(auto_now_add=True)
    photo1 = models.ImageField(default='', upload_to='thumbnail')
    photo2 = models.ImageField(default='', upload_to='thumbnail', blank=True, null=True )
    photo3 = models.ImageField(default='', upload_to='thumbnail', blank=True, null=True)
    day1 = models.DateField(blank=True, default=dt(2020, 10, 18), null=True, help_text="Today Date.")
    # day = models.CharField(max_length=100, default='')
    Price = models.CharField(max_length=100, default='')
    seat = models.CharField(max_length=20, default='')
    meeting = models.CharField(max_length=256, default='')
    special = models.BooleanField(default=False)
    special_desc = models.TextField(default='', blank=True, null=True)
    special_desc = models.TextField(default='', blank=True, null=True, max_length=620)

    # class Meta:
    #     verbose_name = u'Scheduling'
    #     verbose_name_plural = u'Scheduling'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {}".format(self.id, self.name)


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.name

class carousel(models.Model):
    image = models.ImageField(default='', upload_to='carousel')

    def __str__(self):
        return "{}".format(self.id)

class booking(models.Model):
    name = models.CharField(default='', max_length=100)
    cus_id  = models.IntegerField(default='')
    born = models.CharField(default='', max_length=20)
    day = models.DateField(blank=True, default=dt(2020, 10, 18), null=True, help_text="Today Date.")
    gender = models.CharField(default='', max_length=10)
    address = models.CharField(default='', max_length=255)
    email = models.EmailField(default='')
    phone1 = models.IntegerField(default='')
    phone2 = models.IntegerField(default='')
    comment = models.TextField(default='', max_length=255)

    class Meta:
        verbose_name = u'Booking'
        verbose_name_plural = u'Booking'

    def __str__(self):
        return '{} {}'.format(self.id, self.name)