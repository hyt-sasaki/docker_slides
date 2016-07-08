FROM ubuntu:14.04
MAINTAINER Hayato Sasaki <h.sasaki.ynu@gmail.com>
# install applications
RUN apt-get update && \
    apt-get install -y \
    python2.7-dev \
    python-numpy \
    python-opencv \
    openssh-server \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /va/cache/apt/archives/*
# add user 'developer'
RUN adduser --disabled-password --gecos "" developer
RUN echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    echo "developer:developer" | chpasswd
RUN chown -R developer:developer /home/developer
# edit /etc/ssh/sshd_config
RUN sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config
RUN sed -ri 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN mkdir -p /var/run/sshd && \
    chmod 755 /var/run/sshd
# make a shell script for init container
RUN echo '#!/bin/bash\nln /dev/null /dev/raw1394\n/usr/sbin/sshd -D' > /run.sh && \
    chmod +x /run.sh
# avoidance of "libdc1394 error: Failed to initialize libdc1394" error when "import cv" in python
RUN ln /dev/null /dev/raw1394

USER developer
WORKDIR /home/developer
CMD ["sudo", "sh", "-c", "/run.sh"]
