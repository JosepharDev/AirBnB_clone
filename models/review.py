#!/usr/bin/python3
"""
Define SubClass of BaseModel called review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that represents a review

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
