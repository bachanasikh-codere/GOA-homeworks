<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum perferendis, <b>animi esse</b> accusantium delectus fugit sed autem iusto <mark>dolore</mark> maxime expedita <u>impedit soluta</u> deleniti nulla <i>reiciendis</i> ex dolorum sint. Commodi.</p>
</body>
</html>
 
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 1/18/2026 7:53 PM
home  page
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <center> <!-- ცენტრავს შუაში ელემენტებს -->
        <img src="goa.jpg" alt="Goa logo" width="50">
        <a href="./index.html">Home</a> <!-- ამის დაჭერაზე არაფერი არ მოხდება რადგან ისედაც home page ზე ვართ -->
        <a href="./Contact.html">Contact</a> <!-- ამის დაჭერაზე გადავალთ Contact.html ფეიჯზე -->
        <a href="./AboutUs.html">About us</a> <!-- ამის დაჭერაზე გადავალთ AboutUs.html ფეიჯზე -->
        <a href="./Services.html">Services</a> <!-- ამის დაჭერაზე გადავალთ Services.html ფეიჯზე -->
        <button>Login</button>
        <button>Sign up</button>
    </center><br><br><br>
    <center>
        <p>Lorem ipsum dolor, sit amet <b>consectetur</b> adipisicing elit. Quia accusamus cupiditate assumenda! <mark>Est</mark> porro <br> dolorum nesciunt <i>officia</i> blanditiis quis <u>consequuntur</u>, autem quidem amet iusto nisi eius odio, illo nam officiis?</p>
    </center>
</body>
</html>


Services page
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services</title>
</head>
<body>
    <h1>Services</h1>
    <a href="./index.html"><button>Go back to home page</button></a> <!-- ვბრუნდებით home page ზე -->
</body>
</html>


Contact  page
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact us</title>
</head>
<body>
    <h1>Contact us</h1>
    <a href="./index.html"><button>Go back to the home page</button></a> <!-- ვბრუნდებით home page ზე -->
</body>
</html>
About  us page
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About us</title>
</head>
<body>
    <h1>About us</h1>
    <a href="./index.html"><button>Go back to home page</button></a>  <!-- ვბრუნდებით home page ზე -->
</body>
</html>
 
Home page
Image
Contact  page
Image
About us page
Image
Services page
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 1/25/2026 7:40 PM
#          0         1            2         3        4       5         6
names = ['ana', 'aleksandre', 'giorgi', 'daviti', 'shio', 'cotne', 'barbare']
#         -7         -6          -5        -4       -3      -2         -1
# slicing -> სიიდან ამოვიღებთ რამოდენიმე ელემენტს, და ეგ ამოღებული ელემენტები შეინახება ახალ სიაში

print(names[2:5]) # ['giorgi', 'daviti', 'shio']
print(names[2:5][1]) # 'daviti'

# ამ შემთხვევაში გამოვიტანეთ ელემენტები 2 ინდექსიდან 5 ინდექსამდე, ანუ 5 ინდექსი არ ჩაითვალა
# slicing ყოველთვის ქმნის ახალ სიას, გინდც 1 ელემენტი ამოვჭრათ მხოლოდ, მაინც სიაში შეინახება

sliced_names = names[3:6]
print(sliced_names) # ['daviti', 'shio', 'cotne']
print(sliced_names[2]) # 'cotne'



name = 'aleksandre'
print(name[2:6]) # 'eksa'
ბატონი ლუკა გაბელიაRole icon, Moderator — 2/1/2026 7:46 PM
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/8/2026 7:12 PM
#          0         1            2         3        4       5         6
names = ['ana', 'aleksandre', 'giorgi', 'daviti', 'shio', 'cotne', 'barbare']
#         -7         -6          -5        -4       -3      -2         -1
# slicing -> სიიდან ამოვიღებთ რამოდენიმე ელემენტს, და ეგ ამოღებული ელემენტები შეინახება ახალ სიაში
sliced_names = names[2:] # 2 ინდექსის მერე ყველაფერი
sliced_names1 = names[:5] # 5 ინდექსამდე ყველაფერი
print(sliced_names) # ['giorgi', 'daviti', 'shio', 'cotne', 'barbare']
print(sliced_names1) # ['ana', 'aleksandre', 'giorgi', 'daviti', 'shio']
print(names[-6:-4]) # ['aleksandre', 'giorgi']
print(names[-4:]) # ['daviti', 'shio', 'cotne', 'barbare']
print(names[:-2]) # ['ana', 'aleksandre', 'giorgi', 'daviti', 'shio']
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/8/2026 8:02 PM
# ფუნქცია, არის გამოყენებადი კოდის ბლოკი



# მივიდე კარებთან
# გავაღო კარი
# დავკეტოთ კარი
# მივიდე ონკანთან
# ჭიქა ავიღოთ
# დავისხათ წყალი
# დავლიოთ
# დავდგათ ჭიქა უკან
# მივიდეთ კარებთან
# გავაღოთ კარი
# დავკეტოთ კარი

