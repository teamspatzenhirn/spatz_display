# spatz_display

## Build container
```
docker build --tag spatz_display .
```

## run container
```
docker run -ti --net=host --env="DISPLAY" -v /var/run/docker.sock:/var/run/docker.sock spatz_display
```
