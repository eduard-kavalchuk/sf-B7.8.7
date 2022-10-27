Fetches favicon of a specified web site and saves it into a specified directory.  
To run the program as a standalone specify a website and directory as follows:
```
python main.py --src="<website>" --dst="<dest>"
```
e. g.
```
python main.py --src="https://www.python.org/" --dst="/tmp/favicon"
```

docker build .


docker run -d -p 9090:80 -p 9999:8080 --mount source=nginx-vol,target=/var/log/nginx/ --name=nginx_test nginx


Tag obtained image as "favicon"


docker run -d --name favicon --mount type=bind,source="$(pwd)",target=/tmp/favicon favicon:latest
