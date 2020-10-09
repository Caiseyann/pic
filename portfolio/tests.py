from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):

    """
    A test that checks for the
    """

    def setUp(self):
        pass


class CategoryTestClass(TestCase):
    """
    A test  that checks the 
    """

    def setUp(self):
        pass


class ImageTestClass(TestCase):
    def setUp(self):
        pass

        # Creating a new category and saving it
        self.new_category = Category(name='birds')
        self.new_category.save()

        # Creating a new location and saving it
        self.new_location = Location(name='nakuru')
        self.new_location.save()

        # Creating new Image and saving it
        self.new_image = Image(title='flamigo',
        description='The pink flamigo')
        self.new_image.save()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()
