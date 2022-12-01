#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for item in dir(hidden_4):
        # if not item.startswith("__"): <- Does the same thing
        if item[0:2] != "__":
            print(item)
