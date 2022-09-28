#!/usr/bin/python3
def search_replace(my_list, search, replace):
	new_list = []
	for nm in my_list:
		if nm == search:
			new_list.append(replace)
		else:
			new_list.append(nm)
	return new_list