# რობოტი()  ->   იმისათვის რომ შეასრულოს  ეს  მოქმდებები უნდა დავუძახოთ
# მივიდე კარებთან
# გავაღო კარი
# დავკეტოთ კარი
# მივიდე ონკანთან
# ჭიქა ავიღოთ
# დავისხათ წყალი
# დავლიოთ
# დავდგათ ჭიქა უკან
# მივიდეთ კარებთან
# გავაღოთ კარი
# დავკეტოთ კარი



#  რობოტი()
#  რობოტი()
#  რობოტი()
#  რობოტი()
#  რობოტი()
#  რობოტი()
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/15/2026 7:11 PM
    <a href=""></a>
    <img src="" alt=""  width=""  height="">

    <!--  ატრიბუტები
    href -> უთითებს hyperlinks რა მისამართზე უნდა გადაიყვანოს მომხარებელი მაგის დაჭერაზე
    src -> უთითებს img თეგს ფოტოს მისამართს
    alt ->თითებს ფოტოსთვის    alternative texts  ს ანუ იმ  ტექსტს რომელიც გამოჩნდება მაშინ როცა ფოტო რაიმე მიზეზის გამო არ ან ვერ  ჩაიტვირთა
    width -> უთითებს ფოტოს სიგანეს პიქსელებში
    height  -> უთითებს ფოტოს სიმაღლეს პიქსელებში
    -->
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/15/2026 7:36 PM
<!-- nav თეგი გვეხმარება რომ    ერთ  დაჯგუფებაში შევკრიბოთ ყისეთი თეგები  რომელიც გვეხმარება საიტზე ნავიგაციაში -->
<nav>
    <a href="index1.html">Home</a>
    <a href="index1.html">About us</a>
    <a href="index1.html">Contact us</a>
    <a href="index1.html">Services</a>
</nav>
    <h1>First website</h1>

    <!-- nav თეგი გვეხმარება რომ    ერთ  დაჯგუფებაში შევკრიბოთ ყისეთი თეგები  რომელიც გვეხმარება საიტზე ნავიგაციაში -->
    <nav>
        <ul>
            <li> <a href="index1.html">Home</a></li>
            <li><a href="index1.html">About us</a></li>
            <li> <a href="index1.html">Contact us</a></li>
            <li> <a href="index1.html">Services</a></li>
        </ul>
    </nav>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/15/2026 8:16 PM
<nav>
    <ul>
        <li><a href="index1.html">About us</a></li>
        <li> <a href="#p1">Contact us</a></li>
    </ul>
</nav>

    <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>


<p id="p1">this is paragraph</p>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/15/2026 8:48 PM
<!-- 4) შექმენით 1 ფეიჯიანი nav ul li ა თეგების გამოყენებით, და br თეგებით გააკეთთ პატარა დაშორება თეგებს შორის რომ გააკეთოთთ ნავიგაცია მაგ ერთ ფეიჯზე id ების გამოყენებით -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <nav id="main-nav">
        <ul>
            <li><a href="#main-nav">Navigation</a></li>
            <li><a href="#sec-2">Section 2</a></li>
            <li><a href="#sec-3">Section 3</a></li>
        </ul>
    </nav>

    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

    <h1 id="sec-2">Section 2</h1>

    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

    <h2 id="sec-3">Section 3</h2>
</body>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/22/2026 7:17 PM
# მეთოდი არის ისეთი ფუნქცია რომელიც გამოიყენება მხოლოდ ერთ გარკვეულ მონაცემთა  ტიპთან და სხვა მონაცემთა ტიპს არა
#  string არის immutable ანუ შეუცვლადი, ანუ string ს მეთოს არ შეუძლია შეცვალოს არსებული სტრინგი, იგი მარტო ქმნის ახალ სტრინგს

# .upper() -> გარდაქმნის სტრინგში ყველა ასოს დიდ ასოებად
print("aleksandre".upper()) # "ALEKSANDRE"
name = "aleksandre"

print(name.upper()) # "ALEKSANDRE"
print(name) # "aleksandre"

name_upper = name.upper()
print(name_upper) # "ALEKSANDRE"

name = name.upper()
print(name) # "ALEKSANDRE"
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/22/2026 7:50 PM
# მეთოდი არის ისეთი ფუნქცია რომელიც გამოიყენება მხოლოდ ერთ გარკვეულ მონაცემთა  ტიპთან და სხვა მონაცემთა ტიპს არა


# ამ შემთხვავში, ეს  არის string ფუნქციები, ანუ ამ ფუნქციების  გამოყენება შეგვიძლია მხოლოდ სტრინგებზე  და არაფერ სხვაზე

#  string არის immutable ანუ შეუცვლადი, ანუ string ს მეთოს არ შეუძლია შეცვალოს არსებული სტრინგი, იგი მარტო ქმნის ახალ სტრინგს

