import data_base
import phone_book as pb
import view

def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            data_base.load_contacts()
        case 3:
            data_base.save_contacts()
        case 4:
            pb.add_contact()
        case 5:
            pb.change_contact()
        case 6:
            pb.remove_contact()
        case 7:
            pb.find_contact()
        case 0:
            return True

while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break
