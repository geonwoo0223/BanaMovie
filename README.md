# 종합 프로젝트

**필수** 사전 생성 파일

*  `.env.local` 

  * 생성 경로 : final-pjt-front/.env./local

  ```
  VUE_APP_SERVER_URL=서버주소
  
  VUE_APP_SEARCH_URL=https://api.themoviedb.org/3/search/movie?api_key
  
  VUE_APP_API_KEY=TMDB키값
  ```

  * 예시

  ![image-20201126141952996](images/image-20201126141952996.png)

  



## 개발환경

### A. 언어

* Python 3.7.7
* Django 3.1.3
* Node 14.15.0
* Vue.js @vue/cli 4.5.8 





## 개발 팁



### 1. 화면에 pk 숫자 대신 username 출력하는 방법

일반적으로 아래와 같이 models.py를 정의할 때 테이블에 user를 ForiegnKey로 잡는다.

![image-20201121030257955](images/image-20201121030257955.png)

이렇게 하게 되면 user의 pk가 테이블 데이터가 저장이 되고, 시리얼라이징을 통해 vue로 값을 전달할 때 user의 username이 전달되는 것이 아니라 pk인 숫자가 전달된다.



![image-20201121030434023](images/image-20201121030434023.png)

위와 같이 시리얼라이저를 만들 때, user로 하기 때문에 자연스럽게 pk 값만 들어가고 전달이 되는 것

따라서 **유저 시리얼라이저를 만들고 'user'에 매핑할 user 객체를 생성해주면 된다. **

![image-20201121030557334](images/image-20201121030557334.png)



1. `get_user_model` 을 import한다. (User를 직접 불러오지 않고 안전하게 get_user_model을 써야 함)

   ```python
   from django.contrib.auth import get_user_model
   ```

2. User에서 가져오고 싶은 값을 골라서 Serializer 클래스를 만든다.

3. 원래 있던 시리얼라이저에 내가 만든 **User시리얼라이저 인스턴스 생성**

   * 이 때 인스턴스의 이름은 반드시 **<u>필드의 컬럼명과 동일해야 한다.</u>**

* 결과 화면

  ![image-20201121031208784](images/image-20201121031208784.png)

**※주의사항 : 이렇게 데이터를 전송했을 경우, vue 에서 타입을 undefined로 잡는 경우가 있다. 따라서 이럴 경우에는 템플릿이 아닌 함수에서 username 을 직접 this변수에 저장해서 그대로 출력한다.**

![image-20201121045524950](images/image-20201121045524950.png)





#### ManyToMany필드에서 여러 값을 보낼 때도 같은 방법을 사용한다. 

단, 여러 값이 들어가므로 커스터마이징한 인자에 `many=True` 를 설정해준다. 

![image-20201121031354261](images/image-20201121031354261.png)







## 오류와 해결방법

