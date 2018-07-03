from naver_login import login



if __name__ == '__main__':
    my_session = login()
    is_logined = my_session.execute_login_process()
    
    my_session.close_login_session()