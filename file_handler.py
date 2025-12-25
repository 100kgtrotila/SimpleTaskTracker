from typing import List, Dict, Any
import json
import os

class FileHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    #Read
    def read_data(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding='utf-8') as f:
                return json.load(f)
        except(json.JSONDecodeError, IOError):
            return []

    #Save
    def save_data(self, data: List[Dict[str, Any]]) -> None:
        try:
            with open(self.file_path, "w", encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error {e}")
