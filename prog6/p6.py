# Program 6

import re
from difflib import SequenceMatcher as SM

# Will read the file, store information into a dicionary,
# and print the information.
def readLines():
    while True:
        try:
            #global inputLine
            inputLine = input()
            lineSplit = inputLine.split()
            #global d
            # Checks if first token is "CUSTOMER", prints customer name
            if lineSplit[0] == "CUSTOMER":
                stnumli = []
                stnli = []
                sttli = []
                dirli = []
                apli = []
                citli = []
                stali = []
                zipli = []
                count = 0
                print("%s\t\t\t\tStNum\tDirection\tAptNum\tStType\tStName" % (inputLine[9:]))

            # Checks if first token is "ADDBEG", creates empty dictionary
            # with keys "street", "city", "state", and "zip".
            if lineSplit[0] == "ADDRBEG":
                cntLine = 0
                d = {"street":[],"city":[],"state":[],"zip":[]}

            # If first token is "LINE", will store value into key "street".
            # Note : will skip the first token ("LINE") when store value into key
            if lineSplit[0] == "LINE":
                cntLine += 1
                if cntLine == 1:
                    x = inputLine[5:]
                    d["street"] = x
                    st = d["street"]
                if cntLine == 2:
                    y = inputLine[5:]
                    z = x +" "+y
                    d["street"] = z
                    st = "".join(d["street"])

            # If first token is "CITY", will store value into key "city"
            # Note : will skip the first token ("CITY") when store value into key
            if lineSplit[0] == "CITY":
                d["city"] = inputLine[5:]
                citli.append(inputLine[5:])

            # If first token is "STATE", store value into key "state"
            # Note : will skip the first token ("STATE") when store value into key
            if lineSplit[0] == "STATE":
                d["state"] = inputLine[6:]
                stali.append(inputLine[6:])

            # If first token is "ZIP",  store value into key "zip"
            # Note : will skip the first token ("ZIP") when store value into key
            if lineSplit[0] == "ZIP":
                d["zip"] = inputLine[4:]
                zipli.append(inputLine[4:])

            # If first token is "ADDREND",will print customer information
            if lineSplit[0] == "ADDREND":
                stSplit = st.split();
                stNum = stSplit[0]
                direct = checkDir(stSplit)
                stType = checkStreet(stSplit)
                stName = checkStNm(stSplit)
                apNum = checkApt(stSplit)
                count += 1
                print("%d\t%s" % (count,st ))
                print ("\t%s, %s %s\n" % (d.get("city"), d.get("state"),d.get("zip")))
                print("\t\t\t\t\t%s\t%s\t%s\t%s\t%s\n" % (stNum.replace('-',''), direct, apNum,stType,stName))
                stnumli.append(stNum.replace('-',''))
                stnli.append(stName)
                dirli.append(direct)
                sttli.append(stType)
                apli.append(apNum)

            # If first token is "CUSTOMEREND", will call score function
            if lineSplit[0] == "CUSTOMEREND":
                print("\t\tAddress  Address  Score\n")
                comp12(stnumli[0],stnumli[1],stnli[0],stnli[1],dirli[0],dirli[1],sttli[0],sttli[1],
                apli[0],apli[1],citli[0],citli[1],stali[0],stali[1],zipli[0],zipli[1])

                if count >= 3:
                    comp13(stnumli[0],stnumli[2],stnli[0],stnli[2],dirli[0],dirli[2],sttli[0],sttli[2],
                    apli[0],apli[2],citli[0],citli[2],stali[0],stali[2],zipli[0],zipli[2])

                    comp23(stnumli[1],stnumli[2],stnli[1],stnli[2],dirli[1],dirli[2],sttli[1],sttli[2],
                    apli[1],apli[2],citli[1],citli[2],stali[1],stali[2],zipli[1],zipli[2])

                if count == 4:
                    comp14(stnumli[0],stnumli[3],stnli[0],stnli[3],dirli[0],dirli[3],sttli[0],sttli[3],
                    apli[0],apli[3],citli[0],citli[3],stali[0],stali[3],zipli[0],zipli[3])

                    comp24(stnumli[1],stnumli[3],stnli[1],stnli[3],dirli[1],dirli[3],sttli[1],sttli[3],
                    apli[1],apli[3],citli[1],citli[3],stali[1],stali[3],zipli[1],zipli[3])

                    comp34(stnumli[2],stnumli[3],stnli[2],stnli[3],dirli[2],dirli[3],sttli[2],sttli[3],
                    apli[2],apli[3],citli[2],citli[3],stali[2],stali[3],zipli[2],zipli[3])

        except(EOFError):
            break

