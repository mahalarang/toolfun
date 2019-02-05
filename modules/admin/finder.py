from .config import Config
from urllib import request, error

class Finder(Config):
	def __init__(self):
		super().__init__()
		self.target = self.input_target()
		self.pathname = self.input_pathname()

	def input_target(self):
		input_target = ""
		while True:
			input_target = input("Masukkan target: ")
			if type(input_target) == str:
				break
			print("target harus string bosss")

		return input_target

	def input_pathname(self):
		paths = []
		try:
			with open('modules/admin/' + self.file_name, 'r') as file:
				for path in file:
					paths.append(path.strip())
		except IOError as e:
			print("file", self.file_name, "tidak ditemukan")
			exit
		except:
			print('Oppss terjadi kesalahan')
			exit
		return paths

	def checking_header_status(self, url):
		data = { 'status': 0, 'message': '' }
		try:
			res = request.urlopen(url)
			data['status'] = str(res.getcode())
			data['message'] = self.get_message(res.getcode())
		except error.HTTPError as err:
			data['status'] = str(err.getcode())
			data['message'] = self.get_message(err.getcode())
		return data

	def run(self):
		for path in self.pathname:
			full_url = self.target + "/" + path
			response = self.checking_header_status(full_url)
			print("[" + response['status'] + "] " + full_url)


