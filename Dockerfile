FROM ubuntu:20.04
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD [ "shoppinglist.py" ]
