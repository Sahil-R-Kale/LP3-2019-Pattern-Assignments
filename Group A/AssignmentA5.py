'''
Assignment 5: Quick Sort
Date: 19/8/2023
'''
import random 

def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1


def quicksort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quicksort(array, low, pi - 1)
		quicksort(array, pi + 1, high)

def randomPartition(array, low, high):
	i=random.randint(low,high)
	(array[i], array[high]) = (array[high], array[i])
	return partition(array,low,high)

def randomQS(array, low, high):
	if low < high:
		pi = randomPartition(array, low, high)
		randomQS(array, low, pi - 1)
		randomQS(array, pi + 1, high)

if __name__ == '__main__':
	print("----------Quick Sort-----------")
	while(True):
		print("\n------------Menu------------\n1.Deterministic Quick Sort\n2.Non Deterministic Quick Sort\n3.Exit")
		cho=int(input("Enter choice: "))
		arr=[]
		n=int(input("\nEnter number of elements: "))
		for i in range(n):
			a=int(input("Enter number "+str(i+1)+": "))
			arr.append(a)
		if cho==1:
			quicksort(arr, 0, n - 1)
			print('\nSorted array is:')
			for x in arr:
				print(x, end=" ")
			print()
		elif cho==2:
			randomQS(arr, 0, n - 1)
			print('\nSorted array is:')
			for x in arr:
				print(x, end=" ")
			print()
		else:
			print("\nThank you!")
			break 

'''
Output:
----------Quick Sort-----------

------------Menu------------  
1.Deterministic Quick Sort    
2.Non Deterministic Quick Sort
3.Exit
Enter choice: 1

Enter number of elements: 7
Enter number 1: 7
Enter number 2: 12
Enter number 3: 1
Enter number 4: 23
Enter number 5: 4
Enter number 6: 32
Enter number 7: 9

Sorted array is:
1 4 7 9 12 23 32

------------Menu------------
1.Deterministic Quick Sort
2.Non Deterministic Quick Sort
3.Exit
Enter choice: 2

Enter number of elements: 7
Enter number 1: 7
Enter number 2: 12
Enter number 3: 1
Enter number 4: 23
Enter number 5: 4
Enter number 6: 32
Enter number 7: 9

Sorted array is:
1 4 7 9 12 23 32
'''
	