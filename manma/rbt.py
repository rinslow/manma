BLACK = "black"
RED = "red"
NO_COLOR = "no color"


class NILNode(object):
    def __init__(self, parent=None, left=None, right=None, color=BLACK):
        self._left = None
        self._right = right or None
        self._parent = parent or None
        self._color = color

    @property
    def left(self):
        if self._left is not None:
            return self._left

        return NILNode(parent=self)

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        if self._left is not None:
            return self._left

        return NILNode(parent=self)

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def parent(self):
        if self._parent is not None:
            return self._parent

        return NILNode()

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __repr__(self):
        return "nil"

    def __eq__(self, other):
        return isinstance(other, NILNode) or other == "nil"


NIL = NILNode()


class Node(object):
    def __init__(self, key, parent=None, left=None, right=None, color=None):
        self.key = key
        self.parent = parent or NIL
        self.left = left or NILNode(parent=self)
        self.right = right or NILNode(parent=self)
        self.color = color or NO_COLOR

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return "Node(key=%s, parent=%s, left=%s, right=%s, color=%s)" % (
            self.key, self.parent, self.left, self.right, self.color)

    def __eq__(self, other):
        return self.key == other



class RedBlackTree(object):
    def __init__(self, root=None):
        self.root = root or NIL

    def left_rotate(self, x: Node):
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == NIL:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right != NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == NIL:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def insert(self, z):
        if not isinstance(z, Node):
            z = Node(z)

        x = self.root
        y = NIL  # I think there is a mistake in the books code, this is my addition

        while x != NIL:
            y = x
            if z.key < x.key:
                x = x.left

            else:
                x = x.right

        z.parent = y
        if y == NIL:
            self.root = z

        elif z.key < y.key:
            y.left = z

        else:
            y.right = z

        z.left = NIL
        z.right = NIL
        z.color = RED

        self.insert_fixup(z)

    def insert_fixup(self, z: Node):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent

                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)

            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent

                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)

        self.root.color = BLACK

    def search(self, key):
        node = self.root
        while node != NIL and key != node.key:
            if key < node.key:
                node = node.left

            else:
                node = node.right

        return node

    def minimum(self):
        node = self.root
        while node.left != NIL:
            node = node.left

        return node

    def maxmium(self):
        node = self.root
        while node.right != NIL:
            node = node.right

        return node

    def successor(self):
        node = self.root
        if node.right != NIL:
            return RedBlackTree(node.right).minimum()

        y = node.parent
        while y != NIL and node == y.right:
            node = y
            y = y.parent

        return y

    def predecessor(self):
        node = self.root
        if node.left != NIL:
            return RedBlackTree(node.right).maxmium()

        y = node.parent
        while y != NIL and node == y.left:
            node = y
            y = y.parent

        return y

    def delete(self, z):
        if z.left == NIL or z.right == NIL:
            y = z

        else:
            y = RedBlackTree(z).successor()

        if y.left != NIL:
            x = y.left

        else:
            x = y.right

        x.parent = y.parent

        if y.parent == NIL:
            self.root = x

        elif y == y.parent.left:
            y.parent.left = x

        else:
            y.parent.right = x

        if y != z:
            z.key = y.key  # Copy y's satellite data into z

        if y.color == BLACK:
            self.delete_fixup(x)

        return y

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    w.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent

                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                ...
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    w.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent

                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = BLACK

    def inorder_walk(self):
        if self.root != NIL:
            for value in RedBlackTree(self.root.left).inorder_walk():
                yield value

            yield self.root

            for value in RedBlackTree(self.root.right).inorder_walk():
                yield value

    def __repr__(self):
        return repr(list(self.inorder_walk()))

    def __iter__(self):
        return iter(self.inorder_walk())

    def __len__(self):
        return len(list(self.inorder_walk()))

    def search_successor(self, key):
        """Given a key, find the key closest to it that is equal to it or larger than it.

        Returns:
            Node. the node with the sought-after key.
        """
        # This could be implemented in a much simpler way:
        # perform a binary search using two pointers, if the key exists return it,
        # if it doesn't return the next item in the array
        # However, the asymptotic performances stays O(lgn), which is just what we want :)
        sought = self.search(key)
        if sought != NIL:
            return sought

        self.insert(key)
        key_node = self.search(key)
        successor = RedBlackTree(key_node).successor()
        self.delete(key_node)
        return successor
