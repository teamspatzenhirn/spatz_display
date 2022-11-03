# spatz_display

## running with docker
### build container
```
docker build --tag spatz_display .
```

### run container
```
docker run -ti --net=host --env="DISPLAY" -v /var/run/docker.sock:/var/run/docker.sock spatz_display
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