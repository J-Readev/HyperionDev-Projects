def print_values_of(dictionary, keys):
    for key in keys:
        #Syntax - K was not defined, so needed to replace K with Key so it can be used.
        print(dictionary[key])
#Syntax - Changed from '' to "" for "d'oh" as the ' was causing a string error.
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}

#Syntax - TypeError as 4 arguments are given. Needing to separate the text with brackets for the dictionay to function.
print_values_of(simpson_catch_phrases,('lisa', 'bart', 'homer'))

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

