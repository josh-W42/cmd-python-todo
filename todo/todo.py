from typing import List, Union


class Todo:
    """
    Class todo allows you to set up a todo app.
    """
    __todos = ["Code in python", "Get a job", "Profit"]
    __storage_file_path = "todos.txt"

    def __int__(self) -> None:
        try:
            self.__todos = self.__get_todos(self.__storage_file_path)
        except FileNotFoundError:
            self.__store_todos(self.__storage_file_path, self.__todos)
        finally:
            print("Sync Complete...")

    @staticmethod
    def __get_todos(self, filepath: str) -> List[str]:
        """
        Opens a file storing todos and retrieves them.
        :param filepath: The path to the file.
        :return: A list of the stored todos.
        """
        with open(filepath, "r") as local_file:
            todos_local = local_file.readlines()
        return todos_local

    @staticmethod
    def __store_todos(filepath: str, todos: List[str], ) -> None:
        """
        Opens a file for appending and writes a todo line by line.
        :param filepath: Desired path to todo file.
        :param todos: A list of todos in str format to be added.
        """
        with open(filepath, "a") as local_file:
            for todo in todos:
                local_file.write(f"{todo}\n")

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
        self.__store_todos(self.__storage_file_path, self.__todos)

    def start(self) -> None:
        """
        Starts the todo list run loop.
        :return: None
        """
        exit_condition = 'exit'
        user_input = ""
        while user_input != exit_condition:
            user_input = input("Type add, show, edit, complete, or exit: ")
            user_input = user_input.strip()
            if user_input.startswith('add'):
                pass
            elif user_input.startswith('show'):
                self.show()
            elif user_input.startswith(exit_condition):
                self.exit()
                break

