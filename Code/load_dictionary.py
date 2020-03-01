def read_in_data(fileName):
    """Read data in from file"""
    with open(fileName, 'r') as file:
        data = file.read().splitlines()

    return data
