
## Contents
1. [Key Questions](#key-questions)
2. [Hacking Map](#hacking-map)
   - [A. Threat Actors](#a-threat-actors)
   - [B. Target](#b-target)
3. [CVSS](#cvss-the-common-vulnerability-scoring-system)
4. [Attack Vector](#attack-vector-av)

## **Key questions**

- **Q. What does “hacking” mean in the lecture?**

- **Q. Why do we learn Windows?**

- **Q. What is the attack model considered in the lecture?**

## **Hacking Map**

### **A. Threat Actors**

1. Individual
2. State-Sponsored (예: 중국, 북한, 러시아 etc)
3. Cyber-crime
    1. 랜섬웨어 → 암호화 + 데이터 유출 (사례: 서울 보증공사)

### **B. Target**

1. Organization
2. Real World (CPS: Cyber physical System ; 소프트 웨어로 제어 가능한 물리적 장치)
    1. 예시) 자동차의 페달

## **CVSS; The Common Vulnerability Scoring System**

> 사이버 보안 시스템에서 발생하는 취약점의 심각도를 평가하기 위한 개방형 프레임 워크
> >It provides a way to capture the principal characteristics of a vulnerability and produce a numerical score in from 0 to 10 reflecting its severity.
> 

### **CVSS base metric consists of the Exploitability and Impact**

<aside>
Exploitability
1. Attack Vector
2. Attack Complexity
3. Privileges Required
4. User Interaction
</aside>

<aside>
Impact
보안의 3요소 (C I A)
1. Confidentiality
2. Integrity
3. availability
</aside>

## **Attack Vector (AV)**

> 공격자가 취약점을 활용할 때 접근하는 방식의 분류
> 

### **1. Network(N)**

- 공격자가 인터넷이나 원거리 네트워크를 통해 공격 가능
    - The vulnerable component is bound to **the network stack**[¹⁾](#1-os가-네트워크-통신을-처리하는-계층-구조osi-7계층-중-tcpip-스택)
    - **특정 패킷이나 요청을 보내는 것만으로도** 취약점을 악용할 수 있음 → 원격 공격 가능

### **2. Adjacent(A)**

- The attack is limited *at the protocol level to a* logically adjacent topology.
    - **bluetooth or IEEE 802.11**
    - logical (e.g., local IP subnet) network

### **3. Local(L)**
- The vulnerable component is **not** bound to the network stack.
    - The attacker’s path is via read/write/execute capabilities.
    - by accessing the target system locally (e.g., keyboard, console), or remotely (e.g., SSH);
    - The attacker relies on **User Interaction (using social engineering techniques)**

### **4. Physical(P)**

- The attack requires the attacker to physically touch or manipulate the vulnerable component.
    - [The vulnerability of Thunderbolt | Thunderspy ](https://thunderspy.io/)

→ Network, Adjacent 모두 Network Stack에 취약점에 의해 vulnerable component가 생김


## **미주** 

#### 1. OS가 네트워크 통신을 처리하는 계층 구조(OSI 7계층 중 TCP/IP 스택)
- 예: IP, TCP/UDP, ARP, ICMP 같은 프로토콜이 포함