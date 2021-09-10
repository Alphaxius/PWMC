
from random import randint as randint
from source import verify_base_text
vbt = verify_base_text.verify_base_text
from source import convert_to_json
cvj = convert_to_json.convert_to_json
lmc = convert_to_json.load_mc
## svj = convert_to_json.save_json
from source import generate_text
gt = generate_text.generate_text

def help_user():
    print ("Number Unit (Seed) or complete text mode (start with !)")

def main():
    if input("Refresh dictionary? (y/N): ") == 'y':
        cvj()
        vbt()
    (n, mc) = lmc()
    help_user()
    while True:
        user = input()
        if len(user) > 0:
            if user[0] == '!' and len(user) > 1:
                gt(mc, n, user[1:], 1, 4)
            else:
                user = user.split()
                if len(user) == 2:
                    try:
                        user[0] = int(user[0])
                    except ValueError:
                        print(user[0])
                        continue
                    k = list(mc.keys())
                    seed = randint(0,len(k))
                    try:
                        gt(mc, n, seed, user[0], user[1])
                    except Exception as problem: 
                        print(problem)
                        print(problem.args)
                        print(user[1])
                        raise problem
                elif len(user) == 3:
                    try:
                        user[0] = int(user[0])
                    except ValueError:
                        print(user[0])
                        continue
                    try:
                        gt(mc, n, user[2], user[0], user[1])
                    except Exception as problem: 
                        print(problem)
                        print(problem.args)
                        print(user[1])
                        raise problem
                    
                        

if __name__ == "__main__":
    main()
