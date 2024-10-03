#!/bin/sh

export PG_USER="postgres"

psql -c "CREATE DATABASE flask"

# Create extensions for the specified database
psql flask -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"