
#the collatz sequence
def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return(number //2)
	elif number % 2 == 1 :
		result = 3 * number + 1 
		print (result)
		return(result)

n = 3
while n != 1:
	n=collatz(n)
		
#comma code 

def convert(list):

	if len(list)==1:
		
		return list[0]
	else:

		return '{} and {}'.format(','.join(list[:-1]),list[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']

print(convert(spam))



#caracter picture grid 

grid = [['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]


def picture_grid(grid):

	for y in range(len(grid[0])):
		for x in grid:
			print(x[y],end='')


		print('')	



picture_grid(grid)


#fantasy game inventory 

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):

	total=0
	for key , value in inventory.items():
		print(str(value)+':'+key)
		total+=value
	print('the total is:'+str(total) )	


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory,addedItem):
	


	for x in addedItem:
		if x not in inventory.keys():
			inventory[x]=1
		else :
			inventory[x]+=1
			
	return(inventory)	
		


		

inv=addToInventory(stuff,dragonLoot)

displayInventory(inv)


#table printer 
def TablePrinter(table):

	col=[0]* len(tableData)

	for x in range(len(tableData)):
		for y in tableData:
			if len(y[x])>col[x]:
				col[x]=len(y[x])

	for x in range(len(tableData[0])):
		for y in tableData:
			print(y[x].rjust(max(col)),end='')
		print('')	



tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
		
TablePrinter(tableData)


		



	

			





		



