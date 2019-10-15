
def movie():
    print("Find the movie mode")
    q1 = print("is Iron Man in this movie?")
    q1a = input("answer Y for yes and N for no \n")
    if q1a == "Y":
    #########call column which has Ironman present
        print("Ironman 1, Ironman 2, Ironman3")
        q2()
    elif q1a == "N":
        q2()
def q2():
    q2 = print("Is Thor in this movie?")
    q2a = input("answer Y for yes and N for no \n")
    if q2a == "Y":
        print("Thor , Thor 2, Thor:The Dark World, Thor: Ragnorok")
    else:
        print("you win have a nice day")
        

print("Welcome to our AI:chatbot created by team totum")
print("")

def mode():
    print("")
    p = input("Pick a mode ")
    print("")
    if p == "movie":
        movie()
    else:
        print("Mode is not listed")
        mode()
mode()



