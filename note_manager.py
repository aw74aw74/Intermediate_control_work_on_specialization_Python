import json
from pathlib import Path
from typing import List
from note import Note
from datetime import datetime


# Менеджер заметок
class NoteManager:
    def __init__(self, notes_file: str):
        # Путь к файлу, где хранятся заметки
        self.notes_file = notes_file

    def load_notes(self) -> List[Note]:
        # Загружаем заметки из файла
        if not Path(self.notes_file).exists():
            return []
        try:
            with open(self.notes_file, "r") as f:
                notes_dict = json.load(f)
            return [Note.from_dict(note_dict) for note_dict in notes_dict]
        except Exception as e:
            print(e)

    def save_notes(self, notes: List[Note]):
        # Сохраняем заметки в файл
        try:
            with open(self.notes_file, "w") as f:
                json.dump([note.to_dict() for note in notes], f)
            return True
        except Exception as e:
            print(e)

    def add_note(self, notes: List[Note]):
        # Добавляем новую заметку
        # ID заметки ищем от 1 до максимального значения из базы.
        # Если на этом промежутке есть свободный номер, берем для
        # нового ID иначе назначаем максимальный+1
        if not notes:
            note_id = 1
        else:
            note_ids = [note.note_id for note in notes]
            max_note_id = max(note_ids)
            for i in range(1, max_note_id + 1):
                if i not in note_ids:
                    note_id = i
                    break
                else:
                    note_id = max_note_id + 1

        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        note = Note(note_id, title, body)
        notes.append(note)
        if self.save_notes(notes):
            print("Заметка добавлена.")

    def edit_note(self, notes: List[Note]):
        # Редактируем существующую заметку
        while True:
            try:
                note_id = int(input("Введите ID заметки для редактирования: "))
                break
            except ValueError:
                print("Неверный формат ID. Попробуйте снова.")

        for note in notes:
            if note.note_id == note_id:
                note.title = input("Введите новый заголовок заметки: ")
                note.body = input("Введите новое тело заметки: ")
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if self.save_notes(notes):
                    print("Заметка обновлена.")
                return
        print("Заметка не найдена")

    def delete_note(self, notes: List[Note]):
        # Удаляем заметку
        while True:
            try:
                note_id = int(input("Введите ID заметки для удаления (0 - Все): "))
                break
            except ValueError:
                print("Неверный формат ID. Попробуйте снова.")

        if note_id == 0:
            notes.clear()
            if self.save_notes(notes):
                print("Все заметки удалены")
            return

        for i, note in enumerate(notes):
            if note.note_id == note_id:
                del notes[i]
                if self.save_notes(notes):
                    print("Заметка удалена.")
                return
        print("Заметка не найдена")

    def list_notes(self, notes: List[Note]):
        # Выводим список заметок, при необходимости с фильтрацией по дате,
        # как написано в ТЗ.
        filter_date = input("Введите фильтр даты (YYYY-MM-DD), Enter - все: ")
        for note in notes:
            if not filter_date or filter_date in note.timestamp:
                print(
                    f"ID: {note.note_id} - Заголовок: {note.title} - Дата: {note.timestamp}"
                )

    def get_note_by_id(self, notes: List[Note]):
        # Выводим заметку по ID
        while True:
            try:
                note_id = int(input("Введите ID заметки для просмотра: "))
                break
            except ValueError:
                print("Неверный формат ID. Попробуйте снова.")
        note_result = False
        for note in notes:
            if note.note_id == note_id:
                print(
                    f"\nID: {note.note_id}\nЗаголовок: {note.title}\nДата: {note.timestamp}"
                )
                print(f"Заметка:\n{note.body}")
                note_result = True
        if not note_result:
            print("Заметка не найдена")
