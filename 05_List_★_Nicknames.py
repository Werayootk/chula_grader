real = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

n = int(input())
for i in range(n):
    x = input()
    if x not in real and x not in nick:
        print('Not Found')
    elif x in real:
        k = real.index(x)
        print(nick[k])
    else:
        k = nick.index(x)
        print(real[k])
        
