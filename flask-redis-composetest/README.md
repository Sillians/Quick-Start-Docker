### Edit the Compose file to add a bind mount
The new `volumes key` mounts the project directory (current directory) on the host to `/code` inside the container, allowing you to modify the code on the fly, without having to rebuild the image. The environment key sets the `FLASK_ENV` environment variable, which tells flask run to run in development mode and reload the code on change. This mode should only be used in development.

### Update the application
Because the application code is now mounted into the container using a volume, you can make changes to its code and see the changes instantly, without having to rebuild the image.

### Experiment with some other commands
If you want to run your services in the background, you can pass the -d flag (for “detached” mode) to 

`docker-compose up` 

and use `docker-compose ps` to see what is currently running:


You can bring everything down, removing the containers entirely, with the down command. Pass --volumes to also remove the data volume used by the Redis container:

` $ docker-compose down --volumes `