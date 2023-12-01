FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as todos_file:
        return todos_file.readlines()


def get_clear_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items without breaklines. """
    with open(filepath, 'r') as todos_file:
        todos = todos_file.readlines()
        result = [todo.strip('\n') for todo in todos]
        return result


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(__name__)
