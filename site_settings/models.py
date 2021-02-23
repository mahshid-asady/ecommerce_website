import os

from django.db import models


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class MainLogo(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to=upload_image_path)





class SocialLinks(models.Model):
    about_us_short_cut = models.TextField(max_length=10000)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
