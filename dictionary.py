plakalar={ 'İzmir': 35,
            'Muğla':48
}

print(plakalar['İzmir'])
print(plakalar['Muğla'])

plakalar['ISPARTA']=32
plakalar['Antalya']=7

print(plakalar)

users={
    'Gökhan':{
        'age':24,
        'school':'EGE UNIVERSITY',
        'email':'gkhnsahin4848@gmail.com'
    },
    'Muammer':{
        'age':21,
        'school':'DOKUZ EYLUL UNIVERSITY',
        'email':'muammer@muammer.com'
    }
}
print(users)
print(users['Gökhan']['age'])
print(users['Gökhan']['school'])