#Passes a list and returns the given direction
def checkDir(x):
    for i in range(len(x)):
        dirSW = ["S.W.","SOUTH WEST","SOUTHWEST", "SW.", "S WEST", "SOUTH W", "SW"]
        dirSE = ["S.E.", "SOUTH EAST","SOUTHEAST", "SE.", "S EAST", "SOUTH E", "SE"]
        dirNW = ["N.W." , "NORTH WEST","SOUTHWEST", "SW.", "S WEST", "SOUTH W", "SW"]
        dirNE = ["S.W." , "SOUTH WEST","SOUTHWEST", "SW.", "S WEST", "SOUTH W", "SW"]
        street = ["RD", "LN","ST","AVE","STREET","ROAD","LANE","AVENUE","RD.","ST.","AVE.","BLVD.","SQAURE", "SQ.","SQ","CIRCLE","CIR.","CIR"]
        dirW = ["W", "WEST", "W."]
        dirN = ["N", "NORTH","N."]
        dirS = ["S","SOUTH","S."]
        dirE = ["E", "EAST","E."]

        # If list has a form of West followed by a Street type, return nothing
        if x[i] in dirW and x[i + 1] in street:
            return "\t "
        if x[i] in dirN:
            return "NORTH   "
        if x[i] in dirN and x[i + 1] in street:
            return "\t "
        if x[i] in dirS and x[i + 1] in street:
            return "\t "
        if x[i] in dirE and x[i + 1] in street:
            continue
        if x[i] in dirS and x[i + 1] in dirW:
            return "SOUTHWEST"
        if x[i] in dirSW:
            return "SOUTHWEST"
        if x[i] in dirW:
            return "WEST    "
        if x[i] in dirN:
            return "NORTH   "
        if x[i] in dirS:
            return "SOUTH   "
        if x[i] in dirE:
            return "EAST    "
    else:
        return "\t "

# Passes a list and returns the street type
def checkStreet(x):
    for i in range(len(x)):
        strtR = ["RD","ROAD","RD."]
        strtL = ["LN", "LANE","LN."]
        strtS = ["ST", "ST.", "STREET"]
        strtA = ["A.","AVE","AVE.","AVENUE"]
        strtB = ["BLVD.","BLVD"]
        strtC = ["CIRCLE", "CIR.", "CIR"]
        strtSq = ["SQAURE", "SQ.","SQ"]

        if x[i] in strtR:
            return "ROAD"
        if x[i] in strtL:
            return "LANE"
        if x[i] in strtS:
            return "STREET"
        if x[i] in strtA:
            return "AVENUE"
    else:
        return "    "

# Passes a list and returns the street name
def checkStNm(x):
    stRE = re.compile(r'[WEST|S.W.]\s([A-Z]+\s[A-Z]+\s[A-Z]+)\s[ROAD|RD]')
    matchSt = stRE.search(" ".join(x))
    for i in range(len(x)):
        strtR = ["RD","ROAD","RD."]
        strtL = ["LN", "LANE","LN."]
        strtS = ["ST", "ST.", "STREET"]
        strtA = ["A.","AVE","AVE.","AVENUE"]
        strtB = ["BLVD.","BLVD"]
        strtC = ["CIRCLE", "CIR.", "CIR"]
        strtSq = ["SQAURE", "SQ.","SQ"]

        if x[i] in strtR:
            return x[i-1]
        elif matchSt != None:
            return matchSt.group(1)
        elif x[i] in strtL:
            return x[i-1]
        elif x[i] in strtS:
            return x[i-1]
        elif x[i] in strtA:
            return x[i-1]
    else:
        return x[-1]

# Passes a list and returns the apartment number
def checkApt(x):
    aptRE = re.compile(r'#(\d+)\-*([A-Z])')
    matchApt = aptRE.search(x[-1])
    aptRE2 = re.compile(r'\d+')
    matchApt2 = aptRE2.search(x[-1])
    for i in range(len(x)):
        num = ["#"]
        num2 = ["APT"]
        if x[i] in num2:
            return  x[i+1]
        elif matchApt != None:
            return matchApt.group(1) +  matchApt.group(2)
        elif matchApt2 != None:
            return x[-1]
        else:
            return "  "
