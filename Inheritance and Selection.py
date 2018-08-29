#Imports
import random

gen = [] #This is going to have all the genetics stored in it
nospace = []
y = 0
z = 0

#Inputs
start = input("Put in any number of pairs of two letters (Must be at least 2 pairs):\n")

#Taking the input and making it into a list
lstart = list(start)

#Getting rid of all the spaces in the list
temp = [x for x in lstart if x is not ' ']

#Adding the data to a more permanent list
for i in range(0,len(temp)):
    nospace.append(temp[i])
for i in range(0,len(temp)):
    nospace.append(temp[i])
for i in range(0,len(temp)):
    nospace.append(temp[i])

#Defining the natural disasters
flood = random.randint(30,40)
drought = random.randint(40,50)
tsunami = random.randint(45,50)
volcano = random.randint(25,35)
clyclone = random.randint(60,70)
tornado = random.randint(50,60)

#Making a list with the names of the natural disasters and storing the ranges
disaster = ["flood","drought","tsunami","volcano","clyclone","tornado",flood,drought,tsunami,volcano,clyclone,tornado]

x = len(nospace)

#Defining the four types of genes
while y == 0:
    xx = 0
    xy = 0
    yx = 0
    yy = 0

    #Randomly getting rid the genes
    for i in range(0,x):
        random1 = random.randint(0,(len(nospace) - 1))
        gen.append(nospace[random1])
        nospace.pop(random1)
        
    x = len(gen)
    nospace = list(gen)
    #Getting rid of the genes from the last generation
    for i in range(0,len(temp)):
        gen.pop(0)

    #Natural Disasters
    while z == 1:
        disrand = random.randint(0,5)
        a = disaster[disrand+6]
        b = 0
        print("A", disaster[disrand], "has come upon the population!", str(a)+"% of the population died!")
        random.randint(0,100)

        #Randomly generating a fatality percent from specific perameters 
        for i in range(0,len(gen)//2):
            e = gen[b]+gen[b+1]
            live = random.randint(0,100)

            #Making the gene yy have a higher percent chance to live
            if gen[b]+gen[b+1] == "yy":
                live += 50
            if live >= int(a):
                b += 2
            else:
                gen.pop(b)
                gen.pop(b)

            
        z = 0


    c = 0

    #Counting the number of genes
    for i in range(0,len(gen)//2):
        d = gen[c]+gen[c+1]
        if d == "xx":
            xx += 1
        elif d == "xy":
            xy += 1
        elif d == "yx":
            yx += 1
        elif d == "yy":
            yy += 1
        c += 2

    #Joining the genes back together
    joined = "".join(gen)
    
    #Adding a space between every two
    spaces = " ".join(joined[i:i+2] for i in range(0, len(joined), 2))

    #Calculating the total
    total = xx + yy + xy+yx

    #Printing final result
    print("There are "+str(total)+" creatures in this generation: "+str(yy)+" yy, "+str(xx)+" xx, "+str(xy)+" xy, "+
          str(yx)+" yx ")

    #More inputs
    nextgen = input("Would you like another generation?\n")

    #Making the input into a list
    nextgenl = list(nextgen)

    #Seeing if they want to repeat and if they want there to be a natural disaster
    if nextgenl[0] == "y"or nextgenl[0] == "Y":
        y = 0
        disinput = input("Would you like there to be a natural disaster in the next generation?\n")
        disl = list(disinput)
        if disl[0] == "y"or disl[0] == "Y":
            z = 1
        elif disl[0] == "n" or disl[0] == "N":
            z = 0
    elif nextgenl[0] == "n" or nextgenl[0] == "N":
        y = 1
    
    

