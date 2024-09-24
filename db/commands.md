# Useful Commands in a Postgres Shell

## Access to PSQL

`psql -U USER_NAME`

## Basic Database Management

- `\l`: List all databases.
- `\c` database_name: Connect to a specific database.
- `\q`: Quit the current database connection.
- `\x`: Toggle expanded output format.
- `\d`: Describe a table, view, or function.
- `\dt`: List tables.
- `\dv`: List views.

## Data Manipulation

`SELECT \* FROM table_name;`: Select all columns from a table.
`INSERT INTO table_name VALUES (value1, value2, ...);`: Insert a new row.
`UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;`: Update existing rows.
`DELETE FROM table_name WHERE condition;`: Delete rows.

## Creating and Dropping Objects

`CREATE TABLE table_name (column1 data_type, column2 data_type, ...);`: Create a table.
`DROP TABLE table_name;`: Drop a table.
`CREATE INDEX index_name ON table_name (column1, column2);`: Create an index.
`DROP INDEX index_name;`: Drop an index.

## Advanced Queries

`JOIN`: Combine rows from multiple tables.
`GROUP BY`: Group rows based on a column.
`HAVING`: Filter grouped results.
`ORDER BY`: Sort results.
`LIMIT`: Limit the number of rows returned.

## Other Useful Commands

`\h command_name`: Get help for a specific command.
`\COPY table_name TO 'file.csv' CSV;`: Export data to a CSV file.
`\COPY table_name FROM 'file.csv' CSV;`: Import data from a CSV file.
`\password postgres`: Change the password for the postgres user.
