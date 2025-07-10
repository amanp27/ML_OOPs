# Initialte Class
class employee:
    # Special methods/dunder methods/ magic methods
    def __init__(self):
        print("Started executing attributes")
        self.id = 123
        self.salary = 60000
        self.desgination = "AI/ML Engineer"
        print("Attribued have been initiated")

    def travel(self, destination):
        print("Funtions/Methods has been called")
        print(f"Employee is traveling to {destination}")


# Create Object or the instance of class
sam = employee()

# Printing attributes
# print(sam.desgination)
# print(sam.salary)

# Calling the function
# sam.travel("Hyderabad")

print(type(sam))