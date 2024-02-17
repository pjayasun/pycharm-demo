data={1:"Pranesh", 2:"Gunner", 3:"Prathvika"}

print(data.keys())
print(data.values())

print(data[1])

print(data.get(1))

data.pop(1)

print(data)

data.update({4:'Odegaard'})

print(data)

print(data.get(10, "Not Found"))


keys=[1, 2, 3, 4, 5]
values=["Pranesh", "Gunner", "Prathu", "Mango"]

data_dict=dict(zip(keys, values))

data_dict[5]="Saka"

print(data_dict)

"""
===========================================
"""

prog={"JS": "Atom", "Python": "Pycharm", "C++": ["Sublime", "VS Code"], "Java": {"Java SE": "Netbeans", "Java EE": "Eclipse"}}

print(prog)

print(prog['JS'])
print(prog['Python'])
print(prog['C++'][1])


keys.reverse()

print(keys)