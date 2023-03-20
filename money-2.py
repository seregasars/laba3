n,m1,m2,m3,m4,s1,s2,s3,s4=map(int, input('Введите значение сдачи, количество монет М1, М2, M3, М4, номинала: S1, S2, S3, S4,: ').split())
mas_nom=[s1,s2,s3,s4]

s=n
m1_out, m2_out,m3_out,m4_out=0,0,0,0
while n!=0:
    while n/s1>=1 and m1>0:
        n-=s1
        m1-=1
        m1_out+=1
    if n==0:
        s=n
        break
    while n/s2>=1 and m2>0:
        n-=s2
        m2-=1
        m2_out += 1
    if n==0:
        s=n
        break
    while n/s3>=1 and m3>0:
        n-=s3
        m3-=1
        m3_out += 1
    if n==0:
        s=n
        break
    while n/s4>=1 and m4>0:
        n-=s4
        m1-=1
        m4_out += 1
    if n==0:
        s=n
        break

print('Монет номинала ',s1, '- ',m1_out)
print('Монет номинала ',s2, '- ',m2_out)
print('Монет номинала ',s3, '- ',m3_out)
print('Монет номинала ',s3, '- ',m4_out)

#23 2 4 3 7 10 5 2 1 - тестовый ввод
