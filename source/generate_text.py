
import json
from random import random

def generate_text(how_many = 1, how_much = None):
    if how_much == None:
        how_much = "word"
    how_much = parse_how_much(how__much)
    mc = load_mc()
    # how much text?
    # generate text
    # update dictionary

# load the markov chain JSON dictionary to a Python dictionary
def load_mc():
    mc = {}
    with open('mc.json', 'r') as mcjson:
        mc = json.loads(mcjson.read())
    return mc

# choose an index from the list of probabilities
def choose_index(probability_list):

    # convert integer counts to an integrated and normalized
    # probability function
    N = len(probability_list)
    Sl=[probability_list[0]]
    for i in range(1,N):
        Sl.append(Sl[i-1]+probability_list[i])
    segment = 1/sum(probability_list)
    Sp=[e*segment for e in Sl]
    del Sl

    # simple binary search to find index of a random number
    r = random()
    l = 0
    h = len(Sp)
    m = h//2
    i = 7 # shouldn't be more than this, otherwise just return
    while i > 0:
        if l == m:
            break
        elif r == Sp[m]:
            break
        elif r > Sp[m]:
            l = m
            m = (h-l)//2+l
        else:
            h = m
            m = (h-l)//2+l
        i -= 1
    return h

# defines the ways that a user can input the amount of text that is generated
# letter = 0
# word = 1
# sentence = 2
# paragraph = 3
# essay = 4
def parse_how_much(how_much):
    try:
        if type(how_much) == int:
            if 0 <= how_much <= 4:
                raise Exception(how_much, "bueno")
            else:
                raise Exception(how_much)
        elif type(how_much) == str:
            how_much = how_much.lower()
            if how_much[-1] == 's':
                how_much[-1] = ''
            
            options = ["letter","word","sentence","paragraph","essay"]
            for i in range(5):
                if len(how_much)<=options[i] \
                   and how_much == options[i][0:len(how_much)]:
                    raise Exception(i, "bueno")
            raise Exception(how_much)
        else:
            raise Exception(how_much)
    except Exception as out:
        if len(out.args) == 1:
            raise out
        else:
            return out.args[0]
            

    
