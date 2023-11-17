'''
Assignment 1: Iterative and Recursive Fibonacci Series
Date: 22/7/2023
'''
def iterFib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    for i in range(2,n+1):
        c=a+b 
        a=b
        b=c 
    return b 

def recurFib(n):
    if n<=1:
        return n 
    return recurFib(n-1)+recurFib(n-2)

if __name__=='__main__':
    print("-----Iterative and Recursive Fibonacci Series-----")
    while(True):
        print("\n---------Menu---------\n1.Iterative Algorithm\n2.Recursive Algorithm\n3.Exit")
        a=int(input("Enter choice: "))
        b=int(input("Enter value of n: "))
        if a==1:
            ans=iterFib(b)
            print('\nThe',b,'th Fibonacci number is:',ans)
        elif a==2:
            ans=recurFib(b)
            print('\nThe',b,'th Fibonacci number is:',ans)
        elif a==3:
            print("\nThank you!")
        else:
            print("Invalid choice!")

'''
Output:
-----Iterative and Recursive Fibonacci Series-----

---------Menu---------
1.Iterative Algorithm
2.Recursive Algorithm
3.Exit
Enter choice: 1
Enter value of n: 7

The 7 th Fibonacci number is: 13

---------Menu---------
1.Iterative Algorithm
2.Recursive Algorithm
3.Exit
Enter choice: 2
Enter value of n: 7

The 7 th Fibonacci number is: 13

---------Menu---------
1.Iterative Algorithm
2.Recursive Algorithm
3.Exit
Enter choice: 1
Enter value of n: 9

The 9 th Fibonacci number is: 34

---------Menu---------
1.Iterative Algorithm
2.Recursive Algorithm
3.Exit
Enter choice: 2
Enter value of n: 10

The 10 th Fibonacci number is: 55

---------Menu---------
1.Iterative Algorithm
2.Recursive Algorithm
3.Exit
Enter choice: 1
Enter value of n: 55

The 55 th Fibonacci number is: 139583862445

---------Menu---------
1.Iterative Algorithm
2.Recursive Algorithm
3.Exit
Enter choice: 2
Enter value of n: 34

The 34 th Fibonacci number is: 5702887
'''