.PHONY: run
run:
	uvicorn main:app --reload

.PHONY: az
az:
	uvicorn main_az:app --reload

.PHONY: setup
setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

.PHONY: set
test:
	. .venv/bin/activate; python -m py_marktest blog.md

.PHONY: distro_console
distro_console:
	export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true && \
	opentelemetry-instrument \
	  --traces_exporter console \
      --metrics_exporter console \
	  --service_name main \
	  uvicorn main:app

.PHONY: distro
distro:
	export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true && \
	opentelemetry-instrument \
	  --traces_exporter otlp \
	  --metrics_exporter otlp \
	  --metric_export_interval 1000 \
	  --exporter_otlp_protocol 'http/protobuf' \
	  --exporter_otlp_endpoint 'http://localhost:4318' \
	  --service_name main \
	  uvicorn main:app
