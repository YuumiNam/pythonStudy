#변수
#int는 숫자타입 str은 문자타입
#파이썬은 변수선언시 타입을 따로 지정해주지 않아도 됨


#변수 선언 안하고 출력
print(5 + 10)



#변수 선언 후 출력
a = 5
b = 10
print(a+b)



a = 10
b = "dog"
#print(a+b)  숫자와 문자는 더할 수 없음. 곱하기는 가능



a = "dog"
b = "cat"
print(a + " " + b)


#지금 이렇게 a,b에 몇개의 변수를 선언해줘도 상관없는 이유는
#파이썬은 위에서 아래로 쭈욱 내려오면서 해석되기때문에 마지막에 선언된 변수를 기준으로 해석됨
#위로 거슬러가면서 해석할 수는 없다



a = 10
b = 2

print(a * b) #곱하기
print(a ** b) #제곱
print(a / b) #나누기
print(a // b) #몫만구하기
print(a % b) #나머지구하기



#a는 b보다 나이가 많습니다 출력하기
a = "kim"
b = "park"

print("a는 b보다 나이가 많습니다.")
print(f"{a}는 {b}보다 나이가 많습니다.")
print("%s는 %s보다 나이가 많습니다." %(a,b))



#한줄 띄어쓰기
print("오늘 아침에 먹은\n미역국")


#리스트 자료형
a = [1,3,5,7,9,"미역국"] #리스트 안에는 숫자 문자 모두 올수있음

#추가하기 가장 오른쪽에 추가됨
a.append(3)

#제거하기 중복된 3이 있다면, 왼쪽부터 제거됨
a.remove(3)

#리스트의 개수
print(len(a))

#리스트의 마지박번째 값
print(a[len(a) - 1])

#리스트 뒤집기
a.reverse()

#리스트 분류하기 작은수부터 배열
# a.sort()  #지금은 '미역국'이라는 문자가 숫자랑 같이 있으므로 print() 해봐도 안됨

#중복값 제거
a = [1,3,1,3,1,3,4]
a = set(a)
print(a) #대신 중복값 제거 후에는 딕셔너리형으로 바뀜 이후에 리스트형으로 바꿔주려면 for문 돌려야함


#딕셔너리 자료형
#a = {key : value} 관계

#딕셔너리형 선언
person1 = {'name' : 'kim' , 'age' : 20}
person2 = {'name' : 'park' , 'age' : 10}

#딕셔너리형 두개를 리스트 안으로 묶음
persons = [person1,person2]

person3 = {'name' : 'lee' , 'age' : 10}

#뒤늦게 리스트에 per3 추가
persons.append(person3)

#per1의 이름 나타내기
person1.get('name')

#per1의 key값 나타내기
person1.keys()

#per1의 value값 나타내기
person2.values()



#문제1
#park은 70점 kim은 80점 lee는 50점일때
#80점 이상인 사람을 True False로 나타내시오
#딕셔너리 자료형 이용

print("Q1")
a = {"name" : "park" , "score" : 70}
b = {"name" : "kim" , "score" : 80}
c = {"name" : "lee" , "score" : 50}

print("%s는 점수가 80점 이상이 %s" %(a.get("name"),a['score']>=80))
print("%s는 점수가 80점 이상이 %s" %(b.get("name"),b['score']>=80))
print("%s는 점수가 80점 이상이 %s" %(c.get("name"),c['score']>=80))


#문제2
#kim은 50000원 park은 30000원이 있습니다.
#둘 사이에 누가 얼마나 더 있는지 나타내시오.
#둘 사이의 합산을 나타내시오
#둘 사이의 평균을 나타내시오
#딕셔너리자료형 이용

print("Q2")
a = {'name' : "kim", 'money' : 50000}
b = {'name' : "park", 'money' : 30000}

print("%s는 %s보다 %d 있습니다"%(a['name'],b['name'],a['money']-b['money']))
print("%s는 %s보다 %d 있습니다"%(b['name'],a['name'],b['money']-a['money']))

print("%s과 %s의 합산은 %d입니다"%(a['name'],b['name'],a['money']+b['money']))
print("둘의 평균은 %d입니다" %((a['money']+b['money'])/2))