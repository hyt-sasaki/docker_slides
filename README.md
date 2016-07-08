# My Dockerfiles

## Dockerfile for TensorFlow
### Usage
Example
```sh
$ git clone https://github.com/hyt-sasaki/docker_slides.git
$ cd docker_slides
$ git checkout master
$ cd dockerfiles/TensorFlow
$ docker build -t mytensorflow .
$ docker run -d --name tensorflow -p 8888:8888 -p 6006:6006 DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix mytensorflow
```

### For Windows(utilize [MobaXTerm](http://mobaxterm.mobatek.net/))
Example

In boot2docker, 
```sh
$ git clone https://github.com/hyt-sasaki/docker_slides.git
$ cd docker_slides
$ git checkout master
$ cd dockerfiles/TensorFlow
$ docker build -t mytensorflow .
$ docker run -d --name tensorflow -p 8888:8888 -p 6006:6006 -p 10022:22 mytensorflow
```

After running container, 

+ Enter *Session Setting* of MobaXTerm
+ Edit three items
	+ Remote host: 192.168.99.100 
	+ specify username(check): developer
	+ port: 10022
+ Edit *Excute Command*
	+ export DISPLAY=\`echo $SSH_CLIENT | cut -d' ' -f1\`:0.0
+ Check *Do not exit after commands ends*
+ Enter *OK*

## Dockerfile for python-opencv
### Usage
Example
```sh
$ git clone https://gitlab.com/hyt-sasaki/opencv-dockerfile.git
$ cd opencv-dockerfile
$ docker build -t python-opencv .
$ docker run -d --name opencv DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix python-opencv
```

### For Windows(utilize [MobaXTerm](http://mobaxterm.mobatek.net/))
Example

In boot2docker, 
```sh
$ git clone https://gitlab.com/hyt-sasaki/opencv-dockerfile.git
$ cd opencv-dockerfile
$ docker build -t python-opencv .
$ docker run -d --name opencv -p 10023:22 python-opencv
```

After running container, 

+ Enter *Session Setting* of MobaXTerm
+ Edit three items
	+ Remote host: 192.168.99.100 
	+ specify username(check): developer
	+ port: 10023
+ Edit *Excute Command*
	+ export DISPLAY=\`echo $SSH_CLIENT | cut -d' ' -f1\`:0.0
+ Check *Do not exit after commands ends*
+ Enter *OK*
