class person:
    def __init__(self):
        print("HEY I AM A PERSON ")
    def info(self):
        print(f"{self.name} in a {self.occ}")

a=person()
a.name = "ahmed"
a.occ = "manager"
a.info()