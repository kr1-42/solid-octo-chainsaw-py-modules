from typing import Any, List, Dict, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if (self.validate(data) is False):
            raise ValueError("Invalid data for NumericProcessor")
        else:
            try:
                if type(data) in [int, float]:
                    return "Number: " + str(data)
                elif type(data) in [list]:
                    for item in data:
                        if type(item) not in [int, float]:
                            raise ValueError(
                                "All items in the list must be numeric"
                                )
                    sum_data = som(data)
                    avg_data = sum_data / length(data)
                    return self.format_output(
                        "Output: Processed " +
                        f"{length(data)} numeric values," +
                        f" Sum = {sum_data}, Average = {avg_data}"
                        )
            except Exception as e:
                raise e

    @staticmethod
    def validate(data: Any) -> bool:
        if type(data) in [int, float, list]:
            return True
        return False

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if (not self.validate(data)):
            raise ValueError("Invalid data for TextProcessor")
        else:
            try:
                if type(data) is str:
                    tot_chars = length(data)
                    words = 1 if tot_chars > 0 else 0
                    for char in data:
                        if char == " ":
                            words += 1
                    return self.format_output(
                        "Output: Processed text: "
                        f"{tot_chars} characters, {words} words"
                        )
                elif type(data) is list:
                    for item in data:
                        if type(item) is not str:
                            raise ValueError(
                                "All items in the list must be strings"
                                )
                    tot_strings = length(data)
                    total_chars = 0
                    total_words = 0
                    for string in data:
                        total_chars += length(string)
                        words = 1 if length(string) > 0 else 0
                        for char in string:
                            if char == " ":
                                words += 1
                        total_words += words
                    return self.format_output(
                        "Output: Processed "
                        f"{tot_strings} strings, "
                        f"{total_chars} characters, "
                        f"{total_words} words"
                        )
            except Exception as e:
                raise e

    @staticmethod
    def validate(data: Any) -> bool:
        if type(data) in [str, list]:
            return True
        return False

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if (not self.validate(data)):
            raise ValueError("Invalid data for LogProcessor")
        else:
            try:
                if type(data) is dict or type(data) is str:
                    return self.format_output(log_process(data))
            except Exception as e:
                raise e

    def validate(self, data: Any) -> bool:
        if type(data) is dict:
            if length(list(data.keys())) != 1:
                return False
            key = str(list(data.keys())[0]).strip()
            return key in ["ERROR", "INFO"]
        elif type(data) is str:
            parts = data.split(":", 1)
            level = parts[0].strip()
            return level in ["ERROR", "INFO"]
        return False

    def format_output(self, result: str) -> str:
        return result


def log_process(log: Union[Dict[str, str], str]) -> str:
    if type(log) is dict:
        log_type = str(list(log.keys())[0]).strip()
        log_message = str(log[log_type]).strip()
    elif type(log) is str:
        parts = log.split(":", 1)
        log_type = parts[0].strip()
        log_message = parts[1].strip() if length(parts) > 1 else ""
    if log_type == "ERROR":
        return f"[ALERT] ERROR level detected: {log_message}"
    elif log_type == "INFO":
        return f"[INFO] INFO level detected: {log_message}"
    else:
        raise ValueError("Unknown log type")


def length(data: any) -> int:
    len_data = 0
    for _ in data:
        len_data += 1
    return len_data


def som(numbers: List[Union[int, float]]) -> float:
    tot = 0
    for n in numbers:
        tot += n
    return tot


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    # Numeric processing
    print("\nInitializing Numeric Processor...")
    try:
        c = str(numeric_processor.process([10, 20, 30]))
        print(c)
        print(numeric_processor.process(42))
    except Exception as e:
        print(e)

    # Text processing
    print("\nInitializing Text Processor...")
    try:
        print(text_processor.process("Hello world! This is a test."))
        print(text_processor.process(["Hello world!", "This is a test."]))
    except Exception as e:
        print(e)

    # Log processing
    print("\nInitializing Log Processor...")
    try:
        print(log_processor.process({"ERROR": "Disk space low"}))
        print(log_processor.process("INFO: System rebooted successfully"))
    except Exception as e:
        print(e)
