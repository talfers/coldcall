FROM ubuntu:latest

# Install Cron, update system
RUN apt-get update && apt-get -y install python3 python3-pip 

# Copy over project directory
ADD ./ /coldcall

# Install package dependencies
RUN pip install --no-cache-dir -r /coldcall/requirements.txt

WORKDIR /coldcall

# Give permission to run scripts
RUN chmod +x /coldcall/app.py

# Run the command on container startup
CMD /coldcall/app.py