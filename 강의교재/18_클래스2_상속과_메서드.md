# 18장 클래스 2 (상속과 메서드)

---

## 📚 **학습 목표 (Learning Objectives)**

이번 장을 마치면 여러분은 상속을 통해 기존 클래스를 확장하고 재사용할 수 있습니다. 메서드 오버라이딩과 super() 함수를 활용하여 더욱 유연하고 강력한 객체지향 프로그램을 작성할 수 있습니다.

---

## 1️⃣ **상속이란 무엇인가?**

지난 시간에 클래스를 만드는 방법을 배웠습니다. 하지만 비슷한 클래스를 여러 개 만들어야 한다면 어떻게 해야 할까요?

```python
# 비효율적인 방법 - 코드 중복!
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    def eat(self):
        print(f"{self.name}이(가) 먹이를 먹습니다.")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    def eat(self):
        print(f"{self.name}이(가) 먹이를 먹습니다.")
```

개와 고양이는 둘 다 동물이고, 공통된 특징(이름, 나이, 먹기)을 가지고 있습니다. 이런 공통 부분을 매번 복사하는 것은 비효율적입니다. 이럴 때 **상속(Inheritance)**을 사용합니다!

### **상속은 부모-자식 관계다**

상속은 마치 부모가 자식에게 재산을 물려주듯이, 기존 클래스(부모)의 속성과 메서드를 새로운 클래스(자식)가 물려받는 것입니다.

```
상속의 개념

      ┌─────────────┐
      │   Animal    │  ← 부모 클래스 (상위 클래스)
      │  (동물)     │
      ├─────────────┤
      │ name        │
      │ age         │
      │ eat()       │
      └──────┬──────┘
             │ 상속
        ┌────┴────┐
        │         │
   ┌────▼────┐ ┌─▼─────┐
   │   Dog   │ │  Cat  │  ← 자식 클래스 (하위 클래스)
   │  (개)   │ │ (고양이)│
   ├─────────┤ ├───────┤
   │ bark()  │ │ meow()│  ← 자신만의 기능 추가
   └─────────┘ └───────┘
```

### **실생활 비유**

```
분류 체계

생물
 └─ 동물
     ├─ 포유류
     │   ├─ 개
     │   ├─ 고양이
     │   └─ 사람
     └─ 조류
         ├─ 참새
         └─ 독수리
```

상위 분류의 특성을 하위 분류가 물려받습니다:

- 모든 동물은 먹고, 자고, 움직인다
- 모든 포유류는 털이 있고, 새끼를 낳는다
- 개는 짖고, 고양이는 야옹거린다 (각자의 특징)

### **상속의 장점**

**1. 코드 재사용**: 공통 코드를 한 곳에만 작성
**2. 유지보수 용이**: 수정이 필요하면 부모 클래스만 수정
**3. 계층 구조**: 논리적으로 체계적인 구조
**4. 확장성**: 기존 코드를 건드리지 않고 기능 추가

---

## 2️⃣ **상속 기본 문법**

상속은 클래스 정의할 때 괄호 안에 부모 클래스를 지정합니다.

### **기본 형태**

```python
class 부모클래스:
    # 부모 클래스 내용
    pass

class 자식클래스(부모클래스):
    # 자식 클래스 내용
    pass
```

### **간단한 예제**

```python
# 부모 클래스
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    def eat(self):
        print(f"{self.name}이(가) 먹이를 먹습니다.")
  
    def sleep(self):
        print(f"{self.name}이(가) 잠을 잡니다.")

# 자식 클래스 1
class Dog(Animal):
    def bark(self):
        print(f"{self.name}: 멍멍!")

# 자식 클래스 2
class Cat(Animal):
    def meow(self):
        print(f"{self.name}: 야옹~")

# 사용
dog = Dog("멍멍이", 3)
dog.eat()    # 부모 메서드 사용 가능!
dog.sleep()  # 부모 메서드 사용 가능!
dog.bark()   # 자식만의 메서드

cat = Cat("나비", 2)
cat.eat()    # 부모 메서드 사용 가능!
cat.meow()   # 자식만의 메서드
```

**실행 결과:**

