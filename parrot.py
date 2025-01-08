class dog :
    species= "canine"
    def __init__(self, name, age):
        self. name=name
        self.age=age

lucky= dog("lucky",13)
nicky= dog( "nicky",7)
print("lucky is a {}".format(dog.species))
print("nicky is also a {}".format(dog.species))
print("{} is {} years old".format(lucky.name,lucky.age))
print("{} is {} years old".format(nicky.name,nicky.age))