# Assignments for Associate Data Engineer role at Krisp

### Instructions for building and running

\# Make sure you're on on a Linux system, whether natively or virtually. Certain distributions and versions may require additional dependencies to be installed manually.

On Debian-based derivatives:
$ sudo apt update
$ sudo apt install docker-compose

On Red Hat Enterprise Linux (RHEL) derivatives:
$ sudo yum update
$ sudo yum install docker-compose

*On newer versions YUM is an alias to DNF, a next-generation package manage, again based on RPM.

On Arch-based derivatives:
$ sudo pacman -Syu
$ sudo pacman -S docker-compose

On OpenSUSE-based derivatives:
sudo zypper refresh
sudo zypper install docker-compose

On Alpine-based derivatives:
$ sudo apk update
$ sudo apk add doctor-compose

sudo systemctl start docker
sudo systemctl enable docker

sudo docker-compose up --build
to only run post-build, just omit the `--build` option.


Tested on Ubuntu 22.04.4 LTS (Jammy Jellyfish).