# .upper() -> გარდაქმნის სტრინგში ყველა ასოს დიდ ასოებად
print("aleksandre".upper()) # "ALEKSANDRE"
name = "aleksandre"

print(name.upper()) # "ALEKSANDRE"
print(name) # "aleksandre"

name_upper = name.upper()
print(name_upper) # "ALEKSANDRE"

name = name.upper()
print(name) # "ALEKSANDRE"


# .lower() -> სტრინგში ყველა ასოს გარდაქმნის პატარა  ასოებად
name = "ALEKSANDRE"
print(name.lower()) # "aleksandre"


# .capitalize() -> სტრინგში მხოლოდ პირველ ასოს გაადიდებს
name = "aleksandre"
print(name.capitalize()) # "Aleksandre"


# .title() -> სტრინგში ყველა სიტყვის პირველ ასოს გაადიდებს
name = "aleksandre is mentor"
print(name.title()) # "Aleksandre Is Mentor"


# .replace() -> იღებს ორ ცალ არგუმენტს,  სტრინგში პირველი არგუმენტში რაც წერია იმ ასოს ჩაანაცვლებს  მეორე არგუმენტში  მითითებული სტრინგით
name = "bleksbndre"
print(name.replace("b", "a")) # "aleksandre"


# .isupper() -> ამოწმებს სტრინგი დიდი ასოებით თუ წერია,  თუ წერია მაშინ True ს მოგვცემს, თუ არაა False ს მოგვცემს
name = "ALEKSANDRE"

if name.isupper():
    print("string is uppercase")
else:
    print("string is lowercase")

name = "aleksandre"
print(name.isupper()) # False

name = "ALEKSANDRE"
print(name.isupper()) # True


# .islower() -> ამოწმებს სტრინგი პატარა ასოებით თუ წერია,თუ წერია მაშინ True ს მოგვცემს, თუ არაა False ს მოგვცემს
name = "aleksandre"

if name.islower():
    print("string is lowercase")
else:
    print("string is uppercase")

name = "aleksandre"
print(name.islower()) # True

name = "ALEKSANDRE"
print(name.islower()) # False

# .find() -> არგუმენტად რა ასოსაც  გადავცემთ, იმ ასოს ინდექსს მოგვცემს სტრინგში
name = "abcdefgh"
print(name.find("b")) # 1
print(name.find("f")) # 5
print(name.find("j")) # -1 (ანუ ვერ მოიძებნა)

print(name[name.find("h")]) # "h"
index = name.find("f")
print(name[index])


# .count() -> არგუმენტად რასაც გადავცემთ, იმის რაოდენობას მოგვცემს სტრინგში ან სიაში
name = "aleksandre"
print(name.count("a")) # 2
print(name.count("k")) # 1

arr = [1, 2, 3, 4, 5, 5, 5]
print(arr.count(5)) # 3


# .strip() -> აშორებს სტრინგს ზედმეტტ დაშორებებს ბოლოდან და დასაწყისში
name = "          aleksandre dzukaevi                "
print(name.strip()) # "aleksandre dzukaev"


# .lstrip() -> აშორებს სტრინგს ზედმეტ  დაშორებებს დასაწყისში
name = "          aleksandre dzukaevi                "
print(name.lstrip()) # "aleksandre dzukaevi                "


# .rstrip() -> აშორებს სტრინგს ზედმეტ დაშორებებს ბოლოდან
name = "          aleksandre dzukaevi                "
print(name.rstrip()) # "          aleksandre dzukaevi"
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 2/22/2026 8:51 PM
# 1) მომხარებელს შემოატანინე სტრინგი. გადაიყვანე ყველა ასო დიდ ასოებად და დაბეჭდე.
text = input("Enter some text: ")
print(text.upper())

# 2) მომხარებელს შემოატანინე სტრინგი. გადაიყვანე ყველა ასო პატარა ასოებად.
text = input("Enter some text: ")
print(text.lower())

# 3) მომხარებელს შემოატანინე სტრინგი და პირველი ასო დიდად გადააქციე.
text = input("Enter some text: ")
print(text.capitalize())

# 4) მომხარებელს შემოატანინე სტრინგი. ყველა სიტყვის პირველი ასო გაადიდე.
text = input("Enter some text: ")
print(text.title())

# 5) მომხარებელს შემოატანინე სტრინგი. შეცვალე ყველა "a" სიმბოლო "o"-თი.
text = input("Enter some text: ")
print(text.replace("a", "o"))

# 6) მომხარებელს შემოატანინე სტრინგი. შეამოწმე — სულ დიდი ასოებით არის თუ არა. თუ არის დაპრინტე "string is uppercase", სხვა შემთხვევაში "string is lowercase"
text = input("Enter some text: ")
if text.isupper():
    print("string is uppercase")
else:
    print("string is lowercase")

