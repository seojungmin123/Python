person = {  '이름':'서정민',
            '나이':17,
            '키':170, 
            '집주소':'남동구 구월동'}

print(person['이름'])
print(person)
person['몸무게'] = 60
print(person)
person['키'] = 180
print(person)                                                                   
del person ['나이']
print(person)
print(person.get('집주소'))

print ('나이' in person)
print ('이름' in person)
print ('서정민' in person.values())
