from image_search import predict_from_path
import threading
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("num_threads", 
    help="number of threads to run",
    type=int)
parser.add_argument("run_time", 
    help="number of seconds to run test for",
    type=int)
args = parser.parse_args()

class test_frequency():

	def __init__(self, time_limit):
		self.global_lock = threading.Lock()
		self.count = 0
		self.start = time.time()
		self.time_limit = time_limit


	def main(self, thread_num):
		print "starting thread {}".format(thread_num)
		personal_count = 0
		while time.time() - self.start < self.time_limit:
			path = "test_images/fish.jpg"
			prediction = predict_from_path(path)
			if prediction == "fish":
				with self.global_lock:
					self.count += 1
				personal_count += 1
				print "thread {} finsihed search {}".format(thread_num, personal_count)
		if thread_num == 0:
			print "finished {} requests".format(self.count)






if __name__ == '__main__':
	test = test_frequency(args.run_time)
	for i in range(args.num_threads):
		t = threading.Thread(target=test.main, args=(i,))
		t.start()