// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'package:dart_class/models/person.dart';
import 'package:dart_class/models/user.dart';
import 'package:dart_class/repositories/fetch_user.dart';
import 'package:flutter/material.dart';

class UserListPage extends StatefulWidget {
  const UserListPage({super.key});

  @override
  State<UserListPage> createState() => _UserListPageState();
}

class _UserListPageState extends State<UserListPage> {
  //init
  List<User> users = [];
  String error = '';
  bool loading = false;

  @override
  void initState() {
    super.initState();
    _fetchUser();
  }

  void _fetchUser() async {
    try {
      setState(() => loading = true);
      users = await fetchUsers();
      error = '';
    } catch (e) {
      error = e.toString();
    } finally {
      setState(() => loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Users')),
      body:
          loading
              ? const Center()
              : error.isEmpty
              ? ListUsers(users: users)
              : buildError(),
    );
  }

  Widget buildError() {
    return Center(
      child: Padding(
        padding: EdgeInsets.all(30),
        child: Column(
          children: [
            Text(
              error,
              style: TextStyle(fontSize: 18),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 20),
            OutlinedButton(onPressed: _fetchUser, child: Text('Retry')),
          ],
        ),
      ),
    );
  }
}

class ListUsers extends StatelessWidget {
  final List<User> users;
  const ListUsers({super.key, required this.users});

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      itemBuilder: (BuildContext context, int index) {
        final user = users[index];
        return ListTile(
          leading: CircleAvatar(child: Text(user.id.toString())),
          title: Text(user.name),
        );
      },
      separatorBuilder: (BuildContext context, int index) {
        return Divider();
      },
      itemCount: users.length,
    );
  }
}
