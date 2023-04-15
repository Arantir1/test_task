# pull official base image
FROM python:3.8.10

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . .

# install dependencies
# RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["/usr/src/app/main.py"]

ENTRYPOINT ["python"]