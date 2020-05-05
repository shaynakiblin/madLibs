"""
This is a program for a madlibs game, the user can choose or have a madlibs prompt chosen for them
the user can then fill in the prompt to get a funny story

Author: Shayna Kiblin

"""

keys = {
    "[ADJ]" : "adjective",
    "[VRB]" : "verb",
    "[NOUN]" : "noun",
    "[ADV]" : "adverb",
    "[PNOUN]" : "proper noun",
    "[PERS]" : "person",
    "[CITY]" : "city",
    "[BODYPART]" : "body part",
    "[NUM]" : "number",
    "[PLACE]" : "place"

}

file = open(("/Users/shaynakiblin/PycharmProjects/madLibs/src/prompts/" + "sentenceTest.txt"), 'r')

lines = file.readlines()

for line in lines:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in keys:
            userin = input("Give a(n) " + keys[word] + ": ")
        else:
            pass
    for word in words:
        if word in keys:
            print(userin, end =" ")
        else:
            print(word, end =" ")








file.close()