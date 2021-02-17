import re
import os
from delete_file import *

# 前提：有记录文件jilu.txt

dataFile = "jilu.txt"

def classify_by_type():
	'''
	根据文件类型将记录分拣
	'''
	global dataFile
	try:
		os.mkdir("classify_by_type") #mkdir 如果目录已经存在，则会报错
	except:
		pass
	
	remove_all_files('classify_by_type', '*_data.txt', show = True)  # 删除所有*_data.txt文件

	with open(dataFile, "r") as f:
		for line in f:
			msg_type = re.search("message_type: (?P<TYPE>\d+)", line).group("TYPE")
			msg = re.search("message:(?P<msg>.+)$", line).group("msg")
			
			filename = msg_type+'_data.txt'
			with open(filename, "a") as f2:
				f2.write(msg+'\n')


def classify_by_chatroom(*chatroom_id):
	'''
	根据群将记录分拣
	'''
	global dataFile
	try:
		os.mkdir("classify_by_chatroom")
	except:
		pass
	# os.chdir("classify_by_chatroom")
	remove_all_files('classify_by_chatroom', '*_data.txt', show = True)  # 删除所有*_data.txt文件
	for id in chatroom_id:
		with open(dataFile, "r") as f:
			for line in f:
				filename = "classify_by_chatroom/"+id+'_data.txt'
				with open(filename, "a") as f2:
					if(id in line):
						f2.write(line)



if __name__ == "__main__":
	# classify_by_type()
	cr = "18729918322@chatroom"
	classify_by_chatroom(cr)

