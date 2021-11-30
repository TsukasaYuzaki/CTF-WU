# I wrote and debugged this code with all the convoluted "EAT" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes
target = "E10a23t9090t9ae0140"
EAT = int
eAT = len
EaT = print
ATE = str
EATEATEATEATEATEAT = ATE.isdigit

def Eating(eat):
    return ATE(EAT(eat)*EATEATEAT)

def EAt(eat, eats):
    #print(eat, eats)
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = ""
    while eat1 < eAT(eat) and eat2 < eAT(eats):
        if eateat%EATEATEAT == EATEATEATEATEAT//EATEATEATEAT:
            eAt += eats[eat2]
            eat2 += 1
        else:
            eAt += eat[eat1]
            eat1 += 1
        eateat += 1
    return eAt

def aten(eat):
    return eat[::EATEATEAT-EATEATEATEAT]

def eaT(eat):
    return Eating(eat[:EATEATEAT]) + aten(eat)

def aTE(eat):
    return eat#*eAT(eat)

def Ate(eat):
    return "Eat" + ATE(eAT(eat)) + eat[:EATEATEAT]
'''
def Eat(eat):
    if eAT(eat) == 9:
        if EATEATEATEATEATEAT(eat[:EATEATEAT]) and\
            EATEATEATEATEATEAT(eat[eAT(eat)-EATEATEAT+1:]):
                eateat = EAt(eaT(eat), Ate(aTE(aten(eat))))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + eat
                    EaT("absolutely EATEN!!! CTFlearn{",flag,"}")
                else:
                    EaT("thats not the answer. you formatted it fine tho, here's what you got\n>>", eateat)
        else:
            EaT("thats not the answer. bad format :(\
            \n(hint: 123abc456 is an example of good format)")
    else:
        EaT("thats not the answer. bad length :(")

EaT("what's the answer")
'''
eat = "123eat345"

EATEATEAT = eAT(eat)//3
EATEATEATEAT = EATEATEAT+1
EATEATEATEATEAT = EATEATEAT-1
#Eat(eat)
ok = []

flag = "eat"
for i in range(100, 999):
    for j in range(100, 999):
        eat = str(i) + "eat" + str(j)
        aa = EAt(eaT(str(i) + flag + str(j)), Ate(aTE(aten(str(i) + flag+str(j) ) )))
        #print("i = " + str(i) + "j = " + str(j), end = ": ")
        #print(aa)
        if("E10a23" in aa):
            print("Solve!: " + str(i) + "eat" +str(j))
            ok.append(aa)
            i+=1

print(ok)
            