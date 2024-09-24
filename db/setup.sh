#!/bin/sh

export PG_USER="postgres"

psql -c "CREATE DATABASE fkcommerce"

# Create extensions for the specified database
psql fkcommerce -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"