def count_fun(l):
    even = 0
    odd = 0

    for i in l:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even, odd


l = [1, 2, 3, 4, 5, 6]
even, odd = count_fun(l)

print(even, odd)

print("Even: {}, Odd: {}".format(even, odd))






def count_fun(l):
    users = []
    for name in l:
        if len(name)>5:
            users.append(name);

    return users


l = ["Pranesh", "Gunner", "Prathvika", "Mango"]
users = count_fun(l)

print(users)

print("Users: {}".format(users))