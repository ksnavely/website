# Docker

Docker isn't used in the production deploy yet. It can be used for local development. I'm having issues specifically with exposing ports and the --publish flag of `docker run`.

Cheat sheet for using docker with the site:

```
boot2docker up
boot2docker ssh
docker build -t BUILD_NAME .
docker run --name NAME  -t BUILD_NAME -P
docker ps
docker exec -i -t INSTANCE_ID bash
```
