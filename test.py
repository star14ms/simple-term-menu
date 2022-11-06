from simple_term_menu import show_menu, select_file


# value, key = show_menu({'[a] Choice-1' : 1, '[b] Choice-2': 2, '[q] Quit': None})
# print('value:', value)
# print('key:', key)


_, view_path = select_file()
print(view_path)
