# Capstone-2 Project

Project to create a webapp which detects and counts human in images and videos.
Currently experimenting with 2 ML models: Pointrend (ResNet backbone) & OpenCV's HOG descriptor

#### Install the dependencies by :

``pip install -r requirements.txt``

#### To run this on a Django Server :

``python manage.py runserver``

#### To run this on Docker :

1. Run ``docker run -d --name myapp ncmohit/capstoneproject -p 8000:8000 myapp``
