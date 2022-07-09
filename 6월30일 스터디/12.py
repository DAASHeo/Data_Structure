from curses.ascii import isupper


movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
movie_rank.append("배트맨")
movie_rank.insert(1,"슈퍼맨")
movie_rank.remove("럭키")
#del movie_rank[3]
print(movie_rank)

# 1. movie_rank 리스트에 "배트맨"을 추가하세요.
# 2. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하세요.
# 3. ‘럭키’를 삭제하세요.

##13
nums = [1,2,3,4,5,6,7]
print(min(nums),max(nums))

##14
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

##15
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
for i in interest:
    print(i, end=" ")

##16
# t = ('a', 'b', 'c')
# t[0] = 'A'
# t = ('A', 'b', 'c')
# t = ('a', 'b', 'c')
# # 튜플 값 변경 불가
# # 리스트로 바꾸고 값 변경 후 다시 튜플로 변환
# h = list(t)
# h[0]='A'
# t = tuple(h)
# print(t

print(" ")
##17
inventory = {"메로나":300,"비비빅":400,"죠스바":250}

# 1. inventory 딕셔너리에서 메로나의 가격을 화면에 출력하세요.
# 2. inventory 딕셔너리에서 key 값으로만 구성된 리스트를 생성하세요.
# 3. inventory 딕셔너리에서 value 값으로만 구성된 리스트를 생성하세요.
# 4. inventory 딕셔너리에서 key:“죠스바” value:250을 삭제하세요.

print(inventory["메로나"])
item = list(inventory.keys())
print(item)
price = list(inventory.values())
print(price)
del inventory["죠스바"]
print(inventory)

# inventory.pop("죠스바");
# inventory.popitem();
# print(inventory);

##18
mylist = ["SK하이닉스", "삼성전자", "LG전자"]
for i in mylist:
  print(len(i))

##19
mylist = ["가", "나", "다", "라"]
for i in mylist[::-1]:
  print(i)

for i in range(0, len(mylist), -1):
    print(mylist[i])

##20
mylist= ["A", "b", "c", "D"]
for i in mylist:
    if i.isupper():
        print(i)

##21
mylist= ['dog', 'cat', 'parrot']
for i in mylist:
    first = i[0].upper()
    print(first+i[1:])

# mylist= ['dog', 'cat', 'parrot']
# for i in mylist:
#     i=i.capitalize();
#     print(i);

##22
for i in range(2002,2051,4):
    print(i)

##23
def print_arithmetic_operation(num1, num2):
    print("합 :",num1 + num2)
    print("차 :",num1 - num2)
    print("곱 :",num1 * num2)
    print("나눗셈 :",num1 / num2)

print_arithmetic_operation(5, 2)

##24
def print_max(num1, num2, num3):
    max = 0
    if num1 > max:
        max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max

print(print_max(1, 2, 3),"이 가장 큰 수이다.")

# def print_max():
#     num = list(map(int, input().split()))
#     max=0
#     for _ in num:
#         if max < _:
#             max=_

#     print(max)

# print_max()

##25
def print_score(list):
    return sum(list)/len(list)

print(print_score([100,80,90]))

##26
class Stock:
    pass 
##pass : 속성과 메서드를 가지고 있지 않음

##27
class Stock:
    def stock(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)

##28
