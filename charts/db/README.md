
Mysql
===========

MySQL based database application


## Configuration

The following table lists the configurable parameters of the Mysql chart and their default values.

| Parameter                         | Description                                          | Default           |
|-----------------------------------|------------------------------------------------------|-------------------|
| `name`                            |                                                      | `"meteorites-db"` |
| `namespace`                       | Default namespace                                    | `"planet-earth"`  |
| `version`                         |                                                      | `"1.0.0"`         |
| `app.storageSize`                 | Storage size of the PersistentStorage used by the DB | `"10Gi"`          |
| `app.storageClaimSize`            | Storage Claim Size                                   | `"5Gi"`           |
| `app.envs.MYSQL_USER`             | Default MySQL user                                   | `"mysql"`         |
| `app.secrets.MYSQL_ROOT_PASSWORD` | Default MySQL root user's password                   | `"iamroot"`       |
| `app.secrets.MYSQL_PASSWORD`      | Default MySQL password                               | `"changeme"`      |
| `app.secrets.MYSQL_DATABASE`      | Default MySQL database                               | `"mysql"`         |
| `pma.port`                        | PhpMyAdmin listen port                    | `8081`                 |

