# aircraft class
class Aircraft:
    def __init__(self, cargo):
        self.cargo = cargo

    def fly(self):
        return 'croom'
# attributes: cargo

# define a couple of methods, accelerate and brake

aircraft1 = Aircraft('50')
print(aircraft1)

print(aircraft1.cargo) # checking attribute cargo
print(aircraft1.fly()) # calling method fly()

# how to create object
# how to define attributes in object
# how to get information out objsct
#
# attributes vs methods