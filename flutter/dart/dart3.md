## 1. async란?
> 작성하는 함수가 비동기 함수임을 나타내는 keyword
- 일반 함수를 작성하면, 코드가 위에서 아래로 순차적으로 실행됨
- `async` 함수는 `await`와 함께 사용해서 시간이 오래 걸리는 작업을 기다렸다가 결과를 받아 처리할 수 있음.

### 1.1 async 함수가 필요한 배경 
- API 호출
- 파일 읽기/쓰기 
- DB 읽기
- 인터넷에서 이미지 불러오기 
위와 같은 작업을 sync로 처리하게 되면 앱이 멈춘 것처럼 보이게 됨

### 1.2 사용법
#### 1.
```dart
Future<void> fetchData() async {
  // 비동기 작업
}
```

### 1.3 