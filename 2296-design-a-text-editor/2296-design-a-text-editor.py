class Node:
    def __init__(self, char: str="", prev=None, next=None):
        self.char = char
        self.prev, self.next = prev, next

class TextEditor:

    # TC: O(1), SC: O(1)
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.head  # Cursor initially at the beginning

    # TC: O(text), SC: O(1)
    def addText(self, text: str) -> None:
        for char in text:
            new_node = Node(char)
            new_node.prev = self.cursor
            new_node.next = self.cursor.next
            self.cursor.next.prev = new_node
            self.cursor.next = new_node
            self.cursor = new_node

    # TC: O(k), SC: O(1)
    def deleteText(self, k: int) -> int:
        count = 0
        while k > 0 and self.cursor != self.head:
            prev_node = self.cursor.prev
            prev_node.next = self.cursor.next
            self.cursor.next.prev = prev_node
            self.cursor = prev_node
            k -= 1
            count += 1
        return count

    # TC: O(k), SC: O(1)
    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.cursor != self.head:
            self.cursor = self.cursor.prev
            k -= 1
        return self._get_left_text()

    # TC: O(k), SC: O(1)
    def cursorRight(self, k: int) -> str:
        while k > 0 and self.cursor.next != self.tail:
            self.cursor = self.cursor.next
            k -= 1
        return self._get_left_text()

    # we can use memory to save left_text instead
    # TC: O(10), SC: O(1)
    def _get_left_text(self) -> str:
        text = []
        curr = self.cursor
        count = 0
        while curr != self.head and count < 10:
            text.append(curr.char)
            curr = curr.prev
            count += 1
        return "".join(text[::-1])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)