#True or False
#"80은 짝수인가??" 를 true or false와 함께 나타내보시오.

print(f"80은 짝수인가?? {80%2 == 0}")



#리스트 [2,1,5,6,2,40,50,2,5,32] 와 리스트 [4,6,2,3,9,10,2,3,42,5,4,63]의 교집합중 최대값을 구하시오.
a = [2,1,5,6,2,40,50,2,5,32]
b = [4,6,2,3,9,10,2,3,42,5,4,63]

result = list(set(a) & set(b)) #중복제거해주고 딕셔너리 형으로 바뀐걸 다시 리스트로 변환해줌
print(result[len(result)-1]) #최대값구하기



#if문
#<if문의 기본공식>
#  if  조건문 :          
#   수행할 문장​
#  elif 조건문 :​
#   수행할 문장​
#  else :
#   수행할 문장


a = 10
b = 5

if a > b : 
    print("a는 b보다 크다")
elif a < b : 
    print("a는 b보다 작다")
else : 
    print("a와 b는 같다")



#for문
# <for문의 기본공식>

# for 변수 in 조건범위 :
#     수행할 문장


#리스트에 있는 숫자들 더하기
a = [1,2,3,4,5]
sum = 0

for el in a : 
    sum += el
print(sum)



#while문
# <while문의 기본공식>

# while 조건문 :
#     수행할 문장

#1부터 5까지의 숫자들 더하기
sum = 0
i = 0

while i <= 5 : 
    sum += i
    i += 1
print(sum)




# list = [1,2,3,4,5,6,2,3,5,1]
# '뭐는 짝수입니다.' '뭐는 홀수입니다.' 로 나타내기

list = [1,2,3,4,5,6,2,3,5,1]

#for문을 사용
for i in list :
    if i%2 == 1 :
        print("%d는 홀수입니다" %i)
    else :
        print("%d는 짝수입니다" %i)

#while문을 사용
# i = 0
# while i < len(list):
#     if list[i]%2 == 1 :
#         print("%d는 홀수입니다" %list[i])
#     else :
#         print("%d는 짝수입니다" %list[i])
#     i += 1




#2부터 20까지 짝수의 합은???

#for문을 사용
list1 = range(2,21)
sum = 0
for el in list1 :
    if el % 2 == 0 :
        sum += el
print(sum)

#while문을 사용
i = 2
sum = 0
while i <= 20 :
    if i % 2 == 0 :
        sum += i
    i += 1
print(sum)




#phone이 애플이라면 "iphone" 갤럭시라면 version을 보고 플립이면 "flip" 아니라면 "galaxy" 출력
phone = {"name" : "갤럭시" , "version" : "플립"}

if phone.get("name") == "갤럭시" :
    if phone.get("version") == "플립" :
        print("flip")
    else :
        print("galaxy")
else :
    print("iphone")