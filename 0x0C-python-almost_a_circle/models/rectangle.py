#!/usr/bin/python3
"""
Rectangle module
Create a Rectangle class, inheriting from Base.
"""


from models.base import Base


class Rectangle(Base):
    """Class describing a rectangle.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.
        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