# 7) მომხარებელს შემოატანინე სტრინგი. შეამოწმე — სულ პატარა ასოებით არის თუ არა. თუ არის დაპრინტე "string is lowercase", სხვა შემთხვევაში "string is uppercase"
text = input("Enter some text: ")
if text.islower():
    print("string is lowercase")
else:
    print("string is uppercase")

# 8) მომხარებელს შემოატანინე ერთი სტრინგი და შემდგომ ერთი ცალი ასო. იპოვე პირველ სტრინგში ამ მეორე ასოს ინდექსი.
text = input("Enter some text: ")
letter = input("Enter some letter: ")
print(text.find(letter))

# 9) მომხარებელს შემოატანინე ერთი სტრინგი და შემდგომ ერთი ცალი ასო. დაითვალე რამდენჯერ გვხვდება ეს მეორე ასო სტრინგში.
text = input("Enter some text: ")
letter = input("Enter some letter: ")
print(text.count(letter))

# 10) მომხმარებელს შეაყვანინე წინადადება და წაშალე ზედმეტი space-ები თავიდან და ბოლოდან.
text = input("Enter some text: ")
print(text.strip())

# 11) მომხარებელს შემოატანინე სტრინგი. მოაშორე მხოლოდ მარცხენა მხრიდ white space-ები.
text = input("Enter some text: ")
print(text.lstrip())

# 12) მომხარებელს შემოატანინე სტრინგი. წაშალე მხოლოდ მარჯვენა მხრიდან space-ები.
text = input("Enter some text: ")
print(text.rstrip())

# 13) მოძებნე ასო სტრინგში და დაბეჭდე ის ასო მისი ინდექსის გამოყენებით.
text = input("Enter some text: ")
letter = input("Enter some letter: ")
index = text.find(letter)
print(text[index])
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/1/2026 8:26 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- form თეგი გამოიყენება სარეგიტრაციო ფორმის შესაქმნელად, ანუ ყველა ისეთი ელემენტის დასაჯგუფებლად რომელიც რეგისტრაციისთვის გამოიყენება -->

    <!-- input თეგი, empty თეგია ანუ არააქ დამხურავი თეგუ -->
    <!-- type -> ტიპი, გვეხმარება იმაში რომ მივუთითთო input ს რა ტიპისაა იგ -->



    <!-- type="email" -> უთითებს ინფუთს რომ აქ უნდა ჩაიწეროს ელფოსტა -->
    <!-- type="password" -> უთითებს ინფუთს რომ აქ უნდა ჩაიწეროს პაროლი -->
    <!-- type="submit" -> უთითებს რომ ეს ინფუთი/ღილაკი უნდა იღოს დასადასტურებელი ღილაკი -->
    <!-- type="text" -> უთითებს ინფუთს რომ აქ უნდა ჩაიწეროს რაიმე ტექსტი, მაგალითად სახელი და გვარი, nickname, წერილი და ა.შ-->
    
    <!-- placeholder -> გვეხმარება მივუთითოთ input ს მიმანიშნებელი ტექსტი მომხარებლისთვის -->

    <!-- label არის container თეგი, რომელიც გვეხმარება რომ მივუთითოთ მომხარებელს ქვემოთ მოცემულ ინფუთში რა უნდა ჩაწეროს -->
    <!-- for="" გვეხმარება რომ დავაკავშიროთ label და input ერთმანეთთან, id ის საშუალებით-->
    <center>
        <h1>Registration form</h1>
        <form>
            <label for="username">Enter your name</label><br>
            <input type="text" id="username" placeholder="username"><br><br>

            <label for="usersurname">Enter your surname</label><br>
            <input type="text" id="usersurname" placeholder="usersurname"><br><br>

            <label for="useremail">Enter your email</label><br>
            <input type="email" id="useremail" placeholder="useremail"><br><br>

            <label for="userpass">Enter your password</label><br>
            <input type="password" id="userpass" placeholder="userpass"><br><br>


            <input type="submit"> <!-- აქ შეგვეძლო ჩაგვესვა <button type="submit">Submit</button> -->
        </form>
    </center>
</body>
</html>
ბატონი ლუკა გაბელიაRole icon, Moderator — 3/8/2026 8:25 PM
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/15/2026 7:34 PM
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/15/2026 7:44 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <!-- მონაცემთა ბაზები და სერვერები -->

    <!-- maxlength -> მაქსიმალური character ების რაოდენობას უწერს ინფუთს -->
    <!-- minlength -> მინიმალურ character ების რაოდენობას უწერს ინფუთს-->
    <!-- name -> ანიშნებს სერვერს რომელ column შ გადააგზავნოს ეს კონკრეტული ინფუთ, ჯერჯერობიუთ უბრალოთ კარგი პრაქტიკის სახით გაუწერეთ ინფუთებს -->
    <!-- reqiured -> ხდის ინფუთის შევსებას აუცილებელს-->
    
    <center>
        <h1>Registration form</h1>
        <form>
            <label for="username">Enter your name</label><br>
            <input type="text" id="username" placeholder="username" name="username" maxlength="24" minlength="3" required><br><br>

            <label for="usersurname">Enter your surname</label><br>
            <input type="text" id="usersurname" placeholder="usersurname" name="surname" maxlength="14" minlength="4" required><br><br>

            <label for="useremail">Enter your email</label><br>
            <input type="email" id="useremail" placeholder="useremail" name="email" required><br><br>

            <label for="userpass">Enter your password</label><br>
            <input type="password" id="userpass" placeholder="userpass" name="password" required><br><br>

            <label for="female">Female</label>
            <input type="radio" name="gender" id="female" required>
            <br>
            <label for="male">Male</label>
            <input type="radio" name="gender" id="male" required><br><br>

            <input type="submit"> <!-- აქ შეგვეძლო ჩაგვესვა <button type="submit">Submit</button> -->
        </form>
    </center>
