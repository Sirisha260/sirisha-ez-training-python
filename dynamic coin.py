#all solutions of coin change
'''def count(S, m, n):
    table = [0 for k in range(n+1)]
    print(table)
    table[0] = 1
    for i in range(0,m):#0,1,2
        for j in range(S[i],n+1):#s[0]=1
            table[j] += table[j-S[i]]
    #t[1]=t[1]+t[1-s[0]]
            print(table)
    return table[n]
arr=[1,2,3]
m=len(arr)
n=7
x=count(arr,m,n)
print(x)
'''
#mimum solutions in coin change
class solution:
    def coinchange(self,List,amount):
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for a in range(1,amount+1):#from dp[1] to dp[11]
            print("a: ",a)
            for c in List:#picking up currencies
                print("c: ",c)
                if a-c>=0:
                    dp[a]=min(dp[a], 1+dp[a-c])
                    print(a)
                    print("dp: ",dp[a])
        return dp[amount] if dp [amount]!=amount+1 else -1
obj=solution()
List=[1,3,4,5]
amount=11
print(obj.coinchange(List,amount))










                    
    
