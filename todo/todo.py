from typing import List, Union, Tuple


class Todo:
    """
    Class todo allows you to set up a cmd line todo app.
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

        """
        Proposal - In addition to adding the todos to memory,
        consider also making a write to the local file as well.
        As it currently stands, we only write to the file when
        a user uses to exit command.
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

    @staticmethod
    def __parse_for_editing(user_input: str) -> Tuple[int, str]:
        """
        Parses user input to be used by the edit method.
        Throws a ValueError if improperly formatted.
        :param user_input: Input from the user.
        """
        formatted = [item.strip() for item in user_input[5:].split(',')]
        if len(formatted) < 2:
            raise ValueError
        return int(formatted[0]) - 1, formatted[1]

    def edit(self, i: int, revised_todo) -> None:
        """
        Replaces the todo  at the specified index in the todo memory store.
        Throws a ValueError if index is out of range.
        :param i: The index of the desired todo to edit.
        :param revised_todo: A new todo.
        """
        if i < 0 or i >= len(self.__todos):
            raise ValueError
        self.__todos[i] = revised_todo

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
            elif user_input.rfind('edit ', 0, 5) == 0:
                try:
                    i, todo = self.__parse_for_editing(user_input)
                    self.edit(i, todo)
                except ValueError:
                    print("Invalid input please try again.")
                    print("Usage:\nadd [todo], [todo]\nshow\nedit [number], [revised todo]\ncomplete [number]\nexit")
            elif user_input.startswith('show'):
                self.show()
            elif user_input.startswith(self.__EXIT_CONDITION):
                self.exit()
                break
            else:
                print("Usage:\nadd [todo], [todo]\nshow\nedit [number], [revised todo]\ncomplete [number]\nexit")

