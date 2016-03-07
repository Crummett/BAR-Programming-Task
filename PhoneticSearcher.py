import sys

def main():
    inputNames, surnamesFile = getInputs()
    #Read the surnames file, and make a list of the names.
    surnames = open(surnamesFile, 'r').read().splitlines()
    equivalents = generateEquivalents()
    output = ""
    # Generate a string of equivalents for each of the input names
    for name in inputNames:
        output = output + match(name, surnames, equivalents) + '\n'
    # Remove the trailing /n
    output = output[:-2]
    
    print(output)
    
def getInputs():
    # Return the input names. Ignoring all other input.
    inputNames = sys.argv[1:-1]
    # Takes the last 
    surnamesFile = sys.argv[-1]
    
    return inputNames, surnamesFile
    
def match(nameFromCMD, surnamesFileContents, equivalentsDictionary):
    nameInput, surnamesList = nameFromCMD, surnamesFileContents
    equivalents, matches = equivalentsDictionary, []
    # Cleans the string of any unnescessary letters
    name = disregarder(cleanName(nameInput), equivalents)
    # Cleans up each surname before comparing it to the input name
    for surname in surnamesList:
        surnameToCheck = disregarder(cleanName(surname), equivalents)
        if (compareEquivalents(name, surnameToCheck, equivalents)):
            matches.append(surname)
    # Creates the output string
    output = nameInput + ':'
    try:
        for match in matches:
            output = output + ' ' + match + ','
    except IndexError:
        output = output + ' No matches found  '
    if (matches == []):
        output = output + ' No matches found  '
    # Removes the trailing comma
    output = output[:-1]
    return output

def compareEquivalents(nameInput, surnameInput, equivalentsDictionary):
    name, surname, equivalents = nameInput, surnameInput, equivalentsDictionary
    equivalent = True
    # Initially assumes names are equivalent. Cycles through each letter of the
    # surname comparing it to the letter at the same position of the input name
    for i in range(len(surname)):
        try:
            if (surname[i] not in equivalents[name[i]]):
                equivalent = False
        except IndexError: # catches in case surname longer than input name
            equivalent = False
    
    return equivalent
    
def cleanName(nameInput):
    # Converts the name to lower case
    name = nameInput.lower()
    cleanedName = ""
    # Removes any non-chars
    for letter in name:
        if letter.islower():
            cleanedName = cleanedName + letter
    
    return cleanedName
    
def disregarder(nameInput, equivalentsDictionary):
    name, equivalents = nameInput, equivalentsDictionary
    # Keeps the 1st letter
    firstStage = name[0]
    # Removes any of the letters disregardable after the first
    for letter in name[1:]:
        if (letter not in ['a', 'e', 'i', 'h', 'o', 'u', 'w', 'y']):
            firstStage = firstStage + letter
    # Keeps the 1st letter
    secondStage = name[0]
    # Removes any letters that are equivalent to the previous letter
    for letterNum in range(1, len(firstStage)):
        if (firstStage[letterNum] not in equivalents[firstStage[letterNum-1]]):
            secondStage = secondStage + firstStage[letterNum]
    
    return secondStage
    
def generateEquivalents():
    # Creates a dictionary of equivalents.
    # Enter a letter into the dictionary, and it'll return a list of all of its equivalents
    equiv1 = {x: ['a', 'e', 'i', 'o', 'u' ] 
        for x in ['a', 'e', 'i', 'o', 'u' ]}
    equiv2 = {x: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'y', 'z'] 
        for x in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'y', 'z']}
    equiv3 = {x: ['b', 'f', 'p', 'v', 'w'] 
        for x in ['b', 'f', 'p', 'v', 'w']}
    equiv4 = {x: ['d', 't'] 
        for x in ['d', 't']}
    equiv5 = {x: ['m', 'n'] 
        for x in ['m', 'n']}
    equiv6 = {x: []
        for x in ['h', 'l', 'r']}
    # Create 1 mega-dictionary
    equiv1.update(equiv2)
    equiv1.update(equiv3)
    equiv1.update(equiv4)
    equiv1.update(equiv5)
    equiv1.update(equiv6)
    
    return equiv1

main()