# All fucntions passes list and finds score
def comp12(li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16):
    tot = 0
    rat1 = SM(None,li1,li2).ratio()
    rat2 = SM(None,li3,li4).ratio()
    rat3 = SM(None,li5,li6).ratio()
    rat4 = SM(None,li7,li8).ratio()
    rat5 = SM(None,li9,li10).ratio()
    rat6 = SM(None,li11,li12).ratio()
    rat7 = SM(None,li13,li14).ratio()
    rat8 = SM(None,li15,li16).ratio()
    if li1.isspace() or li2.isspace():
        tot -= 20
    else:
        if rat1 == 1.0:
            tot += 20
        if rat1 != 1.0:
            tot -= 20

######
    if li7.isspace() or li8.isspace():
        if li7.isspace() and li8.isspace():
            tot += 10
        else:
            tot += 5
    else:
        if rat4 == 1.0:
            tot += 10
        else:
            tot -= 10
#####
    if li5.isspace() or li6.isspace():
        if li5.isspace()and li6.isspace():
            tot += 5
        else:
            tot -= 5
    else:
        if rat3 == 1.0:
            tot += 5
        else:
            tot -= 10
#####

    if li9.isspace() or li10.isspace():
        if li9.isspace() and li10.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat5 == 1.0:
            tot += 20
        else:
            if rat5 > .6:
                tot += (rat5 * 5)
            else:
                tot -= 20
#########
    if li11.isspace()or li12.isspace():
        if li11.isspace() and li12.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat6 == 1.0:
            tot += 20
        else:
            if rat6 > .6:
                tot += (rat6 * 15)
            else:
                tot -= 20
######
    if rat7 == 1.0:
        tot += 10
    if rat7 != 1.0:
        tot -= 20
#####
    if li3.isspace() or li4.isspace():
        if li3.isspace() and li4.isspace():
            tot -= 20
        else:
            tot -= 20
    else:
        if rat2 == 1.0:
            tot += 20
        else:
            if rat2 > .6:
                tot += (rat2 * 10)
            else:
                tot -= 5
####
    if len(li15) == 10 and len(li16) == 10:
        tot += 80
    if len(li15) == 5 and len (li16) == 5:
        tot += 5
######
    if tot > 100:
        tot = 100
    if tot < 0:
        tot = 0
    print("\t\t",1,"\t",2,"\t",tot)

def comp13(li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16):
    tot = 0
    rat1 = SM(None,li1,li2).ratio()
    rat2 = SM(None,li3,li4).ratio()
    rat3 = SM(None,li5,li6).ratio()
    rat4 = SM(None,li7,li8).ratio()
    rat5 = SM(None,li9,li10).ratio()
    rat6 = SM(None,li11,li12).ratio()
    rat7 = SM(None,li13,li14).ratio()
    rat8 = SM(None,li15,li16).ratio()
    if li1.isspace() or li2.isspace():
        tot -= 20
    else:
        if rat1 == 1.0:
            tot += 20
        if rat1 != 1.0:
            tot -= 20

######
    if li7.isspace() or li8.isspace():
        if li7.isspace() and li8.isspace():
            tot += 10
        else:
            tot += 5
    else:
        if rat4 == 1.0:
            tot += 10
        else:
            tot -= 10
#####
    if li5.isspace() or li6.isspace():
        if li5.isspace()and li6.isspace():
            tot += 5
        else:
            tot -= 5
    else:
        if rat3 == 1.0:
            tot += 5
        else:
            tot -= 10
#####

    if li9.isspace() or li10.isspace():
        if li9.isspace() and li10.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat5 == 1.0:
            tot += 20
        else:
            if rat5 > .6:
                tot += (rat5 * 5)
            else:
                tot -= 20
#########
    if li11.isspace()or li12.isspace():
        if li11.isspace() and li12.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat6 == 1.0:
            tot += 20
        else:
            if rat6 > .6:
                tot += (rat6 * 15)
            else:
                tot -= 20
######
    if rat7 == 1.0:
        tot += 10
    if rat7 != 1.0:
        tot -= 20
#####
    if li3.isspace() or li4.isspace():
        if li3.isspace() and li4.isspace():
            tot -= 20
        else:
            tot -= 20
    else:
        if rat2 == 1.0:
            tot += 20
        else:
            if rat2 > .6:
                tot += (rat2 * 10)
            else:
                tot -= 5
####
    if len(li15) == 10 and len(li16) == 10:
        tot += 80
    if len(li15) == 5 and len (li16) == 5:
        tot += 5
######
    if tot > 100:
        tot = 100
    if tot < 0:
        tot = 0
    print("\t\t",1,"\t",3,"\t",tot)

