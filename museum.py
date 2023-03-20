n=int(input('Введите число экспонатов: '))
m=int(input('Введите количество заходов: '))
k=int(input('Введите предельный вес, который может унести вор: '))
k_copy=k
inf=[]
for i in range(n):
    weight=int(input('Введите вес экспоната: '))
    price=int(input('Введите цену экспоната: '))
    inf.append([weight,price])
inf.sort(key=lambda x: x[1],reverse=True)
s=0
delete=[]
for i in range(m):
    k=k_copy
    for j in inf:
        if k-j[0]>=0 and not(j in delete):
            k-=j[0]
            s+=j[1]
            delete.append(j)
            print(j)

print(s)





