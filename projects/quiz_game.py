print("welcome to my quiz game")

a = input("do you want to play? ")
if a.lower()!= "yes":
    quit()

print("okay! lets play  :")
score = 0

b = input("what does cpu stands for?  ")
if b.lower() == "central processing unit":
    print('correct')
    score +=1
else:
    print('incorrect')

c = input("what does ram stands for?  ")
if c.lower() == "random access memory":
    print('correct')
    score +=1
else:
    print('incorrect')

d = input("who is the father of nation?  ")
if d == "MAhatma gandhi ji".lower():
    print('correct')
    score +=1
else:
    print('incorrect')

e = input("who the fuck is pm of india?  ")
if e.lower() == "modi":
    print('gandu')
    score +=1
else:
    print('incorrect')

print("you got" + str(score) + "questions correct")
print("you got" + str((score /4)*100)+ "%")


