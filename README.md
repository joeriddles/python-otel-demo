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
- To start the version of the app with Azure Metrics: `make az`
