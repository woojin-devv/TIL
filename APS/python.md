## 1. 배열 역순 나열
```python
list[start:end:step] 활용
list[::-1]
```
### 예시 
```python 
list = [1,2,3,4,5]
reverse_list = list[::-1]
print(reverse_list)
```
> 결과 `[5, 4, 3, 2, 1]`

## 2. list의 element값 형태 변환 
### 2.1 list의 문자형 원소를 숫자형 원소로 바꾸기
> 예시) list_a=['1', '2', '3', '4'] -> list_a=[1,2,3,4]로 변환
```python
list_a=list(map(int, list_a))
```
- map() 함수 기본 문법
```python
map(function, iterable)
```
- map 함수는 iterable의 각 요소에 대하여 function 함수를 적용한 결과를 새로운 iterator로 변환한다. 
- function 함수는 각 요소를 인자로 받아서 처리하며, 함수의 반환값이 새로운 iterator의 각 요소가 됨



## 3. iterable
> iterable 객체 : 반복 가능한 객체 
- list, dict, set, str, bytes, tuple, range


## 4. 에러 
### 4.1 Type error
> TypeError: 'NoneType' object is not iterable
- for 루프나 리스트 언팩킹 등에서 None 값을 반복하려고 할 때 발생