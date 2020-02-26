 # NAME : Rana Mahmoud Awlad Mohammad
        # ID : 161050
file=open("sic.txt","r")   #open text file & read it
labellist = list()
opcodedlist = list()
operandlist = list()
indexedaddresslist = list()
directive = ['START ', 'BYTE  ', 'WORD  ',  'RSUB  ', 'RESW  ', 'BASE  ', 'NOBASE' , 'END   ']
numberofdirective = 0
numberofcomment = 0

f = file.readlines()        # read each lines in the file
for i in f:
    if i[9] != "." :
        if not i[0:8].isspace():
            labellist.append(i[0:8])
        if not i[9:15].isspace():
            opcodedlist.append(i[9:15])
        if i[9:15] in directive:
            numberofdirective += 1
        if not i[17:35].isspace():
            operandlist.append(i[17:35])
        if "," in i[17:35]:
            indexedaddresslist.append(i)
        else:
            numberofcomment  += 1
# what is the name of the program ?
print("The name of file is : " + f[0][0:8])
# separate each column as a list .
print("Label column : ")
print(labellist)
print("opcode column : ")
print(opcodedlist)
print("operand column : ")
print(operandlist)
# How many lines are comments ?
print("Number of lines are comment is  : " + str(numberofcomment))
# How many lines are directives ?
print("Number of directives is : " + str(numberofdirective))
# How many instruction in the source code ?
print("Number of instructions  is : " + str(len(opcodedlist) - numberofdirective))
# which lines contain indexed addreesing ?
print("Lines contain indexed addressing  : ")
print(indexedaddresslist)
