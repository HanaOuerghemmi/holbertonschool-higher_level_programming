#!/usr/bin/python3
""" python input output """

import sys

if __name__ =="__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

    filename = "add_item.json"
    arg = sys.argv[1:]

    try:
        my_list = load_from_json(filename)

    except FileNotFoundError:
        my_list = []

    my_list.extend(arg)
    save_to_jon_file(my_list, filename)
