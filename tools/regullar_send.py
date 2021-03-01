import time


def send


target_time = "2021-02-28 10:32"
while True:
	time.sleep(60)
	arr = time.localtime(time.time())
	if time.strftime("%Y-%m-%d %H:%M", arr) == target_time:
		print("hei")
	else:
		print("no")
