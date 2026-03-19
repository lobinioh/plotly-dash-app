class PlotIterator:
    def __init__(self, data=None):
        self.data = data if data is not None else [1, 2, 3, 4, 5]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Nur Testcode hier, importiert nicht sich selbst!
if __name__ == "__main__":
    pi = PlotIterator()
    for val in pi:
        print(val)
