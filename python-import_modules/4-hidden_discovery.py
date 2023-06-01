#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    
    words = dir(hidden_4)
    for name in words:
        if name[:2] != "__":
            print(name)
