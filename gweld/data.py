class Data:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Data({self.data!r})'

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    @property
    def max(self):
        return max(self.data)

    @property
    def min(self):
        return min(self.data)
