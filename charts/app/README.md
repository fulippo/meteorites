
Meteorites-app
===========

Example CRUD app to interact with NASA's meteorites catalog


## Configuration

The following table lists the configurable parameters of the Meteorites-app chart and their default values.

| Parameter                         | Description                               | Default                |
|-----------------------------------|-------------------------------------------|------------------------|
| `name`                            |                                           | `"meteorites-catalog"` |
| `namespace`                       | Default namespace                         | `"planet-earth"`       |
| `version`                         |                                           | `"1.0.0"`              |
| `app.port`                        | Default application's port                | `8080`                 |
| `app.envs.MYSQL_USER`             | MySQL used to connect to the DB server    | `"mysql"`              |
| `app.envs.MYSQL_HOST`             | Service name for the MySQL server service | `"meteorites-db-svc"`  |
| `app.secrets.MYSQL_ROOT_PASSWORD` | Default MySQL root password               | `"iamroot"`            |
| `app.secrets.MYSQL_PASSWORD`      | Default MySQL applicative password        | `"changeme"`           |
| `app.secrets.MYSQL_DATABASE`      | Default MySQL DB name                     | `"meteorites_app"`     |

