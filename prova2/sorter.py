import readline

class Sorter:
    def __init__(self):
        self.lines = []
        self.thousand_line_buffer = []
        with open('files/m1.txt') as file:
            self.file = file.readlines()

    def sort_array(self):
        return sorted(self.lines)

    def sort_lines(self, line_array):
        return sorted(line_array)

    def bufferize(self, line_array):
        for i in range(0, len(line_array), 1000):
            chunk = line_array[i:i+1000]
            self.thousand_line_buffer.append(chunk)