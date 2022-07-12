# Docker

+ **Image** - Created from Dockerfile with `build` command. Read-only templates daw ni containing instructions sa pag create og container.
    + Daghan nig layers. Magsugod sa OS then pun-an og mga packages, imong app, etc.  
    + Pwede ra mo pull og images e.g. `docker pull [name]`   
+ **Container** - Pag e-run na ang mga images, container na sya haha

## Install Docker + WSL2 (Windows)

> service --status-all
> sudo service docker start

1. Install https://strapi.io/documentation/developer-docs/latest/setup-deployment-guides/installation/docker.html#step-1-create-a-docker-compose-yaml-file
2. Need to downgrade pythong 2.8 to 2.7 (failed)
3. Upgraded docker-compose: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04
4. Issue: https://stackoverflow.com/questions/64952238/docker-errors-dockerexception-error-while-fetching-server-api-version
5. Download https://docs.docker.com/docker-for-windows/wsl/

## Images

1. Buhat og `Dockerfile`
2. e-build ang image `docker build . -t hello-gauge-image` with tag 'hello-gauge-image'
3. e-run ang image e.g. `docker run --volume `pwd`:/`pwd` --workdir `pwd` hello-gauge-image gauge run specs`
    + `-v` or `--volume` : e-mount ang current working directory `pwd` sa HOST didto ra gihapon sa the same path `pwd` sa CONTAINER
    + `-w` or `--workdir`: Usba ang working directory sulod sa container sa kung unsa ang result sa `pwd` command (print working directory)

Example: https://docs.gauge.org/howto/ci_cd/docker.html?os=null&language=python&ide=vscode

## Containers
1. List all containers: `$ docker container ls`
2. Build the container image: `$ docker build -t getting-started .`
3. Run: `$ docker run -dp 3000:3000 getting-started`
4. Snyk tests to find vulnerabilities: `$docker scan`
5. Rebuild See #2
6. Get id of containers: `docker ps -a`
7. Stop container: `docker stop <container>`
8. Remove container: `docker rm <container>`
9. Rerun see #3

## Dockerhub
1. Create Public repo
2. `docker push lemsst/getting-started:tagname`
3. `docker image ls`
4. `docker login -u username`
5. `docker tag getting-started lemsst/getting-started`

## Bind mounts
```bash
docker run -dp 3000:3000 \
    -w /app -v "$(pwd):/app" \
    node:12-alpine \
    sh -c "yarn install && yarn run dev"
```
1. Watch: `docker logs -f <container-id>`
2. Make source code changes
3. After changes, rebuild: `docker build -t getting-started .`


## Multi-container apps
1. `docker network create todo-app`


## docker-compose
1. `docker-compose up -d`
2. `docker-compose logs -f`

## View space used
```bash
sudo docker system df
```

## Other
- List all images: `docker images`
- Remove docker image: `docker rmi <IMAGE ID>`

## Docker + WSL2
Follow these guides:
- [Setting up WSL Version 2 and the Ubuntu app](https://codefellows.github.io/setup-guide/windows/)
- [Download Kernel update](https://aka.ms/wsl2kernel)
- [Install NodeJS on Windows Subsystem for Linux (WSL2)](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl)
- [Install STRAPI](https://strapi.io/documentation/developer-docs/latest/setup-deployment-guides/installation/docker.html#step-1-create-a-docker-compose-yaml-file)

