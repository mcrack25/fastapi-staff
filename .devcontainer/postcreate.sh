#!/bin/sh

set -ex

apt update && apt install -y curl postgresql-client && curl -sSL https://get.docker.com/ | sh && curl -L https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose && chmod 400 /root/.ssh/id_rsa && export EDITOR="code --wait"