</body>
</html>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/29/2026 7:14 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- value ში ვუთითებთ რა ინფორმაცია გაიგზავნოს ამ option ის არჩევისას -->
    <!-- selected ეუბნეება საიტს რომ ეს option უნდა იყოს არჩეული default ად -->
    <form>
        <label for="country">Select country:</label>
        <select id="country">
            <option value="GE">Georgia</option>
            <option value="TU">Turkey</option>
            <option value="GER" selected>Germany</option>
        </select>
        <input type="submit">
    </form>
</body>
</html>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/29/2026 7:28 PM
https://en1.savefrom.net/16xF/
Free Online Video Downloader - SaveFrom.net
Download videos from popular platforms with SaveFrom.net, the leading free online video downloader. Easily save videos in various formats and resolutions. Start downloading now!
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/29/2026 7:45 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- controls -> ამაატებს ვიდეოს სამართო ღილაკებს და ვეელებს ( გადიდება, ხმის აწევა, ხმის ჩაწევა, გადახვეევა და ა.შ) -->
    <!-- autoplay -> როცა საიტი ჩაიტვირთება ვიდეო ავტომატურად ჩაირთვება -->
    <!-- loop -> როცა ვიდეო დამთავრდება ახლიდან დაიწყება -->
    <!-- muted -> როცა საიტი ჩაიტვირთება, ვიდეო იქნება დამიუძთებული   -->
    <center>
        <video src="GOA - მატრიციდან გაქცევა.mp4" controls autoplay loop muted></video>
    </center>
</body>
</html>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/29/2026 8:29 PM
https://ytmp3.sc/
YTMP3 - Free YouTube to MP3 Converter
Download your YouTube videos as MP3 or MP4 files for free with one of the fastest and most powerful YouTube to MP3 converters available.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- controls -> ამაატებს ვიდეოს სამართო ღილაკებს და ვეელებს ( გადიდება, ხმის აწევა, ხმის ჩაწევა, გადახვეევა და ა.შ) -->
    <!-- autoplay -> როცა საიტი ჩაიტვირთება ვიდეო ავტომატურად ჩაირთვება -->
    <!-- loop -> როცა ვიდეო დამთავრდება ახლიდან დაიწყება -->
    <!-- muted -> როცა საიტი ჩაიტვირთება, ვიდეო იქნება დამიუძთებული   -->
    <center>
        <video src="GOA - მატრიციდან გაქცევა.mp4" controls autoplay loop muted></video>
    </center>

    <!-- controls ატრიბუტი აქ არის აუცილებელი რომ გამოჩნდეს აუდიო -->
    <!-- autoplay -> როცა საიტი ჩაიტვირთება აუდიო ავტომატურად ჩაირთვება -->
    <!-- loop -> როცა აუდიო დამთავრდება ახლიდან დაიწყება -->
    <!-- muted -> როცა საიტი ჩაიტვირთება, აუდიო იქნება დამიუძთებული   -->
    <center>
        <audio src="Harry Potter and the Philosopher's Stone  Official Teaser  HBO Max.mp3" controls autoplay loop muted></audio>
    </center>
</body>
</html>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 3/29/2026 8:36 PM
ზარმაცებისთვის:
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 4/5/2026 7:16 PM
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 4/5/2026 8:40 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header>
        <center>
            <h1>Goal Oriented Academy</h1>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About us</a></li>
                    <li><a href="#">Services</a></li>
                </ul>
            </nav>
            <button>Login</button>
            <button>Sign up</button>
        </center>
    </header>

    <main>
        <center>
            <h2>Goal Orinted Academy - > მიზნებზე ორინეტირებული აკადემია</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet laborum, dolorem illo minima deserunt porro maxime officiis animi alias voluptatem, magni laboriosam explicabo quia fugit magnam eum totam. Omnis, voluptatibus?</p>
            <video src="GOA - მატრიციდან გაქცევა.mp4" controls></video>
            <img src="image.png" alt="GOA">
        </center>
    </main>

    <footer>
        <center>
            <h3>whatsapp: +995592436651</h3>
            <h3>viber: +99556767612</h3>
            <h3>linkedin: +9955445624</h3>

            <br>

            <h3>facebook: <a href="https://www.facebook.com/search/top?q=goal-oriented%20academy%20%E2%80%A2%20goa">fb</a></h3>
            <h3>Instagram: <a href="#">INSTA</a></h3>
            <h3>TikTok: <a href="#">TT</a></h3>
        </center>
    </footer>
