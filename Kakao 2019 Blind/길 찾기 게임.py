from collections import defaultdict
import sys



class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


    def insert_all(self, ns):
        for n in ns:
            self.insert(n)


    def insert(self, n):
        has_children = self.insert_recursive(self.root, n)
        if not has_children:
            self.root = Node(n)


    def insert_recursive(self, parent, n):
        if parent is None:
            return False

        if parent.n > n:
            has_left = self.insert_recursive(parent.left, n)
            if not has_left:
                parent.left = Node(n)
            return True

        if parent.n < n:
            has_right = self.insert_recursive(parent.right, n)
            if not has_right:
                parent.right = Node(n)
            return True


    def pre_order(self):
        bucket = []
        self.pre_order_recursive(bucket, self.root)
        return bucket


    def pre_order_recursive(self, bucket, parent):
        if parent is None:
            return

        bucket.append(parent.n)
        self.pre_order_recursive(bucket, parent.left)
        self.pre_order_recursive(bucket, parent.right)


    def post_order(self):
        bucket = []
        self.post_order_recursive(bucket, self.root)
        return bucket


    def post_order_recursive(self, bucket, parent):
        if parent is None:
            return

        self.post_order_recursive(bucket, parent.left)
        self.post_order_recursive(bucket, parent.right)
        bucket.append(parent.n)


def solution(nodeinfo):
    sys.setrecursionlimit(10001)
    level = defaultdict(lambda: [])
    bst = BST()
    x_to_node = {}

    for i, (x, y) in enumerate(nodeinfo):
        x_to_node[x] = (i + 1)
        level[y].append(x)

    level_key = sorted(level.keys(), reverse=True)
    for k in level_key:
        level[k].sort()
        bst.insert_all(level[k])


    answer = [[x_to_node[k] for k in bst.pre_order()],
              [x_to_node[k] for k in bst.post_order()]]
    return answer


nodeinfo = [[5,3], [6, 4]]
print(solution(nodeinfo))