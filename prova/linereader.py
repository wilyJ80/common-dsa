class HistoryEntry:
    """
    Doubly linked list.
    """

    def __init__(self, text):
        self.text = text
        self.prev = None
        self.next = None


class Editor:
    def __init__(self, commands_file):
        self.text = ''
        self.history_head = HistoryEntry(self.text)
        self.currentHistory = self.history_head
        self.commands = {"add": self.add,
                         "replace": self.replace,
                         "delete": self.delete,
                         "undo": self.undo,
                         "redo": self.redo,
                         "clean": self.clean}

        try:
            with open(commands_file, 'r') as file:
                # Currently only reading one line
                self.line = file.readline().strip()
        except Exception as e:
            raise e

    def eval_line(self, line):
        parts = line.split(maxsplit=1)
        command = parts[0]

        if len(parts) == 1:
            self.commands[command]()

        elif len(parts) == 2:
            text_to_operate = parts[1]

            if command == 'replace':
                subparts = text_to_operate.split(maxsplit=1)
                subcommand = subparts[0]
                subtext_to_operate = subparts[1]

                self.commands[command](subcommand, subtext_to_operate)

            else:
                self.commands[command](text_to_operate)

    def add_to_history(self, text):
        new_entry = HistoryEntry(text)
        new_entry.prev = self.currentHistory
        self.currentHistory.next = new_entry
        self.currentHistory = new_entry

    def add(self, string):
        self.text += string
        self.add_to_history(self.text)

    def replace(self, quantity, string):
        quantity = int(quantity)
        self.text = self.text[:-quantity] + string
        self.add_to_history(self.text)

    def delete(self, quantity):
        self.text = self.text[:-quantity]
        self.add_to_history(self.text)

    def undo(self):
        if self.currentHistory.prev:
            self.currentHistory = self.currentHistory.prev
            self.text = self.currentHistory.text

    def redo(self):
        if self.currentHistory.next:
            self.currentHistory = self.currentHistory.next
            self.text = self.currentHistory.text

    def clean(self):
        self.text = ''


if __name__ == "__main__":
    editor = Editor("edits.txt")
    pass
