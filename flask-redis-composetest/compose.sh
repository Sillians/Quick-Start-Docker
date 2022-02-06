#!/bin/bash
docker-compose -f docker-compose.yml up -d

"""
Compose pulls a Redis image, builds an image for your code, and starts the services you defined. 
In this case, the code is statically copied into the image at build time.

"""
