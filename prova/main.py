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

        try:
            with open(commands_file, 'r') as file:
                # Currently only reading one line
                self.line = file.readline().strip()
        except Exception as e:
            raise e

    def add_to_history(self, text):
        new_entry = HistoryEntry(text)
        new_entry.prev = self.currentHistory
        self.currentHistory.next = new_entry
        self.currentHistory = new_entry

    def add(self, string):
        self.text += string
        self.add_to_history(self.text)

    def replace(self, quantity, string):
        self.text = self.text[:-quantity] + string
        self.add_to_history(self.text)

    def delete(self, quantity):
        self.text = self.text[:-quantity]
        self.add_to_history(self.text)

    def undo(self):
        if self.currentHistory.prev:
            self.currentHistory = self.currentHistory.prev
            self.text = self.currentHistory.text


if __name__ == "__main__":
    editor = Editor("edits.txt")
    pass
