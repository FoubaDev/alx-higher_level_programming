#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key if isinstance(a_dictionary[best_key], int) else None

    print(f"Best Score: {best_key}")
