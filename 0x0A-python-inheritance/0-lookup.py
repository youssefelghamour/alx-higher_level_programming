""" Module containing lookup method """

def lookup(obj):
    """ Method that returns the list of available attributes and methods of an object
    
    Args:
        obj: object
    
    Returns:
        the list of available attributes and methods of the object
    """
    return dir(obj)
