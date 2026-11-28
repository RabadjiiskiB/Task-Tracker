from datetime import datetime
import json


count = 0
try:
    with open("tasks.json", "r") as f:
        dict = json.loads(f.read())
        count = len(dict)

except Exception as err:
    print(err)


available_commands = ["add"]
try:
    with open("tasks.json", "w") as f:
        input = input(f'Add a task in the format: add "Buy groceries" ')
        placeholder = input.split()
        command = placeholder[0].lower()
        if command not in available_commands:
            raise Exception("Not a command")
        placeholder.pop(0)
        task = " ".join(placeholder).strip("\"")
        print(task)
        count += 1
        print(f"Added task: {task} ID:{count}")
        x = datetime.now()
        dict[count] = {
                "description" : task,
                "status" : "todo",
                "createdAt" : x.strftime("%d.%m.%y %H:%M"),
                "updatedAt" : x.strftime("%d.%m.%y %H:%M")
            }
        count += 1
        print(dict)
        json = json.dumps(dict)
        print(json)
        f.write(json)
except Exception as err:
    print(err)