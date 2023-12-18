# OpenTelemetry and Python

## Intro to OTel

## Build basic app using [FastAPI](https://fastapi.tiangolo.com/#example)
```python
print("hello world")
```

## Start local [OTel collector](https://opentelemetry.io/docs/collector/getting-started/)

###  OTel collector config
- https://opentelemetry.io/docs/collector/configuration/
- https://jessitron.com/2021/08/11/run-an-opentelemetry-collector-locally-in-docker/
- [zPages](https://github.com/open-telemetry/opentelemetry-collector/blob/main/extension/zpagesextension/README.md)
   - http://localhost:55679/debug/servicez
   - http://localhost:55679/debug/tracez

### Automatic instrumentation
- https://opentelemetry.io/docs/instrumentation/python/automatic/
- https://opentelemetry.io/docs/instrumentation/python/distro/
- https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-instrumentation#opentelemetry-bootstrap
- https://opentelemetry-python.readthedocs.io/en/stable/index.html#integrations
- `pip install opentelemetry-distro[otlp] opentelemetry-instrumentation`
- "opentelemetry-instrument automatically instruments a Python program and its dependencies and then runs the program."

### Azure Monitor
- https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview
- https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable
- https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/azuremonitorexporter
- https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/ch04.html
