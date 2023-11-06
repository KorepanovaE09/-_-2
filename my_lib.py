def Fibonnachi(N):
    
    if (N < 0):
        raise ValueError("Неверно введенный формат данных\n 'N' не может быть отрицательным")
    elif (N == 0):
        return [0]
    X_list = ([0,1])
    for i in range (2,N):
        X_list.append(X_list[i-2]+X_list[i-1])

    return X_list

def bubble_sort(list1):
    for i in range(0,len(list1)-1): 
        for j in range(len(list1)-1): 
            if(list1[j]>list1[j+1]): 
                temp = list1[j] 
                list1[j] = list1[j+1] 
                list1[j+1] = temp 
    return list1 

def calculate(a, b, op):
    if (op == "+"):
        return a + b
    elif (op == "-"):
        return a - b
    elif (op == "/"):
        if (b == 0): raise ZeroDivisionError
        return a / b
    elif (op == "*"):
        return a*b
    else: raise ValueError("Неверно введенный формат данных\n Пример: calculate(a, b, +)")
