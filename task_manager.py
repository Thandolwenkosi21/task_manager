user, pas ='',''#declare empty variables 

with open('user.txt', 'r') as f1:#opening a file as f1
    userList = []#creating an empty list

    for line in f1: #for line in f1
        userList.append(line.strip('\n').split(', '))#userlist is appended with line.strip(\n) and split(',')
    print(userList)

    login = True#login is true

    while login:
        username = input("Enter username: ")#requests user for user input
        print(username)
        password = input("Enter password : ")#requests user for password input
        print(password)

        for user in userList:
            if user[0] == username and user[1] == password:#if user[0] is equal to username and user[1] is equal password
                login = False#login is true
                break


        if login:
            print("invalid username or password ,please enter correct details")#prints the statement if the details are incorrect
        else:
            print("your login was successful")#prints the statement if the details are correct
            

with open('user.txt','a') as f2:#open txt file as f2

    if username == "admin" and password == "adm1n" :#if username is admin and password is adm1n
        option = input("please select one of the options : \n[r]register \n[a]add task \n[va]view all tasks \n[vm]view my tasks\n[s]view statistics \n[e]exit")#request user input , the menu displayed
        print(option)

    else:
        option = input("please select one of the options : \n[a]add task \n[va]view all tasks \n[vm]view my tasks \n[e]exit")#requests user input from the displayed menu
        print(option)


    if option == "r":#if option "r"

        #requests user input
        name1 = input("enter name")

        password_1 = input("enter password")

        password_2 = input("enter password")

        if password_1 == password_2 :#if password1 matches password2
            print("registration sucessful")#prints statement
        else: 
            print("passwords do not match")#if not print password not match
        f2.write(f"\n{name1}, {password_2}")#f2 writes statement in format form calling the variables name1 and password
    
    if option == "a" :#if input is "a"
        with open('tasks.txt','a') as f3:

        #requests user input
    
            task_username = input("enter username")

            title = input("enter title of task ")

            description = input("enter description")

            date_assigned = input("enter date assigned")
        
            due_date = input("enter due date")

            task_completition = 'no'
            print("task added")
            f3.write(f"\n{username}, {title}, {description},{date_assigned}, {due_date}, {task_completition}")#f4 writes the variables being called in txt file in a formated style
    
    if option == "va" :#if input is "a"

        with open('tasks.txt','r') as f4:
       
            a_tasks = f4.read()#variable a_tasks reads data in f4 
            print(a_tasks)

    if option == "vm":#if option is vm
    
        with open ("tasks.txt","r") as task_file:#opens txt file as task_file
    
    
            for line in task_file:

                userTasks = line.split(", ")#variable user_tasks consists of line.split(",")spliting at each coma
                if userTasks[0] == username:#if userTasks position[0] is equal to username

                    print(f'''
                    task : {userTasks[1]}
                    Assigned to : {userTasks[0]}
                    Date assigned : {userTasks[3]} 
                    Due date : {userTasks[4]} 
                    task : {userTasks[5]}
                    Task description  : {userTasks[2]}
                    ''')#prints the data in a formated style indexing the positions in  tasks.txt
    
    if option  == "s": #if option is s
        with open ('tasks.txt','r') as t_file:
        
            count = 0#has count as 0

            for line in t_file:    
                count += 1#count as 0 counts each task

        print(f"The number of lines is {count}")

        with open ('user.txt','r') as u_file:

            count = 0#has count as 0

            for line in u_file:  
                count += 1#has count as 0  counts each user 

        print(f'The number of users is {count}')

    if option == "e"#if option 'e' is selected
        print("you have exited")
        exit()
