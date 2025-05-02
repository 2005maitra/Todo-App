from typing import final
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
import function
while True:
    user_action = input("type add,show,edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        if not todo:
            todo = input("What todo would you like to add? ").strip()

        todos = function.get_todos()
        todos.append(todo + '\n')
        function.write_todos(todos)
        print(f"Added: {todo}")

    elif user_action.startswith("show"):


        todos = function.get_todos()


        for  index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}--{item}"
            print(row)
    elif  user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number -1

            todos = function.get_todos()

            new_todo = input("enter new todo:")
            todos[number]= new_todo +'\n'

            function.write_todos(todos)
        except ValueError:
            print("your command is not valid.")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = function.get_todos()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)


            function.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from list."
            print(message)
        except IndexError:
            print("there is no item  with the number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("commnad is not valid")

print("bye!")

