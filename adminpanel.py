import time
Admin = int(input("Admin Password: "))
#
  
if Admin == 6121:
  print("Access Granted!")

else:
  print("The Password Does Not Match Our System Please contact fakepanel@panel.com for More Info")
  
if Admin == 6121:
  time.sleep(3)
  print("WELCOME TO N&N ADMIN PANEL")
Network = str(input("Which Port You Would Like to Moderate: "))

if Network in ['91231', '51542', '61351', '59581','12345', '67890', '54321', '98765', '24680', '13579', '86420', '98713', '45678', '32109', '65432', '87654', '23456', '78901', '54321', '12345', '67890', '54321', '98765', '24680', '13579', '86420', '11111', '99999', '44444']:
  print("Conneting to", Network)
time.sleep(0.9)
print("Succesfully Connected to", Network)

new_password = input("Would you like to change the password of " + Network + " Y/N: " )
if new_password == "Y":
  
  time.sleep(1.5)
  print("Enter New Password: ")
  
  print(f"Port for {Network} has been changed to {new_password}, If The Customer Of {Network} Asked For This Kindly deliver the new Port To them!")
  time.sleep(1)
else:
  time.sleep(5)
  print("ADMIN PANEL TIMEOUT PLEASE RESTART PROGRAM!")