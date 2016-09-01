class Contact(object): 
	def __init__(self, first_name, last_name, mobile_number ="", work_number ="", email ="", twitter_handle=""): 
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_number = mobile_number
		self.work_number = work_number
		self.email = email
		self.twitter_handle = twitter_handle
	
	def text(self, message): 
		if self.mobile_number is "": 
			return "no mobile number exists" 
		else:  
			return "To: %s - %s" % (self.mobile_number,message)
