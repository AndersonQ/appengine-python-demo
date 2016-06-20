#!/usr/bin/env bash

rm -rf .datastore

gcloud preview app run\
 ./app.yaml --admin-host=localhost:8000\
  --host=localhost:8080\
  --storage-path=./datastore
