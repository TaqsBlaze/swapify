from files import passwordWindow


try:
    passwordWindow.window.show()
except Exception as error:
    print(error)