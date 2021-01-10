# Rest API for Motorola coding task

A rest API allowing to post devices, set their location and get the location of a device.

## Build

Steps to run the project:

1. Pull the repository `git clone https://github.com/Johanpdrsn/moto-rest-api.git`
2. Navigate to directory
3. Build docker image `docker build --rm --pull -f "./Dockerfile" -t "radiopy:latest" .`
4. Run the container `docker run --rm -d  -p 5000:5000/tcp radiopy:latest`