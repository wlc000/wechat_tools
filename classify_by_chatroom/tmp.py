import json
# with open("1.txt","w") as f:
#	 f.write(json.dumps("问问"))
with open("1.txt","r") as f:
	print(eval(f.readline()))