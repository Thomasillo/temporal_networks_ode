
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def dummy(a, b):
    """Frob the draf.

    Example:
    >>> dummy(1, 2)
    3
    """
    return a + b