def comp14(li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16):
    tot = 0
    rat1 = SM(None,li1,li2).ratio()
    rat2 = SM(None,li3,li4).ratio()
    rat3 = SM(None,li5,li6).ratio()
    rat4 = SM(None,li7,li8).ratio()
    rat5 = SM(None,li9,li10).ratio()
    rat6 = SM(None,li11,li12).ratio()
    rat7 = SM(None,li13,li14).ratio()
    rat8 = SM(None,li15,li16).ratio()
    if li1.isspace() or li2.isspace():
        tot -= 20
    else:
        if rat1 == 1.0:
            tot += 20
        if rat1 != 1.0:
            tot -= 20

######
    if li7.isspace() or li8.isspace():
        if li7.isspace() and li8.isspace():
            tot += 10
        else:
            tot += 5
    else:
        if rat4 == 1.0:
            tot += 10
        else:
            tot -= 10
#####
    if li5.isspace() or li6.isspace():
        if li5.isspace()and li6.isspace():
            tot += 5
        else:
            tot -= 5
    else:
        if rat3 == 1.0:
            tot += 5
        else:
            tot -= 10
#####

    if li9.isspace() or li10.isspace():
        if li9.isspace() and li10.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat5 == 1.0:
            tot += 20
        else:
            if rat5 > .6:
                tot += (rat5 * 5)
            else:
                tot -= 20
#########
    if li11.isspace()or li12.isspace():
        if li11.isspace() and li12.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat6 == 1.0:
            tot += 20
        else:
            if rat6 > .6:
                tot += (rat6 * 15)
            else:
                tot -= 20
######
    if rat7 == 1.0:
        tot += 10
    if rat7 != 1.0:
        tot -= 20
#####
    if li3.isspace() or li4.isspace():
        if li3.isspace() and li4.isspace():
            tot -= 20
        else:
            tot -= 20
    else:
        if rat2 == 1.0:
            tot += 20
        else:
            if rat2 > .6:
                tot += (rat2 * 10)
            else:
                tot -= 5
####
    if len(li15) == 10 and len(li16) == 10:
        tot += 80
    if len(li15) == 5 and len (li16) == 5:
        tot += 5
######
    if tot > 100:
        tot = 100
    if tot < 0:
        tot = 0
    print("\t\t",1,"\t",4,"\t",tot)

def comp23(li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16):
    tot = 0
    rat1 = SM(None,li1,li2).ratio()
    rat2 = SM(None,li3,li4).ratio()
    rat3 = SM(None,li5,li6).ratio()
    rat4 = SM(None,li7,li8).ratio()
    rat5 = SM(None,li9,li10).ratio()
    rat6 = SM(None,li11,li12).ratio()
    rat7 = SM(None,li13,li14).ratio()
    rat8 = SM(None,li15,li16).ratio()

    if li1.isspace() or li2.isspace():
        tot -= 20
    else:
        if rat1 == 1.0:
            tot += 20
        if rat1 != 1.0:
            tot -= 20

######
    if li7.isspace() or li8.isspace():
        if li7.isspace() and li8.isspace():
            tot += 10
        else:
            tot += 5
    else:
        if rat4 == 1.0:
            tot += 10
        else:
            tot -= 10
#####
    if li5.isspace() or li6.isspace():
        if li5.isspace()and li6.isspace():
            tot += 5
        else:
            tot -= 5
    else:
        if rat3 == 1.0:
            tot += 5
        else:
            tot -= 10
#####

    if li9.isspace() or li10.isspace():
        if li9.isspace() and li10.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat5 == 1.0:
            tot += 20
        else:
            if rat5 > .6:
                tot += (rat5 * 5)
            else:
                tot -= 20
#########
    if li11.isspace()or li12.isspace():
        if li11.isspace() and li12.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat6 == 1.0:
            tot += 20
        else:
            if rat6 > .6:
                tot += (rat6 * 15)
            else:
                tot -= 20
######
    if rat7 == 1.0:
        tot += 10
    if rat7 != 1.0:
        tot -= 20
#####
    if li3.isspace() or li4.isspace():
        if li3.isspace() and li4.isspace():
            tot -= 20
        else:
            tot -= 20
    else:
        if rat2 == 1.0:
            tot += 20
        else:
            if rat2 > .6:
                tot += (rat2 * 10)
            else:
                tot -= 5
####
    if len(li15) == 10 and len(li16) == 10:
        tot += 80
    if len(li15) == 5 and len (li16) == 5:
        tot += 5
######
    if tot > 100:
        tot = 100
    if tot < 0:
        tot = 0
    print("\t\t",2,"\t",3,"\t",tot)

