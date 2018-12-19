
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

iter = 0

def mult(list,iter):

    if list ==[]:
        return None

    if iter == len(list):
        return None

    return list[iter]*mult(list,iter+1)

print( mult(list,0) )