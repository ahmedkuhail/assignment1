# Question 1 
coffee = 25 
cake = 40
water = 10

total_bill = (coffee * 2) + (cake * 1)+ ( water * 3)
print (total_bill   )

print(total_bill > 100 )
print(total_bill == 120)

coffee += 5
print(coffee)

# Question 2  ----------------------------------------------------------------------------------------------------- 
points = 40

points += 20 
points -=10
points *=2
vip_customer = points >=100


total_bill = 125 # any amount to count free delivery  
free_delivery = total_bill >150 or vip_customer  
print (points)
print(vip_customer)
print(free_delivery)
#Question 3 ----------------------------------------------------------------------------------------------------------
result = 10+5*2
print(result)
result2 = (10+5)*2
print(result2)

print (True or False and False)   #   ((and) excuted before or)  # false and false  is false ( then true or false == true )
print ( (True or False ) and False)# in the brackets first  --> true  (then true and false  == ) 

total_bill = 120 
points =20
premuim_member = True

print (total_bill>150 and points >50 or premuim_member)
print ( total_bill > 150 and (points>50 or premuim_member))

 