def comp24(li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16):
    tot = 0
    rat1 = SM(None,li1,li2).ratio()
    rat2 = SM(None,li3,li4).ratio()
    rat3 = SM(None,li5,li6).ratio()
    rat4 = SM(None,li7,li8).ratio()
    rat5 = SM(None,li9,li10).ratio()
    rat6 = SM(None,li11,li12).ratio()
    rat7 = SM(None,li13,li14).ratio()
    rat8 = SM(None,li15,li16).ratio()

    if li1.isspace() or li2.isspace():
        tot -= 20
    else:
        if rat1 == 1.0:
            tot += 20
        if rat1 != 1.0:
            tot -= 20

######
    if li7.isspace() or li8.isspace():
        if li7.isspace() and li8.isspace():
            tot += 10
        else:
            tot += 5
    else:
        if rat4 == 1.0:
            tot += 10
        else:
            tot -= 10
#####
    if li5.isspace() or li6.isspace():
        if li5.isspace()and li6.isspace():
            tot += 5
        else:
            tot -= 5
    else:
        if rat3 == 1.0:
            tot += 5
        else:
            tot -= 10
#####

    if li9.isspace() or li10.isspace():
        if li9.isspace() and li10.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat5 == 1.0:
            tot += 20
        else:
            if rat5 > .6:
                tot += (rat5 * 5)
            else:
                tot -= 20
#########
    if li11.isspace()or li12.isspace():
        if li11.isspace() and li12.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat6 == 1.0:
            tot += 20
        else:
            if rat6 > .6:
                tot += (rat6 * 15)
            else:
                tot -= 20
######
    if rat7 == 1.0:
        tot += 10
    if rat7 != 1.0:
        tot -= 20
#####
    if li3.isspace() or li4.isspace():
        if li3.isspace() and li4.isspace():
            tot -= 20
        else:
            tot -= 20
    else:
        if rat2 == 1.0:
            tot += 20
        else:
            if rat2 > .6:
                tot += (rat2 * 10)
            else:
                tot -= 5
####
    if len(li15) == 10 and len(li16) == 10:
        tot += 80
    if len(li15) == 5 and len (li16) == 5:
        tot += 5
######
    if tot > 100:
        tot = 100
    if tot < 0:
        tot = 0
    print("\t\t",2,"\t",4,"\t",tot)


def comp34(li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16):
    tot = 0
    rat1 = SM(None,li1,li2).ratio()
    rat2 = SM(None,li3,li4).ratio()
    rat3 = SM(None,li5,li6).ratio()
    rat4 = SM(None,li7,li8).ratio()
    rat5 = SM(None,li9,li10).ratio()
    rat6 = SM(None,li11,li12).ratio()
    rat7 = SM(None,li13,li14).ratio()
    rat8 = SM(None,li15,li16).ratio()
    if li1.isspace() or li2.isspace():
        tot -= 20
    else:
        if rat1 == 1.0:
            tot += 20
        if rat1 != 1.0:
            tot -= 20

######
    if li7.isspace() or li8.isspace():
        if li7.isspace() and li8.isspace():
            tot += 10
        else:
            tot += 5
    else:
        if rat4 == 1.0:
            tot += 10
        else:
            tot -= 10
#####
    if li5.isspace() or li6.isspace():
        if li5.isspace()and li6.isspace():
            tot += 5
        else:
            tot -= 5
    else:
        if rat3 == 1.0:
            tot += 5
        else:
            tot -= 10
#####

    if li9.isspace() or li10.isspace():
        if li9.isspace() and li10.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat5 == 1.0:
            tot += 20
        else:
            if rat5 > .6:
                tot += (rat5 * 5)
            else:
                tot -= 20
#########
    if li11.isspace()or li12.isspace():
        if li11.isspace() and li12.isspace():
            tot += 10
        else:
            tot -= 10
    else:
        if rat6 == 1.0:
            tot += 20
        else:
            if rat6 > .6:
                tot += (rat6 * 15)
            else:
                tot -= 20
######
    if rat7 == 1.0:
        tot += 10
    if rat7 != 1.0:
        tot -= 20
#####
    if li3.isspace() or li4.isspace():
        if li3.isspace() and li4.isspace():
            tot -= 20
        else:
            tot -= 20
    else:
        if rat2 == 1.0:
            tot += 20
        else:
            if rat2 > .6:
                tot += (rat2 * 10)
            else:
                tot -= 5
####
    if len(li15) == 10 and len(li16) == 10:
        tot += 80
    if len(li15) == 5 and len (li16) == 5:
        tot += 5
######
    if tot > 100:
        tot = 100
    if tot < 0:
        tot = 0
    print("\t\t",3,"\t",4,"\t",tot)

