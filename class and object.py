class person:
    name = "abubakar"
    occupation ="AI  Developer"
    gpa = 4.5
    def info(self):
         print(f"{self.name} is a {self.occupation}")
a = person()
b = person()
a.name = "ali" 
a.occupation=("software developer")

b.name = "khubaib"
b.occupation = "student"

print(a.name)
print(a.occupation)
print(b.name)
print(b.occupation)