from typing import List, Union


class Todo:
    """
    Class todo allows you to set up a todo app.
    """
    __todos = ["Code in python", "Get a job", "Profit"]

    def __int__(self):
        pass

    def add(self, items: Union[List[str], str]) -> None:
        """
        Adds a new todo list item to the todo list store.
        :param items: a list of todo items to add to todo store.
        :return: None
        """
        if type(items) == str:
            self.__todos.append(items)
        elif type(items) == List:
            self.__todos.append(*items)

    def show(self) -> None:
        """
        Prints a formatted list of todos currently stored.
        :return: None
        """
        for i, todo in enumerate(self.__todos):
            print(f'{i + 1}. {todo}')

    def start(self) -> None:
        """
        Starts the todo list run loop.
        :return: None
        """
        exit_condition = 'exit'
        user_input = input("Type add, show, edit, complete, or exit: ")
        while user_input != exit_condition:
            user_input = user_input.strip()
            if user_input.startswith('add'):
                pass
