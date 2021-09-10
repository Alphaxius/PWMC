
import json

'''
# Converts a large text to a dictionary.
# The text is expected to be in base_text.txt in the working directory.
# The resulting file will provide a markov chain dictionary of length n.
# This has a very high cost, and so should be used sparingly.
# If nowrite is True, this will not create a json file. For testing.
'''
def convert_to_json(n = 4, nowrite = False):

    # ensure n is type int
    if type(n) is not int:
        print("n specifies the number of characters that will be mapped.\nA larger value will create a larger table and more realistic words.")
        return
    
    with open("./resources/base_text.txt", 'r', encoding = 'utf-8') as f:

        # mc stores the markov chain dictionary temporarily then is written to a json file
        mc = {}
        # default list holds 95 ones, equal to all written characters in ASCII code.
        default_list = [1]*95
        
        # reading line by line
        for l in f.readlines():
            # populate dictionary
            for i in range(n, len(l)):
##            for i in range(n, 20):
                current_string = l[i-n:i]
                try:
                    mc[current_string]
                except KeyError:
                    mc[current_string] = list(default_list)
                try:
                    mc[current_string][ord(l[i])-32]+=1
                except IndexError as err:
                    print(f"error at {i} -- {l[i]} : {ord(l[i])-32}\n")
                    raise err

        # send mc to file
        if not nowrite:
            with open("../resources/mc.json", "w") as mcjson:
                mcjson.write(str(n)+'\n')
                mcjson.write(json.dumps(mc))



''' load the markov chain JSON object to a Python dictionary
returns the number of letters per key and the dictionary in tuple
'''
def load_mc():
    mc = {}
    dict_length = 0
    with open('./resources/mc.json', 'r') as mcjson:
        lines = mcjson.readlines()
        dict_length = int(lines[0])
        mc = json.loads(lines[1])
        #mc = json.loads(mcjson.read())
    return (dict_length, mc)


###### update_json
