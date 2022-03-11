#!/bin/bash

# Start the primary process and put it in the background
python3 server.py &
# Start the helper process
python3 client.py

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?