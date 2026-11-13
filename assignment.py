from datetime import datetime
import general_mykyta as gen
import json
ilegal = False
try:
    with open("shelter.json","r") as file:
        shelter_data = json.load(file)
except FileNotFoundError:
    print("JSON File not found")
    ilegal = True
except json.decoder.JSONDecodeError:
    print("JSON file not legit")
    ilegal = True
changes = []
def view_data():
    """showes all data in shelter_data on sepparate lines, shows radio as yes/no"""
    for key in shelter_data:
        print(f"\n{key} : ")
        if key != "radio_working":
            print(f"{shelter_data[key]}")
        else:
            if shelter_data[key]:
                print("yes")
            else:
                print("no")
    print()

def add(list1,str1,val1,val2):
    """writes data into the changes list in a specific way, partialy used to log changes"""
    if val1 != val2:
        list1.append(f"\n{str(datetime.now())[:19]} | {str1} was changed from {val1} to {val2}")

def change_info():
    """asks the user for the name of the variable to change and what to change it to, 
    keeps asking until the user is satisfied and then updates the shelter.json file and the shelter.log file"""
    while True:
           decision2 = gen.secure("Enter the value you want to change or finish modifying(Q): ","any",1)
           if decision2  in ["shelter_name", "leader"]:
               general_check(decision2,"Enter Nonempty text: ","any",1)
           elif decision2  in ["survivors","food","water"]:
               general_check(decision2,"Enter a positive whole number: ",int)
           elif decision2  in ["barricade_health"]:
               val1 = shelter_data[decision2]
               shelter_data[decision2]= gen.secure("Enter a positive whole number bellow 100: ",int,0,100)
               add(changes,decision2,val1,shelter_data[decision2])
           elif decision2 == "radio_working":
              radio_check(decision2)
           elif decision2.lower() == "q":
               break
           else:
               print("Invalid")
    with open("shelter.json","w") as file:
           json.dump(shelter_data,file,indent = 4)
    with open("shelter.log","a") as file:
           file.write("".join(changes))

def general_check(decision2,prompt,type1):
    """does all of the verification fo the user's input and puts it in the shelter_data and change log"""
    val1 = shelter_data[decision2]
    shelter_data[decision2]= gen.secure(prompt,type1,1)
    add(changes,decision2,val1,shelter_data[decision2])

def radio_check(decision2):
    """does what general_check() does but specificaly for the radio"""
    val1 = shelter_data[decision2]
    while True:
        a = gen.secure("Enter 1 for working,0 for not working: ",int,0,1)
        if a == 1:
            shelter_data[decision2] = True
            break
        elif a == 0:
            shelter_data[decision2] = False
    add(changes,decision2,val1,shelter_data[decision2])

def main():
    """ asks the user to chose an option and does either a showcase of the data in shelter.json,
    Allows them to change as many variables in that file as they want and then changes the shellter data and reports to the change log,
    Allows them to veiw the changelog with time stamps,
    or to exit"""
    while True:
    
        print("""   Main Menu
        1) View shelter info
        2) Change shelter info
        3) View change log
        4) Quit""")
        if ilegal:
            print("*Note: file shelter.json is unreachable, please add that file and run this program again*")
            print()
        decision = gen.secure("Enter choice: ",int,1,4)
        if decision == 1:
            if not ilegal:
                view_data()
        elif decision == 2:
            if not ilegal:
                change_info()
        elif decision == 3:
            with open("shelter.log","r") as file:
                content = file.read()
            print(content)
        elif decision == 4:
            break
    print("GOODBYE!!!")


main()            

                

