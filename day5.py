#3,6,9 게임
#들어온 숫자에 3 or 6 or 9 있으면 "c"
#계속 지속되어야하는 게임
#369369 현재 {i}

#첫번째방법
def game() :
    i = 0
    while True :
        i += 1
        myInput = input(f"현재 값 {i} ")
        answer = str(i + 1)
        for c in str(i + 1) :
            if c == "3" or c == "6" or c == "9" :
                answer = "c"
        if myInput == answer :
            print("맞았다")
        else :
            print("game over")
            break
game()


#전화번호 표시하기
#input 번호받아서 010-2222-2222
#뒤 4자리만 살리고 ***-****-****

def solution(phone_number) :
    answer = ''
    for i in range(0,len(phone_number)) :
        if i < len(phone_number) - 4 :
            # answer += "*"
            if phone_number[i] == "-" :
                answer += "-"
            else :
                answer += "*"
        else :
            answer += phone_number[i]
    return answer 

# print(solution("01011112222"))


phone_number = input("번호 000-0000-0000 ")    
print(solution(phone_number))

# print(solution("01033334444")) 
# print(solution("027778888"))



#클래스
#계산기를 만들거임
#다른 계산을 할때마다 변수를 다르게 설정해야하므로 계산을 100번하려면 변수를 100개를 써줘야하는 불상사가 일어남

def add(a,b) : 
    return a + b

def diff(a,b) :
    return a - b

i = 0
i = add(i, 10)
i = diff(i,5)
print(i)

# 하나의 클래스를 만든다면
# 그 클래스에 정의된 속성이나 기능들을 반복해서 재사용할수있다.

# 뿐만아니라,
# 계산기에는 덧셈기능만 있는 것이 아닌 뺄셈,나눗셈,곱셈 기능도 있는데
# 어떠한 클래스를 만들었다면 그 클래스를 정의할수 있는 속성이나 기능들을 하나의 클래스에 다 넣어줄 수 있다.



#자동차 도면 설계해보고 찍어보기
class Car : 
    #필드
    color = ""
    speed = 0
    count = 0

    #생성자 = 인스턴스를 만들었을때 자동으로 생성되는 메소드
    #기본생성자를 만들면 인스턴스 생성시 따로 color나 speed의 초기값을 정의해 줄 필요가 없다.
    def __init__(self) :
        self.color = "" #인스턴스 변수
        self.speed = 0
        Car.count += 1 #클래스 변수

    #메소드
    def upSpeed(self,value) :
        self.speed += value
    def downSpeed(self,value) : 
        self.speed -= value

#객체,인스턴스
myCar1 = Car()
myCar2 = Car()

print(myCar1.count)
print(myCar2.count)

myCar1.color = "red"
myCar2.color = "white"
myCar1.upSpeed(30)
myCar2.upSpeed(50)

print(myCar1.color)
print(myCar1.speed)
print(myCar2.color)
print(myCar2.speed)



myCar2 = Car()
print(myCar1.count)


#기본생성자도 매개변수 설정 가능
#물론, 이렇게되면 객체를 설정할때 매개변수를 꼭 넣어줘야함

# class Car1 : 
#     def __init__(self,color,speed) : 
#         self.color = color
#         self.speed = speed

# myCar4 = Car1("black","70")
