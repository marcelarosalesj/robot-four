# Databases

This uses influxdb

## Interact with the DB
```
# Show databases
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "q=show databases"

```

## InfluxDB concepts
- InfluxDB is a Time Series Database (TSDB)
- TSDB are optimized for timestamp usage
- measurement
- points
- time/timestamp
- field
- tags
- InfluxDB line protocol `<measurement>[,<tag-key>=<tag-value>...] <field-key>=<field-value>[,<field2-key>=<field2-value>...] [unix-nano-timestamp]`
- [InfluxQL query language](https://docs.influxdata.com/influxdb/v1.7/query_language/)

## References
* [Getting Started with Python and InfluxDB](https://www.influxdata.com/blog/getting-started-python-influxdb/)
* [Cannot connect from python to influxdb when running in docker](https://stackoverflow.com/questions/44551462/cannot-connect-from-python-to-influxdb-when-running-in-docker)
* [bitnami-docker-influxdb github](https://github.com/bitnami/bitnami-docker-influxdb)
* [Time series database (TSDB) explained](https://www.influxdata.com/time-series-database/)
* [DB-Engines](https://db-engines.com/en/)
