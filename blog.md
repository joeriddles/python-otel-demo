# OpenTelemetry and Python

## Intro to OTel

Designing a software application to be observable is table stakes in modern software development. Observability is a non-functional requirement that when done right enables the state of a system to be continuously communicated and visible to those maintaining it. Because observability is a non-functional requirement, it has more to do with the way the system is designed than any specific feature.

The modern path to making a software system more observable is to begin with the three pillars of observability: **logs**, **metrics**, and **traces**.
### Logs
You're probably already familiar with logs; logging can be as simple as a `print` statement or using the Python standard library's `logging` package:

```python
import logging

def get_foo():
	logging.info("foo has been gotten")
	return "foo"
```

### Traces
Traces are provide context as a request works it through a microservice architecture. They use a randomly generated unique ID to track events from various microservices while maintaining shared context. Traces can be visualized using a flamegraph or icicle chart:

![](static/icicle.png)

### Metrics
With metrics, we can measure the performance of the system over varying periods of time. In this article we are going to focus on setting up metrics with a basic Python web server.

The amount of products that deal with metrics is dizzying. A few of the more important ones in this space are:
- [OpenTelemetry](https://opentelemetry.io/): a vendor-agnostic standard for handling metrics, logs, and traces.
- [Prometheus](https://prometheus.io/): a monitoring system and time series database.
- [Grafana](https://grafana.com/): an open source analytics an monitoring solution with a focus on charts and alerts.

All major cloud providers provide their own metric solution:
- [Azure Monitor Metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics)
- [AWS CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [GCP Cloud Monitoring Metrics](https://cloud.google.com/monitoring/api/metrics_gcp)

## Build basic app using [FastAPI](https://fastapi.tiangolo.com/#example)

[FastAPI](https://fastapi.tiangolo.com/) is one of the most popular Python web frameworks. It utilizes modern Python features like type hints to provide a world-class developer experience. It is more similar to its older sibling [Flask](https://flask.palletsprojects.com/en/3.0.x/) than [Django](https://www.djangoproject.com/) (the [two most popular Python web frameworks](https://lp.jetbrains.com/python-developers-survey-2022/#FrameworksLibraries)).

Let's create a simple FastAPI application. All code samples can be found on GitHub at [joeriddles/python-otel-demo](https://github.com/joeriddles/python-otel-demo/).

### Setting up our environment

First, let's create a virtual environment, activate it, and install FastAPI. Note we also need to an ASGI ("asynchronous server gateway interface"... if that doesn't mean anything to you, consider checking out the [ASGI docs](https://asgi.readthedocs.io/en/latest/)). In this case, we'll use [uvicorn](https://www.uvicorn.org/).
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi==0.105.0 uvicorn==0.24.0
```

Next, let's write a basic app in your code editor of choice (I prefer [VS Code](https://code.visualstudio.com/) for Python):
```python
import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}/")
def get_naughty_or_nice(name: str):
	naughty_or_nice = "naughty" if bool(random.randint(0, 1)) else "nice"
	return f"{name}, you have been very {naughty_or_nice} this year!"
```

To start the web server, open a terminal and run:
```shell
uvicorn main:app
```

## Start local [OTel collector](https://opentelemetry.io/docs/collector/getting-started/)

###  OTel collector config
- https://opentelemetry.io/docs/collector/configuration/
- https://jessitron.com/2021/08/11/run-an-opentelemetry-collector-locally-in-docker/
- [zPages](https://github.com/open-telemetry/opentelemetry-collector/blob/main/extension/zpagesextension/README.md)
   - http://localhost:55679/debug/servicez
   - http://localhost:55679/debug/tracez

## Automatic instrumentation
- https://opentelemetry.io/docs/instrumentation/python/automatic/
- https://opentelemetry.io/docs/instrumentation/python/distro/
- https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-instrumentation#opentelemetry-bootstrap
- https://opentelemetry-python.readthedocs.io/en/stable/index.html#integrations
- `pip install opentelemetry-distro[otlp] opentelemetry-instrumentation`
- "opentelemetry-instrument automatically instruments a Python program and its dependencies and then runs the program."

## Azure Monitor
- https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview
- https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable
- https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/azuremonitorexporter
- https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/ch04.html
