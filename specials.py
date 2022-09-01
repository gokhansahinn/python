from re import S


class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
    def __str__(self):
        return f'{self.title} created by {self.director}'

    def __len__(self):
        return self.duration
    def __del__(self):
        print('Movie has Canceled')

m=Movie('film adı','filmin yönetmeni',120)

print(str(m))
print(len(m))

del(m)
