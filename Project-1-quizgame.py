q1="""who is the best kabaddi player
a.rahul chaudhary
b.pardeep narwal
c.ajay
d.rohit"""
q2="""what is the best season
a.summer
b.winter
c.mansoon
d.autumn"""
q3="""what is best sweet
a.cova
b.rasaagulla
c.kaaja
d.laddu"""
q4="""what is the national animal
a.tiger
b.anu
c.sanju
d.lion"""
q5="""who is ur favourite heroine
a.anuskha
b.sridevi
c.tamannah
d.sai pallavi"""
questions={q1:"a",q2:"b",q3:"a",q4:"a",q5:"d"}
name=input("hi,what's ur name")
print("Hello",name,"Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip the question in quiz(yes/no)")
    if flag1=="yes":
        continue
    ans=input("Enter ur answer: ")
    if ans==questions[i]:
        print("Wow!you got one point")
        score=score+1
        print("Your current score is: ",score)
    else:
        print("Wrong answer,you lost 1 mark")
        score=score-1
        print("Your current score is: ",score)
    flag2=input("Do u want to quit?(yes/no)")
    if flag2=="yes":
        break
print("Your total score is: ",score)
        
    
