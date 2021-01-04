#!/bin/bash
action=$1
postgresMountPath='/Users/keiranworrell/Documents/mount/data'

if [ "${action}" == "apply" ]; then
    # Start the postgres deployment
    kubectl apply -f ./postgres/postgres-configmap.yaml
    kubectl apply -f ./postgres/postgres-storage.yaml
    kubectl apply -f ./postgres/postgres-deployment.yaml
    kubectl apply -f ./postgres/postgres-service.yaml

    # Start API deployment
    kubectl apply -f ./startAPI/api-deployment.yaml

elif [ "${action}" == "delete" ]; then 
    # Delete the postgres deployment
    kubectl delete -f ./postgres/postgres-deployment.yaml
    kubectl delete -f ./postgres/postgres-configmap.yaml
    kubectl delete -f ./postgres/postgres-storage.yaml
    kubectl delete -f ./postgres/postgres-service.yaml

    # Delete API deployment
    kubectl delete -f ./startAPI/api-deployment.yaml

elif [ "${action}" == "api" ]; then
    kubectl delete -f ./startAPI/api-deployment.yaml
    docker system prune -fa
    cd api
    docker build -t worrellkeiran/api .
    docker push worrellkeiran/api
    cd ..
    kubectl apply -f ./startAPI/api-deployment.yaml
else
    echo "Please supply a valid action: apply/delete"
fi