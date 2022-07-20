#!/usr/bin/env python3

import requests
import sys
import time
from tqdm import tqdm


directories_list=open("directories2.txt").read()
directories_formatted=directories_list.splitlines()


for dir in tqdm(directories_formatted):
	dir_enum=f"http://{sys.argv[1]}/{dir}" #sys.argv[1] takes the input from the cli. sys.argv[0] is always the name of the script.
	try:
		get_request=requests.get(dir_enum)
		if get_request.status_code == 404:
			pass
		else:
			print("A directory has been found! ", dir_enum)
	except requests.Timeout as e:
		print("We are sending way too many packets!!")
		print(f"Let's sleep for {x} seconds")
		x=5
		time.sleep(x)
		print("Boy, I slept well")
		continue
	except KeyboardInterrupt:
		print("The user interrupted the program.")
		break