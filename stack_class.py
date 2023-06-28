class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        """проверка стека на пустоту. Метод возвращает True или False."""
        if len(self.stack) > 0:
            return False
        elif len(self.stack) == 0:
            return True

    def push(self, element):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает."""
        self.stack.append(element)

    def pop(self):
        """удаляет верхний элемент стека. Стек изменяется.
        Метод возвращает верхний элемент стека"""
        return self.stack.pop()

    def peek(self):
        """возвращает верхний элемент стека, но не удаляет его. Стек не меняется."""
        return self.stack[-1]

    def size(self):
        """возвращает количество элементов в стеке."""
        return len(self.stack)

    def fullstack(self):
        return self.stack
