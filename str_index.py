my = "저는 인평자동차고등학교 AI소프트웨어과 1학년 1반 서정민입니다"

school = my[3:12]
print(school)
print(my[1:15:2])
major = my[13:21]
print(major)



text = "python programming"

print(text[7:11])
print(text[-7:-3])
print(text[7:])
print(text[:6])
print(text[-13:-19:-1])
print(text[7::2])
print(text[::])



major = "AI소프트웨어과"
print(major[3])
print(major[:2])
print(major[-8:-6])
print(major[2:])



print(len(major))
major = "AI software!!!"
print(major.count("!"))
print(major.upper())
print(major.lower())
major = major.replace("AI","Happy AI")
print(major)
