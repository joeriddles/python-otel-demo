.PHONY: run,distro,distro_console

run:
	uvicorn main:app --reload

test:
	source .venv/bin/activate \
	&& python -m py-marktest blog.md

distro_console:
	export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true && \
	opentelemetry-instrument \
	  --traces_exporter console \
      --metrics_exporter console \
	  --service_name main \
	  uvicorn main:app

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
