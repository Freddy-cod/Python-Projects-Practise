    # import re - a regex library: we will use to validate emails
import re
from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE 

# A list to store emails 
inbox = []
# spam emails
# A variable to store user choice
user_choice = ""

# Make a regular expression for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# For custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 

# Function to validating an Email 
def check(email):  
    # if the email matches an email address payttern
    if(re.search(regex,email)):  
        print(f"'{email}' is a valid email\n")
        return True
    else:  
        print(f"'{email}' is an invalid email\n")
        return False


# An Email Simulation Class
class Email:
    def __init__(self, email_contents, from_address):
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False
        self.email_contents = email_contents

    # Method to mark email as read
    def mark_as_read(self):
        self.has_been_read = True
    
    # Method to mark email as spam
    def markk_as_spam(self):
        self.is_spam = True

    # Overide str function to return custom string
    def __str__(self):
        return f"From: {self.from_address} \nContent: {self.email_contents} "


inbox = []
# Function to add emails
def add_email(message, email):
    # creats an email object
    send = Email(message, email)
    # adds email to the inboxs list
    inbox.append(send) 
    print("Email sent successfully!")


# Function to return the number of emails from the inbox
def get_count(inbox):
    return len(inbox) # use len to count the number of items


# Function to return the content of an email
def get_email(index):
    print()
    # return an email based on the index passed and mark it as read
    message = inbox[index]
    message.mark_as_read()
    print(message)


# Function that returns all unread emails
def get_unread_emails():
    print()
    messages =[]
    for n, i in enumerate(inbox):
        # if an email is not read store it on a list 
        if not i.has_been_read:
            message = inbox[n]
            messages.append(message) 
            print(message.email_contents)
    return messages # a list of all unread emails


# Function that returns all spam emails
def get_spam_emails():
    print()
    messages =[]
    for n, i in enumerate(inbox):
        # if an email is marked as spam store it on a list
        if i.markk_as_spam:
            message = inbox[n]
            messages.append(message)
            print(f"spam: {message.email_contents}")
    return messages # a list of spam emails


# Functions that marks an email as a spam
def add_spam(index):
    # get requested email based on index
    message = inbox[index]
    # mark email as spam
    message.markk_as_spam()
    print("Email added to spam!")


# Function to delete an email 
def get_remove(index):
    # persist a delete with a try block
    try:
        # use the remove function to remove email from inbox using index
        inbox.remove(inbox[index])
        print("Email deleted successfully")
    except:
        print("Error: couldn't delete email")
# Add email


# Initial email 
init_emails = [
    'Hie how are you,alfred@gmail.com',
    'Hie lets meet us,thuba@gmail.com'
]

for i in init_emails:
    message, email = i.split(',')
    add_email(message,email)


# Get user input or choice
while user_choice != "quit":
    # provide options for the user to choose
    user_choice = input("\nWhat would you like to do - read | mark spam | send | delete | quit? ")
    # if user wants to read

    if user_choice == "read":
        # if there are no mails
        if len(inbox) == 0:
            print(f"You have no emails to read")
        else:
            # else show all mails and ask user to pick a mail to read
            print(f"You have {len(inbox)} email(s).")
            getmail_index = int(input(f"\nEnter a number from 1 - {get_count(inbox)} to retrieve unread email: "))
            # if user chooses a number greater than the number of mails in the inbox: give an error
            if getmail_index > len(inbox) or getmail_index < 0:
                print(f"Error: Invalid entry!! please enter a valid number in the range of 1 - {get_count(inbox)}")
            # else if number is valid : get mail
            get_email(getmail_index-1)
    # if the user wants to mark an email as spam
    
    elif user_choice == "mark spam":
        # if the inbox is empty
        if len(inbox) == 0:
            print(f"You have no emails")
        else:
            # else provide emails the user can choose from
            print(f"You have {len(inbox)} email(s).")
            getmail_index = int(input(f"\nEnter a number from 1 - {get_count(inbox)} to mark as spam: "))
            # if entry is invalid give an error
            if getmail_index > len(inbox) or getmail_index < 0:
                print(f"Error: Invalid entry!! please enter a valid number in the range of 1 - {get_count(inbox)}")
            # else if entry is valid: mark as spam and retrive it for proof
            add_spam(getmail_index-1)
            get_spam_emails()

    # if the user wants to send an email
    elif user_choice == "send":
        # get email address from user 
        email = input("Enter the recipient email\n(must be a valid email): \n")
        # while the email is invalid keep asking
        while check(email) != True:
            email = input("Enter the recipient email\n(must be a valid email): \n")
        # if email is valid get email body from user
        message = input("Enter email body: \n")
        # while body message is empty keep asking
        while message == "":
            message = input("Email body can not be empty \nEnter email body: \n")
        # else if both message and email are valid send
        add_email(message, email)
        
    # if the user wants to delete a email
    elif user_choice == "delete":
        # if there are no emails
        if len(inbox) == 0:
            print(f"You have no emails")
        else:
            # else get an index from user to use to delete an email
            print(f"You have {len(inbox)} email(s).")
            getmail_index = int(input(f"\nEnter a number from 1 - {get_count(inbox)} to delete: "))
            # if the index is out of bounds
            if getmail_index > len(inbox) or getmail_index < 0:
                print(f"Ooops Invalid entry!! please enter a valid number in the range of 1 - {get_count(inbox)}")
            # else delete email using valid index
            get_remove(getmail_index-1)

    # if the user quits say good bye and exit
    elif user_choice == "quit":
        print("Goodbye")
        break
    # else alet user that the entry is invalid
    else:
        print("Oops - incorrect input")









