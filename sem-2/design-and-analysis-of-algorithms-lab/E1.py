"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms Lab.
* Lab Experiment No. 1 - Write a program that uses functions to perform the following operations on singly linked list
 i) Creation 
 ii) Insertion (at any position in linked list)
 iii) Deletion  (at any position in linked list)
 iv) Traversal
 Take input from user.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, data, index):
        if index > self.len:
            print("Index is greater than the length of the array.\n")
            return None

        if self.head is None:
            self.head = Node(data)
        elif index == 0:
            self.head = Node(data, self.head)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = Node(data, curr.next)
        self.len += 1

    def remove(self, index):
        if index >= self.len:
            print("Index is greater than the length of the array.\n")
            return

        if index == 0:
            self.head = self.head.next
        else:
            i, prev, curr = 0, None, self.head

            while i < index:
                prev = curr
                curr = curr.next
                i += 1

            if curr is not None:
                prev.next = curr.next
            else:
                prev.next = None

            self.len -= 1

    def __len__(self):
        return self.len

    def __str__(self):
        values = []

        curr = self.head
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next

        return (
            " -> ".join(values) if values else "None"
        ) + f"\nThe length of the linked list is {self.len}.\n"


if __name__ == "__main__":
    ll = LinkedList()
    print("List created.\n")

    res = None

    while res != 4:
        res = int(
            input(
                "1. Print the list.\n2. Insert an Element.\n3. Delete an Element.\n4. Exit.\n\n"
            )
        )
        print()

        if res == 1:
            print(ll)
        elif res == 2:
            data, index = list(
                map(
                    int,
                    input(
                        "Enter the element to insert and index at which to be inserted.\n"
                    ).split(" "),
                )
            )
            ll.insert(data, index)
            print()
        elif res == 3:
            ll.remove(int(input("Enter index of the value to be removed.\n")))
            print()

    print("Exiting...")