</body>
</html>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 4/24/2026 7:31 PM
<!-- article -> თეგი რომელიც გამოიყენება იმისათვის რომ ისეთი ელემენტები ჩავსვათ ერთ თეგში რომლებიც დამოუკიდებლად შეუძლიათ რომ რაღაც მნიშვნელობა ქონდეთ სხვა თეგებისგან განცალკევებით -->
    <!-- aside -> თეგი რომელიც გამოიყენება იმისათვის რომ რაღაც დამატებითი მოერეხარისხოვან ინფორმაციასთან დაკავშირებული თეგები ერთ თეგში მოვათავსოთ მაგ: 
    რეკლამა
    სხვა თემათიკასთან დაკავშირებული hyperlink ები
    საინტერესო ფაქტები საიტის შესახებ
    sidebar
    -->
    <!-- section -> თეგი რომელიც გამოიყენება იმისათვის რომ ერთ თემატიკასთან დაკავშირებული თეგები ჩავსვათ ერთ თეგში -->
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 4/24/2026 7:40 PM
<header>
       <center>
            <h1>Goal Oriented Academy</h1>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About us</a></li>
                    <li><a href="#">Services</a></li>
                </ul>
            </nav>
            <button>Login</button>
            <button>Sign up</button>
        </center>
</header>
<main>
        <center>
            <section>
                <article>
                    <h2>Goal Orinted Academy - > მიზნებზე ორინეტირებული აკადემია</h2>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet laborum, dolorem illo minima deserunt porro maxime officiis animi alias voluptatem, magni laboriosam explicabo quia fugit magnam eum totam. Omnis, voluptatibus?</p>
                    
                </article>
                <video src="GOA - მატრიციდან გაქცევა.mp4" controls></video>
                <img src="image.png" alt="GOA">
            </section>
            <aside>
                <h3>სხვა კურსები</h3>
                <ul>
                    <li>გრაფიკული დიზაინი</li>
                    <li>game development</li>
                    <li>კიბერუსაფრთხოება</li>
                    <li>რობოტიკა</li>
                    <li>SQL (postgreSQL)</li>
                    <li>ალგორითმები & მონაცემთა სტრუქტურები</li>
                </ul>
            </aside>
        </center>
</main>
<footer>
        <center>
            <section>
                <h3>whatsapp: +995592436651</h3>
                <h3>viber: +99556767612</h3>
                <h3>linkedin: +9955445624</h3>
            </section>
            <br>
            <section>
                <h3>facebook: <a href="https://www.facebook.com/search/top?q=goal-oriented%20academy%20%E2%80%A2%20goa">fb</a></h3>
                <h3>Instagram: <a href="#">INSTA</a></h3>
                <h3>TikTok: <a href="#">TT</a></h3>
            </section>
        </center>
</footer>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 4/24/2026 8:34 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <!-- block element -> ისეთი ელემენტები რომლებიც იკავებენ მათ მყოფ ხაზზეე აბსოლიტურად მთლიან ხაზზ ბოლომდე, ანუ სიგანეში თავიდან ბოლომდე იკავებენ ადგილს გინდც მაგდენი ტექსტიც არ ეწეროს შიგ, ამიტომ ყველა block ელემენტი ყოველთვუს ახალი ხაზიდან იწყება -->
    <p>Hello World!</p>
    <p>Hello World!</p>
    <p>Hello World!</p>
    <p>Hello World!</p>
    <p>Hello World!</p>

    <h1>Heading</h2>
    <h2>Heading</h3>
    <h3>Heading</h1>
    <h4>Heading</h4>
    <h5>Heading</h5>
    <h6>Heading</h6>


    <!-- inline element -> ისეთი ელემენტები რომლებიც იკავებენ მხოლოდ თავისთვის საჭირო ადგილს, ანუ არც მეტს და არც ნაკლებს ამიტომ ახალი ხაზიდან არასოდეს არ იწყება, ყველა inline element ერთ ხაზზე არის ჩამოწიკწიკებული -->
    <button>Inline Button</button>
    <button>Inline Button</button>
    <button>Inline Button</button>
    <button>Inline Button</button>
    <button>Inline Button</button>
    <button>Inline Button</button>
    <audio src="Harry Potter and the Philosopher's Stone  Official Teaser  HBO Max.mp3" controls></audio>
    <audio src="Harry Potter and the Philosopher's Stone  Official Teaser  HBO Max.mp3" controls></audio>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>
