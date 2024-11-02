#!/bin/bash

# Update package list and install required packages
sudo apt update
sudo apt install -y wget tar

# Kill existing tmate sessions if any
pkill -9 tmate

# Download the latest tmate release
TMATE_VERSION="2.4.0"
TMATE_URL="https://github.com/tmate-io/tmate/releases/download/${TMATE_VERSION}/tmate-${TMATE_VERSION}-static-linux-i386.tar.xz"
wget -nc "$TMATE_URL"

# Extract the downloaded file
tar --skip-old-files -xvf "tmate-${TMATE_VERSION}-static-linux-i386.tar.xz"

# Clean up previous logs
rm -f nohup.out

# Start a new tmate session in detached mode
bash -ic "nohup ./tmate-${TMATE_VERSION}-static-linux-i386/tmate -S /tmp/tmate.sock new-session -d & disown -a" >/dev/null 2>&1

# Wait for tmate to be ready
./tmate-${TMATE_VERSION}-static-linux-i386/tmate -S /tmp/tmate.sock wait tmate-ready

# Display SSH connection string
echo "Connect using the following command:"
./tmate-${TMATE_VERSION}-static-linux-i386/tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}'
