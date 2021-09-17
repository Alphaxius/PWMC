

from random import random as rand
from random import randint as randint


'''


takes how_much as int or str
not case sensitive
not plural sensitive
returns int or throws error
# character = 0
# letter = 1
# word = 2
# sentence = 3
# paragraph = 4
# essay = 5

'''
def generate_text(mc, dict_length, seed = None, how_many = 1, how_much = None, depth = 1):
    
    # fix how_much
    if how_much == None:
        how_much = 2
    how_much = parse_how_much(how_much)

    # fix seed
    if seed == None:
        seed = 'Hello there, general Kenobi'
    seed = fix_seed(seed, mc, dict_length, depth)
    # if small, it is known that there are no super matches,
    # and that there are no right-justified super matches of the given depth
    # e.g. seed ghDEF would match key abcDEF given a depth of 3

    # update dictionary
    if not len(seed) >= dict_length:
        try:
            mc[seed] += 1
        except KeyError:
            mc[seed] = [1]*95
    else:
        seed = increase_seed(seed, dict_length)
        mc[seed] = [1]*95

    # generate text
    string = ''
    if how_much < 4:
        string = generator_internal(mc, seed, how_many, how_much)
    elif how_much == 4:
        string = p_generator(mc, seed, how_many)
    else:
        string = e_generator(mc, seed, how_many)
    return string

'''

'''
def e_generator(mc, seed, how_many):
    string = ''
    for _ in range(how_many):
        e_len = int((7*rand()*rand()+2.99)//1)
        string += p_generator(mc, seed, e_len) + '\nnn'
    return string


'''

'''
def p_generator(mc, seed, how_many):
    string = ''
    for _ in range(how_many):
        p_len = int((6*rand()*rand()+2.1)//1)
        string += generator_internal(mc, seed, p_len, 3) + '\n'
    return string


'''
'''
def generator_internal(mc, seed, how_many, how_much):
    string = str(seed)
    num_found = 0
    while num_found < how_many:
        next_index = choose_index(mc[seed])
        mc[seed][next_index]+=1
        if how_much == 0:
            num_found += 1
        elif how_much == 1:
            if (65 <= next_index <= 90) or (97 <= next_index <= 122):
                num_found += 1
        elif how_much == 2:
            if next_index == 32:
                num_found += 1
        elif how_much == 3:
            if next_index == 33 or next_index == 46 or next_index == 63:
                num_found += 1
        string += chr(next_index+32)
        seed.replace(seed[0],'')
        seed += chr(next_index+32)
        try:
            mc[seed] += 1
        except KeyError:
            mc[seed] = [1]*95
    return string


'''
'''
def find_key(seed, mc, depth):
    ls = len(seed)
    for i in range(depth):
        for e in mc.keys():
            if e[i-ls:] == seed[i:]:
                return e
    return False


# very dumb, needs improvement
def increase_seed(seed, length_required):
    for _ in range(length_required-len(seed)):
        seed = chr(randint(32,126)) + seed
    return seed


'''fix_seed updates the seed to ensure that it conforms to the dictionary
takes seed: unformatted seed input string
takes mc: markov chain dictionary - does not modify
takes dict_length: the length of each entry in the dictionary
takes depth: the number of characters to try to match if the length of the seed is less
    than dict_length. a larger depth will take longer
returns better seed or original if already fixed
'''
def fix_seed(seed, mc, dict_length, depth):
    ls = len(seed)
    if ls >= dict_length:
        return seed[-dict_length:]
    # small seed
    else: # this has high cost
        if depth > ls:
            depth = ls
        e = find_key(seed, mc, depth)
        if e:
            return e
        # if no match found, simply return small seed
        return seed
            


''' convert_probabilites creates an integrated, normalized, and discrete
probability function from a list of integers
takes the integer list stored in the markov chain dictionary - does not modify
returns a float list of probability boundaries
'''
def convert_probabilities(probability_list):
    N = len(probability_list)
    Sl=[probability_list[0]]
    for i in range(1,N):
        Sl.append(Sl[i-1]+probability_list[i])
    segment = 1/sum(probability_list)
    return [e*segment for e in Sl]

''' choose_index picks the next character by index of the probablity_list
takes probability_list, expecting the list stored in the markov chain dictionary - does not modify
returns the next character
'''
def choose_index(probability_list):

    # convert integer counts to an integrated and normalized
    # probability function
    Sp = convert_probabilities(probability_list)

    # simple binary search to find index of a random number
    r = rand()
    l = 0
    h = len(Sp)
    m = h//2
    # shouldn't be more than 7 steps, otherwise just return
    for i in range(7):
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

    return h



''' parse_how_much defines the ways that a user can input the amount of text that is generated
takes how_much as int or str
not case sensitive
not plural sensitive
returns int or throws error
# character = 0
# letter = 1
# word = 2
# sentence = 3
# paragraph = 4
# essay = 5
'''
def parse_how_much(how_much):
    try:
        if type(how_much) == int:
            if 0 <= how_much <= 4:
                return how_much
            else:
                raise Exception('hme', 'fail', 'out of bounds')
        elif type(how_much) == str:
            how_much = how_much.lower()
            if len(how_much) != 1 and how_much[-1] == 's':
                how_much[-1] = ''
            
            options = ["character","letter","word","sentence","paragraph","essay"]
            for i in range(6):
                if len(how_much) <= len(options[i]) \
                   and how_much == options[i][0:len(how_much)]:
                    return i
            raise Exception('hme', 'fail', 'bad word')
        else:
            raise Exception('hme', 'fail', 'not int or str')
    except Exception as out:
        a = out.args
        if len(a)==3 and a[0] == 'hme':
            if not a[1]:
                raise out
            elif a[1] == 'fail':
                print('error in parse_how_much: ', a[2], '\n', how_much)
                raise out
            else:
                raise out
        else:
            raise out
            
            

    
