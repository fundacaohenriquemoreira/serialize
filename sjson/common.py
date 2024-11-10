# common.py  (c)2024  Henrique Moreira

""" Common JSON manipulation
"""

# pylint: disable=missing-function-docstring

import json
import unidecode

null = None

A_SAMPLE = {
    "DatadeFim": null,
    "DatadeInicio": null,
    "DatadeRec.": null,
    "Estado": null,
    "Imovel": null,
    "Importanciarecebida": null,
    "Locador": null,
    "Locatario": null,
    "N.deContrato": null,
    "N.deRecibo": null,
    "Referencia": null,
    "RetencaoIRS": null,
    "Valor": null,
}

SAMPLE_DLIST = {
    'listarecibos.json': [
        A_SAMPLE,
    ],
}


class GenericData():
    """ Generic data class (Abstract)
    """
    _def_encoding = "utf-8"
    _indent = 2
    _ensure_ascii = True

    def __init__(self, name, encoding=None):
        self.name, self._raw = name, []
        enc = GenericData._def_encoding
        self.encoding = enc if encoding is None else encoding
        self._msg, self._comment = "", ""

    def clear_msg(self):
        self._msg = ""

    def message(self):
        return self._msg

    def dump_json(self, data=None, asort=True) -> str:
        ind = GenericData._indent
        ensure = GenericData._ensure_ascii
        if data is None:
            cont = self._raw
        else:
            cont = data
        astr = json.dumps(cont, indent=ind, sort_keys=asort, ensure_ascii=ensure)
        return astr + "\n"

    @staticmethod
    def default_encoding() -> str:
        return GenericData._def_encoding

    def _can_write(self) -> bool:
        return False

    def _can_read(self) -> bool:
        return True

    def __repr__(self) -> str:
        """ Returns ascii representation.
        Please redefine in the specific classes what you judge correct for that representation.
        """
        astr = to_ascii(str(self._raw))
        return astr


def to_ascii(astr):
    ustr = unidecode.unidecode(astr)
    return ustr
