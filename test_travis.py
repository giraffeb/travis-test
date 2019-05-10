import os
import requests
import timeit


working_dir = os.getcwd()
default_driver_path = working_dir+'/geckodriver'
default_driver_file_path = default_driver_path+'/geckodriver'
default_config_path = working_dir+'/sample.yaml'

url_list=['http://snui.snu.ac.kr/main/css/NanumGothic.woff',
          'http://snui.snu.ac.kr/ocw/index.php?mode=view&id=623',
          'http://snui.snu.ac.kr/main/js/jquery-ui-1.10.3.custom.min.js',
          'http://snui.snu.ac.kr/lms/mod/lcms/player/js/jwplayer.js',
          'http://extcm.c.appier.net/bizspring?bzuid=cfrKNRK8AXns1sGUrzAbQU0GrXr5i1vvhXg4O0do&url=%2F%2Ftm.bizspring.co.kr%2Fappier.php%3Fbzuid%3DcfrKNRK8AXns1sGUrzAbQU0GrXr5i1vvhXg4O0do%26appieruid%3D%25%25APPIER_UID%25%25',
          'http://snui.snu.ac.kr/lms/auth/uniquetab/unique.js.php',
          'http://snui.snu.ac.kr/main/js/jquery-1.10.2.min.js',
          'http://cdn-aitg.widerplanet.com/js/wp_astg_3.0.js',
          'http://snui.snu.ac.kr/lms/mod/lcms/player/swf/player.swf',
          'http://snui.snu.ac.kr/lms/mod/lcms/player/skins/darkrv5.zip',
          'http://snui.snu.ac.kr/admin/userfiles/file.php?d=files&f=nowon(525).JPG']


def test_proxy_two():
    print("PROXY TIME")

    test_proxy = '206.189.234.211:80'

    proxies = {
        'http': test_proxy
    }

    s = requests.Session()
    s.proxies = proxies

    for url in url_list:
        print('#->',url)
        start = timeit.default_timer()
        r = s.get(url)
        stop = timeit.default_timer()
        print('SECOND -> ',stop - start)

def test_proxy_three():
    print("DEFAULT TIME")


    s = requests.Session()

    for url in url_list:
        print('#->', url)
        start = timeit.default_timer()
        r = s.get(url)
        stop = timeit.default_timer()
        print('SECOND -> ',stop - start)
