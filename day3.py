#만약에 홀수면 2배, 짝수면 그대로의 리스트 만들고
#합이 20이 넘으면 끝

list1 = [9,4,2,1,6,7,5,4,3,7]
list0 = []
sum = 0

for i in list1 :
    sum += i
    if i % 2 == 1 :
        list0.append(i * 2)
       
    else :
        list0.append(i)
        
    if sum > 20 :
        break
    
print(list0)



#짝수와 홀수
#정수 num이 짝수일경우
#"Even"을 반환하고
#정수 num이 홀수인경우
#"Odd"를 반환하는 함수 solution을 완성해주세요


def solution(num) :
    answer = ''    
    if num % 2 == 1 :
        answer = "Odd"
    else :
        answer = "Even"
    return answer
   

print(solution(0))
print(solution(3))
print(solution(4))



#구구단 만들기
for i in range(2,10) : 
    for j in range(1,10) : 
        print(f"{i} * {j} = {i * j}")




#2부터 30까지의 숫자 중 소수를 구해보자
#소수란? 1과 자신만으로 나누어지는 수

answer = []

for i in range(2,31) :
    isPrimary = True
    for j in range(2,i) :
        if i % j == 0 : 
            isPrimary = False
        break
    if isPrimary :
        answer.append(i)
print(answer)


#함수
#함수란?? "입력값을 넣었을때 출력값이 나오는것"
#즉, 입력값 -> 함수 -> 결과값

# <함수의 기본공식>
# def 매개변수 :     <<<     def는 define의 약자라고 한다.
#   수행할 문장

def sum(a,b) : #sum(a,b) => a,b는 매개변수
    return a+b
print(sum(1,2)) #sum(1,2) => 1,2는 인수

#매개변수를 설정 안해준경우
def sum1() :
    return 2+2
print(sum1())


def sum1(*args) : # *이 붙은 매개변수는 개수에 제한이 없다.
    print(args) #튜플형으로 나옴
    pppp = 0
    for arg in args :
        pppp += arg
    return pppp
print(sum1(1,1,1,1,1,1))


def printFunc(**kwargs) : #*이 2개붙은 매개변수는 딕셔너리로
    print(kwargs)
printFunc(name = 'kim' , age = 20 )


def makeHuman(name,age) :
    return {"name" : name, "age" : age}
human1 = makeHuman("kim" , 20)
human2 = makeHuman("park" , 34)

print(human1)
print(human2)




#소수를 나타내주는 함수를 짜보자
def isPrimaryNumber(num) :
    isPrimary = True
    for j in range(2,num) :
        if num % j == 0 :
            isPrimary = False
            break
    if isPrimary :
        return f"{num}은 소수입니다"
    else :
        return f"{num}은 소수가 아닙니다."

print(isPrimaryNumber(8))
print(isPrimaryNumber(13))


def isPrimaryNumbers(*nums) : #nums = (9,4,2,11,16)
    for num in nums : #(중요) *이 추가된 매개변수는 튜플이기때문에 맨앞에 무조건 for를 쓴다.
        isPrimary = True
        for j in range(2,num) :
            if num % j == 0 :
                isPrimary = False
                break
        if isPrimary :
            print(f"{num}은 소수입니다") #하나하나 찍어야 되기때문에 return이 아닌 print
        else :
            print(f"{num}은 소수가 아닙니다.")

print(isPrimaryNumbers(9,4,2,11,16)) #return이 없기때문에(입력을했는데 불러올 결과가 없음) none이 뜸




#함수 안에서 사용한 변수의 효력범위
#함수 안에서 사용한 매개변수는 함수 밖의 변수 이름과는 상관없음

name = "park" #전역변수
name1 = ""

def setName1(name) : #매개변수
    print(f"2.{name}") #kim
    name1 = name
    name = name
    pppp = name #지역변수
    print(f"3.{name} {name1}") #kim

print(f"0.name1 : {name1}") #1.name1 : ""
print(f"1.{name}") #park
setName1("kim")
print(f"4.{name}") #park
print(f"5.name1 : {name1}") #1.name1 : ""