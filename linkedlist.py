class LinkedList:
	def __init__(self):
		self.head = None

	def printit(self, data_text = "LinkedList list is printed below"):
		temp = self.head
		print(data_text)
		while temp:
			print(temp.data,"--->",end = "")
			temp = temp.next
		print()

	def create(self, l):
		self.head = Node(l[0])
		temp = self.head
		for i in range(1,len(l)):
			temp.next = Node(l[i])
			temp = temp.next

	def delete(self, index = 0):
		temp = self.head
		#1--->2--->3
		if index == 0:
			#Delete head
			self.head = self.head.next
		else:
			#Delete any element except head
			count = 0
			temp = self.head
			previous = None
			while temp:
				if count == index:
					previous.next = temp.next	
					break
				previous = temp	
				count+=1	
				temp = temp.next

	def add(self, data, index = 0):
		temp = self.head
		if index == 0:
			f = Node(data)
			f.next = self.head
			self.head = f

		else:
			count = 0
			previous = None
			while temp:
				if count == index:
					f = Node(data)
					previous.next = f 
					f.next = temp	
					break
				
				elif temp.next == None:
					temp.next = Node(data)
					break	

				count += 1
				previous = temp
				temp = temp.next		

	def remove(self, value):
		pass			


class Node:
	def __init__(self, data):
		self.data = data	
		self.next = None	
	

####### Convert list to LinkedList #######
l = [11,1,2,3,4,5]
new_l = LinkedList()
new_l.create(l)
# new_l.printit("List to LinkedList")
# new_l.delete()
# new_l.printit("After deleting head")
new_l.add(121,6)
new_l.printit("After adding at head")


####### Create LinkedList normally #######
# ll = LinkedList()
# ll.head = Node(1)
# n1 = Node(2)
# n2 = Node(3)
# n3 = Node(4)
# n4 = Node(5)
# n5 = Node(6)

# ll.head.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# ll.printit()

