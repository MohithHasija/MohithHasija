class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None	

def inorder(obj):

	if obj:
		inorder(obj.left)
		print(obj.data)
		inorder(obj.right)
    
def printit(obj):
	print("I am inorder traversal without recursion")
	l = []
	current = obj
	while True:
		if current:
			l.append(current)
			current = current.left

		elif l:
			f = l.pop()
			print(f.data)
			current = f.right

		else:
		    break	

def check_bst(obj):	
	if obj:
		if obj.left!=None and obj.left.data>=obj.data:
			print("Not a bst")
			return False

		if obj.right!=None and obj.right.data<=obj.data:
			print("Not a bst")
			return False

		else:
			check_bst(obj.left)	
			check_bst(obj.right)
			
		


   #       6
   #    4      8
   # 3     5
#Inorder with recursion
n = Tree(6)
n.left = Tree(4)
n.right = Tree(8)
n.left.left = Tree(3)	
n.left.right = Tree(5)
inorder(n)		
# inorder(n)
# printit(n)
# check_bst(n)