```
멍멍이이(가) 먹이를 먹습니다.
멍멍이이(가) 잠을 잡니다.
멍멍이: 멍멍!
나비이(가) 먹이를 먹습니다.
나비: 야옹~
```

자식 클래스가 부모 클래스의 메서드를 자동으로 물려받았습니다!

---

## 3️⃣ **자식 클래스에서 기능 추가하기**

자식 클래스는 부모의 모든 것을 물려받으면서, 자신만의 속성과 메서드를 추가할 수 있습니다.

### **속성 추가하기**

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        # 부모의 __init__ 호출 필요!
        Animal.__init__(self, name, age)
        # 또는: super().__init__(name, age)
    
        # 자식만의 속성 추가
        self.breed = breed
  
    def info(self):
        print(f"{self.name} ({self.breed}) - {self.age}살")

dog = Dog("멍멍이", 3, "진돗개")
dog.info()  # 멍멍이 (진돗개) - 3살
```

### **메서드 추가하기**

```python
class Vehicle:
    """탈것 (부모 클래스)"""
  
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
  
    def start(self):
        print(f"{self.brand} {self.model} 시동 켜기")
  
    def stop(self):
        print(f"{self.brand} {self.model} 시동 끄기")

class Car(Vehicle):
    """자동차 (자식 클래스)"""
  
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)  # 부모 초기화
        self.fuel_type = fuel_type
        self.trunk_open = False
  
    def open_trunk(self):
        """트렁크 열기 (자동차만의 기능)"""
        self.trunk_open = True
        print("트렁크가 열렸습니다.")
  
    def close_trunk(self):
        """트렁크 닫기"""
        self.trunk_open = False
        print("트렁크가 닫혔습니다.")

class Motorcycle(Vehicle):
    """오토바이 (자식 클래스)"""
  
    def __init__(self, brand, model, helmet_storage):
        super().__init__(brand, model)
        self.helmet_storage = helmet_storage
  
    def wheelie(self):
        """앞바퀴 들기 (오토바이만의 기능)"""
        print("앞바퀴를 들었습니다!")

# 사용
car = Car("현대", "소나타", "가솔린")
car.start()        # 부모 메서드
car.open_trunk()   # 자식 메서드
car.close_trunk()  # 자식 메서드
car.stop()         # 부모 메서드

print()

bike = Motorcycle("야마하", "R1", True)
bike.start()   # 부모 메서드
bike.wheelie() # 자식 메서드
bike.stop()    # 부모 메서드
```

**실행 결과:**

```
현대 소나타 시동 켜기
트렁크가 열렸습니다.
트렁크가 닫혔습니다.
현대 소나타 시동 끄기

야마하 R1 시동 켜기
앞바퀴를 들었습니다!
야마하 R1 시동 끄기
```

---

## 4️⃣ **메서드 오버라이딩 (재정의)**

자식 클래스에서 부모의 메서드를 **다시 정의**할 수 있습니다. 같은 이름의 메서드를 만들면 자식 것이 우선됩니다.

### **왜 오버라이딩이 필요한가?**

부모의 기본 동작이 자식에게 맞지 않을 때 수정해서 사용합니다.

```python
class Animal:
    def __init__(self, name):
        self.name = name
  
    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다.")

class Dog(Animal):
    def speak(self):  # 오버라이딩
        print(f"{self.name}: 멍멍!")

class Cat(Animal):
    def speak(self):  # 오버라이딩
        print(f"{self.name}: 야옹~")

class Cow(Animal):
    def speak(self):  # 오버라이딩
        print(f"{self.name}: 음메~")

# 사용
animals = [
    Dog("멍멍이"),
    Cat("나비"),
    Cow("얼룩이")
]

for animal in animals:
    animal.speak()  # 각자의 speak() 실행
```

**실행 결과:**

```
멍멍이: 멍멍!
나비: 야옹~
얼룩이: 음메~
```

같은 `speak()` 메서드를 호출했지만, 각 클래스에서 오버라이딩했기 때문에 다른 결과가 나옵니다!

### **실전 예제: 직원 관리**

```python
class Employee:
    """직원 (부모 클래스)"""
  
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary
  
    def get_salary(self):
        """급여 계산"""
        return self.base_salary
  
    def info(self):
        """정보 출력"""
        print(f"{self.name} (사번: {self.emp_id})")
        print(f"급여: {self.get_salary():,}원")

