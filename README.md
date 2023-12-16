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

### Blog notes
1. build basic app using FastAPI
2. Start local OTel collector
3. OTel collector config
   1. https://opentelemetry.io/docs/collector/configuration/
   2. https://jessitron.com/2021/08/11/run-an-opentelemetry-collector-locally-in-docker/
4. [zPages](https://github.com/open-telemetry/opentelemetry-collector/blob/main/extension/zpagesextension/README.md)
   - http://localhost:55679/debug/servicez
   - http://localhost:55679/debug/tracez
5. Automatic instrumentation
   1. https://opentelemetry.io/docs/instrumentation/python/distro/
   2. `pip install opentelemetry-distro[otlp] opentelemetry-instrumentation`
   3. "opentelemetry-instrument automatically instruments a Python program and its dependencies and then runs the program."
