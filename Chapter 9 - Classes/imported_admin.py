# Imported Admin: Start with your work from Exercise 9-8 (page 178).
# Store the classes User, Privileges, and Admin in one module. Create a
# separate file, make an Admin instance, and call show_privileges() to
# show that everything is working correctly.

import users
import privileges

user_01 = users.User('marie', 'curie')
user_01.describe_user()

admin = privileges.Privileges('roald', 'dahl')
admin.describe_user()
admin.display_rights()