class Manager(Employee):
    """관리자 (자식 클래스)"""
  
    def __init__(self, name, emp_id, base_salary, team_size):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size
  
    def get_salary(self):  # 오버라이딩
        """관리자 수당 추가"""
        bonus = self.team_size * 100000
        return self.base_salary + bonus
  
    def info(self):  # 오버라이딩
        super().info()  # 부모 메서드 호출
        print(f"관리 인원: {self.team_size}명")

class Developer(Employee):
    """개발자 (자식 클래스)"""
  
    def __init__(self, name, emp_id, base_salary, language):
        super().__init__(name, emp_id, base_salary)
        self.language = language
  
    def get_salary(self):  # 오버라이딩
        """기술 수당 추가"""
        tech_bonus = 500000
        return self.base_salary + tech_bonus
  
    def info(self):  # 오버라이딩
        super().info()
        print(f"주 언어: {self.language}")

# 직원 생성
employees = [
    Employee("김철수", "E001", 3000000),
    Manager("박영희", "M001", 4000000, 5),
    Developer("이민수", "D001", 3500000, "Python")
]

# 정보 출력
for emp in employees:
    print("\n" + "=" * 40)
    emp.info()
```

**실행 결과:**

```
========================================
김철수 (사번: E001)
급여: 3,000,000원

========================================
박영희 (사번: M001)
급여: 4,500,000원
관리 인원: 5명

========================================
이민수 (사번: D001)
급여: 4,000,000원
주 언어: Python
```

---

## 5️⃣ **super() 함수 완전 정복**

`super()`는 부모 클래스의 메서드를 호출할 때 사용합니다.

### **왜 super()를 사용할까?**

부모의 기능을 그대로 사용하면서 추가 작업을 할 때 유용합니다.

```python
# super() 없이 (비추천)
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)  # 부모 클래스 이름 직접 사용
        self.breed = breed

# super() 사용 (권장)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 더 간결하고 유연함
        self.breed = breed
```

### **super()의 활용**

```python
class Shape:
    """도형 (부모)"""
  
    def __init__(self, color):
        self.color = color
  
    def describe(self):
        print(f"색상: {self.color}")

class Rectangle(Shape):
    """직사각형 (자식)"""
  
    def __init__(self, color, width, height):
        super().__init__(color)  # 부모 초기화
        self.width = width
        self.height = height
  
    def area(self):
        return self.width * self.height
  
    def describe(self):
        super().describe()  # 부모 메서드 먼저 실행
        print(f"가로: {self.width}, 세로: {self.height}")
        print(f"넓이: {self.area()}")

class Circle(Shape):
    """원 (자식)"""
  
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
  
    def area(self):
        return 3.14 * self.radius ** 2
  
    def describe(self):
        super().describe()
        print(f"반지름: {self.radius}")
        print(f"넓이: {self.area():.2f}")

# 사용
rect = Rectangle("빨강", 10, 5)
rect.describe()

print()

circle = Circle("파랑", 7)
circle.describe()
```

**실행 결과:**

```
색상: 빨강
가로: 10, 세로: 5
넓이: 50

