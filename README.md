# boilerplateflask-api

Modular based flask api boilerplate for Active Record and Repository patterns flask APIs. This boilerplate was inspired by clean architecture, Domain Driven Designed and ports and adapters. 

## Setting Up Local

#### Installing
    $ vim .bashrc
        alias load-env='export $(cat .env | xargs)'
        alias load-env-test='export $(cat .env.test | xargs)'
    $ cd boilerplateflask-api
    $ cp .env.sample .env
    $ cp .env.sample .env.test
    $ mkdir logs
    $ python3.8 -m venv boilerplateflask-api
    $ source boilerplateflask-api/bin/activate
    $ pip install -r requirements.txt
    $ pip install -r requirements_dev.txt

#### Running

    $ load-env
    $ python3 runner.py
    $ curl http://localhost:5324/api/items
    
#### Running tests

    $ load-env-test
    $ python3.8 -m unittest

## Setting up Docker

#### Installing

```
$ cp .env.sample .env.docker
$ docker-compose up --build -d
```

#### Running
```
$ docker-compose up
$ curl http://localhost:5324/api/items
``` 

### Running tests

```
$ docker-compose up
$ docker-compose exec boilerplate-web-api bash
```

This will take you inside the Web Container Bash.

```bash
$ python -m unittest
```
