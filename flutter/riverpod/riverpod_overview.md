## 1. Why Riverpod?
- State Management를 하기 위한 Tool
- Remi가 만듦

> ### Riverpod 특징
- 유연한 state caching
- 편리한 async state handling
- widget rebuild optimization
- 문서화가 잘 되어 있음 -> 기본을 익힌 후에 self-study하기 용이함


## 2. What is Riverpod?
> **Riverpod** is a reactive caching framework for Flutter/Dart
> Using declarative and reactive programming, Riverpod is able to take care of a large part your application's logic for you. It can perform netwrok-requests with built-in error handling and caching, while automatically re-fetching data when necessary

> ### 배경
- App에 대한 요구사항 증가 (빠르게 요구사항을 수용해야함) -> data가 복잡해짐에 따라 State management가 더욱 강조됨
>### 요구사항 예시
- 특정 페이지를 빠져나와도 데이터가 유지되어야 함
- 특정 페이지를 빠져나올 때 데이터가 Reset되었으면 함
- 이 페이지는 한 번 액세스한 사용자가 다시 한 번 더 보는 경우가 많기 때문에 10분 동안은 데이터가 유지되고 10분이 지난 후에 데이터를 reset하길 요함
- 앱은 외부 데이터에 의존, 하지만 UI에서 API 호출하지 말 것
- UI에서는 데이터 변화를 Watch하고 있다가 데이터 변화가 생길 경우 UI를 새로 그리길 요함
- 외부 데이터를 불러 올 때마다 반복되는 data loading case나 error case는 간단하게 처리하길 요함

## 3. Riverpod Package
> 1. `flutter_riverpod`
> 2. `hook_riverpod`

- `riverpod_lint`
    - a package designed to help developers avoid commom mistakes and simplify repetitive tasks
    - (optional, but recommened)


## 4. 준비 작업 

 1. App의 widget을 `ProviderScope()`로 감쌈
```dart
//App에서 만든 모든 widget을 관리하기 위함
//상태 공유 및 의존성 주입을 위한 루트 컨테이너
void main() {
    runApp(
        ProviderScope(
            child: MyApp(),
        ),
    );
}
```