# test.py  (c)2024  Henrique Moreira

""" DataClass - serializing/ deserializing json
"""

import sjson.common
from sjson.dataclass import DataClass

def main_test():
    """ Basic tests! """
    lst = [sjson.common.A_SAMPLE]
    new = DataClass(lst, "Tst")
    print("main_test():", new)
    print()
    print("Message():", new.message())
    skel = new.get_skel()
    print('+' + '\n+'.join([skel["low"][item] for item in skel["low"]]), end="!\n\n")


# Main script
if __name__ == "__main__":
    main_test()
