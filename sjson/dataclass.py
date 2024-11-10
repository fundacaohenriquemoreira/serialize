# dataclass.py  (c)2024  Henrique Moreira

""" DataClass - serializing/ deserializing json
"""

# pylint: disable=missing-function-docstring

import re
import sjson.common

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

    def get_skel(self) -> dict:
        assert self._skel, self.name
        return self._skel

    def _reload_data(self, data, kind="i"):
        """ Load or reload data from list.
        """
        assert isinstance(data, list), self.name
        is_ok = True
        self._raw = data
        if kind == "e":	# edit
            return True
        if kind == "i":
            msg = self._init_opt(data[-1] if data else {})
            self._msg = msg
            is_ok = msg == ""
        else:
            assert False, f"Wrong kind: {repr(kind)}"
        return is_ok

    def _init_opt(self, item):
        """ Initialize optimizations; returns empty if all ok,
        or a comprehensive message on error.
        """
        if not item:
            return ""
        skel = {
            "low": {},
            "field2low": {},
        }
        self._skel = skel
        for key in sorted(item):
            low = clean_key(key).lower()
            if low in skel["low"]:
                return f"Dup key={key}, as {repr(low)}"
            skel["low"][low] = key
            skel["field2low"][key] = low
        self._skel = skel
        return ""

    def __str__(self) -> str:
        return self.to_string()


def clean_key(key):
    return re.sub(r'[-.]', '', key)


# Main script
if __name__ == "__main__":
    print("Please import me!")
