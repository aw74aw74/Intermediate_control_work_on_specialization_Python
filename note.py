from datetime import datetime
from typing import Dict, Any


# Модель заметки
class Note:
    def __init__(self, note_id: int, title: str, body: str):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def from_dict(note_dict: Dict[str, Any]) -> "Note":
        # Создаем объект Note из словаря
        return Note(note_dict["id"], note_dict["title"], note_dict["body"])

    def to_dict(self) -> Dict[str, Any]:
        # Возвращаем словарь, представляющий объект Note
        return {
            "id": self.note_id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp,
        }