</body>
</html>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 5/3/2026 7:25 PM
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 5/3/2026 8:51 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header>
        <nav>
            <div>
                <img src="image.png" alt="">
                <h1>Sololearn</h1>
            </div>
            <ul>
                <li><a href="/learn">Learn</a></li>
                <li><a href="/leaderboard">Leaderboard</a></li>
                <li><a href="/codebits">Code Bits</a></li>
                <li><a href="/discuss">Discuss</a></li>
                <li><a href="/blog">Blog</a></li>
            </ul>
        </nav>
        <div>
            <section>
                <ul>
                    <li>0</li>
                    <li>5</li>
                    <li>182</li>
                </ul>
                <button>Go PRO</button>
            </section>
        </div>
    </header>
    <main>
        <div>
            <h2>Introduction to HTML</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi optio totam, qui, reprehenderit doloremque quasi nobis delectus quia est eos incidunt enim nesciunt. Suscipit pariatur est excepturi quasi vero corrupti?</p>
        </div>
        <section>
            <h2>Getting Started with HTML</h2>
            <div>
                <div>
                    <h5>Lesson</h5>
                    <h2>The Core Web Techonoly</h2>
                </div>
                <div>
                    <h5>Lesson</h5>
                    <h2>HTML Code</h2>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
ბატონი ლუკა გაბელიაRole icon, Moderator — 5/10/2026 7:59 PM
Image
<html>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- table -  მთავარი ჩონჩხი -->
    <!-- th(Table Header) -  ჩვენი ცხრილის სათაური  -->
    <!-- tr(Table Row) -  მწკრივი რომელის დახამრებითაც ჩვენ შეგვიძლია შევქმნათ რამოდენიმე განტყოფილება ინფორმაცის დასაწერად -->
    <!-- td(Table Data) - ინფორმაცის დასაწერი მასალა -->
</head>

<body>

    <table border="30">
        <tr>

            <th><a href="https://www.realmadrid.com/en-US">Real Madrid</a></th>
            <th>Liverpool</th>
            <th>Manchester United</th>
            <th>Atletico</th>
            <th>Arsenal</th>
            <th>PSG</th>
            <th>Sporting</th>
        </tr>

        <tr>
            <td>15</td>
            <td>6</td>
            <td>3</td>
            <th>0</th>
            <th>0</th>
            <th>1</th>
            <th>0</th>
        </tr>

        <tr>
            <td>Ronaldo</td>
            <td>Salah</td>
            <td>Ronaldo</td>
            <td>Grizman</td>
            <td>Henry</td>
            <td>Ronaldinho</td>
            <td>Ronaldo</td>
        </tr>
    </table>

</body>

</html>
Image
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 5/17/2026 7:50 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="background-color: darkorchid;">
    <!-- inline css, internal css, external css -->
    
    
    
    <!-- inline css -->
    <!-- style ატრიბუტი არის ატრიბუტი სადაც ვუთითებთ თეგის დიზიანის შესახებ ინფორმაციას -->


    <!-- syntax -->
    <!-- property: value; property1: value; property2: value; -->

    <!-- properties -->

    <!-- color -> ანიჭებს ტექსტს ფერს-->
    <!-- value დ უნდა მივანიჭოთ რაიმე ფერი -->

    <!-- background-color -> ანიჭებს უკანა ფონის ფერს -->
    <!-- value დ უნდა მივანიჭოთ რაიმე ფერი -->

    <!-- font-size -> ანიჭებს ტექსტს ზომას -->
    <!-- value დ უნდა მივანიჭოთ რაიმე ტექსტის ზომა პიქსელებში -->

    <!-- text-align -> ანიჭებს ტექსტს განლაგებას -->
    <!-- value დ უნდა მივანიჭოთ სად განლაგდეს ტექსტი  (left, center, right) -->


    <h1 style="background-color: blue; color: red;">Hello World!</h1>
    <p style="color: blue; background-color: lime;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea quia libero eveniet. Cumque natus consequatur alias. Cumque recusandae sapiente impedit sunt nobis blanditiis illum. Architecto aut ad quam velit accusantium?</p>
    <button style="color: orange; background-color: aqua;">Click me!</button>


