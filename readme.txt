This module needs selenium moudle,so make sure the module is downloaded before you use this.
You can login to Naver with your id and pw by calling execute_login_process(). After calling the function, you will have to call close_login_session() to quit the webdriver

**
The location of chromedriver is very important. Please make sure that the chromedriver is in the same directory of naver_login.py. Otherwise you will have to change the location of chromedriver manually in naver_login.py. 
**

Kor__

이 모듈은 Selenium 모듈을 필요로 합니다. 이 모듈을 사용하기전에 Selenium이 설치되어있는지 확인해주세요.
excute_login_process()를 호출함으로써, 네이버에 로그인 할 수 있습니다. 이 함수를 호출한다음에는 webdriver를 닫기위해 close_login_session()함수를 호출해주세요.

**
chromedirver의 위치는 매우 중요합니다. chromedriver가 naver_login.py와 같은 디렉토리에 있는지 확인해주세요. 원하시면 naver_login.py에서 chromedriver의 위치를 바꿀수도 있습니다.
**
