from __future__ import annotations

import json
import time
from abc import ABC, abstractmethod
from collections import deque
from typing import Any, Deque, Dict, Iterable, List, Protocol, Union


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self._stages: List[ProcessingStage] = []
        self._processed: int = 0
        self._failures: int = 0
        self._durations: Deque[float] = deque(maxlen=50)

    def add_stage(self, stage: ProcessingStage) -> None:
        self._stages.append(stage)

    def stats(self) -> Dict[str, Union[str, int, float]]:
        avg_duration = (
            sum(self._durations) / len(self._durations)
            if self._durations
            else 0.0
        )
        return {
            "pipeline_id": self.pipeline_id,
            "processed": self._processed,
            "failures": self._failures,
            "avg_duration_ms": round(avg_duration * 1000, 2),
        }

    def _run_stages(self, data: Any) -> Any:
        current = data
        for stage in self._stages:
            current = stage.process(current)
        return current

    def _record_success(self, duration: float) -> None:
        self._processed += 1
        self._durations.append(duration)

    def _record_failure(self) -> None:
        self._failures += 1

    def process(self, data: Any) -> Any:
        start = time.perf_counter()
        try:
            result = self._run_stages(data)
            self._record_success(time.perf_counter() - start)
            return result
        except Exception:
            self._record_failure()
            raise

    @abstractmethod
    def adapt(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> List[Any]:
        if data is None:
            raise ValueError("InputStage received no data")
        return [item for item in data]


class TransformStage:
    def process(self, data: Iterable[Any]) -> List[str]:
        return [f"record:{idx}:{item}" for idx, item in enumerate(data)]


class OutputStage:
    def process(self, data: Iterable[str]) -> Dict[str, Any]:
        return {entry.split(":", 2)[1]: entry for entry in data}


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def adapt(self, data: Any) -> Any:
        return json.dumps(data)

    def process(self, data: Any) -> str:
        processed = super().process(data)
        return json.dumps({"id": self.pipeline_id, "payload": processed})


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())

    def adapt(self, data: Any) -> Any:
        if not isinstance(data, str):
            raise TypeError("CSVAdapter expects CSV string input")
        return [part.strip() for part in data.split(",") if part.strip()]

    def process(self, data: Any) -> List[str]:
        adapted = self.adapt(data)
        return super().process(adapted)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def adapt(self, data: Any) -> Any:
        return list(data)

    def process(self, data: Any) -> Dict[str, Any]:
        adapted = self.adapt(data)
        return super().process(adapted)


class NexusManager:
    def __init__(self) -> None:
        self._pipelines: List[ProcessingPipeline] = []

    def register(self, pipeline: ProcessingPipeline) -> None:
        self._pipelines.append(pipeline)

    def run_all(self, payloads: List[Any]) -> List[Any]:
        if len(payloads) != len(self._pipelines):
            raise ValueError("Payload count must match pipelines")
        results: List[Any] = []
        for pipeline, data in zip(self._pipelines, payloads):
            try:
                results.append(pipeline.process(data))
            except Exception as exc:
                results.append(
                    {"pipeline": pipeline.pipeline_id, "error": str(exc)}
                )
        return results

    def chain(self, *pipelines: ProcessingPipeline) -> Any:
        if not pipelines:
            raise ValueError("At least one pipeline required for chaining")
        output: Any = []
        for pipe in pipelines:
            try:
                output = pipe.process(output)
            except Exception:
                output = pipe.adapt(output)
        return output


if __name__ == "__main__":
    manager = NexusManager()
    json_pipeline = JSONAdapter("JSON_MAIN")
    csv_pipeline = CSVAdapter("CSV_MAIN")
    stream_pipeline = StreamAdapter("STREAM_MAIN")

    manager.register(json_pipeline)
    manager.register(csv_pipeline)
    manager.register(stream_pipeline)

    payloads = [
        ["sensor", "temp", "pressure"],
        "alpha,beta,gamma",
        ("login", "error", "logout"),
    ]

    results = manager.run_all(payloads)
    print("=== Nexus Results ===")
    for res in results:
        print(res)

    chained = manager.chain(json_pipeline, stream_pipeline)
    print("=== Chained Output ===")
    print(chained)

    print("=== Pipeline Stats ===")
    for pipe in [json_pipeline, csv_pipeline, stream_pipeline]:
        print(pipe.stats())
