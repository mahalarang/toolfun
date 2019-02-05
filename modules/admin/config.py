class Config:
	
    def __init__(self):
    	self.__target = ""
    	self.__pathname = ""
    	self.__file_name = "pathname.txt"
    	self.__message = {
	        '200' : "Admin Founded",
	        '302' : "Moved Temporarily",
	        '400' : "Bad Request",
	        '401' : "Unauthorized",
	        '403' : "Forbidden",
	        '404' : "Not Found",
	        '408' : "Request Timeout",
	        '410' : "Removed Permanently",
	        '500' : "Server error" }

    def get_message(self, status):
    	return self.__message[str(status)]

    def set_message(self, status, msg):
    	self.__message[str(status)] = msg

    @property
    def target(self):
    	pass

    @target.getter
    def target(self):
    	return self.__target

    @target.setter
    def target(self, inp):
    	self.__target = inp

    def input_target(self):
    	pass

    @property
    def pathname(self):
    	pass

    @pathname.getter
    def pathname(self):
    	return self.__pathname

    @pathname.setter
    def pathname(self, inp):
    	self.__pathname = inp

    @property
    def file_name(self):
    	pass

    @file_name.getter
    def file_name(self):
    	return self.__file_name
