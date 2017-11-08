from image_search import predict_from_path, predict_from_url
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
		self.use_url = True


	def main(self, thread_num):
		print("starting thread {}".format(thread_num))
		personal_count = 0
		while time.time() - self.start < self.time_limit:
			path = "test_images/fish.jpg"
			if not self.use_url:
				prediction = predict_from_path(path)
			else:
				prediction = predict_from_url("http://sn.uploads.im/xdmfZ.jpg")
			if prediction == "fish":
				with self.global_lock:
					self.count += 1
				personal_count += 1
				print("thread {} finsihed search {}".format(thread_num, personal_count))
			elif prediction is None:
				print("thread {} failed".format(thread_num))
			else:
				print("thread {} incorrectly prediction {}".format(thread_num, prediction))
		if thread_num == 0:
			print("finished {} requests".format(self.count))






if __name__ == '__main__':
	test = test_frequency(args.run_time)
	for i in range(args.num_threads):
		t = threading.Thread(target=test.main, args=(i,))
		t.start()