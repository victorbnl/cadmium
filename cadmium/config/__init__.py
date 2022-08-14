"""Access and manage configuration items."""

from cadmium.config import load


_inst = load.load()
get = _inst.get
set = _inst.set
to_dict = _inst.to_dict


def write():
    """Write config on disk."""

    load.write(_inst)


def set(*args, **kwargs):
    """Wrapper around Config.set to also write it on disk."""

    _inst.set(*args, **kwargs)
    write()


# Write config right after having loaded it
# (useful if there is no config or current config misses keys)
write()
