## Capstone-2 Project

Project to create a webapp which detects and counts human in images and videos.
Currently experimenting with 2 ML models: Pointrend (ResNet backbone) & OpenCV's HOG descriptor

## Directly run docker image from dockerhub

```docker run ncmohit/capstoneproject```

## Run it Locally

### Copy the pickle file to location

To the directory traincrud/pointrend_resnet101.pkl

### Install the dependencies by

``pip install -r requirements.txt``

### Create Database

```python manage.py migrate```

### To run this on a Django Server:

``python manage.py runserver``

### To build docker image :

1. Build the image by ``docker build -t myapp .``
2. Run ``docker run --name myapp -p 8000:8000 myapp``
