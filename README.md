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
xhost +
```
```
docker run --rm -ti --net=host --env="DISPLAY" -v /var/run/docker.sock:/var/run/docker.sock --env VNC_HOST="localhost" --env VNC_PASSWD="" spatz_display
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