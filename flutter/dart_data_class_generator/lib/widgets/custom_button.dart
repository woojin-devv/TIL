// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'package:flutter/material.dart';

class CustomButton extends StatelessWidget {
  final String title;
  final Widget child;
  const CustomButton({super.key, required this.title, required this.child});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(5),
      child: FilledButton(
        onPressed: () {
          Navigator.of(context).push(MaterialPageRoute(builder: (_) => child));
        },
        child: Text(title, style: TextStyle(fontSize: 18)),
      ),
    );
  }
}
