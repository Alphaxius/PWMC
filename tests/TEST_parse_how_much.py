from source import generate_text
phm = generate_text.parse_how_much
from random import randint as ri

def TEST_parse_how_much():
    test = True
    options = ["character","letter","word","sentence","paragraph","essay"]
    try:
        for i in range(len(options)):
            for j in range(1,len(options[i])):
                if phm(options[i][0:j]) != i:
                    print("FAIL: problem with ", options[i][0:j])
                    test = False
                if phm(options[i][0:j]+'s') != i:
                    print("FAIL: problem with ", options[i][0:j]+'s')
                    test = False
                rand_cap_string = list(options[i][0:j])
                for k in range(j):
                    rand_cap_string[k] = chr(ord(rand_cap_string[k])-ri(0,1)*32)
                rand_cap_string = ''.join(rand_cap_string)
                if phm(rand_cap_string[0:j]) != i:
                    print("FAIL: problem with ", rand_cap_string[0:j])
                    test = False
        if test:
            print("PASS: all standard words and random capitals")
    except Exception as e:
        print(type(e.args))
        print(e.args)
        print("FAIL: exception thrown on normal string")
        test = False

    try:
        phm("")
    except Exception as e:
        if e.args[0] == "Empty String":
            print("PASS: empty string throws error")
        else: 
            print(type(e.args))
            print(e.args)
            print("FAIL: empty string exception is not in expected format")
            test = False
        pass
    else:
        print("FAIL: exception not thrown on empty string")
        test = False

    for _ in range(100):
        rand_string = []
        for _ in range(ri(1,10)):
            rand_string.append(chr(ri(97,122)-ri(0,1)*32))
        rand_string = ''.join(rand_string)
        try:
            phm(rand_string)
        except Exception as e:
            if e.args[0] == ("Bad String"):
                print("PASS: random string throws error")
            else:
                print(type(e.args))
                print(e.args)
                print("FAIL: random string did not throw exception in expected format")
                test = False
            pass
        else:
            rand_string = rand_string.lower()
            if rand_string[-1] == 's':
                rand_string = rand_string[:-1]
            in_options = False
            options_lens = []
            for option in options:
                options_lens.append(len(option))
            if len(rand_string) < max(options_lens):
                for i in range(len(options)):
                    if len(rand_string) < options_lens[i]:
                        if rand_string == options[i][:len(rand_string)]:
                            # rand_string is substring of an option
                            in_options = False
                            break
            if in_options:
                print("FAIL: exception not thrown on random string:", rand_string)
                test = False
    
    num_test = True
    for i in range(6):
        try:
            value = phm(i)
            if value != i:
                print("FAIL: unexpected return value on ", i, ": ", value)
        except Exception as e:
            print(type(e.args))
            print(e.args)
            print("FAIL: exception thrown on normal integer: ", i)
            test = False
            num_test = False
            pass
    if num_test:
        print("PASS: all regular numbers work")

    test_values = [-1, -100, -100000, 6, 7, 20, 100000]
    for v in test_values:
        try:
            phm(v)
        except Exception as e:
            if e.args[0] == "Out of Bounds":
                print("PASS: correct exception thrown on bad number")
            else:
                print(type(e.args))
                print(e.args)
                print("FAIL: exception is not as expected for bad number")
                test = False
        else:
            print("FAIL: no exception thrown on bad number")
            test = False
    
    for _ in range(100):
        try:
            phm(ri_phm_test())
        except Exception as e:
            if e.args[0] == "Out of Bounds":
                print("PASS: correct exception thrown on big or small number")
            else:
                print(type(e.args))
                print(e.args)
                print("FAIL: exception is not as expected for big or small number")
                test = False
        else:
            print("FAIL: no exception thrown on big or small number")
            test = False

    test_values = [False, True, None, 1.2, 1., 5.1, 5., 0.]
    for v in test_values:
        try:
            phm(v)
        except Exception as e:
            if e.args[0] == "Not Int or String":
                print("PASS: correct exception thrown on bad input")
            else:
                print("FAIL: exception is not as expected for bad input")
                test = False
        else:
            print("FAIL: no exception thrown on bad input")
            test = False

    return test


def ri_phm_test():
    if ri(0,1) == 0:
        return ri(-100000,-1)
    else:
        return ri(6,100000)
