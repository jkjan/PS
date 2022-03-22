class Node:
    def __init__(self, alphabet=None):
        self.alphabet = alphabet
        self.adj_list = []


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, x):
        x = list(x)
        self.recursive_insert(self.root, x, 0)

    def recursive_insert(self, parent, x, s):
        if s == len(x):
            return

        i = 0
        while i < len(parent.adj_list):
            if parent.adj_list[i].alphabet == x[s]:
                child = parent.adj_list[i]
                break
            i += 1

        if i == len(parent.adj_list):
            new_node = Node(x[s])
            parent.adj_list.append(new_node)
            child = new_node

        self.recursive_insert(child, x, s + 1)


    def find_word(self, x):



t = Trie()
t.insert("frodo")
t.insert("frame")
t.insert("kakao")
t.insert("frozen")

