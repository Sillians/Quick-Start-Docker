## Compose sample application

### Python/Flask application

Project structure:
```
├── docker-compose.yaml
├── README.md
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

Docker compose yaml file
```
services: 
  web: 
    build: app 
    ports: 
      - '5000:5000'
```

#### Deploy with docker-compose
`docker-compose up -d`
``` Creating network "flask-compose_default" with the default driver
Building web
[+] Building 97.7s (11/11) FINISHED


WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating flask-compose_web_1 ... done
```

After the application starts, navigate to `http://localhost:5000` in your web browser or run:

`$ curl localhost:5000`
``` Hello Sillians World!
```

Stop and remove the containers
`$ docker-compose down`