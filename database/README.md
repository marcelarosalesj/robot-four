# Databases

This uses influxdb

## Interact with the DB
```
# Show databases
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "q=show databases"

```

## About InfluxDB and DB concepts
InfluxDB is a Time Series Database (TSDB). It doesn't have keys as RDBMS.
TSDB are optimized for timestamp usage.
TSDB is the gastest growing segment in the database industry.



## References
* [Getting Started with Python and InfluxDB](https://www.influxdata.com/blog/getting-started-python-influxdb/)
* [Cannot connect from python to influxdb when running in docker](https://stackoverflow.com/questions/44551462/cannot-connect-from-python-to-influxdb-when-running-in-docker)
* [bitnami-docker-influxdb github](https://github.com/bitnami/bitnami-docker-influxdb)
* [Time series database (TSDB) explained](https://www.influxdata.com/time-series-database/)
* [DB-Engines](https://db-engines.com/en/)
