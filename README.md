# Demo of using OpenTelemetry with a Python API

## Local development

### Getting started

```shell
python3 -m venv .venv
source .venv/bin/activate  # or Windows equivalent
pip install -r requirements.txt
```

### Running

- To start the FastAPI web server: `make run`
- To start the web server with auto instrumentation that logs to the console: `make distro_console`
- To start the web server with auto instrumentation that connects to the local docker OTel collector container:
  - `docker compose up -d`
  - `make distro`

## Blog notes

### [Technical Report Writing](https://ias.ieee.org/wp-content/uploads/2023/06/2020-01-16_IET_Technical_Report_Writing_Guidelines.pdf)
- What does the reader already know about the material of this report?
  - Basic Python. Do not need to know anything about OTel or telemetry in general.
- How wide is the reader’s knowledge of the subject?
  - Little to no knowledge.
- Why should the particular reader need this particular report?
  - To learn how and why to add basic OTel to their Python projects.
- What is it necessary to tell the reader?
  - Why OTel is important and useful
  - The basics of how OTel works
  - How to setup OTel with a Python web server, in this case FastAPI
  - Where to learn more
- What will be the reader’s expected response?
  - They will go try and add OTel instrumentation to their own Python web server.
- What, from the writer’s point of view, is the desired response?
  - See last answer.
  - Increased trust of IntelliTect for OTel, Python, and other metrics needs.
- How can the writer bridge the gap between what the reader knows already and what the writer wants the reader to know, in order to produce the desired response?
  - ...

### Outline
1. build basic app using [FastAPI](https://fastapi.tiangolo.com/#example)
2. Start local [OTel collector](https://opentelemetry.io/docs/collector/getting-started/)
3. OTel collector config
   1. https://opentelemetry.io/docs/collector/configuration/
   2. https://jessitron.com/2021/08/11/run-an-opentelemetry-collector-locally-in-docker/
4. [zPages](https://github.com/open-telemetry/opentelemetry-collector/blob/main/extension/zpagesextension/README.md)
   - http://localhost:55679/debug/servicez
   - http://localhost:55679/debug/tracez
5. Automatic instrumentation
   1. https://opentelemetry.io/docs/instrumentation/python/automatic/
   2. https://opentelemetry.io/docs/instrumentation/python/distro/
   3. https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-instrumentation#opentelemetry-bootstrap
   4. https://opentelemetry-python.readthedocs.io/en/stable/index.html#integrations
   5. `pip install opentelemetry-distro[otlp] opentelemetry-instrumentation`
   6. "opentelemetry-instrument automatically instruments a Python program and its dependencies and then runs the program."
