from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify


# Create your models here.
from auths.modules import generate_random_string


class Profile(models.Model):
    sex = [
        ("M", "Male"),
        ("F", "Female"),
        ("x", "Rather not say"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    secondary_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=30, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=4, blank=True)

    # social_media_links
    website = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    google = models.CharField(max_length=100, blank=True)
    snapchat = models.CharField(max_length=100, blank=True)
    tumblr = models.CharField(max_length=100, blank=True)
    pinterest = models.CharField(max_length=100, blank=True)
    reddit = models.CharField(max_length=100, blank=True)
    vimeo = models.CharField(max_length=100, blank=True)
    twitch = models.CharField(max_length=100, blank=True)
    soundcloud = models.CharField(max_length=100, blank=True)
    whatsapp = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=100, blank=True)
    stack_over_flow = models.CharField(max_length=100, blank=True)
    github_profile = models.CharField(max_length=100, blank=True)
    # social_media_links

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'username': self.username})

# company profile


class Company(models.Model):
    class Meta:
        verbose_name_plural = "Companies"
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    company_description = models.TextField(max_length=500, blank=True)
    company_address = models.CharField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.company_name+str(generate_random_string(10)))
        super(Company, self).save(*args, **kwargs)


class Application(models.Model):
    stats = [
        ("free", "Freemium"),
        ("premium", "Premium"),
    ]
    company = models.ForeignKey(Company, verbose_name="company", on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name="subscribers", blank=True)
    application_name = models.CharField(max_length=250, unique=True)
    token = models.CharField(max_length=200, blank=True)
    redirect_url = models.URLField(blank=True, help_text="Page you want to redirect to")
    domain = models.URLField(blank=True, help_text="Domain on which the app is located")
    status = models.CharField(max_length=10, choices=stats, default="free")
    company_logo = models.ImageField(
        upload_to='apps/', null=True, blank=True)
    client_id = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(User, related_name="creator", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    token_expiration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.company.company_name

    def save(self, *args, **kwargs):
        if not self.client_id:
            self.client_id =generate_random_string(25)
        if not self.token:
            self.token = generate_random_string(60)
        super(Application, self).save(*args, **kwargs)


# after creating a user, create a profile for that user automatically
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


