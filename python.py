1#Update Values in Dictionaries and Lists.

x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)


2#Iterate Through a List of Dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
 
def iterateDictionary(some_list):
    for i in range(len(some_list)):
       print("first_name - "+some_list[i]['first_name'] +
              ", last_name - "+some_list[i]['last_name'])


    iterateDictionary(students)


# # 3
def iterateDictionary2(key_name, some_list):
   for i in range(0, len(some_list), 1):
    print(some_list[i][key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4
from re import X


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def dojoData(some_dict):
    for i in some_dict:
        print(len(some_dict[i]), i.upper())
        for j in some_dict[i]:
            print(j)
        print("")


dojoData(dojo)