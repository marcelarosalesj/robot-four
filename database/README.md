# Databases

This uses influxdb

## Interact with the DB
```
# Show databases
curl -G "http://somehost:8086/query?pretty=true" --data-urlencode "q=show databases"

```

## References
* [Getting Started with Python and InfluxDB](https://www.influxdata.com/blog/getting-started-python-influxdb/)
* [Cannot connect from python to influxdb when running in docker](https://stackoverflow.com/questions/44551462/cannot-connect-from-python-to-influxdb-when-running-in-docker)
*
*
