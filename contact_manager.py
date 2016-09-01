# class Contact(object): 
# 	def __init__(self, first_name, last_name, mobile_number ="", work_number ="", email =""): 
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.mobile_number = mobile_number
# 		self.work_number = work_number
# 		self.email = email
	
# 	def text(self, message): 
# 		if self.mobile_number is "": 
# 			print "no mobile number exists" 
# 		else:  
# 			print "To: %s - %s" % (self.mobile_number,message)

from contact import Contact

contact_list =[]


def add_new_contact():
	contact_name = raw_input("enter first name: ").lower()
	contact_last_name = raw_input("enter last name: ").lower()
	contact_mobile_number = raw_input("enter mobile: ").lower()
	contact_work_number = raw_input("enter work number: ").lower()
	contact_email = raw_input("enter email: ").lower()
	contact_twitter = raw_input("enter twitter handle:  ").lower()
	new_contact = Contact(contact_name,contact_last_name,contact_mobile_number,contact_work_number,contact_email,contact_twitter)
	global contact_list
	contact_list.append(new_contact)

def delete_contact():
	contact_delete_name= raw_input("What is the first name of the contact you want to delete? ").lower()
	contact_delete_last_name = raw_input("What is the last name of the contact you want to delete? ").lower()
	for contact in contact_list:
		if contact.first_name == contact_delete_name and contact.last_name == contact_delete_last_name:
			contact_list.remove(contact)
			return
	print "Contact Not Found"

def show_contact():
	for contact in contact_list:
		print contact.first_name + " " + contact.last_name + " " + contact.mobile_number + " " + contact.work_number + " " + contact.email

def edit_contact():
	contact_edit_name= raw_input("What is the first name of the contact you want to edit? ").lower()
	contact_edit_last_name = raw_input("What is the last name of the contact you want to edit? ").lower()

	for contact in contact_list:
		if contact.first_name == contact_edit_name and contact.last_name == contact_edit_last_name:
			print "This is the contact you have chosen to edit:  " + contact.first_name + " " + contact.last_name + " " + contact.mobile_number + " " + contact.work_number + " " + contact.email

			field_choice = int(raw_input("What would you like to edit?\n1 - Edit first name\n2 - Edit last name\n3 - Edit mobile\n4 - Edit work number\n5 - Edit email\n6 - Edit twitter handle"))
			new_info = raw_input("What do you want to change it to? ")
			
			for contact in contact_list:
				if contact.first_name == contact_edit_name and contact.last_name == contact_edit_last_name:
					if field_choice == 1:
						contact.first_name = new_info
					elif field_choice==2:
						contact.last_name = new_info
					elif field_choice==3:
						contact.mobile_number = new_info
					elif field_choice==4:
						contact.work_number = new_info
					elif field_choice==5:
						contact.email = new_info
					elif field_choice==6:
						contact.twitter_handle = new_info
					print "This is your updated contact:  " + contact.first_name + " " + contact.last_name + " " + contact.mobile_number + " " + contact.work_number + " " + contact.email
					return
	print "Contact Not Found."


def write_file(file_name):
	contact_string = ""
	for contact in contact_list:
		contact_string = contact_string + contact.first_name + "," + contact.last_name + "," + contact.mobile_number + "," + contact.work_number + "," + contact.email
	with open (file_name, mode = 'a') as my_file:
		my_file.write(contact_string)

# def main():
# 	add_new_contact()
# 	add_new_contact()
# 	edit_contact()
# 	# delete_contact()
# 	# show_contact()
	
# if __name__ == '__main__':
# 	main()
