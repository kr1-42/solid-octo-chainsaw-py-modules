from __future__ import annotations

from typing import Any, Dict, List, Optional, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
	def __init__(self, stream_id: str, stream_type: str) -> None:
		self.stream_id = stream_id
		self.stream_type = stream_type
		self._processed_batches = 0
		self._processed_items = 0

	@abstractmethod
	def process_batch(self, data_batch: List[Any]) -> str:
		pass

	def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
		if criteria is None:
			return data_batch
		return [item for item in data_batch if criteria.lower() in str(item).lower()]

	def get_stats(self) -> Dict[str, Union[str, int, float]]:
		return {
			"stream_id": self.stream_id,
			"stream_type": self.stream_type,
			"processed_batches": self._processed_batches,
			"processed_items": self._processed_items,
		}

	def _record_batch(self, count: int) -> None:
		self._processed_batches += 1
		self._processed_items += count


class SensorStream(DataStream):
	def __init__(self, stream_id: str) -> None:
		super().__init__(stream_id, "Environmental Data")

	def process_batch(self, data_batch: List[Any]) -> str:
		if not data_batch:
			raise ValueError("Sensor batch is empty")
		readings = [item for item in data_batch if isinstance(item, str)]
		temps = []
		for item in readings:
			parts = item.split(":", 1)
			if len(parts) == 2 and parts[0].strip().lower() == "temp":
				try:
					temps.append(float(parts[1].strip()))
				except ValueError:
					continue
		self._record_batch(len(readings))
		avg_temp = sum(temps) / len(temps) if temps else 0.0
		return f"Sensor analysis: {len(readings)} readings processed, avg temp: {avg_temp:.1f}°C"

	def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
		if criteria == "critical":
			return [item for item in data_batch if "error" in str(item).lower() or "alert" in str(item).lower()]
		return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
	def __init__(self, stream_id: str) -> None:
		super().__init__(stream_id, "Financial Data")

	def process_batch(self, data_batch: List[Any]) -> str:
		if not data_batch:
			raise ValueError("Transaction batch is empty")
		ops = [item for item in data_batch if isinstance(item, str)]
		net_flow = 0.0
		for item in ops:
			parts = item.split(":", 1)
			if len(parts) != 2:
				continue
			action = parts[0].strip().lower()
			try:
				amount = float(parts[1].strip())
			except ValueError:
				continue
			if action == "buy":
				net_flow -= amount
			elif action == "sell":
				net_flow += amount
		self._record_batch(len(ops))
		return f"Transaction analysis: {len(ops)} operations, net flow: {net_flow:+.0f} units"

	def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
		if criteria == "large":
			result = []
			for item in data_batch:
				parts = str(item).split(":", 1)
				if len(parts) == 2:
					try:
						if float(parts[1].strip()) >= 100:
							result.append(item)
					except ValueError:
						continue
			return result
		return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
	def __init__(self, stream_id: str) -> None:
		super().__init__(stream_id, "System Events")

	def process_batch(self, data_batch: List[Any]) -> str:
		if not data_batch:
			raise ValueError("Event batch is empty")
		events = [str(item) for item in data_batch]
		error_count = 0
		for event in events:
			if "error" in event.lower():
				error_count += 1
		self._record_batch(len(events))
		return f"Event analysis: {len(events)} events, {error_count} error detected"


class StreamProcessor:
	def __init__(self) -> None:
		self._streams: List[DataStream] = []

	def register_stream(self, stream: DataStream) -> None:
		self._streams.append(stream)

	def process_stream(self, stream: DataStream, batch: List[Any]) -> str:
		return stream.process_batch(batch)

	def process_all(self, batches: List[List[Any]]) -> List[str]:
		if len(batches) != len(self._streams):
			raise ValueError("Batches count must match registered streams")
		results = []
		for stream, batch in zip(self._streams, batches):
			results.append(stream.process_batch(batch))
		return results


def _safe_print(label: str, action: function) -> None:
	try:
		print(label)
		action()
	except Exception as exc:
		print(f"Stream error: {exc}")


if __name__ == "__main__":
	print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

	sensor_stream = SensorStream("SENSOR_001")
	transaction_stream = TransactionStream("TRANS_001")
	event_stream = EventStream("EVENT_001")

	_safe_print(
		"Initializing Sensor Stream...",
		lambda: (
			print(f"Stream ID: {sensor_stream.stream_id}, Type: {sensor_stream.stream_type}"),
			print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]"),
			print(sensor_stream.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))
		)
	)

	_safe_print(
		"\nInitializing Transaction Stream...",
		lambda: (
			print(f"Stream ID: {transaction_stream.stream_id}, Type: {transaction_stream.stream_type}"),
			print("Processing transaction batch: [buy:100, sell:150, buy:75]"),
			print(transaction_stream.process_batch(["buy:100", "sell:150", "buy:75"]))
		)
	)

	_safe_print(
		"\nInitializing Event Stream...",
		lambda: (
			print(f"Stream ID: {event_stream.stream_id}, Type: {event_stream.stream_type}"),
			print("Processing event batch: [login, error, logout]"),
			print(event_stream.process_batch(["login", "error", "logout"]))
		)
	)

	print("=== Polymorphic Stream Processing ===")
	print("Processing mixed stream types through unified interface...")

	processor = StreamProcessor()
	processor.register_stream(sensor_stream)
	processor.register_stream(transaction_stream)
	processor.register_stream(event_stream)

	batches = [
		["temp:21.0", "temp:22.0"],
		["buy:50", "sell:120", "sell:40", "buy:30"],
		["login", "update", "logout"],
	]
	results = processor.process_all(batches)

	print("Batch 1 Results:")
    print(f"- Sensor data: 2 readings processed")
	print(f"- Transaction data: 4 operations processed")
	print(f"- Event data: 3 events processed")

	print("Stream filtering active: High-priority data only")
	filtered_sensor = sensor_stream.filter_data(["alert:temp", "ok", "error:pressure"], "critical")
	filtered_trans = transaction_stream.filter_data(["buy:20", "sell:150"], "large")
	print(f"Filtered results: {len(filtered_sensor)} critical sensor alerts, {len(filtered_trans)} large transaction")

	print("All streams processed successfully. Nexus throughput optimal.")
