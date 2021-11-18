FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install torch==1.7.1 torchvision==0.8.2 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install libgl1 -y
RUN python manage.py migrate
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]