#The problem
#This is your first interactive programming task, so let's have some fun with the user! You want to write a program that automatically combines two names given by the user. 
#That's an open-ended problem statement, so let's add a few more details and restrictions:
#Tell the user to give you two names in the format: FIRST LAST
#Show the user two possible new names in the format:FIRST LAST.
#The new first name is a combination of the first names given by the user, and the new last name is a combination of the last names given by the user. 
#For example, if the user gives you Alice Cat and Bob, a possible mashup is Bolice Dot.

user_first=input("Give two names: ") #ask the user to give two names
answer1=user_first.upper() #make the answer uppercase
print(answer1)


user_second=input("Give again two names: ") #ask the user to give two names
answer2=user_second.upper() #make the answer uppercase
print(answer2)

split_index_1=answer1.find(" ")
split_index_2=answer2.find(" ")

print(split_index_1) #finds the index of the space

#split the first names and the last names
firstname1=answer1[0:split_index_1]
print(firstname1)
firstname2=answer2[0:split_index_2]
print(firstname2)

#Tuka asked me to simplify from line 29 to line 39
lastname1=answer1[split_index_1+1:len(answer1)]
print(lastname1)
lastname1a=answer1[len(answer1)-1:split_index_1]
print(lastname1a)

lastname2=answer2[split_index_2+1:len(answer2)]
print(lastname2)

#split letters and combine them first name 1 and first name 2
sub_string_first_name_1=firstname1[0:1]
sub_string_first_name_2=firstname2[0:1]

print(firstname1.replace(sub_string_first_name_1,sub_string_first_name_2))
print(firstname2.replace(sub_string_first_name_2,sub_string_first_name_1))

#split letters and combine them last name 1 and last name 2
sub_string_last_name_1=last_name_1[len(last_name_1)-1:len(last_name_1)-2:-1]
sub_string_last_name_2=last_name_2[len(last_name_1)-1:len(last_name_1)-2:-1]

print(lastname1.replace(sub_string_last_name_1,sub_string_last_name_2))
print(lastname2.replace(sub_string_last_name_2,sub_string_last_name_1))