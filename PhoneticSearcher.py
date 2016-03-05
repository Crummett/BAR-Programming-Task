import sys

def main():
    
    inputNames, surnamesFile = getInputs()
    surnames = open(surnamesFile, 'r').read().splitlines()
    output = ""
    for name in inputNames:
        output = output + match(name, surnames)
    print(surnames)
    print(inputNames)
    
def getInputs():
    
    inputNames = sys.argv[1:(len(sys.argv)-1)]
    surnamesFile = sys.argv[(len(sys.argv)-1)]
    
    return inputNames, surnamesFile
    
def match(nameFromCMD, surnamesFileContents):
    
    nameInput, surnamesList = namesFromCMD, surnamesFileContents
    equivalents = generateEquivalents()
    
    
    for letterNum in range(len(treatedName)):
    
def treat(nameInput):
    
    name = nameInput.lower()
    treatedName = ""
    
    for letter in nameInput:
        if letter.islower():
            treatedName = treatedName + letter
    
    return treatedName
    
def generateEquivalents()
    equiv1 = {x: ['a', 'e', 'i', 'o', 'u' ] 
        for x in ['a', 'e', 'i', 'o', 'u' ]}
    equiv2 = {x: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'y', 'z'] 
        for x in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'y', 'z']}
    equiv3 = {x: ['b', 'f', 'p', 'v', 'w'] 
        for x in ['b', 'f', 'p', 'v', 'w']}
    equiv4 = {x: ['d', 't'] for x in ['d', 't']}
    equiv5 = {x: ['m', 'n'] for x in ['m', 'n']}
    
    return dict(equiv1.items() + equiv2.items() + equiv3.items() +
                equiv4.items() + equiv5.items())

main()