from note_manager import NoteManager


def main():
    notes_manager = NoteManager("notes.json")
    notes = notes_manager.load_notes()
    while True:
        print("\n1 - Вывести список заметок")
        print("2 - Вывести заметку")
        print("3 - Добавить заметку")
        print("4 - Редактировать заметку")
        print("5 - Удалить заметку")
        print("6 или Enter - Выйти")
        choice = input("Введите ваш выбор: ")
        if not choice or choice == 6:
            break
        try:
            choice = int(choice)
        except ValueError:
            choice = 0

        if choice == 1:
            notes_manager.list_notes(notes)
        elif choice == 2:
            notes_manager.get_note_by_id(notes)
        elif choice == 3:
            notes_manager.add_note(notes)
        elif choice == 4:
            notes_manager.edit_note(notes)
        elif choice == 5:
            notes_manager.delete_note(notes)
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
