'''
singer_list = ["아넌딜라이트","케이셉"]
print(type(singer_list))

print (singer_list[0])

singer_list.append("포이즌")
print (singer_list)

singer_list.insert(0,"푸바오")
print (singer_list)

singer_list.insert(1,"뉴진스")
print (singer_list)

singer_list.insert(2,"르세라핌")
print (singer_list)

print(singer_list[1:3])



sports = ["야구","축구","농구"]

print("농구" in sports)
print("배구" in sports)

sports.remove("축구")
print(sports)
print(len(sports))
sports[0] = "배드민턴"
print(sports)

sports = ["야구","축구","농구"]
sports.remove ("축구")
sports.append("족구")
print(sports)

del sports[0]
sports.pop()
print(sports)

sports.append("족구")
sports.append("축구")
sports.append("배구")
print(sports)

sports.pop(1)
print(sports)

sports.clear()
print(sports)
'''

fruit = ["apple","banana","mango"]
food = ["떡볶이","치킨","국밥"]

fruit.append("strawberry")
food.append("짜장면")
del fruit[0]
food.remove("치킨")
fruit.insert(1,"melon")
print(fruit)
print(food)
fruit.extend(food)
print(fruit)
