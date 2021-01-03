#!/bin/bash

# Start the postgres pod
kubectl apply -f ./postgres/postgres-configmap.yaml
kubectl apply -f ./postgres/postgres-storage.yaml
kubectl apply -f ./postgres/postgres-deployment.yaml