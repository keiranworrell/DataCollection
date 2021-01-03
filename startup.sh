#!/bin/bash
action=$1

if [ "${action}" = "apply" ]; then
    # Start the postgres deployment
    kubectl apply -f ./postgres/postgres-configmap.yaml
    kubectl apply -f ./postgres/postgres-storage.yaml
    kubectl apply -f ./postgres/postgres-deployment.yaml
    kubectl apply -f ./postgres/postgres-service.yaml
elif [ "${action}" = "delete" ]; then 
    # Delete the postgres deployment
    kubectl delete -f ./postgres/postgres-deployment.yaml
    kubectl delete -f ./postgres/postgres-configmap.yaml
    kubectl delete -f ./postgres/postgres-storage.yaml
    kubectl delete -f ./postgres/postgres-service.yaml
else
    echo "Please supply a valid action: apply/delete"
fi