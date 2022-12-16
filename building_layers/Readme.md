# Welcome to our TechSession on 16-12-2022

### Run Lambda functions locally with lambci/lambda image
```
# General command #
docker run --rm \
  -v <code_dir>:/var/task:ro,delegated \
  [-v <layer_dir>:/opt:ro,delegated] \
  lambci/lambda:<runtime> \
  [<handler>] [<event>]
```
