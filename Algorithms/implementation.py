
months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",)

def getMonth(months:tuple, monthNum:float):
    print(months[int(monthNum)-1])


favFruitsAndVeggies = {
    "apple", "Orange", "banana", "grapes", "cucumber"
}

newFavs = [{"stawberry", "raspberry"}, {"asparagus", "tomato"}]

def addFavs(favFruitsAndVeggies:set[str], newFavs:list[set]):
    blankSet= set()
    for favs in newFavs:
        blankSet = blankSet.union(favs)
    for item in blankSet:
        favFruitsAndVeggies.add(item)
    for favorite in favFruitsAndVeggies:
        print(favorite)

profile = {
    "First Name": "Bob",
    "Last Name": "Johnson",
    "Email": "bob@Gmail.com",
    "phone Number": 8014541212
}

def printProfile(profile:dict):
    for key, value in profile.items():
        print(f'{key}: {value}')

myFam = [
    {"First Name": "Rick",
     "Last Name": "Lyman",
     "Relation to Rick": "Self"
     },
    {"First Name": "Paige",
     "Last Name": "Lyman",
     "Relation to Rick": "Wife"
     },
    {"First Name": "Reed",
     "Last Name": "Lyman",
     "Relation to Rick": "Son"
     },
    {"First Name": "Ruth",
     "Last Name": "Lyman",
     "Relation to Rick": "daughter"
     },
    
]

def printDictList(myFam: list[dict[str,str]]):
    for person in myFam:
        print(f'{person["First Name"]}, {person["Relation to Rick"]}')