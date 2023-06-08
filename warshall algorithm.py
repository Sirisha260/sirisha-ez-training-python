#considering all vertices one by one to all vertices dynamic
nV= 4
INF = 999
#algorithm implementation
def floyd_warshal(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    #Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    print_solution(distance)
#printing solution
def print_solution(distance):
    for i in range(nV):
            for j in range(nV):
                if (distance[i][j] == INF):
                    print("INF" , end=" ")
                else:
                    print(distance[i][j] ,end=" ")
            print(" ")
G = [[0, 3, INF, 5],[2, 0, INF, 4],[INF, 1, 0, INF],[INF,INF,2,0]]
floyd_warshal(G)

                        
    
