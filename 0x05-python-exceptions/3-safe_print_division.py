#!/usr/bin/python3
def safe_print_division(a, b);
    try:
        result = a / b
    except ZeroDIvisionError:
        result = None
    finally:
        print("Iniside result: {}".format(result))
    return result
