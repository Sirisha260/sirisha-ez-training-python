'''what  is the recursive  problem of coin change?

The coin change problem seeks a solution that returns the min number of coins required to sum bup to given value.
The recursive approach checks the length of all the combinations'''

def count(s,target):
    if target ==0:
        return 1
    if target<0:
        return 0
    result=0
    for c in s:
        #recur to see if total can be reached by including current coin c
        result+=count(s,target-c)
    return result
if __name__=='__main__':
    s=[1,2,3]
    target=3
    print("Total no.of ways to get 3:",count(s,target))
