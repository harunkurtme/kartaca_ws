FROM ubuntu:20.04
LABEL Name=kartaca_ws Version=0.0.1

RUN docker run -d -p 80:80 -p 80:80 \
-v /traefik/traefik.toml \
-v /var/run/docker.sock:/var/run/docker.sock \
traefik:v2.4

CMD [ "traefik", "--configFile=./traefik/traefik.toml" ]