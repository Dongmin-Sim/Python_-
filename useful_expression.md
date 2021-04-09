### ternary expression 

`if` 문을 조금 더 효율적으로 써줄 수 있는 구문을 말함. *ternary expression* 을 사용하면 `if`, `else` 구문을 보다 쉽게 사용할 수 있음. 

```python
wallet = 5000

if wallet >= 1000:
  soda = "you can buy soda!"
else:
  soda = "you can't buy soda :("
  
print(soda)  # => "you can buy soda!"
```

위의 `if`, `else` 구문을 *ternary expression*  을 사용하여 표현하면 다음과 같음.

```python
wallet = 5000

soda = "you can buy soda!" if wallet >= 1000 else "you can't buy soda :("

print(soda)  # => "you can buy soda!"
```



### list comprehension

List comprehension은 리스트를 생성할때 간편하기 때문에 매우매우매우 많이 쓰이기 때문에 방법을 알아두면 좋음. 한줄의 코드로 매우 간단하게 생성이 가능함. 

*List comprehension* 을 사용하는 가장 기본적인 방법은 다음과 같음. 

```python
# list comprehension 기본 문법
[expression for element in iterable]

# 조건문 추가된 list comprehension
[expression for element in iterable if condition]
```



일반적으로 `for` 반복문으로 리스트를 만드는 방법

```python
new_list = []
for i in range(10):
  new_list.append(i)

print(new_list)  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

위의 구문을 *List comprehension*  을 사용하여 표현하면 다음과 같음. 위의 코드와 비교해봤을때도 한줄의 코드로 간편하게 리스트를 생성할 수 있음.

```python
new_list = [i for i in range(10)]

print(new_list)  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



### lambda expression

함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법임. 편리해서 자주 사용됨. 

```python
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

my_function = lambda a, b: a+b

result = map(my_function, list1, list2)

print(list(result))  # => [7, 9, 11, 13, 15]
```