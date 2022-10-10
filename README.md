# spatz_display

## Build container
```
docker build --tag spatz_display .
```

## run container
```
docker run -ti --rm --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" spatz_display
```
