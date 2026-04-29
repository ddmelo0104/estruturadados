class ArrayList:
    def __init__(self):
        self.MEMORY_SPACE = 10
        self.lastPosition = 0
        self.array = [None] * self.MEMORY_SPACE

    def get(self, position: int):
        if position < 0 or position > (self.size() - 1):
            raise IndexError("Index out of bounds exception")
        return self.array[position]

    def updateRemoveArray(self, start: int, end: int):
        for index in range(start, end):
            self.array[index] = self.array[index + 1]
        self.lastPosition -= 1

    def updateInsertArray(self, start: int, end: int):
        for index in range(start, end, -1):
            self.array[index] = self.array[index - 1]
        self.lastPosition += 1

    def removeAll(self):
        self.lastPosition = 0

    def add(self, value):
        if self.lastPosition == self.capacity():
            self.resizeMemory()
        self.array[self.lastPosition] = value
        self.lastPosition += 1

    def insertAt(self, value, position: int):
        if position < 0 or position > self.lastPosition:
            raise IndexError("Index out of bounds exception")
        if self.lastPosition == self.capacity():
            self.resizeMemory()
        self.updateInsertArray(self.lastPosition, position)
        self.array[position] = value

    def removeAt(self, position: int):
        if position < 0 or position > (self.size() - 1):
            raise IndexError("Index out of bounds exception")
        copy = self.array[position]
        self.updateRemoveArray(position, self.size() - 1)
        return copy

    def remove(self):
        last = self.array[self.lastPosition - 1]
        self.lastPosition -= 1
        return last

    def capacity(self):
        return len(self.array)

    def size(self):
        return self.lastPosition

    def print(self):
        for position in range(0, self.lastPosition):
            print(self.array[position])

    def resizeMemory(self):
        print("Mais memoria man")
        newArray = [None] * (self.capacity() * 2)
        for position in range(self.capacity()):
            newArray[position] = self.array[position]
        self.array = newArray


phoneBook = ArrayList()

def addContact(name, phone):
    contact = name + " - " + phone
    phoneBook.add(contact)
    print("Contact added:", contact)

def removeContact(position):
    removed = phoneBook.removeAt(position)
    print("Contact removed:", removed)

def searchContact(name):
    for i in range(phoneBook.size()):
        contact = phoneBook.get(i)
        if name.lower() in contact.lower():
            print(f"Found at position {i}:", contact)
            return
    print("Contact not found:", name)

def listContacts():
    print("\n=== Phone Book ===")
    if phoneBook.size() == 0:
        print("List is empty.")
    else:
        for i in range(phoneBook.size()):
            print(f"[{i}]", phoneBook.get(i))
    print(f"Total: {phoneBook.size()} contact(s)")
    print("==================\n")


addContact("Ana Souza", "(61) 99100-1111")
addContact("Bruno Lima", "(61) 99200-2222")
addContact("Carla Mendes", "(61) 99300-3333")
addContact("Diego Ferreira", "(61) 99400-4444")

listContacts()

print("--- Inserting contact at position 1 ---")
phoneBook.insertAt("Fernanda Costa - (61) 99500-5555", 1)
listContacts()

print("--- Searching contact ---")
searchContact("Bruno")
searchContact("Joao")

print("--- Removing position 0 ---")
removeContact(0)
listContacts()

print("--- Removing last ---")
phoneBook.remove()
listContacts()

print("--- Clearing list ---")
phoneBook.removeAll()
listContacts()
