#!/bin/sh

set -ex

apt-get update && apt-get install -y git && apt-get install -y openssh-client
