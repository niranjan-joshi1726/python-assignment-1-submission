

# FUNCTIONS OF STRING IN PYTHON
# lower() function:
txt="My Name is NIRANJAN "
x=txt.lower()
print(x)

# upper() 

txt="my name is niranjan sharma"
x=txt.upper()
print(x)


# title()
 
 txt="Hello world"
 x=txt.title()
 print(x)


 # replace()

 txt = "I like to eat"

x = txt.replace("eat", "read")

print(x) 


# split()

txt = "welcome to my world"

x = txt.split()

print(x)


#  functions of list objects in python

# 1). clear()

places= ['Bangalore','mumbai','Bihar','Hastinapur']
places.clear()

# 2). copy()

vegetables=['carrot','beetroot','peas']
vegetables.copy()

# 3). remove()
   fruits=['banana','apple', 'avacado']
   fruits.remove("apple")


 # 4). reverse()
  
    places=['Bangalore','patna','mumbai','Maharastra']
    places.reverse()

    # 5). index()

    vegetables=['carrot','beetroot','peas']
    vegetables.index("carrot")


##########  DEFAULT FUNCTIONS OF DICTIONARY

# 1). clear()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car) 

# 2). copy()

shoe = {
   "barnd": "adidas"
    "price": "5000"
    "size":  "7"
}
   x=car.copy()
   print(x)


# 3). pop()
   
   shoe = {
   "barnd": "adidas"
    "price": "5000"
    "size":  "7"
}
   car.pop("price")
   print(shoe)

   # 4). get()

   shoe = {
   "barnd": "adidas"
    "price": "5000"
    "size":  "7"
}
  x= car.get("price")
   print(x)


    

