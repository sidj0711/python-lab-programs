from easygui import  *
import sys
list_m = []
sum = 0
while 1:
    msgbox("Hello, world!")
    msg ="Choose a product from below" 
    title = "E-bazaar" 
    choices = ["Ice cream", "Biscuits", "Soap"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " + str(choice))
    if (choice == "Ice cream"):
        msg =  "Which flavour?"
        title = "Ice cream flavour"
        choices = ["Chocolate","Vanilla"]
        choice = choicebox(msg,title,choices)
        msgbox("You chose: "+str(choice))
        if (choice == "Chocolate"):
             msg = "Which vendor?"
             title = "Select vendor"
             choices = ["Suresh = $4.50","Ramesh = $5.50"]
             choice = choicebox(msg,title,choices)
             msgbox("You chose: "+str(choice))
             if (choice == "Suresh = $4.50"):
                sum+=4.50
             else:       
                sum+=5.50
             list_m = [choice]
        else:  
             msg = "For vanilla, Which vendor?"
             title = "Select vendor"
             choices = ["Suresh = $3.50","Ramesh = $4.50"]
             choice = choicebox(msg,title,choices)
             msgbox("You chose: "+str(choice))
             if (choice == "Suresh = $3.50"):
                sum+=3.50
             else:       
                sum+=4.50
             list_m = [choice]
    elif (choice == "Biscuits"):
        msg = "Which Brand?"
        title = "Select brand"
        choices = ["Parle-G","Jim Jam"]
        choice = choicebox(msg,title,choices)
        if (choice == "Jim Jam"):
             msg = "Which vendor?"
             title = "Select vendor"
             choices = ["Suresh = $4","Ramesh  $5"]
             choice = choicebox(msg,title,choices)
             msgbox("You chose: "+str(choice))
             if (choice == "Suresh = $4"):
                sum+=4
             else:
                sum+=5
             list_m.append(choice)
        elif (choice == "Parle-G") :
             msg = "Which vendor?"
             title = "Select vendor"
             choices = ["Suresh = $3","Ramesh = $2"]
             choice = choicebox(msg,title,choices)
             msgbox("You chose: "+str(choice))
             if (choice == "Suresh = $3"):
                sum+=3
             else:
                sum+=2
             list_m.append(choice)
    elif (choice == "Soap"):
        msg = "Which brand?"
        title = "Select brand"
        choices = ["Lux","Dove"]
        choice = choicebox(msg,title,choices)
        msgbox("You chose: "+str(choice))
        if (choice == "Lux"):
             msg = "Which vendor?"
             title = "Select vendor"
             choices = ["Suresh = $3","Ramesh = $2"]
             choice = choicebox(msg,title,choices)
             msgbox("You chose: "+str(choice))
             if (choice == "Suresh = $3"):
                sum+=3
             else:
                sum+=2
             list_m.append(choice)
        else:
             msg = "Which vendor?"
             title = "Select vendor"
             choices = ["Suresh = $3.4","Ramesh = $4.3"]
             choice = choicebox(msg,title,choices)
             msgbox("You chose: "+str(choice))
             if (choice == "Suresh = $3.4"):
                sum+=3.4
             else: 
                sum+=4.3
             list_m.append(choice) 
    if ccbox('Would you like to continue?', 'Add to cart'):     # show a Continue/Cancel dialog
        pass  # user chose Continue
        #print(sum)
        #print(list_m)
    else:
        print(sum)
        print(list_m)
        sys.exit(0)