
art = '''

 ___      _______  _______  _______  _______  ______      _______  _______  __   __  __    _  _______  _______  ______   
|   |    |       ||       ||       ||       ||    _ |    |       ||       ||  | |  ||  |  | ||       ||       ||    _ |  
|   |    |    ___||_     _||_     _||    ___||   | ||    |       ||   _   ||  | |  ||   |_| ||_     _||    ___||   | ||  
|   |    |   |___   |   |    |   |  |   |___ |   |_||_   |       ||  | |  ||  |_|  ||       |  |   |  |   |___ |   |_||_ 
|   |___ |    ___|  |   |    |   |  |    ___||    __  |  |      _||  |_|  ||       ||  _    |  |   |  |    ___||    __  |
|       ||   |___   |   |    |   |  |   |___ |   |  | |  |     |_ |       ||       || | |   |  |   |  |   |___ |   |  | |
|_______||_______|  |___|    |___|  |_______||___|  |_|  |_______||_______||_______||_|  |__|  |___|  |_______||___|  |_|
'''
def lettercount():
    print(art)
    firstletter = input("What is your first name: ")
    lastletter = input("What is your last name: ")

    totallength = len(firstletter)+len(lastletter)

 
    print(f"The total length in your namer is {totallength}")
    print("Thank You for using me!")

lettercount()
