# Commands Collection

## General
| Description                            | Example                                                    |
| -------------------------------------- | ---------------------------------------------------------- |
| List containers including stopped ones | ```docker ps -a```                                         |
| Start container                        | ```docker container start {container_id}```                |
| Start a bash session for the container | ```docker exec -it {container_id} bash```                  |
| Remove unused images                   | ```docker image prune```                                   |
| Remove unused(stopped) containers      | ```docker container prune```                               |
| Copy from container to host            | ```docker cp <container_id>:/path/to/file /path/on/host``` |

https://docs.docker.com/engine/reference/run/