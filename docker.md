boot2docker up
boot2docker ssh
docker build -t BUILD_NAME .
docker run --name NAME  -t BUILD_NAME -P
docker ps
docker exec -i -t INSTANCE_ID bash