색상: 파랑
반지름: 7
넓이: 153.86
```

---

## 6️⃣ **실전 예제: 음식점 배달 시스템**

배달 앱의 음식점 시스템을 만들어봅시다.

```python
class Restaurant:
    """음식점 기본 클래스"""
  
    def __init__(self, name, location, rating=0):
        self.name = name
        self.location = location
        self.rating = rating
        self.menu = {}
        self.reviews = []
  
    def add_menu(self, item, price):
        """메뉴 추가"""
        self.menu[item] = price
        print(f"✓ '{item}' 메뉴 추가 ({price:,}원)")
  
    def show_menu(self):
        """메뉴판 표시"""
        print(f"\n{'='*40}")
        print(f"📋 {self.name} 메뉴")
        print(f"📍 위치: {self.location}")
        print(f"⭐ 평점: {self.rating}/5.0")
        print("-"*40)
        if len(self.menu) == 0:
            print("등록된 메뉴가 없습니다.")
        else:
            for item, price in self.menu.items():
                print(f"{item:20} {price:>8,}원")
        print("="*40)
  
    def add_review(self, rating, comment):
        """리뷰 추가"""
        if 0 <= rating <= 5:
            self.reviews.append({
                "rating": rating,
                "comment": comment
            })
            # 평균 평점 계산
            total = sum(r["rating"] for r in self.reviews)
            self.rating = round(total / len(self.reviews), 1)
            print(f"✓ 리뷰 등록 (평점: {rating}/5)")
        else:
            print("❌ 평점은 0-5 사이여야 합니다.")
  
    def calculate_delivery_fee(self, distance):
        """배달비 계산 (기본)"""
        base_fee = 3000
        if distance > 3:
            extra_fee = (distance - 3) * 500
            return base_fee + extra_fee
        return base_fee

class KoreanRestaurant(Restaurant):
    """한식당 클래스"""
  
    def __init__(self, name, location):
        super().__init__(name, location)
        self.side_dishes = ["김치", "단무지", "콩나물"]
  
    def banchan_service(self):
        """반찬 서비스"""
        print(f"\n🍚 {self.name}의 기본 반찬")
        print(f"   {', '.join(self.side_dishes)}")
        print("   무료 제공!")
  
    def calculate_delivery_fee(self, distance):
        """배달비 계산 (한식당은 할인)"""
        base_fee = super().calculate_delivery_fee(distance)
        discount = 500
        final_fee = base_fee - discount
        print(f"💰 배달비: {base_fee:,}원 → {final_fee:,}원 (한식당 할인 -500원)")
        return final_fee
  
    def show_menu(self):
        super().show_menu()
        print(f"🎁 기본 반찬: {', '.join(self.side_dishes)} (무료)")
        print("="*40)

class ChineseRestaurant(Restaurant):
    """중식당 클래스"""
  
    def __init__(self, name, location):
        super().__init__(name, location)
        self.min_order = 15000
  
    def free_jjajang(self, order_amount):
        """짜장면 서비스 (3만원 이상 주문시)"""
        if order_amount >= 30000:
            print(f"\n🎉 3만원 이상 주문! 짜장면 1개 무료 증정!")
            return True
        return False
  
    def calculate_delivery_fee(self, distance):
        """배달비 계산 (중식당은 거리에 따라 다름)"""
        if distance <= 2:
            fee = 2000
        elif distance <= 4:
            fee = 3000
        else:
            fee = 4000
        print(f"💰 배달비: {fee:,}원 ({distance}km)")
        return fee
  
    def show_menu(self):
        super().show_menu()
        print(f"📦 최소 주문 금액: {self.min_order:,}원")
        print("🎁 3만원 이상 주문시 짜장면 무료!")
        print("="*40)

class ItalianRestaurant(Restaurant):
    """이탈리안 레스토랑 클래스"""
  
    def __init__(self, name, location):
        super().__init__(name, location)
        self.premium = True
  
    def wine_pairing(self, dish):
        """와인 페어링 추천"""
        wine_menu = {
            "파스타": "화이트 와인",
            "피자": "레드 와인",
            "리조또": "스파클링 와인"
        }
    
        for food in wine_menu:
            if food in dish:
                print(f"\n🍷 '{dish}'와 어울리는 와인: {wine_menu[food]}")
                return wine_menu[food]
    
        print(f"\n🍷 레드 와인 추천")
        return "레드 와인"
  
    def calculate_delivery_fee(self, distance):
        """배달비 계산 (프리미엄 배달)"""
        base_fee = 5000  # 프리미엄 배달
        if distance > 5:
            print("❌ 배달 가능 거리를 초과했습니다. (최대 5km)")
            return None
        print(f"💰 배달비: {base_fee:,}원 (프리미엄 배달 서비스)")
        return base_fee
  
    def show_menu(self):
        super().show_menu()
        print("✨ 프리미엄 배달 서비스 (포장 품질 보장)")
        print("📍 배달 가능 거리: 최대 5km")
        print("="*40)

