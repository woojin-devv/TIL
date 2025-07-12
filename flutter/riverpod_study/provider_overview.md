# Provider Overview

## 1. Provider
> 가장 기본적인 쓰임 -> widget이나 다른 provider에게 값을 제공하는 용도
> - The provider is the most basic of the providers offered by Riverpod
> - The "Provider" creates value
 
### 1.1 Riverpod에서 제공하는 Provider의 종류 
> - StateProvider
> - StateNotifierProvider
> - ChangeNotifierProvider
> - NotifierProvider
> - AsyncNotifierProvider
> - FutureProvider
> - StreamProvider
> - StreaNotifierProvider

### 1.2 기존 상태관리 Solution vs Riverpod provider
> -  Provider가 특정 Widget에서 watch될 때, 해당 Provider의 상태(state)가 변경되면 그 상태를 watch(구독)한 위젯만 리빌드된다.
> - **Riverpod** : 한 provider가 다른 provider를 watch할 수 있어, **provider 간 의존성 관리**가 가능
```
ProviderA <- ProviderB <- Widget
// 화살표 방향은 watch (ProviderB가 ProviderA를 watch하고, Widget이 ProviderB를 watch함)
```
> - ProviderA → 변경됨
> - ProviderB → ref.watch(ProviderA) 하고 있으므로 ProviderB의 build 메서드 재실행
> - 이로 인해 ProviderB의 결과값이 바뀌면, 이를 watch하던 Widget도 리빌드됨

## 2. Todo앱에서 Provider예시 
```
todosProvider <-- completedTodosProvider <-- ShowCompletedTodos 위젯
         (watch)                  (watch)

```
> - todosProvider는 state로 `List<Todo> todos`를 제공
> - **State를 변경시킬 수 있는 Method**
>   - `addTodo`
>   - `toggleTodo`
>   - `editTodo`
>   - `removeTodo`
가 존재한다고 가정하자. 

이 `TodosProvider`를 watch(구독)하며,List에서 완료된 항목들을 관리하는 CompletedTodosProvider(Provider)가 존재한다고 가정하자.
```dart
completedTodosProvider(Provider)
return todos.where(
    (todo) => todo.completed,
).toList()
```
-> return값들은 todos 리스트 중 완료된 항목들만 
- todosProvider를 통해 만든 provider임
    - todosProvider를 watch하고있으므로, state가 변할 때, completedTodosProvider가 rebuild됨
-  completedTodosProvider는 ShowCompletedTodos라는 widget에 값들을 제공하게되고, rebuild될 경우 ShowCompletedTodos라는 widget 또한 Rebuild 된다.

## 3. Provider Modifier
> **Modifier의 역할** : Provider의 동작을 조정 
> 1. **none**
>    - 아무런 modifier도 적용하지 않은 기본 provider의 상태
> 2. **autoDispose**
>    - Provider가 더 이상 사용되지 않을때, 자동으로 해제    
> 3. **family**
>    - provider 생성 시, 파라미터 전달, 동적으로 값 변경 가능
> 4. **autoDispose + family**
>    - 자동해제 + 파라미터 값 받음
