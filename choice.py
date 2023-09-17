def inputchoice(strlist, stext="Choose one of the following options:"):
    print(stext)
    for i in range(len(strlist)):
        print(str((i + 1)) + ". " + strlist[i])
    
    choice = input("\n:")
    if not choice.isdigit():
        print("\nError: Type a valid number")
        return
    else:
        if len(strlist) > 9:
            if int(choice[0:1]) > 0 and int(choice[0:1]) <= len(strlist):
                chosen = int(choice[0:1])
            else:
                print("\nError: Type a valid number")
                return
        else:
            if int(choice[0]) > 0 and int(choice[0]) <= len(strlist):
                chosen = int(choice[0])
            else:
                print("\nError: Type a valid number")
                return
        
        return chosen
