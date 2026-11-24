# Используя словесное описание реализовать обход дерева

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 1. Прямой обход Pre-order
def pre_order(node):
    if node:
        print(node.value, end=" ") 
        pre_order(node.left)       
        pre_order(node.right)      

# 2. Симметричный обход In-order: 
def in_order(node):
    if node:
        in_order(node.left)        
        print(node.value, end=" ") 
        in_order(node.right)       

# 3. Обратный обход Post-order
def post_order(node):
    if node:
        post_order(node.left)      
        post_order(node.right)     
        print(node.value, end=" ") 

# Проверка работы 
# Создадим дерево вручную:


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Прямой обход (Pre-order):")
pre_order(root)
print("\n")

print("Симметричный обход (In-order):")
in_order(root)
print("\n")

print("Обратный обход (Post-order):")
post_order(root)
print("\n")