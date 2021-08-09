import logging

logger = logging.getLogger(__name__)

def example_module_function(name: str) -> str:
    """
    Generates a string including a name.

    :param str name: the name of someone
    :return: a string in the form 'Hello, my name is {name}'
    """
    logger.debug(f"Constructing a string from the following input: {name}")
    return f"Hello, my name is {name}"
