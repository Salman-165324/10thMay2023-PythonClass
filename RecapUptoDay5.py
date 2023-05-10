#Target to build a todo app with add, show, edit, complete and Exit functionality.

todoList = []

while True:
    user_command = input("Please write Add, Show, Edit, Complete and Exit to perform a task:\n")

    match user_command:

        case 'Add':
            todo = input("Please write your todo items or write 'Back' to go back:\n")
            todoList.append(todo)
        case 'Show':
            for todo in todoList:
                print(todo)
        case 'Edit':
            print("Inside Edit")
        case 'Complete':
            print("Inside Complete")
        case 'Exit':
            print("Tata Bye Bye. Never see you again")
            break