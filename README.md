# spatz_display

## running with docker

### prepare named pipes
Create pipes with `sudo mkfifo /mnt/inputpipe /mnt/outputpipe`.

Set permissions for pipes with `sudo chown spatz /mnt/*pipe`

Execute stuff from pipes and send output back to docker:
```
while true;
    do eval "$(cat /mnt/inputpipe)" 2>&1 | tee /mnt/outputpipe;
done
```
### build container
```
docker build --tag spatz_display .
```

### run container
```
docker run --rm -ti --net=host --env="DISPLAY" -v /var/run/docker.sock:/var/run/docker.sock --env VNC_HOST="localhost" --env VNC_PASSWD="" spatz_display
```
### Run container with tmux
```
tmux -S /tmp/tmux-spatz #this has to be run by hand rn but should be ran at start up on the spatz
```
```
xhost +
```
```
docker run --rm -ti --net=host --env="DISPLAY" -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/tmux-spatz:/tmp/tmux-spatz --env VNC_HOST="localhost" --env VNC_PASSWD="" spatz_display
```
If you want to attach to the session for debugging purposes
```
tmux -S /tmp/tmux-spatz attach-session -t spatz
```
---
## running without docker
### install dependencies
```
pip3 install -r requirements.txt
git submodule update --init --recursive
```

### build protoc python classes
- install binary from [protoc-*.zip](https://github.com/protocolbuffers/protobuf/releases)
```
protoc -I=protobuf_types --python_out=. protobuf_types/*.proto
```

### Granting access to /var/run/docker.sock
```
sudo usermod -aG docker $USER
```
