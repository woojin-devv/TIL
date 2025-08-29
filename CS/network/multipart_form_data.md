## table of contents
1. [`multipart/form-data`의 정의](#1-multipartform-data의-정의)
2. [`multipart/form-data`의 필요성 및 특성](#2-주요-특성과-역할)
3. [`multipart/form-data`의 사용법 및 handling](#3-클라이언트-to-서버-업로드-과정)
4. [`multipart/form-data` 예시](#4-example)



# 1. Multipart/form-data의 정의
> **Multipart/form-data**는 여러 종류의 데이터를 하나의 HTTP 요청 Body에 담아 전송할 수 있도록 설계된 [MIME 타입](#mime-타입)기반 인코딩 방식으로, 원래 이메일 첨부파일 전송을 위해 개발된 형식을 기반으로 한다. 
> - 주로 파일 업로드 및 복합 폼 데이터 전송에 사용된다. 
> - HTTP 헤더에서 [`content-type`](#content-type)지정 가능

# 2. 주요 특성과 역할
> - **혼합 데이터 전송**
>   - 텍스트, 파일(binary), 체크박스등 여러 타입의 데이터(e.g., text, images, JSON)를 한 번의 요청으로 서버에 전달할 수 있다. 
> - **boundary로 각 파트 구분** 
>   - Body 내부 데이터는 boundary(경계 문자열)로 파트별로 구분되고, 각 파트는 자체 Content-Disposition, Content-Type 등 헤더를 가짐. 
> - **파일 업로드에 최적화**
>   - HTML 폼(form)의 enctype 속성을 multipart/form-data로 지정하면, 파일과 기타 입력값(설명 등)을 한 번에 전송한다. 

# 3. 클라이언트 to 서버 업로드 과정 
> 1. 클라이언트가 웹브라우저인 경우, [form](#form)을 통해 파일을 등록 및 전송한다. 
> 2. 웹브라우저가 보내는 HTTP 메시지의 경우, `Content-Type`속성이 `multipart/form-data`로 지정되고 정해진 형식에 따라 메시지를 인코딩하여 전송한다. 
> 3. 서버는 multipart message에 대해 각 파트별로 분리하여 개별 파일의 정보를 얻게 된다. 

# 4. Example
```json
POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="username"

john_doe
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="profile_picture"; filename="profile.jpg"
Content-Type: image/jpeg

[Binary data of the JPEG file]
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="metadata"
Content-Type: application/json

{"age": 30, "location": "New York"}
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```
- Content-Type 헤더는 "주 타입/서브 타입" 형식을 기본으로 하며, 필요시 charset, boundary 등 추가 파라미터를 붙일 수 있다. 
    - 위 예시에서 주 타입은  `multipart`이며, 서브 타입은 `/form-data`이다.
    - 추가 파라미터는 `boundary`이하의 값이다. 

# 각주
## content-type
```
//Syntax
Content-Type: <media-type>
```
for example: 
```
Content-Type: text/html; charset=utf-8
Content-Type: multipart/form-data; boundary=ExampleBoundaryString
```
- HTTP Content-Type 헤더에는 다양한 MIME 타입을 지정할 수 있고, 이는 본문 데이터 형식을 명확하게 지정하는 역할을 함. 
> **주요 Content-Type**값 예시
> - text/plain: 일반 텍스트 데이터.
> - text/html: HTML 문서 
> - text/css: CSS 스타일시트
> - application/json: JSON 데이터 
> - application/xml: xml 데이터 
> - application/octet-stream: 바이너리 데이터, 주로 파일 다운로드 시 사용
> - multipart/form-data: 파일 및 데이터의 폼 전송 시 사용(예: 파일 첨부)
> - application/x-www-form-urlencoded: 폼 데이터 기본 타입.
> - image/png, image/jpeg, image/gif: 이미지 파일.
> - audio/mpeg, video/mp4: 오디오 및 비디오 파일

## MIME 타입
- MIME(Multipurpost Internet Mail Extensions)은 일종의 인코딩 방식
    - 이메일과 함께 보낼 첨부 파일을 텍스트 문자로 전환하기 위해 개발되었음
    - 7bit ASCII만 지원하던 이메일 시스템에서 바이너리를 텍스트로 안전하게 전달하기 위해 Base64 같은 인코딩을 도입함

## form
> form은 사용자 입력을 모아 서버로 전송하기 위한 입력 양식 전체를 감싸는 태그를 말한다. 
```javascript
<form action="/upload" method="POST" enctype="multipart/form-data">
  <input type="text" name="username" />
  <input type="file" name="profile_picture" />
  <button type="submit">Upload</button>
</form>

```

 **form의 주요 속성**
- `name`: 폼의 이름. 자바스크립트에서 폼을 식별할 때 주로 사용
- `action`: 데이터를 전송할 목적지 URL 지정 (비워둘 경우, 현재 페이지로 전송)
- `method`: 데이터를 서버로 전송할 HTTP 메서드 지정 (보통 GET(쿼리스트링 전송), POST(본문 전송) 사용)
- `autocomplete`: 브라우저의 자동 완성 기능을 사용할지 여부(`on`이 기본)
- `enctype`(encoding type):
    - `application/x-www-form-urlencoded`
        - 기본값
        - 모든 폼 데이터를 key=value&key2=value2 형태로 인코딩
        - 공백은 +로, 특수문자는 URL 인코딩됨
    - `multipart/form-data`
        - 파일 업로드 시 필수
        - 각 입력 필드를 boundary로 구분해 전송 (텍스트 + 파일 모두 가능)
    - `text/plain`
        - 디버깅용. 인코딩 없이 단순 텍스트로 전송

# 참고 자료 
- [Understanding multipart/form-data: The Ultimate Guide for Beginners](https://medium.com/@muhebollah.diu/understanding-multipart-form-data-the-ultimate-guide-for-beginners-fd039c04553d)
- [Content-Type header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type)