from abc import ABC, abstractmethod

class Page(ABC):
    """
    The Page is an interface which all page objects will inherit. It represents a webpage
    in the student event tracking system application which can load for the student to see.

    ...

    Methods
    -------
    display()
        Displays the given webpage onto the screen for the student to see.
    """

    @abstractmethod
    def display(self):
        """Displays the given webpage onto the screen for the student to see."""
        pass

