import json

class JournalEntry:
    # Class variables to keep track of used IDs and emails
    used_ids = set()
    used_emails = set()

    def __init__(self, id, title, content, author):
        self.id = self.generate_unique_id(id)
        self.title = title
        self.content = content
        self.author = author
        self.check_unique_email(author)

    def generate_unique_id(self, id):
        if id in JournalEntry.used_ids:
        
            new_id = id
            while new_id in JournalEntry.used_ids:
                new_id += 1
            return new_id
        else:
            JournalEntry.used_ids.add(id)
            return id

    def check_unique_email(self, email):
        if email in JournalEntry.used_emails:
            raise ValueError(f"Duplicado encontrado: {email}")
        else:
            JournalEntry.used_emails.add(email)


with open("ejercicio1/journal_entries.json", "r") as json_file:
    data = json.load(json_file)


journal_entries = []
for entry_data in data:
    try:
        entry = JournalEntry(entry_data["id"], entry_data["title"], entry_data["content"], entry_data["author"])
        journal_entries.append(entry)
    except ValueError as e:
        print(f"Error: {e}")

# Print the created objects for demonstration
for entry in journal_entries:
    print(f"ID: {entry.id}, Title: {entry.title}, Content: {entry.content}, Author: {entry.author}")
