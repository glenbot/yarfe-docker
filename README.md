Example for presentation purposes on how to deploy python applications using docker using a simple TCP python application

# Instructions on how to use example

## Development

* Start a virtual machine somewhere using Ubuntu 14.04 64-bit. This example assumes Digital Ocean.
* SSH into the machine
* Follow the steps below to bootstrap a development environment. The steps assume you have root privileges. In your HOME folder:

```bash
$ apt-get update
$ apt-get install git
$ apt-get install python-setuptools
$ easy_install pip
$ pip install fig
$ curl -sSL https://get.docker.com/ubuntu/ | sudo sh
$ git clone https://github.com/glenbot/yarfe-docker.git
$ cd yarfe-docker
$ fig build
$ fig up -d
```

# Building image for production

```bash
$ cd yarfe-docker
$ docker login
$ docker build -t "<yourusername>/yarfe-docker"
$ docker push "<yourusername>/yarfe-docker"
```

## Production

* Start a virtual machine somewhere using Ubuntu 14.04 64-bit. This example assumes Digital Ocean.
* SSH into the machine
* Follow the steps below to bootstrap a production environment. The steps assume you have root privileges. In your HOME folder:

```bash
$ apt-get update
$ apt-get install git
$ apt-get install python-setuptools
$ easy_install pip
$ pip install fig
$ curl -sSL https://get.docker.com/ubuntu/ | sudo sh
$ git clone https://github.com/glenbot/yarfe-docker.git
$ ln -s yarfe-docker/fig_production.yml fig.yml
$ docker login
$ fig up -d
```
