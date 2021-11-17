from django.test import TestCase
from .models import Train

class TrainTestCase(TestCase):
    def test_image_objects(self):
        first_obj = Train.objects.all().first()
        self.assertIsInstance(first_obj,Train)
