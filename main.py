

## import and rename source
from random import randint as randint
from source import verify_base_text
vbt = verify_base_text.verify_base_text
from source import convert_to_json
cvj = convert_to_json.convert_to_json
lmc = convert_to_json.load_mc
## svj = convert_to_json.save_json
from source import generate_text
gt = generate_text.generate_text

## import test functions
from tests.TEST_parse_how_much import TEST_parse_how_much

## import necessary standard libraries
import sys


def run_test(TEST):
    test_success = TEST()
    if test_success:
        print(f"PASS: {TEST.__name__}")
    else:
        print(f"FAIL: {TEST.__name__}")

def run_tests():
    run_test(TEST_parse_how_much)

def main():
    print("Running PWMC")

    how_many = 1
    how_much = 1
    depth = 1
    seed = "a"
    dict_length = 3

    flag_n = False
    flag_w = False
    flag_g = False
    flag_g2 = False
    flag_s = False
    flag_d = False
    flag_no = False
    flag_dl = False
    flag_rr = False

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        if flag_n:
            how_many = int(arg)
            flag_n = False
        elif flag_w:
            how_much = arg
            flag_w = False
        elif flag_g:
            how_many = int(arg)
            flag_g = False
            flag_g2 = True
        elif flag_g2:
            how_much = arg
            flag_g2 = False
        elif flag_s:
            seed = arg
            flag_s = False
        elif flag_d:
            depth = int(arg)
            flag_d = False
        elif flag_dl:
            dict_length = int(arg)
            flag_dl = False
        else:
            al = arg.lower()
            if al == "t":
                run_tests()
            elif al == "n":
                flag_n = True
            elif al == "w":
                flag_w = True
            elif al == "g":
                flag_g = True
            elif al == "s":
                flag_s = True
            elif al == "d":
                flag_d = True
            elif al == "no":
                flag_no = True
            elif al == "dl":
                flag_dl = True
            elif al == "rr":
                flag_rr = True
            else:
                print(f"unknown flag: {arg} at {i}")
    
    if flag_rr:
        if not vbt('.'):
            print("Bad Path")
            raise Exception
        cvj(dict_length, path='.')
        
    if not flag_no:
        (n, mc) = lmc(path='.')
        print( gt(mc, n, seed, how_many, how_much, depth) )

if __name__ == "__main__":
    main()

