# Database Migration Commands for Flask

## Initializing Flask-Migrate

```sh
# 1. Move to the directory
cd server

# 2. Initialize Flask-Migrate
flask db init

# 3. Generate an Initial Migration
flask db migrate -m "initial migration"

# 4. Apply Migrations
flask db upgrade
```
