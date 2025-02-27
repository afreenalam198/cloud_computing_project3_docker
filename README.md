# Docker Text Processing Container

This project demonstrates the creation of an end-to-end Docker container that automates the process of reading text files, processing data, and generating output. 

## Overview

The container is designed to:

1.  Read two text files (`IF-1.txt` and `AlwaysRememberUsThisWay-1.txt`) located at `/home/data` inside the container.
2.  Perform various text processing tasks, including word counting, frequency analysis, and contraction handling.
3.  Generate a `result.txt` file at `/home/data/output/` containing the processed data.
4.  Print the contents of `result.txt` to the console before exiting.

## Script Functionality

The Python script (scripts.py) performs the following tasks:  
1.  Reads two text files located in /home/data inside the container.  
2.  Counts the total number of words in each file.
3.  Computes the grand total of words across both files.
4.  Identifies the top 3 most frequent words in IF-1.txt.
5.  Handles contractions and finds the top 3 most frequent words in AlwaysRememberUsThisWay-1.txt.
6.  Determines the IP address of the machine running the container.
7.  Writes all results to /home/data/output/result.txt.

## Docker Image Optimization

The project uses a lightweight base image - python:3.9-alpine to reduce image size (target: <200MB).  
Final Image size - 81MB.

## Orchestratation of Container Deployment Using Kubernetes

To deploy the container using Kubernetes:

1.  Apply the Kubernetes manifest:
    kubectl apply -f deployment.yaml
2.  Check the running pods:
    kubectl get pods
4.  Scale the deployment:
    kubectl scale deployment text-processing-deployment --replicas=6
6.  Save the output:
    kubectl get pods > kube_output.txt; cat kube_output.txt

## Output

<img width="705" alt="Screenshot 2025-02-26 at 10 53 54 PM" src="https://github.com/user-attachments/assets/097ce7f4-15a0-4cad-9d11-9a96a369b1d2" />






