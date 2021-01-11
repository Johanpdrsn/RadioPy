# Rest API for Motorola coding task

A rest API allowing to post devices, set their location and get the location of a device. Implemented in python 3.8 using flask and
sqlAlchemy with sqlite.

## Build

Steps to run the project:

1. Pull the repository `git clone https://github.com/Johanpdrsn/moto-rest-api.git`
2. Navigate to directory
3. Build docker image `docker build --rm --pull -f "./Dockerfile" -t "radiopy:latest" .`
4. Run the container `docker run --rm -d  -p 5000:5000/tcp radiopy:latest`


## Test

Example use of the api:

1. Add device `http://localhost:5000/radios/100` POST with payload `{
    "alias": "Radio100",
    "allowed_locations": ["CPH-1", "CPH-2"]
}`. This will return 201 CREATED and the added device.

2. Set location `http://localhost:5000/radios/100/location` POST with payload `{
    "location": "CPH-1".
}`. Returns 200 OK.

3. Get location `http://localhost:5000/radios/100/location` GET. Returns 200 OK and the location. 

