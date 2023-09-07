
class Tree(object):

    def __init__(self, name, height, diameter, talktive = False):
        self.name = name
        self.height = height
        self.diameter = diameter
        self.talktive = talktive
        
    def __str__(self):
        if self.talktive == True:
            return ("{} es un árbol parlante que mide {}cm de altura y {}cm de diámetro".format(self.name, self.height, 
            self.diameter))
        else:
            return ("{} es un árbol no parlante que mide {}cm de altura y {}cm de diámetro".format(self.name, self.height, 
            self.diameter))
    
    def talk(self, message):
        if self.talktive == True:
            print(message)
        else:
            print("El árbol no es parlante")
    
    def grow(self, add_height = 0, add_diameter = 0):
        self.height += add_height
        self.diameter += add_diameter
        
        
trees = []

def born_tree(tree_object):
    trees.append(tree_object)
    print("{} acaba de nacer".format(tree_object.name))
    
def dead_tree(tree_object):
    if tree_object in trees:
        trees.remove(tree_object)
        print("Descansa en paz, {}".format(tree_object.name))
    else:
        print("El arbol no existe")