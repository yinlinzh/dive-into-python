class Indexer:
    A = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        if index > 3:
            raise TypeError()
        print('getitem: ', index)
        return self.A[index]
        # return index ** 3

I = Indexer()
# print(I[0:4])
for item in I:
    print(item)

ii = iter(I)
