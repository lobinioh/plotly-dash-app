# PlotIterator.py
class PlotIterator:
    def __init__(self, data=None):
        self.data = data if data else [1, 2, 3, 4, 5]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Testcode nur hier, niemals selbst importieren!
if __name__ == "__main__":
    pi = PlotIterator()
    for val in pi:
        print(val)
