![](https://velog.velcdn.com/images/woojin-devv/post/0fda64f1-a4ab-43fe-9184-4de731a7023c/image.png)


#### pubspec.yaml
```
flutter:
  assets:
    - assets/images/
  fonts:
    - family: GyeonggiBatang
      fonts:
        - asset: fonts/GyeonggiBatang_Bold.ttf
        - asset: fonts/GyeonggiBatang_Regular.ttf
    - family: GyeonggiTitle
      fonts:
        - asset: fonts/GyeonggiTitle_Light.ttf
          weight: 300
        - asset: fonts/GyeonggiTitle_Medium.ttf
          weight: 500
        - asset: fonts/GyeonggiTitle_Bold.ttf
          weight: 700
    - family: GyeonggiTitleV
      fonts:
        - asset: fonts/GyeonggiTitleV_Bold.ttf

```

-> 이런식으로 적용해서 

#### code
```
Text(
                      '학부모 / 자녀 ',
                      style: TextStyle(
                        fontFamily: 'GyeonggiTitle',
                        fontSize: 14,
                        fontWeight: FontWeight.w300,
                        color: Color(0xff525152),
                      ),
                    ),
```

fontweight을 적용했더니, ios에서 적용이 안된다. 
![](https://velog.velcdn.com/images/woojin-devv/post/de4248a6-ecef-4d7d-b913-67d5174005ae/image.png)


- 폰트 파일의 내부 Weight Class (예: 300 = Light, 400 = Regular)가 실제로 어떻게 적용되어있는지 파악하기 위해 https://fontdrop.info/ 를 접속해서 확인해봤더니, Weight class가 300으로 지정되어 있었음에도 불구하고 ios 디바이스에서는 font weight이 적용이 되지 않음을 확인 했다. 
- 그래서 안드로이드 에뮬레이터에서도 돌려보니.. 안드로이드 에뮬레이터에서는 font weight이 적용이 되어있었다.
- 결론 = pubspec.yaml 문제는 아님
  - 그래서 구글링을 해서 좀 찾아보았다. 
  - https://github.com/flutter/flutter/issues/75832
  -> Font Weight Light이 weight < 400일 경우, ios 혹은 web 환경에서 렌더가 안되는 이슈가 있었다. 


> 어쨌든, 해결은 해야한다. 
결론, 폰트 family 클래스별로 분류하지 말고 폰트 단일 파일별로 분류를 해야했다. 



#### 수정한 pubspec.yaml
```
  fonts:
    - family: GyeonggiBatangBold
      fonts:
        - asset: fonts/GyeonggiBatang_Bold.ttf
    - family: GyeonggiBatangRegular
      fonts:
        - asset: fonts/GyeonggiBatang_Regular.ttf
    - family: GyeonggiTitleLight
      fonts:
        - asset: fonts/GyeonggiTitle_Light.ttf
    - family: GyeonggiTitleMedium
      fonts:
        - asset: fonts/GyeonggiTitle_Medium.ttf
    - family: GyeonggiTitleBold
      fonts:
        - asset: fonts/GyeonggiTitle_Bold.ttf
    - family: GyeonggiTitleVBold
      fonts:
        - asset: fonts/GyeonggiTitleV_Bold.ttf

```

#### code
```
                    Text(
                      '학부모 / 자녀 ',
                      style: TextStyle(
                        fontFamily: 'GyeonggiTitleLight',
                        fontSize: 14,
                        fontWeight: FontWeight.w300,
                        color: Color(0xff525152),
                      ),
                    ),

```

![](https://velog.velcdn.com/images/woojin-devv/post/f9c5a114-5a7d-49c3-afcf-ca2a1c162245/image.png)



