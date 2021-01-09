from django.db import models
from django.utils.text import slugify
from datetime import date as dt
from PIL import Image as Images

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100, default=None)
    slug = models.SlugField(blank=True, editable=False, max_length=255)
    desc = models.TextField(default=None)
    date = models.DateField(auto_now_add=True)
    max_people = models.IntegerField(default=None)
    photo1 = models.ImageField(default=None, upload_to='thumbnail')
    photo2 = models.ImageField(default=None, upload_to='thumbnail', blank=True, null=True )
    photo3 = models.ImageField(default=None, upload_to='thumbnail', blank=True, null=True)
    # day1 = models.DateField(blank=True, default=dt(2020, 10, 18), null=True, help_text="Today Date.")
    day = models.CharField(max_length=100, default=None)
    Price = models.CharField(max_length=100, default=None)
    seat = models.CharField(max_length=20, default=None)
    meeting = models.CharField(max_length=256, default=None)
    special = models.BooleanField(default=False)
    special_desc = models.TextField(default=None, blank=True, null=True)
    special_desc = models.TextField(default=None, blank=True, null=True, max_length=620)

    # class Meta:
    #     verbose_name = u'Scheduling'
    #     verbose_name_plural = u'Scheduling'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

        all_image = []
        img = Images.open(self.photo1.path)
        all_image.append(img)
        try:
            img2 = Images.open(self.photo2.path)
            all_image.append(img2)
        except:
            pass

        try:
            img3 = Images.open(self.photo3.path)
            all_image.append(img3)
        except:
            pass

        for x in all_image:
            final = x.resize((1980, 1080))
            if x == img:
                final.save(self.photo1.path)
            elif x == img2:
                final.save(self.photo2.path)
            elif x == img3:
                final.save(self.photo3.path)

    def __str__(self):
        return "{}, {}, person {}".format(self.id, self.name, self.seat)

    snp = 85
    def snippet(self):
        return self.desc[:self.snp]

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.name

class carousel(models.Model):
    image = models.ImageField(default=None, upload_to='carousel')

    def __str__(self):
        return "{}".format(self.id)

    def save(self, *args, **kwargs):
        super(carousel, self).save(*args, **kwargs)
        img = Images.open(self.image.path)
        img = img.resize((1980, 1080))
        img.save(self.image.path)


class booking(models.Model):
    name = models.CharField(default=None, max_length=100)
    cus_id  = models.IntegerField(default=None)
    books_ids = models.CharField(default=None, max_length=50)
    trip_sids = models.CharField(default=None, max_length=50)
    seat_av = models.CharField(default=None, max_length=50)
    name_trip = models.CharField(default=None, max_length=100)
    price = models.CharField(default=None, max_length=20)
    day_go = models.CharField(default=None, max_length=20)
    meeting = models.CharField(max_length=256, default=None)
    payment = models.CharField(max_length=256, default=None)
    total_price = models.CharField(default=None, max_length=20)
    born = models.CharField(default=None, max_length=20)
    day = models.DateField(default=dt(2020, 10, 18))
    gender = models.CharField(default=None, max_length=10)
    address = models.CharField(default=None, max_length=255)
    email = models.EmailField(default=None)
    phone1 = models.IntegerField(default=None)
    phone2 = models.IntegerField(default=None)
    comment = models.TextField(default=None, max_length=255)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    people = models.CharField(default=None, max_length=5)

    class Meta:
        verbose_name = u'Booking'
        verbose_name_plural = u'Booking'

    def __str__(self):
        return '{} {}'.format(self.id, self.name)