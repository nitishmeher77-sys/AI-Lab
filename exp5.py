# EXP-5 MIN-MAX ALGORITHEM


def minmax ( depth,nodeindex, ismax,scores,height):
    if depth==height:
        return scores[nodeindex]
    if ismax:
        return max(
            minmax(depth+1,nodeindex*2,False,scores,height),
            minmax(depth+1,nodeindex*2+1,False,scores,height)
        )
    else:
        return min(
           minmax(depth+1,nodeindex*2, True,scores,height),
           minmax(depth+1,nodeindex*2+1,True,scores,height)
            )
score=list(map(int,input("enter 8 leaf node values:").split()))
height=3
result=minmax(0,0,True,score,height)
print("\n the optimal value is:",result)
'''------OUTPUT-----
enter 8 leaf node values:3 5 2 9 12 5 23 23 

 the optimal value is: 12



'''