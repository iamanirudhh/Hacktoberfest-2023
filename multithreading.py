import concurrent.futures

# Max size of array
max_val = 16

# Max number of threads to create
thread_max = 4

a = [1, 5, 7, 10, 12, 14, 15, 18, 20, 22, 25, 27, 30, 64, 110, 220]
key = 202

# Flag to indicate if key is found in a[] or not
f = 0

# Linear search function which will run for all the threads

def thread_search(num):
	global f
	for i in range(num * (max_val // 4), (num + 1) * (max_val // 4)):
		if a[i] == key:
			f = 1
			break

# Driver Code
if _name_ == '_main_':
	with concurrent.futures.ThreadPoolExecutor(max_workers=thread_max) as executor:
		for i in range(thread_max):
			executor.submit(thread_search, i)

	if f == 1:
		print("Key element found")
	else:
		print("Key not present")
