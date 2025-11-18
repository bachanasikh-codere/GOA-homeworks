
#1)ჩამოწერეთ შედარების ოპერატორები
#2)შექმენით 2 ცვლადი და შემდეგ შეადრეთ ერთმანეთზე
#3)ჩამოწერე ყველა შედარების ოპერატორი მაგალით
#4)შექმენით 2 ცვლადი სადაც შეეკითხებოდით რენდომ რიცხვებს,შემდეგ კი შეადარებთ ერთმანეთს
#5)უყურე ჩანაწერს თავიდან


#   პასუხები:

# 1)  
# if <პირობა>  : ...  else :  ... 

# 2)
x=2
a=3

if x > a :
    print( str(x) + " მეტია " + str(a) + "-ზე")
elif  x == a :
    print( str(x) + " ტოლია " + str(a))
else:
    print( str(a) + " მეტია " + str(x) + "-ზე")
        
 # 3) 
asaki = 17

if asaki > 18 :
    print("სტუდენტია")
elif  asaki >= 6 :
    print("მოსწავლეა")
elif  asaki >= 3 :
    print("ბაღელია")
else  :
 print("პატარაა")
    
#4)
user_year1 = int(input("დაწერე რაიმე რიცხვი"))
user_year2 = int(input("კიდევ დაწერე რაიმე სხვა რიცხვი"))
 
if user_year1 > user_year2 :
    print( str(user_year1) + " მეტია " + str(user_year2) + "-ზე") 
elif user_year1 == user_year2 :
 print( str(user_year2) + " ტოლია " + str(user_year1))
else :
    print( str(user_year2) + " მეტია " + str(user_year1) + "-ზე")
