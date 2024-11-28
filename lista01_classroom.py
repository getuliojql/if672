class ObjectArrayList:
    def __init__(self, size=0):
        self.objects = [None] * size
        self.object_counter = 0

    def add(self, obj):
        if self.object_counter >= len(self.objects):
            self.resize()

        self.objects[self.object_counter] = obj
        self.object_counter += 1

    def resize(self):
        new_objects = [None] * (len(self.objects) * 2)

        for i in range(len(self.objects)):
            new_objects[i] = self.objects[i]

        self.objects = new_objects

    def get(self, index):
        if 0 <= index < self.object_counter:
            return self.objects[index]

        else:
            raise IndexError("Index out of range")

    def remove(self, index):
        if 0 <= index < self.object_counter:
            for i in range(index, self.object_counter - 1):
                self.objects[i] = self.objects[i + 1]

            self.objects[self.object_counter - 1] = None
            self.object_counter -= 1

        else:
            raise IndexError("Index out of range")

    def size(self):
        return self.object_counter

    def is_empty(self):
        return self.object_counter == 0

    def __str__(self):
        return "[" + ", ".join(str(self.objects[i]) for i in
range(self.object_counter)) + "]"


if __name__ == "__main__":
    lista = ObjectArrayList(3)

    lista.add("A")
    lista.add("B")
    print(lista)