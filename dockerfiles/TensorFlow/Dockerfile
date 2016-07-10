From tensorflow/tensorflow
MAINTAINER Hayato Sasaki <h.sasaki.ynu@gmail.com>
# install openssh-server for ssh
# install python-qt4 for matplotlib backend
RUN apt-get update && \
    apt-get install -y openssh-server python-qt4
# add user 'developer'
RUN adduser --disabled-password --gecos "" developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    echo "developer:developer" | chpasswd && \
    cp -r /notebooks /home/developer && chown -R developer:developer /home/developer/notebooks && \
    cp -r /root/.jupyter /home/developer && chown -R developer:developer /home/developer/.jupyter
# edit /etc/ssh/sshd_config
RUN sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \
    sed -ri 's/: agg/: Qt4Agg/g' /usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/matplotlibrc && \
    mkdir -p /var/run/sshd && \
    chmod 755 /var/run/sshd
RUN echo "#!/usr/bin/env bash\\n/usr/sbin/sshd\\n/run_jupyter.sh" > /run.sh && chmod +x /run.sh

ENV QT_X11_NO_MITSHM 1
USER developer
WORKDIR /home/developer/notebooks
CMD ["sudo", "/run.sh"]
