"""
Deep-LASI - MATLAB program using Python libraries for automated, multi-color single-molecule data analysis.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Returns a list of random ingredients as strings.
    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise deep-lasi.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
