# #사용자 입력과 출력
# a = input("입력하세요 ")
# print(a)


# #형변환
# def sum(a,b) :
#     return a+b # 5는 문자이므로 "5" + "5" = 55 , 10으로 표현하려면 강제 형변환을 시켜줘야함
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))



# def sum(a,b) :
# #    print(type(a))
# #    print(type(b))
#    try : # 에러가날것같을때 try except를 쓴다.
#     if type(a) == int and type(b) == int :
#         return a + b
#     else :
#         return int(a) + int(b) #문자를 숫자로 형변환
   
#    except :
#     return f"{a}랑 {b}중 숫자가 아닌게 있습니다."


# # a = input("입력하세요 ") #한번하고 끝
# # b = input("입력하세요 ")
# # print(sum(a,b))

# while True : #끝을 내고싶지 않을 때
#     a = input("입력하세요 ")
#     if a == "end" :
#         break
#     b = input("입력하세요 ")
#     if b == "end" :
#         break
#     print(sum(a,b))



#파일 입출력

# 상대 경로란?
# 내 위치를 기준으로 하고 싶은 곳으로 가자
# .   현재폴더
# ..  이전폴더
# /   폴더열기


# 절대경로란?  
# 경로 전체를 다 써줌

#3가지 모드
# w : 쓰기모드 
# r : 읽기모드
# a : 추가모드


# <파일 입출력 공식>
# f = open("파일이름" , "모드") <<< f는 변수라서 원하는 명칭가능
# f.close()


# C:\bitacademyBigdata\pythonTest 안에 test2폴더를 생성 후 파일 입출력을 해보자
f = open("./test2/newfile.txt","w") #상대경로 ./를 사용함
f.write("Hello world!")

f.write("""\nhi
hi
hi""")
f.close()



#파일 읽기
f = open("./test2/newfile.txt","r")
line = f.readline() #한줄읽기
print(line)
f.close()

fr = open("./test2/newfile.txt","r")
lines = fr.readlines() #모든 줄 읽기 결과값은 'hi' 'hi' 'hi\n' 'hi다 찍힘. \n까지
print(lines)
fr.close()



#이쁘게 여러줄 읽기
fr = open("./test2/newfile.txt","r")
lines = fr.readlines()
for i in lines : 
    print(i)
fr.close()


#고쳐쓰기(hi를 hello로)
fw = open("./test2/newfile.txt","w") #이 문장을 쓴 순간부터 newfile.txt파일은 다시 새로작성 원래 내용은 사라짐
for line in lines : 
    line = line.strip()
    if line == "hi" :
        fw.write("hello")
    else :
        fw.write(line)
    fw.write("\n")
fw.close()