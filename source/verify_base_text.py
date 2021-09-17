

# Verify that base_text.txt is sanitized.
def verify_base_text(path = None):
    if path == None:
        path = ".."
    with open(path+"/resources/base_text.txt", 'r', encoding = 'utf-8') as f:
        is_good = True
        ls = f.readlines()
        for l in ls:
            for i in range(len(l)):
                if not ( 31 < ord(l[i]) < 127 ):
                    print(f"error at {i} -- {l[i]} : {ord(l[i])-32}\n")
                    is_good = False
    return is_good
