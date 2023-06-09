pfts=[20,50,30,10,40]
slots=[3,2,1,2,3]
final=[ ]
profit=[ ]
for i in range(max(slots),0,-1):
    print(i)
    for j in range(len(slots)):
        print(j)
        if i == slots[j]:
            final.append(pfts[j])
    print(final)
    profit.append(max(final))
    final.remove(max(final))
    print(profit)
print("total: ",profit[::-1])
print("total: ",sum(profit))
                                                                                                                                                                                                                               
