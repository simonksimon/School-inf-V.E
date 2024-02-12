class Tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def add_right(self,value):
        if self.right==None:
            self.right=Tree(value)
        else:
            temp=Tree(value)
            temp.right=self.right
            self.right=temp
    def add_left(self,value):
        if self.left == None:
            self.left = Tree(value)
        else:
            temp = Tree(value)
            temp.left = self.right
            self.left = temp

    def get_root_value(self):
        pass
    def get_right_tree(self):
        pass
    def get_left_tree(self):
        pass

t=Tree(5)
t.add_left(8)
t.add_right(7)
t.get_right_tree().add_left(5)
t.get_right_tree().add_right(2)
t.get_left_tree().add_right(6)

