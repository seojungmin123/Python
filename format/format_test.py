#출력 포매팅 
name = "서정민"
age = 17
print ("나의 이름은" ,name, "이고 나이는" ,age, "세 입니다.")

print ("나의 이름은 %s이고 나이는 %d세 입니다."%(name,age))

print ("나의 이름은 {}이고 나이는 {}세 입니다.".format(name,age))

print (f"나의 이름은 {name}이고 나이는 {age}세 입니다.")        

print(f"{3.141592:.4f}")
pi = 3.141592                                                                                                                                                                                                                                                         
print(format(pi,".4f"))