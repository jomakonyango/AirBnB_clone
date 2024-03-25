#!/bin/bash

# This line tells the system this file should be run in the bash shell.

# Navigate to the root directory of your git repository
cd /home/otieno/AirBnB_clone

# Generate the AUTHORS file
# This command uses git to list all authors by name and email,
# sorts them uniquely, and writes the output to the AUTHORS file.
git log --format='%aN <%aE>' | sort -u > AUTHORS
