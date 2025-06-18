## 🟢 해쉬테이블 만들어지는 원리에 대한 쉬운 정리  

### 📚 연결 리스트 기반 해시테이블 (체이닝 방식) - 쉬운 정리  

---

### ✅ 1. 해시테이블은 어떻게 생겼나요?  

해시테이블은 **칸이 여러 개인 배열**입니다.  
이 배열의 각 칸은 **연결 리스트(줄)**로 연결되어 있습니다.  

#### 🧱 그림: 초기 상태 (버킷 5개 예시)  

```
bucketList = [  
    dummy → None,   # 0번 칸  
    dummy → None,   # 1번 칸  
    dummy → None,   # 2번 칸  
    dummy → None,   # 3번 칸  
    dummy → None    # 4번 칸  
]  
```

- 각 칸은 연결 리스트의 시작이며, **dummy node (비어있는 노드)**로 시작합니다.  
- 실제 데이터는 dummy 뒤에 붙습니다.  

---

### ✅ 2. 예시: "cat"이라는 키를 삽입하면?  

#### 🔍 해시값 구하기  

```python
def getHash("cat"):  
    total = ord("c") + ord("a") + ord("t")  
         = 99 + 97 + 116 = 312  
    index = 312 % 5 = 2  
```

➡ **"cat"은 bucketList[2]에 저장됨**  

---

### ✅ 3. 연결 리스트에 삽입하기 (head insertion)  

#### 🧱 기존 구조 (2번 버킷에 아무 것도 없음)  

```
bucketList[2] = dummy → None  
```

#### 📦 "cat" 노드를 만들고, 연결하기  

```python
bucket = Node("cat")  
bucket.next = self.bucketList[2].next  # None  
self.bucketList[2].next = bucket  
```

#### 🔁 구조 변화  

```
bucketList[2] = dummy → (cat) → None  
```

---

### ✅ 4. 그 다음 "rain"도 같은 인덱스(2)에 들어가면?  

```python
bucket = Node("rain")  
bucket.next = (cat)  
self.bucketList[2].next = (rain)  
```

#### 📊 결과  

```
bucketList[2] = dummy → (rain) → (cat) → None  
```

> 새 데이터를 항상 **맨 앞(head)**에 붙이는 방식  

---

### 🧠 삽입 과정 요약 그림  

#### 기존 구조:  

```
dummy → A → B → None  
```

#### 새 노드 C 삽입  

```python
C.next = dummy.next  # 즉 A  
dummy.next = C  
```

#### 결과 구조:  

```
dummy → C → A → B → None  
```

---

### ✅ total = 0은 왜 필요한가요?  

```python
def getHash(self, key):  
    total = 0  
    for k in key:  
        total += ord(k)  
    return total % self.cnt  
```

- `total = 0`은 문자의 아스키 코드 합을 누적할 **시작값**입니다.  
- key = "cat" → ord('c') + ord('a') + ord('t') = 312 → 인덱스 = 312 % 버킷 수  

---

### 📦 전체 구조 예시  

```
bucketList = [  
    dummy → None,  
    dummy → (school) → (home) → None,  
    dummy → (rain) → (cat) → None,  
    dummy → None,  
    dummy → (chair) → None  
]  
```

---

