## Compose sample application

### Python/FastAPI application
Project structure:

```
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
├── app
    ├── main.py
    ├── __init__.py
```

#### Docker compose yaml file

```
services:
  api:
    build: .
    container_name: fastapi-application
    environment:
      PORT: 8000
    ports:
      - '8000:8000'
    restart: "no"
```


#### Deploy with docker-compose

`docker-compose up -d --build`

After the application starts, navigate to http://localhost:8000 in your web browser and you should see the following json response:

```
{
"Hello": "San Francisco!!!"
}
```

Stop and remove the containers

`docker-compose down`