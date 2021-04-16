"""
Ron Mansharof  208839787
Benny Shalom 203500780
"""


def print_Matrix(M):
    '''

    :param M:Matrix
    :return: print matrix
    '''
    for i in M:
        for j in i:
            print(j, end=" ")
        print()

def mul_Matrix(A,B):
    '''

    :param A:matrix
    :param B: matrix
    :return: mul A and B (A is in the left, B is in the right)
    '''
    size = len(A)
    size2=len(B)
    result = [[0 for i in range(size2)] for j in range(size)]
    for i in range(len(A)):
        for j in range(size2):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result



def swapRows(A,row1,row2):
    '''

    :param A: matrix
    :param row1: row
    :param row2: row
    :return: swap row1 and row2 and return the new matrix(A is update)
    '''
    temp=A[row1]
    A[row1]=A[row2]
    A[row2]=temp
    return A
#/////////////////////////////////////////////////
def Pivot(A,row):
    '''

    :param A: matrix
    :param row: row index
    :return: make sure all the numbers on the diagonal are the largest in the column(A is update)
    '''
    maximum=abs(A[row][row])
    help=row
    if row!=len(A)-1:
        for i in range(row+1,len(A)):
            if abs(A[i][row])>=maximum:
                maximum=abs(A[i][row])
                help=i
    if help!=row:
        swapRows(A,row,help)
    return A
#/////////////////////////////////////////////////
def identity_Matrix(A):
    '''

    :param A:matrix
    :return: identity matrix in size of A matrix
    '''
    size = len(A)
    b= [[0 for i in range(size)] for j in range(size)]
    for i in range(0,size):
        for j in range(0,size):
            if i==j:
                b[j][i]=1
    return b
#/////////////////////////////////////////////////
def elementary_matrix(A,r):
    '''

    :param A:matrix
    :param r: row index
    :return: elementary matrix
    '''
    maximum=A[r][r]
    k=identity_Matrix(A)
    for i in  range(r+1,len(A)):
        if A[i][r]!=0 and maximum!=0:
            k[i][r]=-1*(A[i][r]/maximum)
    return k
#/////////////////////////////////////////////////
def copyMatrix(M):
    '''

    :param M: Matrix
    :return: copy of matrix M
    '''
    size=len(M)
    m=[[0 for i in range(size)] for j in range(size)]
    for i in range(0,size):
        for j in range(0,size):
                m[i][j]=M[i][j]
    return m

#/////////////////////////////////////////////////
def LU(A,r):
    """

    :param A: Matrix
    :param r: row index
    :return: U,L Matrices
    """
    size=len(A)
    U=copyMatrix(A)
    L=identity_Matrix(A)
    for i in range(size):
        Pivot(U, i)
        help=elementary_matrix(U,i)
        L=mul_Matrix(L,help)
        U=mul_Matrix(help,U)
    for i in range(size):
        for j in range(size):
            if i!=j and L[i][j]!=0:
                L[i][j]=-1*L[i][j]
    return (U,L)
# /////////////////////////////////////////////////

def inverseMatrix(A):
    '''

    :param A: matrix
    :return: A^-1
    '''
    A2=copyMatrix(A)
    I=identity_Matrix(A)
    for a in range(len(A)):
        div1 = 1.0 / A2[a][a]
        for j in range(len(A)):
            A2[a][j] *= div1
            I[a][j] *= div1
        for i in list(range(len(A)))[0:a] + list(range(len(A)))[a + 1:]:
            div2 = A2[i][a]
            for j in range(len(A)):
                A2[i][j] = A2[i][j] - div2 * A2[a][j]
                I[i][j] = I[i][j] - div2 * I[a][j]
    return I

# /////////////////////////////////////////////////

def cond(A,A1):
    '''

    :param A:matrix
    :param A1: inverse matrix of A
    :return: cond (||A||*||A^-1||)
    '''
    size=len(A)
    #size1=len(A1)
    a=0
    a1=0
    for i in range(size):
        temp=0
        temp1=0
        for j in range (size):
            temp=temp+abs(A[i][j])
            temp1=temp1+abs(A1[i][j])
        if temp>a:
            a=temp
        if temp1>a1:
            a1=temp1
    print("a= {0}  , a1= {1}".format(a,a1))
    print("Cond ||A||*||A^-1||= {0}".format(a*a1))
    return a*a1
# /////////////////////////////////////////////////
def first_way(A,b):
    a1=inverseMatrix(A)
    x=mul_Matrix(a1,b)
    print_Matrix(x)
    return x

# /////////////////////////////////////////////////
def second_way(A, b):
    U,L = LU(A,0)
    print("L: ")
    print_Matrix(L)
    print("U: ")
    print_Matrix(U)
# /////////////////////////////////////////////////
A= [[2,3,5],[0,2,1],[1,2,3]]
b=[[1, -1,1]]


if len(A)>=4:
    second_way(A,b)
else:
    first_way(A,b)

