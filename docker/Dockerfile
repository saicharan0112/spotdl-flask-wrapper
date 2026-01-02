FROM python:3.13-alpine

# Install dependencies for adding a user dynamically
RUN apk add --no-cache shadow bash su-exec ffmpeg

# Set up the Python virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install spotdl and its dependencies
RUN pip install spotdl 

# Set the working directory
WORKDIR /tmp/music

# Script to dynamically create a user based on passed UID and GID
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose the required port
EXPOSE 8800

# Set the entrypoint and default command
ENTRYPOINT ["/entrypoint.sh"]
CMD [ "spotdl", "web", "--output=/tmp/music", "--web-use-output-dir", "--host", "0.0.0.0", "--port", "8800" ]
