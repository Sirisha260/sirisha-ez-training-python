'''#addition of2 squarematrix
X=[[1,2,3],[4,5,6],[7,8,9]]
Y=[[9,8,7],[6,5,4],[3,2,1]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]
for r in result:
    print(r)

#user defined matrix
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(R):		
	a =[]
	for j in range(C):	
		a.append(int(input()))
	matrix.append(a)
#forprinting
for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()'''


#diagonal elements
def diagonalMat(a):
    row=len(a)
    col=len(a[0])
    for i in range(row):
        for j in range(col):
            if(i==j):
                print(a[i][j],end=" ")
    print()
a=[[1,2,3,4],[2,3,4,5],[4,5,6,7],[6,7,8,9]]
diagonalMat(a)


def nondiagonalMat(a):
    row=len(a)
    col=len(a[0])
    for i in range(row):
        for j in range(col):
            if(i!=j):
                print(a[i][j],end=" ")
    print()
a=[[1,2,3,4],[2,3,4,5],[4,5,6,7],[6,7,8,9]]
nondiagonalMat(a)

def lowerdiagonalMat(a):
    row=len(a)
    col=len(a[0])
    for i in range(row):
        for j in range(col):
            if(i>j):
                print(a[i][j],end=" ")
    print()
a=[[1,2,3,4],[2,3,4,5],[4,5,6,7],[6,7,8,9]]
lowerdiagonalMat(a)

def upperdiagonalMat(a):
    row=len(a)
    col=len(a[0])
    for i in range(row):
        for j in range(col):
            if(i<j):
                print(a[i][j],end=" ")
    print()
a=[[1,2,3,4],[2,3,4,5],[4,5,6,7],[6,7,8,9]]
upperdiagonalMat(a)













	


