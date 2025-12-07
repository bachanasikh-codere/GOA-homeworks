#1) მომხარებელს შემოატანინე რიცხვი, და შემდეგ შეამოწმე რომ ეს რიცხვი იყოს მეტი 15 ზე და მაგ რიცხვს გამოკლებული 5 იყოს მეტი 12 ზე


user_year1 = int(input("დაწერე რაიმე რიცხვი"))
if user_year1 > 15 :
        print( str(user_year1) + " მეტია " + str(15) + "-ზე")
elif  user_year1 == 15 :
    print( str(user_year1) + " ტოლია " + str(15))
else:
    print( str(15) + " მეტია " + str(user_year1) + "-ზე")
    print(user_year1+16)
    print(user_year1+5)
   
if user_year1 > 12 :
     print( str(user_year1) + " მეტია " + str(12) + "-ზე")
else : 
    print((str(user_year1) + "9"))

    #2) მომხარებელს შემოტანინეთ სახელი და ერთი რიცხვი, და შეამოწმეთ რომ ეს სახელი უდრიდეს "ana" ს და  რიცხვი იყოს 50 ის 
    user_year2=int(input("დაწერე შენი წლოვანება"))
    user_name3=(input("დაწერე შენი სახელი"))
   
    
if user_year2 == 50 :
    print( str(user_year2) + " ტოლია " + str(50))
else :
     print("არ უდრის 50-ს")


if user_name3 == "ana" :
    print( "შენი სახელია ანა")
else :
     print("შენ არ გქვია ანა, შენ გქვია" + user_name3)


#ჩუმთ რატომ ხარ