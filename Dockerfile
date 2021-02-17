FROM ubuntu:20.04
RUN apt-get update -y && apt-get install -y python3-pip
MAINTAINER "Paul Cleary" drprcleary@gmail.com
COPY . /shoppinglist
WORKDIR /shoppinglist/app
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "shoppinglist.py" ]
