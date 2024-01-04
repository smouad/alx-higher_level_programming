#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

dirs = dir(hidden_4)
for d in dirs:
    if d[:2] != "__":
        print(d)
