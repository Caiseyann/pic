from django.db import models
import datetime as dt
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update_category()


class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update_location()

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location


class Image(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    posted_date= models.DateTimeField(auto_now_add=True)
    ## defines where the image will be stored in the file system.
    category_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

  

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

##  method that will query the database and fetch our results.

    @classmethod
    def search_by_category(cls,search_term):
        portfolio = cls.objects.filter(category__name__icontains=search_term)
        return portfolio

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images


    @classmethod
    def get_image_by_id(cls,id):
        img_id = cls.objects.get(pk=id)
        return img_id

    # class Meta:
    #     ordering = ['first_name']
