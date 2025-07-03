## 1. 직렬화 (Serialization)
> [Object -> JSON]으로 바꾸는 것
- Flutter 앱 안에서 사용하는 객체를 저장하거나 전송가능한 형태인 JSON 형태로 변환하는 작업 
- 서버에 전송 혹은 DISK에 저장할 때 필요

## 2. 역직렬화 (Deserialization)
> 데이터(JSON, 문자열등) -> Object로 변환

## 3. toJSON 메소드 예시 
```dart
import 'dart:convert';

import 'package:equatable/equatable.dart';

// ignore_for_file: public_member_api_docs, sort_constructors_first
class Person extends Equatable {
  final int id;
  final String name;
  final String email;

  const Person({required this.id, required this.name, required this.email});

  @override
  String toString() => 'Person(id: $id, name: $name, email: $email)';

  Person copyWith({int? id, String? name, String? email}) {
    return Person(
      id: id ?? this.id,
      name: name ?? this.name,
      email: email ?? this.email,
    );
  }

  //serializaiton, deseiralization은 API에서 보통 처리
  //APP에서는 Map만 처리해주면 되는 경우가 많음
  @override
  List<Object> get props => [id, name, email];

  //toMap Method
  Map<String, dynamic> toMap() {
    return <String, dynamic>{
      'id': id,
      'name': name,
      'email': email,
    };
  }
    //fromMap Method
  factory Person.fromMap(Map<String, dynamic> map) {
    return Person(
      id: map['id'] as int,
      name: map['name'] as String,
      email: map['email'] as String,
    );
  }

  String toJson() => json.encode(toMap());

  factory Person.fromJson(String source) => Person.fromMap(json.decode(source) as Map<String, dynamic>);
}
```

