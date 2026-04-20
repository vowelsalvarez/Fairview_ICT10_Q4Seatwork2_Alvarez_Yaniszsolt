
class Classmate:
    
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
 

    def introduce(self):
        print("Hi! I am " + self.name + " from " + self.section + ". My favorite subject is " + self.favorite_subject + ".")
 
 

 
classmate1 = Classmate("Lance Naldoza", "Ruby", "Math")
classmate2 = Classmate("Ashley Mondragon", "Ruby", "Philosophy")
classmate3 = Classmate("Gab Natividad", "Ruby", "Sex education")
classmate4 = Classmate("vaughn repolona", "Ruby", "ICT")
classmate5 = Classmate("Emmile Barcelona", "Emerald", "English")
 
 
#store in list
 
classmates = [classmate1, classmate2, classmate3, classmate4, classmate5]
 

 
print("=== Classmate List ===")
for classmate in classmates:
    classmate.introduce()
 
 #add new classmates
 
print("")
print("=== Add a New Classmate ===")
 
new_name = input("Enter name: ")
new_section = input("Enter section: ")
new_subject = input("Enter favorite subject: ")
 
new_classmate = Classmate(new_name, new_section, new_subject)
classmates.append(new_classmate)
 
print("")
print("=== Updated Classmate List ===")
for classmate in classmates:
    classmate.introduce()