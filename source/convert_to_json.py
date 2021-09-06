
import json

# Converts a large text to a dictionary.
# The text is expected to be in base_text.txt in the working directory.
# The resulting file will provide a markov chain dictionary of length n.
# This has a very high cost, and so should be used sparingly.
# If nowrite is True, this will not create a json file. For testing.
def convert_to_json(n = 4, nowrite = False):

    # ensure n is type int
    if type(n) is not int:
        print("n specifies the number of characters that will be mapped.\nA larger value will create a larger table and more realistic words.")
        return
    
    with open("base_text.txt", 'r', encoding = 'utf-8') as f:

        # mc stores the markov chain dictionary temporarily then is written to a json file
        mc = {}

        # default list holds 95 ones, equal to all written characters in ASCII code.
        default_list = [1]*95
        
        # reading line by line
        ls = f.readlines()
        for l in ls:
            
            # generate key
            current_string = l[0:n]
            # populate dictionary
            mc[current_string] = list(default_list)
            mc[current_string][ord(l[n])-32]+=1
            # do it for the rest of the text
            for i in range(n+1, len(l)):
                current_string = l[i-5:i]
                try:
                    mc[current_string]
                except KeyError:
                    mc[current_string] = list(default_list)
                try:
                    mc[current_string][ord(l[i])-32]+=1
                except IndexError:
                    print(f"error at {i} -- {l[i]} : {ord(l[i])-32}\n")

        # send mc to file
        if not nowrite:
            with open("mc.json", "w") as mcjson:
                mcjson.write(json.dumps(mc))
