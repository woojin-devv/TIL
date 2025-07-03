//https://jsonplaceholder.typicode.com/users 에서 유저 데이터를 받아서 User 객체 리스트로 반환
import 'package:dart_class/models/user.dart';
import 'package:dio/dio.dart';

Future<List<User>> fetchUsers() async {
  try {
    final Response response = await Dio().get(
      'https://jsonplaceholder.typicode.com/users',
    );
    final List userList = response.data;

    //test case
    print(userList[0]);

    //Dio package를 사용하는 동안, json string을 map으로 변환하는 과정을 거칠 필요가 없음
    final users = [for (final user in userList) User.fromMap(user)];

    print(users[0]);
    return users;
  } catch (e) {
    rethrow;
  }
}
