FROM python:3.9-alpine

# Create data and output directories
RUN mkdir -p /home/data/output

# Copy the Python script and text files
COPY scripts.py /home/scripts.py
COPY IF-1.txt /home/data/IF-1.txt
COPY AlwaysRememberUsThisWay-1.txt /home/data/AlwaysRememberUsThisWay-1.txt

# Run the script
CMD ["python3", "/home/scripts.py"]