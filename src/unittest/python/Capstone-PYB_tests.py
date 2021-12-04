import django
django.setup()
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'traincrud')))

from traincrud import tests
obj = tests.TrainTestCase()
obj.test_image_objects()