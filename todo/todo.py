from typing import List, Union


class Todo:
    """
    Class todo allows you to set up a todo app.
    """
    __todos = []
    __STORAGE_FILE_PATH = "todos.txt"
    __EXIT_CONDITION = 'exit'

    def __init__(self):
        try:
            self.__todos = self.__get_todos(self.__STORAGE_FILE_PATH)
        except FileNotFoundError:
            self.__store_todos(self.__STORAGE_FILE_PATH, self.__todos)
        finally:
            print("Sync Complete...")

    @staticmethod
    def __get_todos(filepath: str) -> List[str]:
        """
        Opens a file storing todos and retrieves them.
        :param filepath: The path to the file.
        :return: A list of the stored todos.
        """
        with open(filepath, "r") as local_file:
            todos_local = [todo.rstrip('\n') for todo in local_file]
        return todos_local

    @staticmethod
    def __store_todos(filepath: str, todos: List[str], ) -> None:
        """
        Opens a file for appending and writes a todo line by line.
        :param filepath: Desired path to todo file.
        :param todos: A list of todos in str format to be added.
        """
        with open(filepath, "w") as local_file:
            for todo in todos:
                local_file.write(f"{todo}\n")

    @staticmethod
    def __parse_for_adding(user_input: str) -> Union[List[str], str]:
        """
        Parses incoming data from a user that will be used with the add method
        :param user_input: input from a user prompt.
        :return: Either one new todo or a list of new todos.
        """
        todos = user_input[4:].split(",")
        return [todo.strip() for todo in todos]

    def add(self, items: Union[List[str], str]) -> None:
        """
        Adds a new todo list item to the todo list store.
        :param items: a list of todo items to add to todo store.
        :return: None
        """
        if type(items) is str:
            self.__todos.append(items)
        elif type(items) is list:
            self.__todos.extend(items)
        else:
            print("Incorrect input (Usage: add [todo], [todo] ")

    def show(self) -> None:
        """
        Prints a formatted list of todos currently stored.
        :return: None
        """
        for i, todo in enumerate(self.__todos):
            print(f'{i + 1}. {todo}')

    def exit(self) -> None:
        """
        Should be called when the program exits.
        Stores todos in file and cleans up.
        """
        self.__store_todos(self.__STORAGE_FILE_PATH, self.__todos)

    def start(self) -> None:
        """
        Starts the todo list run loop.
        :return: None
        """
        user_input = ""
        while user_input != self.__EXIT_CONDITION:
            user_input = input("Type add, show, edit, complete, or exit: ")
            user_input = user_input.strip()
            if user_input.rfind('add ', 0, 4) == 0:
                todos = self.__parse_for_adding(user_input)
                self.add(todos)
            elif user_input.startswith('show'):
                self.show()
            elif user_input.startswith(self.__EXIT_CONDITION):
                self.exit()
                break
            else:
                print("Usage:\nadd [todo], [todo]\nshow\nedit [number] [revised todo]\ncomplete [number]\nexit")

