# API code exercise
### create a microservice with the following
* [X] A User REST resource that allows clients to create, read, update, delete a user or a list of users.
  * see API documentation at /redoc 
  * try each end point at /docs
* [X] You can use a database of your choice but it's also fine to just use a map or dictionary in memory to keep track of users by their ids.
  * currently just internal
* [ ] Use structured logging
* [X] Add Metrics (such as dropwizard, codahale, or prometheus to time routes)
  * Prometheus raw metrics at /metrics/
* [ ] Write unit tests for the service.
* [ ] Generate a code coverage report (for Java you can use the jacoco-maven-plugin for unit test coverage).
* [X] The user JSON can just be id, first name, last name, zip code, and email address.
  * see /users
## run public service
- http://api.4im.im
- Docker running on Azure
## run in local Docker
- docker build -t example-api.v1 .
- docker run -it --rm --name running-api  -p 5000:80 example-api.v1
- access at http://localhost:5000
## run locally
- using pipenv
  - pipenv install
  - pipenv run uvicorn main:app --reload --loop asyncio
  - access at http://localhost:8000
