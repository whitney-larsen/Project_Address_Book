import contact_manager

def main():
	while(True):
		choice = int(raw_input("0 - Main Menu\n1 - Show all contacts\n2 - Add a new contact\n3 - Edit a contact\n4 - Delete a contact\n5 - Exit the program"))
		if choice == 1:
			contact_manager.show_contact()
		elif choice == 2:
			contact_manager.add_new_contact()
		elif choice == 3:
			contact_manager.edit_contact()
		elif choice == 4:
			contact_manager.delete_contact()
		elif choice == 5:
			contact_manager.write_file("contact_list.txt")
			break

if __name__ == '__main__':
	main()