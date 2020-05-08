To run the scripts:

1. Build the docker image
2. Run the container with:
   - Docker:
     - To go straight into python interactive shell: `docker run -it --rm <tagname>` 
     - To go to bash and run scripts from there: `docker run -it --rm <tagname> /bin/sh`
   - docker-compose:
     - `docker-compose up -d`
     - To access the container and run your scripts: `docker-compose exec python /bin/sh`