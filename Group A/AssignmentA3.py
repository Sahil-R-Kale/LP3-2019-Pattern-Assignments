'''
Assignment 3: 0/1 Knapsack
Date: 5/8/2023
'''
def knapsack(wt, profit, W, n, dp):
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    if wt[n-1] <= W:
        dp[n][W] = max(
            profit[n-1] + knapsack(wt, profit, W-wt[n-1], n-1,dp),knapsack(wt, profit, W, n-1,dp))
        return dp[n][W]
    elif wt[n-1] > W:
        dp[n][W] = knapsack(wt, profit, W, n-1,dp)
        return dp[n][W]
    
if __name__ == '__main__':
    print("----------Knapsack Problem----------")
    profit=[]
    weight=[]
    n=int(input("\nEnter number of items: "))
    W=int(input("Enter maximum allowed weight: "))
    for i in range(n):
        a=int(input("Enter weight of item "+str(i+1)+" :"))
        b=int(input("Enter value of item "+str(i+1)+" :"))
        weight.append(a)
        profit.append(b)
    dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    print("\nMaximum profit is: ",knapsack(weight, profit, W, n,dp))
 
'''
 Output:
 ----------Knapsack Problem----------

Enter number of items: 3
Enter maximum allowed weight: 50
Enter weight of item 1 :10
Enter value of item 1 :10
Enter weight of item 2 :20
Enter value of item 2 :20
Enter weight of item 3 :30
Enter value of item 3 :30

Maximum profit is:  50

----------Knapsack Problem----------

Enter number of items: 3
Enter maximum allowed weight: 250
Enter weight of item 1 :60
Enter value of item 1 :60
Enter weight of item 2 :100
Enter value of item 2 :100
Enter weight of item 3 :120
Enter value of item 3 :120

Maximum profit is:  220
 '''