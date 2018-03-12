class Font:

    data = { 48: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
             49: [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
             50: [[1, 1, 1], [0, 0, 1], [1, 1, 0], [1, 1, 1]],
             51: [[1, 1, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]],
             52: [[1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
             53: [[1, 1, 1], [1, 1, 0], [0, 0, 1], [1, 1, 1]],
             54: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 1, 1]],
             55: [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
             56: [[1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
             57: [[1, 1, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]] }

    char_separator = [[0], [0], [0], [0]]

    def concat_rows(self, list1, list2):
        if not list1:
            return list2
        else:
            return [x + y for x, y in zip(list1, list2)]

    def char_to_pixels(self, char):
        return self.data[ord(char)]

    def string_to_pixels(self, string):
        buffer = []
        for char in string:
            buffer = self.concat_rows(buffer, self.char_to_pixels(char))
            buffer = self.concat_rows(buffer, self.char_separator)
        return buffer