</body>
</html>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 5/24/2026 7:27 PM
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {
            background-color: darkorchid;
            color: red;
            text-align: left;
            font-size: 30px;
        }


        p {
            color: blue;
            background-color: chartreuse;
            text-align: center;
            font-size: 25px;
        }

        button {
            background-color: aqua;
            color: chocolate;
            text-align: right;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <!-- inline css, internal css, external css -->
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <h1>Hello World!</h1>
    <!-- internal css, external css -> გვიწევს რომ მივუთითოთ რომელ თეგს ვუწერთ ამ სტილებს -->


    <!-- 
    tag_name {
        background-color: darkorchid;
        color: red;
        text-align: left;
        font-size: 30px;
    }
    
    -->

    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea quia libero eveniet. Cumque natus consequatur alias. Cumque recusandae sapiente impedit sunt nobis blanditiis illum. Architecto aut ad quam velit accusantium?</p>
    <button>Click me!</button>


</body>
</html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- იმისათვის რომ დავაკავშიროთ html და css ფაილი ერთმანეთთან, უნდა გამოვიყენოთ link თეგი რომლეიც აუცილებლად უნდა იყოს head თეგში -->
    <link rel="stylesheet" href="style.css">
</head>
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 6/14/2026 7:49 PM
h1 {
    background-color: darkorchid;
    color: red;
    text-align: left;
    font-size: 30px;
    border: 5px ridge green;
}

/* border -> ანიჭებს ტექსტს ჩარჩოს, პირველი გადაეცემა ბორდერის ზომა, მოერე გადაეცემა ბორდერის სახეობა, მესამე გადაეცემა ბორდერის ფერ */

p {
    color: blue;
    background-color: chartreuse;
    text-align: center;
    font-size: 25px;
    border: 5px ridge green;
}

button {
    background-color: aqua;
    color: chocolate;
    text-align: right;
    font-size: 20px;
    border: 5px ridge green;
}
<link rel="stylesheet" href="style.css">
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 6/28/2026 7:31 PM
Image
Image
ბატონი ლუკა გაბელიაRole icon, Moderator — 7/12/2026 8:27 PM
/* id , class */
/* hex , rgb */

/* class - დაჯგუფება რაღაცის */
/* id - individual - ყველასგან განსხვავებული */

.red{
    color: red;
}
#h1d2{
    color: blue;
}
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 7/19/2026 7:26 PM
body {
    height: 100vh;
}

#parent {
    width: 50%;
    height: 50%;
    background-color: red;
}


/* % -> საზომი ერთეული რომელიბც მშობელი ელემენტისგან აიღებს პროცენტულ ზომას */
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 7/23/2026 3:33 PM
/* text-decoration -> გვეხმარება იმაში რომ ტექსტს გავუსვათ ხაზი ან ზემოდან, ან შუაში, ან ქვემოდან, ასევე გვეხმარება მაგ ხაზის ზომის კონტროლში, ფერის კონტროლში, და სტილის კონტროლში, უნდა მივუთითოთ 3 value */
/* სად გაესვას ხაზი */
    /* underline -> გაესვას ხაზი ქვემოდან */
    /* line-through -> გაესვას ხაზი შუაში ტექსტის */
    /* overline -> გაესვას ხაზი ზემოდან */

/* როგორი ხაზი გაესვას ( სტილი ) */
    /* dotted -> წერტილოვანი ხაზი */
    /* wavy -> ტალღოვანი ხაზი */
    /* dashed -> წყვეტილოვანი ხაზი */
    /* solid -> ჩვეულებრივი ხაზი */
    /* ... მეტი */

/* რა ფერის ხაზი გაესვას  */
    /* ნებისმიერი ფერი, შეგვიძლია გამოვიყენოთ rgb ან hex */
/* (არა აუცილებელი) ხაზის ზომა ნებისმიერ საზომ ერთეულში */

h1 {
    text-decoration: underline solid blue;
}

h2 {
    text-decoration: line-through dotted red 20px;
}

h3  {
    text-decoration: overline wavy rgb(0, 255, 0);
}
ბატონი ალექსანდრე ძუკაევიRole icon, Mentor's Assistant ანალიტიკოსი — 7/23/2026 4:26 PM
/* text-transform */
    /* uppercase -> ყველა ასო დიდ ასოდ რომ გადაიქცეს */
    /* lowercase -> ყველა ასო დიდ პატარა რომ გადაიქცეს */
    /* capitalize -> ყველა სიტყვის პირველ ასოს ადიდებს */

h1 {
    text-decoration: underline solid blue;
    text-transform: uppercase;
}

h2 {
    text-decoration: line-through dotted red 2px;
    text-transform: lowercase;
}

h3  {
    text-decoration: overline wavy rgb(0, 255, 0);
    text-transform: capitalize;
}
ბატონი შიო ლაბაძეRole icon, Moderator — 7/26/2026 7:32 PM
Image
https://fonts.google.com/
Google Fonts
Browse Fonts - Google Fonts
Making the web more beautiful, fast, and open through great typography
Browse Fonts - Google Fonts
ბატონი შიო ლაბაძეRole icon, Moderator — 7/26/2026 8:28 PM
button{
    width: 100px;
    height: 30px;
    border: 2px solid red;
    background-color: orange;
}

button:hover{
    background-color: blue;
}


button:active{
    background-color: red;
}


a:link{
    color: rgb(0, 0, 255);
}
/*
pseudo selectors


item:hover ამის დახმარებით item-ზე მაუსის გადატარებისას შეიცვლება სტილები

item:active ამის დახმარებით itme-ზე დაჭერისას (რამდენი ხანიც გეჭირება) შეიცვლება სტილები

item:link ამის დახმარებით ჩვენ შეგვიძლია შევცვლოთ ისეთი ლინკები რომელიც მომხარებელი ჯერ არ წვეულა

*/