#================== Creating a new class: ====================
''' Creating a new class called Email.

    setting the constructor to have 4 variables:
    *has_been_read = setting to have a default value of False,
    *is_spam = setting to have a default value of False,
    *from address = setting to have a empty string value
    *email contents = setting to have a empty string value
    
    setting the methods as follows
    *mark_as_read = changing the default value to True, this is when an email has been read
    *mark_as_spam = changing the default value to True, this is when an email has been marked as spam
    *__str__= this returns the string of the objects used in this program, allows for output print
    '''
class Email():
    # Setting users email address
    email = "warrick@gmail.com"
    
    def __init__(self, has_been_read = False, is_spam = False, from_address = "", email_contents = ""):
        
        self.has_been_read = has_been_read
        self.is_spam = is_spam
        self.from_address = from_address 
        self.email_contents = email_contents
        
    def mark_as_read(self):
        self.has_been_read = True 

    def mark_as_spam(self):
        self.is_spam = True

    def __str__(self):
        return f'''\n======= Dragon Corperation Messages: =======
        \rEmail From:  {self.from_address}
        \rMessage:     {self.email_contents}\n'''

# Setting variables needed for menu functions.
# Setting empty lists to use to fill data from functions:
menu_choice = ""
user_email = Email()
user_email_address = user_email.email
spam = []
unread_messages = []

# Setting 'inbox' as a empty list,
# then filling the inbox with data using the class Email to create objects:
inbox = []
inbox.append(Email(False, False, "fred@gmail.com", "hello"))


#================== Creating new functions: ====================
# This function is used in menu option 'send'.
# This allows the user to compose a email which 
# gets stored into the inbox list:
def add_email(address,contents):              
    send = Email("","",address,contents)
    inbox.append(send)

# This counts and prints the total nr of emails within the inbox:
def get_count():
    print(f'''====== My Emails: =====
    \rInbox: [{len(inbox)}]\n''')

# This function to be used in menu option 'read'.
# Defining 3 empty_lists which will be used to show the total nr of 
# emails within each seperate inbox (ie-inbox, unread inbox & spam inbox).
# This function prints out all the emails in the inbox
# and allows user to select which email they would like to read:
# Using exception programming to handle user input errors:
def get_email(inbox):
    my_inbox = len(inbox)
    my_unread = len(unread_messages)
    my_spam = len(spam) 

    if my_unread == 0:
        print(f'''======== My Emails: =========
            \rInbox:       [{my_inbox-my_spam}]
            \rUnread:      [{my_inbox-my_spam}]
            \rSpam emails: [{my_spam}]\n
            \rIndex_Nr:    From Address:''')
    else:
        print(f'''======== My Emails: =========
            \rInbox:       [{my_inbox-my_spam}]
            \rUnread:      [{my_unread-my_spam}]
            \rSpam emails: [{my_spam}]\n
            \rIndex_Nr:    From Address:''')
          
    for index,emails in enumerate(inbox,1):
        print(f'''[{index}]          -{emails.from_address}''')

    try:  
        for emails in inbox:
            user_choice = int(input("\nPlease select index number to view email:\n>"))
            print(inbox[user_choice-1])
            inbox[user_choice-1].mark_as_read()
            break       
    except ValueError:
        print("\nERROR ====> Sorry,you have not entered in a number.\nPlease try again\n")
        get_email(inbox)

