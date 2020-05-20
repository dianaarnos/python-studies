# Exercises from the book [Thinking Python 2ed](https://greenteapress.com/wp/think-python-2e/)

Each chapter has it's own folder.

> **Disclaimer:** Most of the solutions are different from the ones presented by the author since they are my own implementations.

## To run the scripts:

1. Build the docker image
2. Run the container with:
   - Docker:
     - To go straight into python interactive shell: `docker run -it --rm <tagname>` 
     - To go to bash and run scripts from there: `docker run -it --rm <tagname> /bin/sh`
   - docker-compose:
     - `docker-compose up -d`
     - To access the container and run your scripts: `docker-compose exec python /bin/sh`