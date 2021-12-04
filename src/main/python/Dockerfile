FROM archlinux
COPY . /app
WORKDIR /app
RUN pacman -Syu --noconfirm
RUN pacman -S gcc python python-pip libglvnd --noconfirm
RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]