# Program 5

# Will read the file, store information into a dicionary,
# and print the information.
def printLines():
    while True:
        try:
            # Read in lines
            inputLine = input()
            # Splits read in lines by space
            lineSplit = inputLine.split()
            # Checks if first token is "CUSTOMER", prints customer name
            if lineSplit[0] == "CUSTOMER":
                count = 0
                print(inputLine[9:])

            # Checks if first token is "ADDBEG", creates empty dictionary
            # with keys "street", "city", "state", and "zip".
            if lineSplit[0] == "ADDRBEG":
                d = {"street":[],"city":[],"state":[],"zip":[]}

            # If first token is "LINE", will store value into key "street".
            # Note : will skip the first token ("LINE") when store value into key
            if lineSplit[0] == "LINE":
                d["street"].append(inputLine[5:])

            # If first token is "CITY", will store value into key "city"
            # Note : will skip the first token ("CITY") when store value into key
            if lineSplit[0] == "CITY":
                d["city"] = inputLine[5:]

            # If first token is "STATE", store value into key "state"
            # Note : will skip the first token ("STATE") when store value into key
            if lineSplit[0] == "STATE":
                d["state"] = inputLine[6:]

            # If first token is "ZIP",  store value into key "zip"
            # Note : will skip the first token ("ZIP") when store value into key
            if lineSplit[0] == "ZIP":
                d["zip"] = inputLine[4:]

            # If first token is "ADDREND",will print customer information
            if lineSplit[0] == "ADDREND":
                count += 1
                print("%d\t%s" % (count, " ".join(d.get("street"))))
                print ("\t%s, %s %s\n" % (d.get("city"), d.get("state"),d.get("zip")))
        except(EOFError):
            break
