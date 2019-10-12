#!/usr/bin/env bash

docker run -dit --name tracker --network=host -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker
docker run -dti --name storage --network=host -e TRACKER_SERVER=192.168.19.20:22122 -v /var/fdfs/storage:/var/fdfs delron/fastdfs storage