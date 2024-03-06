import os
import random
import time
from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.metrics import Observation, CallbackOptions
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource

resource = Resource.create(attributes={
    "service.name": "simple-otel-metric-emitter"
})

otlp_exporter = OTLPMetricExporter(endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317"), insecure=True)
metric_reader = PeriodicExportingMetricReader(exporter=otlp_exporter, export_interval_millis=10000)
meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
metrics.set_meter_provider(meter_provider)

meter = metrics.get_meter("simple_metric_emitter", version="0.1")

def random_gauge_callback(options: CallbackOptions):
    random_value = random.uniform(0.0, 100.0)
    return [Observation(random_value, {})]

meter.create_observable_gauge(
    name="random_gauge",
    description="A random gauge value",
    callbacks=[random_gauge_callback],
    unit="unit",
)

if __name__ == "__main__":
    print("Emitting metrics...")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopped metric emission.")

