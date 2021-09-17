
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
    vbt('.')
    cvj(10, path='.')
    (n, mc) = lmc(path='.')
    print( gt(mc, n) )

if __name__ == "__main__":
    main()
