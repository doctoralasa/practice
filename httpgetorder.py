Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import requests
ImportError: No module named 'requests'
>>> pip
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pip
NameError: name 'pip' is not defined
>>> pip3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pip3
NameError: name 'pip3' is not defined
>>> import sys
>>> print(sys.path)
['', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\idlelib', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\python35.zip', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\DLLs', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\lib', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\lib\\site-packages']
>>> open(sys.path)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    open(sys.path)
TypeError: invalid file: ['', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\idlelib', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\python35.zip', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\DLLs', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\lib', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35', 'C:\\Users\\kalse\\AppData\\Local\\Programs\\Python\\Python35\\lib\\site-packages']
>>> cd sys.path
SyntaxError: invalid syntax
>>> cd(sys.path)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cd(sys.path)
NameError: name 'cd' is not defined
>>> pip3.5
SyntaxError: invalid syntax
>>> pip3
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    pip3
NameError: name 'pip3' is not defined
>>> pip3 requests
SyntaxError: invalid syntax
>>> pip install requests
SyntaxError: invalid syntax
>>> pip install requests
SyntaxError: invalid syntax
>>> import requests
>>> r=requests.get(url='http://www.itwhy.org')
print(r.status_code)
r=requests.get(url='http://dict.baidu.com/s,params=')
>>> r=requests.get(url='http://dict.baidu.com/s',params={'wd':'python'})
print
>>> print()

>>> 
>>> 
>>> r=requests.get(url='http://www.itwhy.org')
print(r.status_code)
SyntaxError: multiple statements found while compiling a single statement
>>> r=requests.get(url='http://www.itwhy.org')
print(r.status_code)


>>> r=requests.get(url='http://dict.baidu.com/s',params={'wd':'python'})
pri
>>> print(r.url)
http://dict.baidu.com/s?wd=python
>>> print(r.text)


<!Doctype html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="https://m.baidu.com/static/index/icon/w_icon2.png" type="image/x-icon" />
    <meta name="keywords" content="python,python读音,python翻译,python的意思,python的造句,python故事"/>
    <meta name="description" content="百度词典python的解释: 百度词典_python，英文翻译，五笔，拼音，组词，例句，用法"/>
    <title>百度词典_python</title>
    <script>
var _hmt = _hmt || [];
var _ziciURL = "//hm.baidu.com/hm.js?aa7a77b165b2c996a2c4b0493fbdbc2b";
var _dictURL = "//hm.baidu.com/hm.js?304463b8a93092da95f0ed0515fb47be";

(function() {
  var hm = document.createElement("script");
  hm.src = _dictURL;
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>        <link rel="stylesheet" href="/asset/css/main.css" />
    <link rel="stylesheet" type="text/css" href="/asset/css/style.css?v=0.2.1" />
    </head><body class="pc module" id="pc-empty-body" data-prop="" data-name="python">

<div style="display:none">
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F304463b8a93092da95f0ed0515fb47be' type='text/javascript'%3E%3C/script%3E"));

window.__start_time = +(new Date());
</script>
</div>
    <div id="search-bar">
        <div class="wrapper">
        <div style="margin-right:300px;position: relative">
    <div class="dict-logo"><a href="/" title="百度词典"></a></div>
    <div class="search-box module" id="search-box">
        <form name="f" id="form" action="" class="fm">
            <span class="bg s_ipt_wr quickdelete-wrap">
                <input id="kw" name="wd" class="s_ipt" value="python" maxlength="40" autocomplete="off">
                <input id="ptype" name="ptype" class="s_ipt" value="empty" type="hidden">
            </span>
            <span class="bg s_btn_wr focus">
                <input type="submit" id="su" value="百度一下" class="bg s_btn">
            </span>
        </form>
    </div>
</div>        <div class="wrap-userbar module" id="wrap-userbar">
    
    <ul class="userbar logout">
    <li class="userbar-item">
        <a href="https://passport.baidu.com/v2/?login&tpl=mn&u=http://dict.baidu.com/s?wd=python" id="login_link">登录</a>
    </li>
    <li class="pipe userbar-item">|</li>
    <li><a href="/download" name="tj_cidian" class="userbar-item download-link">手机版</a></li>
    <li class="pipe userbar-item">|</li>
    <li class="userbar-item">
        <a href="http://www.baidu.com" target="_blank">百度首页</a>
    </li>
    </ul>
</div>        </div>
    </div>
    <!-- 外层包裹 -->
    <div id="body-wrapper">
    <div id="main" class="module">
        <div id="update_tips_div" style="display: none;">
            <div>用&nbsp;<a class="tips-export-a" href="http://hanyu.baidu.com" onclick="_hmt.push(['_trackEvent','汉语导流', '中间页导流', 'PC首页banner跳首页点击']);">百度汉语</a>&nbsp;查看更全面更权威的汉语知识，在百度汉语中查看&nbsp;“<a href="http://hanyu.baidu.com/s?wd=python"  onclick="_hmt.push(['_trackEvent','汉语导流', '中间页导流', 'PC首页banner跳实体页点击']);
            ">python</a>”<img src="/asset/img/icon_hand_click.png"></div>
            <a class="tips-div-close" onclick="_hmt.push(['_trackEvent','汉语导流', '中间页导流', 'PC首页banner关闭点击']);"><img src="/asset/img/icon_close.png"/></a>
        </div>
        <div class="left nav-list module" id="nav-list"></div>
        <div class="content-panel module" id="content-panel">
            <div id="qa-tip" style="display:none"></div>
    

<div class="tab-list module" id="empty-body">


<div class="content" id="fanyi-wrapper">
    <h1><b class="title" id="fanyi">翻译</b></h1>
    <div class="tab-content">
                <p>
            <div style="display:inline-block">python</div>
            <a href="?wd=蟒蛇">蟒蛇</a>
        </p>
            </div>
</div>


    <div class="content" id="baike-wrapper">
    <h1><b class="title" id="baike">百科解释</b></h1>
    <div class="tab-content">
        <p>
            Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议。Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。常见的一种应用情形是…
            <a href="http://baike.baidu.com/view/21087.htm" target="baike">查看百科</a>
        </p>
    </div>
</div>

</div>        <div id="right-panel" class="right module">
            <div class="recmd-panel module" id="recmd-panel">
                                <div class="list">
                                </div>
            </div>
        </div>
    </div>
    <!--content-panel-->
    </div>
    </div>
    <!--body-wapper-->
</div>

<div id="scroll-top"></div>

<p id="copyright">©2017 Baidu
        <a href="http://www.baidu.com/duty/">使用百度前必读</a> 
        <a href="http://www.baidu.com">百度首页</a>
        <a href="/search" style="display:none">站内搜索</a>
        <a href="http://help.baidu.com/add?prod_id=8#1">问题反馈</a>
        <a href="http://weibo.com/5789783834/manage">关注微博</a>
        <span href="#">用户QQ群：484758177</span>
</p>

<div id="fmp_flash_div" style="display:none"><audio id="audio"></audio></div>

<script src="/asset/asset/dep/zepto/zepto.min.js"></script>
<script src="/asset/asset/dep/esl/esl.min.js"></script>

<script>

require.config(
    {
        baseUrl: '/asset/asset',
        urlArgs: 'v=0.2.1'
    }
);
require(['main']);

$("#kw")[0].focus();
window.__finish_time = + (new Date());
window.__used_time = __finish_time - window.__start_time;
</script>

</div>
</body>
</html>
>>> requests.get('https://github.com/timeline.json') #get请求
<Response [410]>
>>> requests.post("http://httpbin.org/post")
<Response [200]>
>>> 
