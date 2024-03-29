#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER ${APP_DB_USER} WITH PASSWORD '${APP_DB_PASS}';

  CREATE            DATABASE ${APP_DB_NAME} encoding 'UTF8';
  ALTER             DATABASE ${APP_DB_NAME} OWNER TO ${APP_DB_USER};

  \connect ${APP_DB_NAME} ${POSTGRES_USER};

  CREATE SCHEMA IF NOT EXISTS ${APP_DB_SCHEMA};
  
  CREATE EXTENSION IF NOT EXISTS "uuid-ossp" with schema ${APP_DB_SCHEMA};
  CREATE EXTENSION IF NOT EXISTS "vector" with schema ${APP_DB_SCHEMA};

  GRANT ALL PRIVILEGES    ON DATABASE ${APP_DB_NAME}      TO ${APP_DB_USER};
  GRANT ALL PRIVILEGES    ON SCHEMA ${APP_DB_SCHEMA}      TO ${APP_DB_USER};
  GRANT ALL PRIVILEGES    ON ALL TABLES                   IN SCHEMA ${APP_DB_SCHEMA} TO ${APP_DB_USER};
  GRANT USAGE, SELECT     ON ALL SEQUENCES                IN SCHEMA ${APP_DB_SCHEMA} TO ${APP_DB_USER};
  GRANT EXECUTE           ON ALL FUNCTIONS                IN SCHEMA ${APP_DB_SCHEMA} TO ${APP_DB_USER};

  \connect ${APP_DB_NAME} ${APP_DB_USER};

  BEGIN;

  COMMIT;
EOSQL