# 음식점 배달 시스템 시작
print("🍽️  음식 배달 앱 시뮬레이션 🍽️")
print()

# 음식점 생성
korean = KoreanRestaurant("맛있는 한식당", "강남구")
chinese = ChineseRestaurant("차이나타운", "서초구")
italian = ItalianRestaurant("벨라 이탈리아", "송파구")

# 메뉴 추가
print("[한식당 메뉴 등록]")
korean.add_menu("김치찌개", 8000)
korean.add_menu("된장찌개", 8000)
korean.add_menu("불고기", 15000)

print("\n[중식당 메뉴 등록]")
chinese.add_menu("짜장면", 6000)
chinese.add_menu("짬뽕", 7000)
chinese.add_menu("탕수육", 18000)

print("\n[이탈리안 레스토랑 메뉴 등록]")
italian.add_menu("까르보나라 파스타", 16000)
italian.add_menu("마르게리타 피자", 22000)
italian.add_menu("해산물 리조또", 20000)

# 메뉴판 보기
korean.show_menu()
chinese.show_menu()
italian.show_menu()

# 리뷰 등록
print("\n" + "="*40)
print("리뷰 등록")
print("="*40)

korean.add_review(4.5, "맛있어요!")
korean.add_review(5.0, "반찬이 푸짐해요")

chinese.add_review(4.0, "배달이 빨라요")

italian.add_review(4.8, "분위기 좋은 음식점")

# 특별 서비스
print("\n" + "="*40)
print("특별 서비스")
print("="*40)

korean.banchan_service()
chinese.free_jjajang(35000)
italian.wine_pairing("까르보나라 파스타")

# 배달비 계산
print("\n" + "="*40)
print("배달비 계산")
print("="*40)

print("\n[한식당 - 4km 거리]")
korean.calculate_delivery_fee(4)

print("\n[중식당 - 3km 거리]")
chinese.calculate_delivery_fee(3)

print("\n[이탈리안 - 6km 거리]")
italian.calculate_delivery_fee(6)

# 업데이트된 메뉴 확인
print("\n" + "="*40)
print("최종 음식점 정보")
print("="*40)
korean.show_menu()
```

**실행 결과:**

```
🍽️  음식 배달 앱 시뮬레이션 🍽️

[한식당 메뉴 등록]
✓ '김치찌개' 메뉴 추가 (8,000원)
✓ '된장찌개' 메뉴 추가 (8,000원)
✓ '불고기' 메뉴 추가 (15,000원)

[중식당 메뉴 등록]
✓ '짜장면' 메뉴 추가 (6,000원)
✓ '짬뽕' 메뉴 추가 (7,000원)
✓ '탕수육' 메뉴 추가 (18,000원)

[이탈리안 레스토랑 메뉴 등록]
✓ '까르보나라 파스타' 메뉴 추가 (16,000원)
✓ '마르게리타 피자' 메뉴 추가 (22,000원)
✓ '해산물 리조또' 메뉴 추가 (20,000원)

========================================
📋 맛있는 한식당 메뉴
📍 위치: 강남구
⭐ 평점: 0/5.0
----------------------------------------
김치찌개                    8,000원
된장찌개                    8,000원
불고기                     15,000원
========================================
🎁 기본 반찬: 김치, 단무지, 콩나물 (무료)
========================================

========================================
📋 차이나타운 메뉴
📍 위치: 서초구
⭐ 평점: 0/5.0
----------------------------------------
짜장면                      6,000원
짬뽕                        7,000원
탕수육                     18,000원
========================================
📦 최소 주문 금액: 15,000원
🎁 3만원 이상 주문시 짜장면 무료!
========================================

========================================
📋 벨라 이탈리아 메뉴
📍 위치: 송파구
⭐ 평점: 0/5.0
----------------------------------------
까르보나라 파스타          16,000원
마르게리타 피자            22,000원
해산물 리조또              20,000원
========================================
✨ 프리미엄 배달 서비스 (포장 품질 보장)
📍 배달 가능 거리: 최대 5km
========================================

