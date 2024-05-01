import json

class JournalEntry:
    def __init__(self, id, title, content, author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author


with open("ejercicio1/journal_entries.json", "r") as json_file:
    data = json.load(json_file)


journal_entries = []
for entry_data in data:
    entry = JournalEntry(entry_data["id"], entry_data["title"], entry_data["content"], entry_data["author"])
    journal_entries.append(entry)


for entry in journal_entries:
    print(f"ID: {entry.id}, Title: {entry.title}, Content: {entry.content}, Author: {entry.author}")
