from todo.todo import Todo


if __name__ == '__main__':
    app = Todo()
    app.show()
    app.add("Make Pancakes")
    app.add(["Laugh", "Live", "Love"])
    app.show()



