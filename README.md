Fetches favicon from www.python.org website and saves it into ```/tmp/favicon``` directory.  To run the application:  
Build an image and tag it as ```favicon```:
```
docker build -t favicon .
```
When creating a container specify a source directory on your host and bind it with ```/tmp/favicon``` directory inside a container:
```
docker run -d --name favicon --mount type=bind,source="$(pwd)"/data,target=/tmp/favicon favicon:latest
```
