# Print all possible subsets for the numbers from 1 to number.

number = int(input())
picked = [False for x in range(number)]

def subsets(index):
	if index == number:
		for i in range(0, number):
			if picked[i]:
				print(i+1, end=''),
		print()
	else:
		picked[index] = True
		subsets(index+1)
		
		picked[index] = False
		subsets(index+1)
		
subsets(0)
