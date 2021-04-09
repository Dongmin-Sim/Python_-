# OOP 

OOP 는 Object Oriented Programing 의 줄임말로, 객체의 관점에서 프로그래밍하는 것을 뜻함.



객체 지향 프로그래밍을 표현할 수 있는 4가지 개념

* Abstraction
* Encapsulation
* Inheritance
* Polymorphism





## Abstraction : 추상화



### 파이썬의 type hinting

파이썬은 대표적인 동적 타이핑 언어임. python 3.5 이후 버전부터 타입을 지정할 수 있는 *Type hint* 기능을 지원하는데, type hinting  강제적인 규칙이 아니기 때문에 type hinting 을 지정하더라도 동적으로 변수 또는 파라미터가 할당될 수 있기 때문에 **예기치 못한 에러**가 발생할 수 있음(int 형으로 type hinting 을 지정했으나 str자료형으로 입력해도 에러가 나지 않음)

**< 변수에서의 type hinting >**

```python
Variable : type
  Parameters: type
```

**< 함수에서의 type hinting >**

```python
# 파라미터로 int 자료형을 받고 bool 값을 return 하는 경우
def type_hint(a:int) -> bool:
  return True

# 파라미터로 float 자료형을 받고 아무것도 return 하지 않는 경우
def type_hint(a:float) -> None:
  return None
```

하지만, *type hinting* 을 사용하게 되면 기존 코드에는 영향을 끼치지 않으면서 변수나 메소드를 사용할때 어떠한 자료형이 들어가고, *return* 되는 지 한눈에 파악이 가능하여 **코드의 가독성**이 좋아지고, **버그가 발생할 확률**도 줄일 수 있다는 장점을 가지고 있어 앞서 **언급한 문제점에 주의**하여 사용하는 것이 좋다. (물론 이 또한 필수는 아님)



## Encapsulation : 캡슐화