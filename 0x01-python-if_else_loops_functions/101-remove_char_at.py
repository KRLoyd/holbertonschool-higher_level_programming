#!/usr/bin/python3
def remove_char_at(str, n):
    if n > 0:
        first_part = str[:n]
        last_part = str[n + 1:]
        if n < len(str):
            return first_part + last_part
        else:
            return first_part
    else:
        return str
