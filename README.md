# Docker_Experiments
This Repository is for learning Docker from beginner to advance

## Docker Installation
- [Docker Installation](https://docs.docker.com/engine/install/)


## Docker Commands for creating image

```
docker build -t <image_name> .
```
* Make sure that Dockerfile is present in the current directory
* Here -t is for tagging the image
* Here <image_name> is the name of the image which we want to create
* Here . is the current directory

## Docker Commands for running container

``` 
docker run -d <image_name>

```
* Here -d is for running container in background or detached mode
* Here <image_name> is the name of the image which we want to run
* If we want to run container in interactive mode then we can use -it instead of -d
* If we want to run container in interactive mode with port mapping then we can use -it -p <host_port>:<container_port> instead of -d
* Here interactive mode means we can interact with the container using terminal
* Here -p is for port mapping
* Here <host_port> is the port of the host machine
* Here <container_port> is the port of the container
* If we want to run container in interactive mode with volume mapping then we can use -it -v <host_path>:<container_path> instead of -d
* Here -v is for volume mapping

## Docker Commands for checking running containers

```
docker ps
```
## Docker Commands for checking all containers

```
docker ps -a
```

## Docker Commands for stopping container

```
docker stop <container_id>
```
## Docker Commands for removing container

``` 
docker rm <container_id>
```
## Docker Commands for removing image

```
docker rmi <image_id>
```
## Docker Commands for checking logs of container

```
docker logs <container_id>
```
## Docker Commands for renaming image

``` 
docker tag <old_image_name> <new_image_name>
```
## Docker Commands for pushing image to docker hub

```
docker push <image_name>
```
## Docker Commands for pulling image from docker hub

```
docker pull <image_name>
```
## Docker Commnds for naming container

```
docker run -d --name <container_name> <image_name>
```

## Docker Commands for checking container details

```
docker inspect <container_id>
```
## Docker Commands for checking image details

```
docker inspect <image_id>
```
## Docker Commnds for creating Network

``` 
docker network create <network_name>
```
## Docker Commands for checking networks

``` 
docker network ls
```
## Docker Commands for removing network

```
docker network rm <network_name>
```
## Docker Commands for checking network details

```
docker network inspect <network_name>
```
## Docker Commands for attaching network to container 

``` 
docker network connect <network_name> <container_name>
```

## Docker Commands for detaching network from container

```
docker network disconnect <network_name> <container_name>
```
## Docker Commands for Running container with network

```
docker run -d --name <container_name> --network <network_name> <image_name>
```

## Docker Commands for checking container IP

```
docker inspect <container_name> | grep "IPAddress"
```

## Docker with multiple containers

### Here I have used MySQL as a database and Python code to connect with MySQL database as a another container

### Steps to run the code

### First Run the MySQL container

```
docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=<database_name> --network <network_name> mysql
```

### Then Run the Python container

``` 
docker build -t <image_name> .
docker run -d --name <container_name> --network <network_name> <image_name>
```

### Port Mapping

```
docker run -d --name <container_name> -p <host_port>:<container_port> <image_name>
```

### Volume Mapping

```
docker run -d --name <container_name> -v <host_path>:<container_path> <image_name>
```

### Docker Compose

### Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.
