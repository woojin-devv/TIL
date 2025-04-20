![](https://velog.velcdn.com/images/woojin-devv/post/c3e4b25b-0e0b-4cb5-a8cd-5381cab7b51b/image.png)

# 개요

> REST, REST API, RESTful에 대한 정의와 특징
> 

---

# 1. API란?

**API(Application Programming Interface)**는 소프트웨어 시스템 간에 기능이나 데이터를 주고받을 수 있도록 정해진 규칙, 명령, 프로토콜을 제공하는 인터페이스

- 한 프로그램이 다른 프로그램의 기능이나 데이터를 사용할 수 있도록 해주는 일종의 다리 역할을 한다.
- API는 운영체제, 라이브러리, 데이터베이스, 하드웨어 등 다양한 환경에서 동작할 수 있으며, 반드시 네트워크를 사용할 필요는 없다.
    - 예시 ) 운영체제 API(Windows API, macOS API), 라이브러리 API(파이썬 pandas 등)

| 용어 | 설명 | 추가정보 / 예시 |
| --- | --- | --- |
| Client | 웹에서 정보에 액세스하려는 사용자 | 사용자는 웹 브라우저, 앱 등 다양한 클라이언트로 서버에 요청을 보냄 |
| Server(서버) | 클라이언트에 리소스를 제공하는 시스템 | 클라이언트 요청을 받아 리소스를 전달하거나 조작하는 역할을 담당 |
| Resource(리소스) | 클라이언트에게 제공하는 정보 | REST에서 서버가 관리하는 모든 데이터 또는 객체 (예: 문서, 사진, DB 내용 등) |

# 2. REST란?

**REST(Representational State Transfer)**는 웹에서 자원의 상태를 표현(Representation)하여 전송(Transfer)하는 아키텍처 스타일

- REST는 HTTP 프로토콜을 기반으로 하며, 자원(Resource)에 대한 고유 식별자(URI)를 사용한다.
- 클라이언트는 서버의 자원에 접근하거나 상태를 변경할 때 JSON, XML 등으로 데이터를 주고받는다.

## 2.1 REST API와 RESTful의 차이

- REST API: REST 원칙을 따르는 API로, HTTP URI로 자원을 명시하고, HTTP Method(POST, GET, PUT, DELETE 등)로 해당 자원에 대한 CRUD(생성, 조회, 수정, 삭제)를 구현한다.
- RESTful: REST의 원칙을 잘 지키도록 설계된 API를 의미한다. RESTful하지 않은 API는 단순히 웹 API 또는 HTTP API로 부른다.

## 2.2 REST의 주요 특징

| 특징 | 설명 |
| --- | --- |
| Uniform Interface | URI로 리소스를 식별하고, HTTP 표준 방식으로 조작한다. |
| Stateless | 서버는 클라이언트의 상태를 따로 저장하지 않고, 각 요청은 독립적으로 처리 |
| Cacheable | HTTP 표준 캐싱 기능을 활용하여 성능을 높일 수 있음 |
| Client-Server 구조 | 클라이언트와 서버의 역할이 명확히 분리되어 의존성이 줄어듦 |
| Layered System | 중간 서버(프록시, 게이트웨이 등)을 둘 수 있어 유연성이 높아짐 |
| Self-descriptiveness | 메시지 자체에 필요한 정보를 포함하기 때문에 별도의 description없이 이해 가능 |

## 2.3 REST API 설계 기본 규칙

1. URI는 자원을 표현한다
    - 동사 대신 명사 사용 / 대문자 대신 소문자 사용
    - 단수 명사는 객체, 복수 명사는 컬렉션 표현
        - 예) `/members/1` (O),  `Member/1` (X)
2. 행위는 HTTP Method로 표현
    - `GET, POST, PUT, DELETE` 등
    - URI에 동사나 행위가 포함되면 안됨
    - `GET /members/1` (O),  `GET /members/delete/1`(X)
3. 슬래시 (/)는 계층 관계 표현, 마지막에 사용하지 않는다.
    - `/users/123/devices` (O),  `/users/123/devices/` (X)
4. 하이픈을 사용하되, 언더스코어는 피한다. 
    - 예: `/user-groups` (O), `/user_groups` (X)
5. 소문자 사용, 파일 확장자 사용 금지
    - 예: `/users` (O), `/Users.json` (X)

## 2.4 **RESTful API 클라이언트 요청 / 응답 예시**

- 가령, 사용자 관리(User Management)를 위한 RESTful API가 존재한다고 가정.
    - 클라이언트는 이 API를 통해 User를 생성하거나 조회할 수 있음
    - RESTful API의 설계에 따라 `/users` 라는 URI로 사용자 리소스를 나타내고, 다양한 HTTP 메서드를 적용 가능함

### 2.4.1 RESTful API 예시 - HTTP Method

| HTTP Method | URI | 설명 |
| --- | --- | --- |
| **GET** | `/users` | 클라이언트는 GET을 사용하여 서버의 지정된 URL에 있는 리소스에 액세스한다. (users의 모든 사용자 조회) |
| **GET** | `/users/{id}` | 특정 사용자 조회한다. (users group의 id값에 따른) |
| **POST** | `/users` | 클라이언트는 POST를 사용하여 서버에 데이터를 전송(새로운 사용자 추가) |
| **PUT** | `/users/{id}` | 클라이언트는 PUT을 사용하여 서버의 기존 리소스를 업데이트 (users group의 새로운 사용자 추가) |
| **DELETE** | `/users/{id}` | 클라이언트는 DELETE 요청을 사용하여 리소스를 제거(사용자 삭제) |
- HTTP Method를 통해 해당 자원에 대하여 CRUD Operation을 적용할 수 있다.


### CRUD란?

> **C**reate: 데이터 생성 (Post)
**R**ead: 데이터 조회 (GET)
**U**pdate: 데이터 수정 (PUT, PATCH)
**D**elete: 데이터 삭제 (DELETE)



## 2.5 REST API 설계 규칙

1. 슬래시 구분자 (/)는 계층 관계를 나타내는데 사용한다. 
    - `/users/123/devices`는 “123번 사용자”의 “devices”라는 하위 리소스를 의미
2. URI 마지막 문자로 슬래시(/)를 포함하지 않는다.
    - REST API에서 URI의 마지막에 슬래시(/)를 붙이지 않는 것은, 혼란을 방지하고 일관성 있는 리소스 식별을 위해 지켜야 할 중요한 설계 규칙이다.
    - 식별자 일관성: URI의 모든 문자는 리소스의 고유 식별자에 포함된다. 즉, `/api/items`와 `/api/items/`는 엄밀히 따지면 서로 다른 URI이며, 다르게 인식될 수 있다
    - 웹 서버나 프레임워크에 따라 두 URI를 동일하게 처리하기도 하지만, 명확하고 예측 가능한 API를 제공하기 위해서는 마지막에 슬래시를 붙이지 않는 것이 표준

---

### 참조

[RESTful API란 무엇인가요? - RESTful API 설명 - AWS](https://aws.amazon.com/ko/what-is/restful-api/)