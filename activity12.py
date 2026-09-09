import getpass

username = 'bautistapogi'
password = 'boyishmewing'

u = input('Input Username ---> ')
p = getpass.getpass('Input Password ---> ')

if username == u and p == password : 			
	print("ACCESS GRANTED")
else: 
	print("ACCESS DENIED")