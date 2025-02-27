# Docker Text Processing Container

This project demonstrates the creation of an end-to-end Docker container that automates the process of reading text files, processing data, and generating output. 

## Project Overview

The container is designed to:

1.  Read two text files (`IF-1.txt` and `AlwaysRememberUsThisWay-1.txt`) located at `/home/data` inside the container.
2.  Perform various text processing tasks, including word counting, frequency analysis, and contraction handling.
3.  Generate a `result.txt` file at `/home/data/output/` containing the processed data.
4.  Print the contents of `result.txt` to the console before exiting.

## Requirements

* **Docker Desktop:** Installed on my personal computer.
* **Lightweight Base Image:** The Dockerfile uses a lightweight base image - `python:3.9-alpine`.
* **Python Script:** A Python script (`scripts.py`) performs the text processing tasks.
* **Text Files:** `IF-1.txt` and `AlwaysRememberUsThisWay-1.txt` are located at `/home/data` inside the container.
* **Output File:** `result.txt` is generated at `/home/data/output/`.