========================================
리뷰 등록
========================================
✓ 리뷰 등록 (평점: 4.5/5)
✓ 리뷰 등록 (평점: 5.0/5)
✓ 리뷰 등록 (평점: 4.0/5)
✓ 리뷰 등록 (평점: 4.8/5)

========================================
특별 서비스
========================================

🍚 맛있는 한식당의 기본 반찬
   김치, 단무지, 콩나물
   무료 제공!

🎉 3만원 이상 주문! 짜장면 1개 무료 증정!

🍷 '까르보나라 파스타'와 어울리는 와인: 화이트 와인

========================================
배달비 계산
========================================

[한식당 - 4km 거리]
💰 배달비: 3,500원 → 3,000원 (한식당 할인 -500원)

[중식당 - 3km 거리]
💰 배달비: 3,000원 (3km)

[이탈리안 - 6km 거리]
❌ 배달 가능 거리를 초과했습니다. (최대 5km)
```

---

## 7️⃣ **isinstance()와 issubclass()**

객체의 타입을 확인하는 함수들입니다.

### **isinstance() - 객체 확인**

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

# isinstance(객체, 클래스)
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (부모도 True!)
print(isinstance(dog, Cat))     # False

print(isinstance(cat, Cat))     # True
print(isinstance(cat, Animal))  # True
print(isinstance(cat, Dog))     # False
```

### **issubclass() - 클래스 확인**

```python
# issubclass(자식클래스, 부모클래스)
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True
print(issubclass(Dog, Cat))     # False
print(issubclass(Animal, Dog))  # False
```

### **활용 예제**

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹~")

def make_sound(animal):
    """동물이 맞는지 확인하고 소리내기"""
    if isinstance(animal, Animal):
        animal.speak()
    else:
        print("동물이 아닙니다!")

dog = Dog()
cat = Cat()
number = 123

make_sound(dog)     # 멍멍!
make_sound(cat)     # 야옹~
make_sound(number)  # 동물이 아닙니다!
```

---

## 8️⃣ **실전 예제: 은행 계좌 시스템**

다양한 종류의 은행 계좌를 만들어봅시다.

```python
class BankAccount:
    """기본 은행 계좌"""
  
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
  
    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"입금: +{amount:,}원")
            print(f"✓ {amount:,}원 입금 완료 (잔액: {self.balance:,}원)")
            return True
        return False
  
    def withdraw(self, amount):
        """출금"""
        if amount > self.balance:
            print(f"❌ 잔액 부족 (잔액: {self.balance:,}원)")
            return False
    
        self.balance -= amount
        self.transactions.append(f"출금: -{amount:,}원")
        print(f"✓ {amount:,}원 출금 완료 (잔액: {self.balance:,}원)")
        return True
  
    def show_info(self):
        """계좌 정보"""
        print(f"\n{'='*40}")
        print(f"예금주: {self.owner}")
        print(f"잔액: {self.balance:,}원")
        print(f"{'='*40}")

class SavingsAccount(BankAccount):
    """적금 계좌"""
  
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
  
    def add_interest(self):
        """이자 추가"""
        interest = int(self.balance * self.interest_rate)
        self.balance += interest
        self.transactions.append(f"이자: +{interest:,}원")
        print(f"✓ 이자 {interest:,}원 추가 (이율: {self.interest_rate*100}%)")
  
    def show_info(self):
        super().show_info()
        print(f"이율: {self.interest_rate*100}%")
        print(f"{'='*40}")

