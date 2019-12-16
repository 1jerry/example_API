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
* [X] Write unit tests for the service.
  * run with ```pytest```  (not complete yet)
* [X] Generate a code coverage report.
  * run with ```pytest --cov=main .```
* [X] The user JSON can just be id, first name, last name, zip code, and email address.
  * see /users
## run public service
- http://api.4im.im
- Docker running on Azure
## run in local Docker
- docker build -t example-api.v1 .
- docker run -it --rm --name running-api  -p 5000:80 example-api.v1
- access at http://localhost:5000
## install locally
- "git clone" or degit this repository
- using pipenv from this directory
  - pipenv install
- using standard Python
  - create a virtual environment (venv)
    - python3 -m venv <*name of your new venv*>
    - -or-
    - from your cloned directory: ```python3 -m venv .venv```
  - activate your venv
    - source .venv/Scripts/activate 
      - or ```.venv\Scripts\activate``` on Windows
      - or replace the ".venv" with the name you gave your venv
  - make sure your venv was activated.  It will display the name in parenthesis on the command prompt.
  - install packages from your cloned directory
    - pip install -r requirements.txt
## run locally
- if venv is activated
  - unicorn main:app
  - when all done running, use command ```deactivate``` to stop using your venv
- if using pipenv
  - pipenv run uvicorn main:app
- access at http://localhost:8000
