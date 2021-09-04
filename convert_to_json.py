
import json

# Converts a large text to a json file. The text is expected to be in base_text.txt in the working directory.
# The resulting file will provide a markov chain dictionary of length n.
# This has a very high cost, and so should be used sparingly.
def convert_to_json(n = 4: int):

    # ensure n is type int
    if type(n) is not int:
        print("n specifies the number of characters that will be mapped.\nA larger value will create a larger table and more realistic words.")
        return
    
    with open("base_text.txt", 'r') as f:

        # mc stores the markov chain dictionary temporarily then is written to a json file
        mc = {}

        # default list holds 95 zeroes, equal to all written characters in Ascii code.
        default_list = [0]*95
        
        # reading line by line
        ls = f.readlines()
        for l in ls:
            current_string = l[0:5]
            mcjson[current_string] = 
            for i in range(5, len(l)):
                
                
                
