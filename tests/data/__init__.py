import os


def test_file(name):
    """
    Return the path to the test file with the given name
    :param name: The name of the test file
    :return: The full path to the test file.
    """
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
