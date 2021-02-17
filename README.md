# shoppinglist
Shopping list app to learn Flask and deployment using Docker

To build: 
```
docker build --tag shoppinglist .
```

To run:

```
docker run --name shoppinglist -d -p 5000:5000 shoppinglist:latest
```

