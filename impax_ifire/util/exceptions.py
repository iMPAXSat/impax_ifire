"""
This module provides errors/exceptions and warnings of general use.

Exceptions that are specific to a given package should **not** be here,
but rather in the particular package.

This code is based on that provided by SunPy see
    licenses/SUNPY.rst
"""

import warnings

__all__ = [
    "iFireWarning",
    "iFireUserWarning",
    "iFireDeprecationWarning",
    "iFirePendingDeprecationWarning",
    "warn_user",
    "warn_deprecated",
]


class iFireWarning(Warning):
    """
    The base warning class from which all IMPAX IFIRE warnings should inherit.

    Any warning inheriting from this class is handled by the IMPAX IFIRE
    logger. This warning should not be issued in normal code. Use
    "iFireUserWarning" instead or a specific sub-class.
    """


class iFireUserWarning(UserWarning, iFireWarning):
    """
    The primary warning class for IMPAX IFIRE.

    Use this if you do not need a specific type of warning.
    """


class iFireDeprecationWarning(FutureWarning, iFireWarning):
    """
    A warning class to indicate a deprecated feature.
    """


class iFirePendingDeprecationWarning(PendingDeprecationWarning, iFireWarning):
    """
    A warning class to indicate a soon-to-be deprecated feature.
    """


def warn_user(msg, stacklevel=1):
    """
    Raise a `iFireUserWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, iFireUserWarning, stacklevel + 1)


def warn_deprecated(msg, stacklevel=1):
    """
    Raise a `iFireDeprecationWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, iFireDeprecationWarning, stacklevel + 1)
