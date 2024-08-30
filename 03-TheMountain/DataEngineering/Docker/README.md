# Docker Survival Guide

## Introduction

[Docker](https://www.docker.com/) has now become an unavoidable tool in many development environments as well as in modern server hosting.

There are very good reasons to this. Well used it can greatly simplify deployment of multiple servers both for development and production.

Unfortunately it's not the easiest tool to master, far from it. Here is a non-exhaustive list of the skills you would need to fully master Docker:

* Very good knowledge of Linux **command line**.
* Extensive experience with Linux **processes and servers**.
* Experience with **application deployment automation**.
* Good knowledge of **Docker itself** but also **with the various tools used around it** (like docker-compose or Kubernetes).

The problem is that knowing everything will probably take your multiple years of learning and multiple big projects to gather sufficient experience. And still you will have to start using Docker right now for your day-to-day development environment.

So this guide's purpose is to teach you what you need to know in order to start using Docker as soon as possible. You won't know *everything* but you should know just enough to use it for some useful purpose.

## The big picture about Docker

### It's all about containers

Docker's purpose is all about running what we call **containers**.

Do you know what is a virtual machine? Did you run one on your PC before? OK, a container is *a little bit* like a virtual machine, with some differences.

A virtual machine will create a whole environment mimicking a real computer and then let a complete operating system inside the virtual machine run *believing* it is running on a real computer. A container will run *only one program* inside a minimal virtual environment. The real operating system is still your normal one. In fact, when running a container Docker will only mimic a few components of a real computer:

* The filesystem
* The network
* ... and not much more in fact

The result is that containers are *much faster to run* (a container can start in less than a second) and are *much more ressource efficient* (they don't consume more memory than the contained program needs) than virtual machines.

Note that containers are a specific feature of the **Linux Kernel**. There are efforts to offer similar features on Windows and Mac but it's not super advanced right now compared to what we can do actually on Linux. So when we're speaking about Docker we are mostly speaking about **Linux**.

**Pro tip**: Now that you know the difference between a container and a virtual machine never say to a Docker expert that it's running virtual machines. He might spit on your face without warnings.

### Program and process, image and container

Do you know the difference between a **program** and a **process**?

It's completely unrelated to Docker and it's just a question of naming: a *program* is a bunch of code that resides somewhere on your filesystem. It's not run by your processor, it's just inert, doing nothing. A *process* is the copy of your program in the RAM of your computer that is actually running. You can of course have multiple processes coming from the same program at the same time. You just have to launch it multiple times.

If you want to see which processes are currently running on your Linux system you can try this command:

```bash
top
```

Now that this differenciation is established, it's easy to speak about the terms **image** and **container** in the context of Docker. An *image* is like a program: it's a bunch of stuff that are on your filesystem doing nothing. A *container* is like a process: it's a copy of an image that is actually running. And just like with processes you can have as much containers as you want coming from the same image. You just have to run them multiple times.

### Where to find Docker images?

OK, if I want to start a container I need an image. But where the hell can I find one?

Well, you *could* create your own image with what we call a *[Dockerfile](https://docs.docker.com/engine/reference/builder/)*. That's basically a script explaining how to create a Docker image, most of the time starting from another existing image. But creating Dockerfiles is a little bit complex and is not 100% necessary for someone that just want to use Docker to launch a few servers.

Instead what almost everyone does is to use [Docker Hub](https://hub.docker.com/search/?type=image&image_filter=official) to download existing Docker images. Want a PostgreSQL image ready to run? [There's one](https://hub.docker.com/_/postgres). Want an environment to run your Node.js application? [There's one too](https://hub.docker.com/_/node).

**Docker Hub** and its ready-to-use images are an important part of what makes Docker a useful tool. Due to this using Docker mostly relies around using existing work made by other people to avoid loosing time yourself.

## Docker as my development environment
Watch [this 30 minutes video](https://www.youtube.com/watch?v=0H2miBK_gAk) to learn how you can use Docker as your development environment without having to re-build your image every time you change your code.