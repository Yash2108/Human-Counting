# Human Counting

Project to create a webapp which detects and counts human in images and videos.
Currently experimenting with YOLO ~~2 ML models: Pointrend (ResNet backbone) & OpenCV's HOG descriptor~~

#### Install the dependencies by :

``pip install -r requirements.txt``

Download the yolov3.weights from [here](https://pjreddie.com/media/files/yolov3.weights) and place it in `humancounter/` folder

### To run the Selenium automation

1. Please download the respective chromedriver from [this link](https://chromedriver.chromium.org/downloads)  and place it in `humancounter/` folder

2. The image being used for automation is `humancounter/upload_test.jpg`. Please replace this with your choice of image and change its name to the one mentioned before.

3. Run `python automate_selenium.py`

#### To run this on a Django Server :

``python manage.py runserver``

#### To run this on Docker :

1. Run ``docker run -d --name myapp ncmohit/capstoneproject -p 8000:8000 myapp``
