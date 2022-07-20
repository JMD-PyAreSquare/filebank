import os

print('welcome to the file bank.')
print('press 1 to read a file, press 2 to edit a file, press 3 to create a file that does not already exist, or press 4 to delete one that does.')
main_choice = int(input('Press 1, 2 , 3, or 4. '))
if main_choice == 1:
    print('the file that you want to read must exist in this folder.')
    choice = str(input('what file do to want to read? include the file extension.'))
    file = open(f'{choice}', 'r')
    print(file.read())
    timepass = input('press [ENTER] to exit')
        
elif main_choice == 2:
    print('the file that you want to edit must exist in this folder.')
    choice = str(input('what file do to want to edit? include the file extension. '))
    file = open(f"{choice}", "a")
    running = True
    line = 0
    x = (input('how many lines do you want to edit? '))
    for i in range(int(x)):
        line += 1
        choice = str(input('what do you want to edit on line ' + str(line) + '?'))
        file.write(f"{choice}\n")
    file.close()
    timepass = input('done. press [ENTER] to exit')
    
elif main_choice == 3:
    choice = input("what do you want to name the file? include the file extension. ")
    file = open(f"{choice}", "x")
    timepass = input('done. press [ENTER] to exit')
    
elif main_choice == 4:
    choice = input('what is the name of the file that you want to delete? include the file extension. ')
if os.path.exists(f"{choice}"):
    os.remove(f"{choice}")
    timepass = input('done. press [ENTER] to exit')

