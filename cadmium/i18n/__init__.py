"""Get i18n strings."""

from cadmium.i18n.load import load

_inst = load('fr')
i18n = _inst.get
