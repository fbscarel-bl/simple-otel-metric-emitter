FROM python:3.12-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://groundcover-opentelemetry-collector.groundcover:4317"

CMD ["python", "app.py"]
