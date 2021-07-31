while(True):
	print("INDIAN RAILWAY WELCOMES YOU\n")
	print("1 . Book your ticket")
	print("2 . Check PNR status")
	ch1=int(input("\nEnter your choice : "))
	if(ch1==1):
		start=input("Choose you station : ")
		end=input("To where : ")
		n=int(input("Enter no. of passengers : "))
		for i in range(1,n+1):
			name=input("Name : ")
			age=input("Age : ")
		print("The amount is : 500")
	ending=input("Do you want to book another ticket? <y/n>")
	if(ending=='n'):
		print("Your ticket has been booked successfully")
		break
