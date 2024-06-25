# Meteorites Catalog

This project is a simple REST application that can be deployed on a Kubernetes cluster and allows interaction with a copy of [NASA's Meteorite Landings Data Set](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data).

It consists of two different [Helm charts](https://helm.sh/) that include all the Kubernetes manifests needed to deploy the required components:

1. **App** - Python application based on Flask that exposes a set of REST endpoints.
2. **DB** - MySQL database that stores the queryable data.

## About the Data Set

This comprehensive data set from The Meteoritical Society contains information on all known meteorite landings. The Fusion Table is collected by Javier de la Torre, and we've also provided an XLS file that consists of 34,513 meteorites.

## Installation

A few notes on the installation process before we begin:
1. Applications are packaged in the form of Helm charts. Please make sure you have a recent version installed on your workstation.
2. This guide will assume you are using [Minikube](https://minikube.sigs.k8s.io/docs/). All examples and commands will use Minikube as the reference cluster application.

Other suggested software: To easily access the Kubernetes cluster, use the [k9s](https://k9scli.io/) CLI.

### Start the Minikube Cluster

0. Start Docker.
1. Open a terminal and issue `minikube start` to start the cluster. Depending on your hardware and internet connection, it may take some time.
2. When the startup process is complete, start the tunnel on Minikube with `minikube tunnel`.

Minikube will set up the Kubernetes context for you to use.

### Install Database Server

From the project root, run the following command:
```
helm upgrade --install --create-namespace --namespace planet-earth db ./charts/db
```

This will create all the required Kubernetes resources to deploy a stateful application based on MySQL server 8.4.0.

The DB is not reachable from outside the cluster but only by other pods using the `meteorites-db-svc` service (ClusterIP).

#### Populate the DB by Importing Existing Data

An additional pod with a `PhpMyAdmin` container is spawned alongside the main application. This is used to populate the database for the first time and for troubleshooting. You can use the zip file included in the repository at the path `dataset/nasa_meteorites.sql.zip` and import it to the DB using PhpMyAdmin.

For the application to work properly, some preliminary activities are required:

1. Get the URL to access PhpMyAdmin:
```
minikube service meteorites-db-pma-svc --namespace planet-earth --url
```
2. Access PhpMyAdmin via browser and use `root` as the user and `iamroot` as the password (default values of the chart if not overridden).

3. Import the `dataset/nasa_meteorites.sql.zip` file. This will create the `meteorites_app` database.

At this point, the DB will be available but still not accessible by the application since no MySQL user has been added and authorized. 

To create a MySQL user, run the following SQL query (change the username if you are not using the chart's default values):

```sql
-- Consider using a password for the user and restricting access to specific hosts only. For testing purposes only, please.
GRANT ALL ON meteorites_app.* TO 'mysql'@'%';
```

If no errors are reported, you can now proceed with the application setup.

### Install RESTful Application

From the project root, run the following command:
```
helm upgrade --install --create-namespace --namespace planet-earth app ./charts/app
```

This will create all the required Kubernetes resources to deploy a Flask-based app supporting a set of RESTful endpoints:

| Endpoint             | HTTP Method | Description                                      |
|----------------------|-------------|--------------------------------------------------|
| /meteorites          | GET         | Get the last 100 meteorites ordered by ID descending |
| /meteorites/[id:int] | GET         | Get a meteorite by ID                            |
| /meteorites/[id:int] | PUT         | Update a meteorite                               |
| /meteorites/[id:int] | DELETE      | Delete a meteorite                               |

The application is reachable from outside the Kubernetes cluster via Minikube tunnel. To generate the accessible link, use the following command:

```
minikube service meteorites-catalog-svc --namespace planet-earth --url
```
This will provide a URL like `http://127.0.0.1:[random-port-number]`. Use the generated URL as the base URL in conjunction with the endpoints above.

#### Populate the DB Using REST Endpoints

For this step, we will use a [Postman](https://www.postman.com/) collection that is available under `postman/Meteorites.postman_collection.json`. Import the collection into Postman and populate the variable `{{baseurl}}` with the URL provided by Minikube for the `meteorites-catalog-svc`.
An example payload is included with the example requests; change it with the values of your choice.
