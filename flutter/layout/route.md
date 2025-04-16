
## 📁 디렉터리 구조
```dart
lib
├── main.dart
└── screens
    ├── main_screen.dart
    └── splash_screen.dart
```

## 실행흐름
- 앱 실행 시 '/'에서 시작됨
    - `'/' : (context) => const SplashScreen()` 으로 설정되어 있어, 앱을 실행하면 SplashScreen UI가 첫 화면으로 초기화됨
    - `splash_screen.dart`에서는 다음과 같이 작성되어 있어, 2초 후에 `'/main'` 경로로 이동하도록 되어 있음:
        
        ```dart
        Future.delayed(const Duration(seconds: 2), () {
          Navigator.pushNamed(context, '/main');
        });
        ```

### GIF
<div align="center">
  <img src="https://velog.velcdn.com/images/woojin-devv/post/7029ea58-1c69-4092-85ef-ebe0911d4f51/image.gif" width="200" />
</div>


        
## 소스코드 
### main.dart
```dart
import 'package:flutter/material.dart';

class SplashScreen extends StatelessWidget {
  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    Future.delayed(const Duration(seconds: 2), () {
      Navigator.pushNamed(context, '/main');
    });
    return Scaffold(
      appBar: AppBar(),
      body: const Center(
        child: Text('Splash Screen'),
      ),
    );
  }
}
```

### main_screen.dart
```dart
import 'package:flutter/material.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MainScreen'),
      ),
      body: const Column(),
    );
  }
}
```

### splash_screen.dart
```dart
import 'package:flutter/material.dart';

class SplashScreen extends StatelessWidget {
  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    Future.delayed(const Duration(seconds: 2), () {
      Navigator.pushNamed(context, '/main');
    });
    return Scaffold(
      appBar: AppBar(),
      body: const Center(
        child: Text('Splash Screen'),
      ),
    );
  }
}
```

