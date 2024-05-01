import os
import json

class JournalEntry:
    def __init__(self, id, title, content, author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author

entry1 = JournalEntry(1, "Primero", "Codigo de inicio: a1234", "Philip Falla")
entry2 = JournalEntry(2, "Segundo", "Codigo de inicio: 2n230s", "Sofia Eggenberger")
entry3 = JournalEntry(3, "Tercero", "Codigo de inicio: af2f", "Jose Ignacio Paccagnela")
entry4= JournalEntry(3, "Tercero", "Codigo de inicio: af2f", "Jose Ignacio Paccagnela")

entry1_dict = {"id": entry1.id, "title": entry1.title, "content": entry1.content, "author": entry1.author}
entry2_dict = {"id": entry2.id, "title": entry2.title, "content": entry2.content, "author": entry2.author}
entry3_dict = {"id": entry3.id, "title": entry3.title, "content": entry3.content, "author": entry3.author}
entry_4dict = {"id": entry4.id, "title": entry4.title, "content": entry4.content, "author": entry4.author}
entries_list = [entry1_dict, entry2_dict, entry3_dict, entry_4dict]

folder_name = "ejercicio1"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


file_path = os.path.join(folder_name, "journal_entries.json")


with open(file_path, "w") as json_file:
    json.dump(entries_list, json_file, indent=4)

print(f"Se han guardado las entradas en {file_path}")

