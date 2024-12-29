#!/bin/bash

# Default to UID and GID 1000 if not provided
USER_ID=${UID:-1000}
GROUP_ID=${GID:-1000}

# Create group and user with the specified IDs
groupadd -g "$GROUP_ID" usergroup
useradd -u "$USER_ID" -g "$GROUP_ID" -m user

# Change ownership of the working directory
chown -R user:usergroup /tmp/music

# Run the main process as the new user
exec su-exec user "$@"