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



class Designers(models.Model):
    name= models.CharField(max_length=32)
    image= models.ImageField(upload_to=upload_image_path)

class AboutUs(models.Model):
    description= models.TextField(max_length=500)
    main_image= models.ImageField(upload_to=upload_image_path)
    bottom_image=models.ImageField(upload_to=upload_image_path)