class CheckingAccount(BankAccount):
    """당좌 계좌 (마이너스 통장)"""
  
    def __init__(self, owner, balance=0, overdraft_limit=1000000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
  
    def withdraw(self, amount):
        """출금 (마이너스 한도 내에서)"""
        max_withdraw = self.balance + self.overdraft_limit
    
        if amount > max_withdraw:
            print(f"❌ 한도 초과 (출금 가능: {max_withdraw:,}원)")
            return False
    
        self.balance -= amount
        self.transactions.append(f"출금: -{amount:,}원")
        print(f"✓ {amount:,}원 출금 완료 (잔액: {self.balance:,}원)")
        return True
  
    def show_info(self):
        super().show_info()
        print(f"마이너스 한도: {self.overdraft_limit:,}원")
        available = self.balance + self.overdraft_limit
        print(f"출금 가능 금액: {available:,}원")
        print(f"{'='*40}")

# 계좌 생성 및 사용
print("🏦 은행 시스템\n")

# 일반 계좌
basic = BankAccount("김철수", 100000)
basic.deposit(50000)
basic.withdraw(30000)
basic.show_info()

# 적금 계좌
savings = SavingsAccount("박영희", 1000000, 0.05)
savings.add_interest()
savings.show_info()

# 당좌 계좌
checking = CheckingAccount("이민수", 50000, 500000)
checking.withdraw(300000)  # 마이너스 사용
checking.show_info()
```

---

## 📝 **핵심 개념 정리**

### **상속(Inheritance)**

부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 것

```python
class Parent:
    pass

class Child(Parent):  # Parent 상속
    pass
```

### **메서드 오버라이딩**

자식 클래스에서 부모 메서드를 재정의

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):  # 오버라이딩
        print("멍멍!")
```

### **super() 함수**

부모 클래스의 메서드 호출

```python
class Child(Parent):
    def __init__(self, params):
        super().__init__(params)  # 부모 초기화
```

### **타입 확인**

- `isinstance(객체, 클래스)`: 객체가 해당 클래스인지
- `issubclass(자식, 부모)`: 상속 관계인지

---

## 💡 **실습 과제**

### **과제 1: 도형 클래스**

```python
# 힌트
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        pass
  
    def area(self):
        # 넓이 계산
        pass

class Circle(Shape):
    def __init__(self, radius):
        pass
  
    def area(self):
        # 넓이 계산
        pass
```

### **과제 2: 학생 클래스 상속**

```python
# 힌트
class Student:
    def __init__(self, name, student_id):
        pass

class Undergraduate(Student):
    def __init__(self, name, student_id, major):
        pass

class Graduate(Student):
    def __init__(self, name, student_id, advisor):
        pass
```

---

## ✅ **퀴즈**

### **[초급] 1번**

상속 문법으로 올바른 것은?

```python
1. class Child extends Parent:
2. class Child(Parent):
3. class Child inherits Parent:
4. class Child <- Parent:
```

### **[중급] 2번**

부모 메서드를 호출하는 함수는?

```python
1. parent()
2. base()
3. super()
4. inherit()
```

### **[중급] 3번**

메서드 오버라이딩이란?

```python
1. 메서드 삭제
2. 메서드 재정의
3. 메서드 추가
4. 메서드 복사
```

### **[고급] 4번**

다음 코드의 실행 결과는?

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

dog = Dog()
dog.speak()
```

1. ...
2. 멍멍!
3. 둘 다 출력
4. 오류 발생

### **[고급] 5번**

isinstance(dog, Animal)의 결과는? (dog = Dog()일 때)

```python
1. True
2. False
3. None
4. 오류 발생
```

---

## 🔑 **퀴즈 정답 및 해설**

**1번 정답: 2**
파이썬에서는 `class Child(Parent):` 형태로 상속합니다.

**2번 정답: 3**
`super()` 함수로 부모 클래스의 메서드를 호출합니다.

**3번 정답: 2**
메서드 오버라이딩은 부모의 메서드를 자식에서 재정의하는 것입니다.

**4번 정답: 2**
자식 클래스에서 오버라이딩한 메서드가 실행되어 "멍멍!"이 출력됩니다.

**5번 정답: 1**
Dog는 Animal을 상속받았으므로 True입니다.

---

## 🎯 **다음 장 예고**

다음 장에서는 클래스의 고급 개념인 특수 메서드, 프로퍼티, 정적 메서드 등을 배웁니다. 더욱 전문적이고 파이썬다운 객체지향 프로그래밍을 할 수 있게 됩니다!

---

수고했습니다.   
조정현 교수([peterchokr@gmail.com](mailto:peterchokr@gmail.com)) 영남이공대학교

이 수업자료는 Claude와 Gemini를 이용하여 제작되었습니다.
