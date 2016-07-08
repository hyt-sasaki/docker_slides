From tensorflow/tensorflow
MAINTAINER Hayato Sasaki <h.sasaki.ynu@gmail.com>
RUN apt-get update && \
    apt-get install -y openssh-server python-qt4
RUN adduser --disabled-password --gecos "" developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    echo "developer:developer" | chpasswd && \
    cp -r /notebooks /home/developer && chown -R developer:developer /home/developer/
RUN sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \
    sed -ri 's/: agg/: Qt4Agg/g' /usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/matplotlibrc && \
    mkdir -p /var/run/sshd && \
    chmod 755 /var/run/sshd
ENV QT_X11_NO_MITSHM 1
USER developer
WORKDIR /home/developer
CMD ["sudo", "/usr/sbin/sshd", "-D"]
