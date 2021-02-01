import sys
from googletrans import Translator


while True:
	if len(sys.argv) > 1:
		to_tl = sys.argv[1]
	else:
		to_tl = input("Please enter the full file path for the file you want to translate: ")
	with open(to_tl, "r",  encoding="utf8") as data:
		act_data = data.read()
		for item in act_data.split("END STRING"):
			print(item)


	if input("Translate another file? y/n: ").strip()[0] == "y":
		sys.argv = [sys.argv[0]]
	else:
		break
