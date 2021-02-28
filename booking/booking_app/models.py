from django.db import models
from django.utils.text import slugify
from datetime import date as dt
from PIL import Image as Images
import string,random
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100, default=None)
    slug = models.SlugField(blank=True, editable=False, max_length=255)
    desc = models.TextField(default=None)
    date = models.DateField(auto_now_add=True)
    max_people = models.IntegerField(default=None)
    photo1 = models.ImageField(default=None, upload_to='thumbnail')
    # day1 = models.DateField(blank=True, default=dt(2020, 10, 18), null=True, help_text="Today Date.")
    departure_day = models.DateField(default=dt(2020, 10, 18))
    Price = models.IntegerField(default=None)
    seat = models.CharField(max_length=20, default=None)
    meeting = models.CharField(max_length=256, default=None)
    special = models.BooleanField(default=False)
    special_desc = models.TextField(default=None, blank=True, null=True)
    special_desc = models.TextField(default=None, blank=True, null=True, max_length=620)
    Token = models.CharField(max_length=255, unique=True, blank=True, editable=False, default='')

    class Meta:
        verbose_name = u'Trip'
        verbose_name_plural = u'Trip'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.Token == '':
            self.Token = self.randomGenerate()
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

    def randomGenerate(self, size=25, chars=string.ascii_letters + string.digits):
        slug = list(Post.objects.all())
        generate = ''.join(random.choice(chars) for _ in range(size))
        qs = Post.objects.filter(Token=generate).exists()
        if qs:
            randomGenerate(size=size + 1)
        return generate

class PostImage(models.Model):
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.id)

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
    name_trip = models.CharField(default=None, max_length=100)
    seat_available = models.CharField(default=None, max_length=50)
    price = models.CharField(default=None, max_length=20)
    place_born = models.CharField(default=None, max_length=20)
    day_born = models.CharField(default=None, max_length=15)
    gender = models.CharField(default=None, max_length=10)
    address = models.CharField(default=None, max_length=255)
    phone1 = models.CharField(default=None,max_length=255)
    people = models.CharField(default=None, max_length=5)
    # automatic
    user_name = models.CharField(default=None, max_length=100)
    customer_id  = models.CharField(default=None,max_length=255)
    booking_id = models.CharField(default=None, max_length=50)
    trip_id = models.CharField(default=None, max_length=50)
    departure_day = models.CharField(default=None, max_length=20)
    meeting_point = models.CharField(max_length=256, default=None)
    total_price = models.CharField(default=None, max_length=20)
    email = models.CharField(default=None,max_length=255)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    # day = models.DateField(default=dt(2020, 10, 18))

    # class Meta:
    #     verbose_name = u'Booking'
    #     verbose_name_plural = u'Booking'

    def __str__(self):
        return '{} {}'.format(self.id, self.user_name)

class test(models.Model):
    name = models.CharField(default=None, max_length=100)
