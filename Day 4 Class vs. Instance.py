class Person:
    def __init__(self,initialAge):
        self.age = initialAge
        if self.age <= 0:
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif (13<=self.age< 18):
            print('You are a teenager.')
        else:
            print('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
         self.age +=1
        # Increment the age of the person in here

