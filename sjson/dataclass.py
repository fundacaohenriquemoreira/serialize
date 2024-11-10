# dataclass.py  (c)2022, 2023  Henrique Moreira

""" DataClass - serializing/ deserializing json
"""

# pylint: disable=missing-function-docstring

import re
import sjson.common

def main_test():
    lst = [sjson.common.A_SAMPLE]
    new = DataClass(lst, "Tst")
    print("main_test():", new)
    print()
    print(new._skel)

class DataClass(sjson.common.GenericData):
    """ Deserialized data from JSON.
    """
    def __init__(self, obj=None, name="tbl", encoding=None):
        super().__init__(name, encoding)
        self._skel = {}
        data = [] if obj is None else obj
        self._reload_data(data, "i")

    def to_string(self) -> str:
        """ Reports the 'original' JSON string. """
        astr = self.dump_json(asort=True)
        return astr

    def _reload_data(self, data, kind="i"):
        """ Load or reload data from list.
        """
        assert isinstance(data, list), self.name
        is_ok = True
        self._raw = data
        if kind == "e":	# edit
            return True
        if kind == "i":
            is_ok = self._init_opt(data[-1] if data else {}) == ""
        else:
            assert False, f"Wrong kind: {repr(kind)}"
        return is_ok

    def _init_opt(self, item):
        """ Initialize optimizations; returns empty if all ok,
        or a comprehensive message on error.
        """
        if not item:
            return ""
        skel = {}
        for key in sorted(key):
            low = clean_key(key)
            if key in skel:
                return f"Dup key={key}, as {repr(low)}"
            skel[key] = low
        self._skel = skel
        return ""

    def __str__(self) -> str:
        return self.to_string()


def clean_key(key):
    return re.sub(r'[-.]', '', key)


# Main script
if __name__ == "__main__":
    print("Please import me!")
    main_test()
