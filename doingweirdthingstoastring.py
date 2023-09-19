before = "hi my name is john and i am learning python"

def doingweirdthingstoastring(string):
    weird_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            weird_string += string[string_index].upper()
        else:
            weird_string += string[string_index].lower()
    print(weird_string)


doingweirdthingstoastring(before)