# This function allows users to view which emails are in the unread inbox email.
# This function works on a iteration going through entire inbox
# The condition uses method in Class Email to mark the email as True. 
# once the condition is executed the unread mails get appended into 'unread_messages' inbox 
def get_unread_emails(inbox):
    print("\n======== My Unread Emails: =========")
    for index,emails in enumerate(inbox):
        if not emails.has_been_read:
            unread_emails = inbox[index]
            unread_messages.append(unread_emails)
        
            print(f'''From: {unread_emails.from_address}
                    \rMessage:{unread_emails.email_contents}\n''')

# This function prints out all the emails in the inbox.
# It allows the user to select which email they would like to mark as spam
# The condition uses method in class Email to marke the email as True.
# Once the code is executed all the spam emails are appended into 'my_spam' inbox:
# Using exception programming to handle user input errors:
def mark_spam(inbox):
    my_inbox = len(inbox)
    print(f'''======== My Emails: =========
            \rInbox:[{my_inbox}]\n
            \rIndex_Nr:    From Address:''') 

    for index,emails in enumerate(inbox,1):
        print(f'''[{index}]          -{emails.from_address}''')
    try:
        for emails in inbox:
                user_choice = int(input("\nPlease select index number for email to be marked as spam:\n>"))
                
                print(f"\n****The following has been marked as spam:****{inbox[user_choice-1]}\n")
                inbox[user_choice-1].mark_as_spam()
                break
    except ValueError:
        print("\nERROR ====> Sorry,you have not entered in a number.\nPlease try again\n")
        mark_spam(inbox)

# This functions allows the user to view all the spam emails in the spam_inbox.
# The inbox is updated by subtracting the nr of spam messages from inbox:
def get_spam_emails(inbox):
    print("======== My Spam Emails: =========")
    my_inbox = len(inbox)

    for index,emails in enumerate(inbox):
        if emails.is_spam:
            spam_emails = inbox[index]
            spam.append(spam_emails)
            total_spam = len(spam)
            
            print(f'''
            \rInbox:[{my_inbox-total_spam}]
            \rSpam Inbox[{total_spam}]''')

            print(f'''From Address: {spam_emails.from_address}
            \rMessage: {spam_emails.email_contents}\n''')

# This Function prints out all the emails in the inbox.
# The user can then select which email they would like to delete
# by using 'pop' function, it delets the email from the inbox.
# Using exception programming to handle user input errors:
def delete():
    my_inbox = len(inbox)
    print(f'''======== My Emails: =========
            \rInbox:[{my_inbox}]\n
            \rIndex_Nr:    From Address:''') 

    for index,emails in enumerate(inbox,1):
        print(f'''[{index}]          -{emails.from_address}''')
    try:
        for emails in inbox:
                user_choice = int(input("\nPlease select index number for email to be deleted:\n>"))
                print(f"\n****The following has been deleted:****{inbox[user_choice-1]}\n")
                inbox.pop(user_choice-1)
                break
    except ValueError:
        print("\nERROR ====> Sorry,you have not entered in a number.\nPlease try again\n")
        delete()
        
#================== Menu Section: ====================
# Setting menu options for user to chose what to execute.
# Activating defined functions within the options chosen.
# Setting while loop to allow user to return to the main menu after options selected:
while menu_choice != "exit":
    
    menu_choice = input(f'''======== Welcome {user_email_address}! ======
Please select the following options:
Check number of emails       =  (check)
Read you emails              =  (read)
Mark as spam                 =  (spam)
Send an email                =  (send)
Delete                       =  (delete)
Exit                         =  (exit)
>''').lower()

    if menu_choice == "check":
        get_count()

    elif menu_choice == "read":
        get_email(inbox)
        user_choice = input("Do you want to view unread messages (select: 'yes' or 'no')?\n>").lower()
        if user_choice == 'yes':
            get_unread_emails(inbox)
        if user_choice == 'no':
            menu_choice
        
    elif menu_choice == "spam":
        user_choice = input('''\nPlease select following options:
        \rMark email as spam  -  (mark)
        \rView spam inbox     -  (view)\n>''').lower()
        if user_choice == 'view':
            get_spam_emails(inbox)
        if user_choice == 'mark':
            mark_spam(inbox)

    elif menu_choice == "send":
        print("==== Compose your email ====")
        send_to_email = input("to: ")

        if "@" not in send_to_email:
            print("Sorry invalid email address. Please try again\n")
        else:
            menu_choice            

            print("==== Email Contents ====")
            email_contents = input("Message: ")

            add_email(send_to_email,email_contents)
            print("\nThanks email sent!\n")
  
    elif menu_choice == "delete":
        delete()

    elif menu_choice == "exit":
        print("Goodbye")
        exit()
        
    else:
        print("Oops - incorrect input. Please try again:\n")
