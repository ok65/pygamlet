# Library import
from typing import Callable, List, Dict, Optional, Any
import functools


class Signal:

    def __init__(self, signature: Optional[Dict[str, Any]] = None):
        """
        Signal/slot pattern. Signature can be supplied as a dict
        :param signature: Dictionary of keyword arguments (kwargs)
        """
        self._bound_functions = []
        self._signature = signature if signature else {}

    @property
    def signature(self) -> Dict[str, Any]:
        """ :return: Dict of keyword arguments """
        return self._signature

    def bind(self, function: Callable):
        """
        Bind given function, which should be compatible with the signature keyword arguments.
        Return values will be ignored
        :param function:
        """
        self._bound_functions.append(function)

    def unbind(self, function: Callable):
        """
        Unbind given function
        :param function:
        """
        self._bound_functions.remove(function)

    def trigger(self, kwargs: Dict[str, Any]) -> None:
        """
        Trigger the signal, calling every bound function with the kwargs provided
        :param args: List of postional arguments
        :param kwargs: Dictionary of keyword arguments
        :raises: TypeError if the kwargs provided don't match the bound function's signature
        """
        kwargs = kwargs if kwargs else {}
        for func in self._bound_functions:
            func(**kwargs)


class SignalBox:

    def __init__(self, signals: Optional[Dict[str, Signal]] = None, new_signals: Optional[List[str]] = None):
        """
        Collection of signals, referenced by name.
        :param signals: Dict of signals with string name as key.
        :param new_signals: List of signal names to be created
        """
        self._signals = signals if signals else {}
        if new_signals:
            self._signals.update({sig_name: Signal() for sig_name in new_signals})

    @property
    def list(self) -> List:
        """ :return: List of signal names """
        return list(self._signals.keys())

    def bind(self, signal: str, func: Callable) -> None:
        """
        Bind given function to the signal name specified
        :param signal: string name of signal
        :param func: function to bind (must conform to signal signature)
        :raises: KeyError if signal name not found
        """
        self._signals[signal].bind(func)

    def unbind(self, signal: str, func: Callable) -> None:
        """
        Unbind given function from signal specified.
        :param signal: string name of signal
        :param func: function to unbind
        :raises: Keyerror if signal name not found, ValueError if function not found.
        """
        self._signals[signal].unbind(func)

    def trigger(self, signal: str, kwargs: Optional[Dict] = None) -> None:
        """
        Trigger the given signal, with the args specified
        :param signal: string name of the signal
        :param kwargs: Dict of keyword arguments (optional)
        :raises: KeyError if the signal name is not found, TypeError if the kwargs doesn't match the bound function's
                 signature
        """
        self._signals[signal].trigger(kwargs)

    def set(self, name: str, signal: Optional[Signal] = None) -> None:
        """
        Adds signal with the specified name (if signal isntance not provided, a blank one will be generated)
        :param name: string name of signal
        :param signal: Signal instance
        """
        self._signals[name] = signal if signal else Signal()

    def get(self, name) -> Signal:
        """
        Gets the signal instance of the signal with the specified name
        :param name: string name of instance
        :return: Signal instance
        :raises: KeyError if the signal name is not found
        """
        return self._signals[name]


class SignalBoxClass:

    def __init__(self, signals: Optional[List[str]] = None):
        """
        Convenience inheriting class, adds a SignalBox instance to self.signals
        :param signals: List of signal names to create
        """

        self.signals = SignalBox(new_signals=signals)


class SignalDec:
    def __init__(self, *args, **kwargs):
        # store arguments passed to the decorator
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def newf(*args, **kwargs):

            # the 'self' for a method function is passed as args[0]
            slf = args[0]

            # replace and store the attributes
            saved = {}
            for k, v in self.kwargs.items():
                if hasattr(slf, k):
                    saved[k] = getattr(slf, k)
                    setattr(slf, k, v)

            # call the method
            ret = func(*args, **kwargs)

            # put things back
            for k, v in saved.items():
                setattr(slf, k, v)

            return ret

        newf.__doc__ = func.__doc__
        return newf