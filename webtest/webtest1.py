# CS即客户端，服务端编程
# 客户端，服务端之间需要使用Socket ，约定的协义，版本，往往使用的协义TCP 或者UDP,指定地址和商品，就可以通信了
# 客户端，服务端传输数据，数据可以有一定的格式，双方必须先约定好
# BS编程，即Brower,server开发
# Browser浏览器，一种特殊的客户端，支持HTTP(s)协义，能够通过URL向服务端发起请求，等待服务端返回HTML等待服务端发起请求，HTML
# 等数据，并在浏览器内可视化展示的程序
# Server，支持HTTP(s)协义一座城池，经过处理，将HTML等 ，并在浏览器内可视化展示的程序
# Server，支持HTTP(s)协义，能够的亲爱人多客户端发起的HTTP协义请求经过处理，将HTML等数据返回给浏览器
# 本质上，
# 使用httpd服务，观察http 协义
# http 协义是无状态的协义
# 同一个客户端的再次请求之间没有任何关系，从服务器端角度来说，它不知道这两个请求来自同一个客户端
# 键值对信息
# 浏览器发起每一次请求时，都会把cookie信息发给服务器端
# 是一种客户端，服务器端传递数据的技术
# 协义Http协义是一个无状态的协义，
# 同一个客户端两次请求没有任何关系，从服务器端角度来说，它不知道这两个请求同一个客户端
# cookie
# 键值对信息
# 浏览器发起每一个请求时，都会把cookie信息发给服务端
# 是一种客户端，服务器端的技术
# 服务端可以能完决断这些信息，来确定这次请求是否有，总有第一次，这些值是怎样来的呢？联接服务器，请求
# URL 组成
# URL 可以说就是地址，uniofrm resource locator 统一资源定位符 ，每一个链接指向一个资源，10个
# 这个没有的值是怎样的，但是唯一的值是我们发送给他们的，服务器端，由客户端，sessionid
# cookie 是动态网页技术中的一种动态的技术，保存的值
# 服务器看到这些值就可以发送了，没有建立什么关系的，这里面不仅仅，
# 最简单的方式，可以保存一些信息在里面，登陆信息在里面，登陆信息在，cookie 在里面是名文保存的，就算你压缩 了
# 计算机性能就可以算出来的，这个地方我们有很多的东西需要做，cookie 里有很多的不安全的 方法，我们必须要强加密的方法来做的
# cooKie 中有很多的无状态的，所以，我们就可以将数据在客户端和服务端来做的，我们就可以通过cookie 和session来完成无状态的
# 你觉得长时间没有来连接这些东西，在服务器没有用的，http协义就是为了短期的时间来完成
# url 可以说是地址，uniform resource locator 统一资源定位符，每一个链接指向一个资源供客户端访问
# schema://host[:port#]/path/.../[;url-params][?query-string][#anchor]
# 例如，通过下面的URL访问网页
# http://www.magedu.com/pathon/index.html?id=5&name=python
# 访问静态资源时，通过上面这个url访问网站的某个路径下的index.html文件，而这个文件对应的是磁盘上的真实的文件，就会从磁盘上读取这个文件
# 并把文件的内容改回浏览器端
# scheme模式，协义：
# http,ftp,https,mailto等等，mysql
# www.magedu.com:80 80商品默认是商品可以不写，域名使用DNS解析，域名会解析成ip才能使用，实际上会对解析后返回的TCP的80端口发起访问
# 请求消息行，请求的方法Method请求的路径协义版本CRLF
# 请求方法Method
# GET 请求获取 URL 对应的资源
# POST 提交数据到服务器端
# HEAD 和GET类似，不过不返回消息的正文
# GET : HTTP/1.1
# HOST :www.baidu.com
# User-agent: MOzilaz
# Accept-Encoding:gzip,deflate
# Cookie: 53gid2=10019938298932983
# Connection : keep-alive
# Upgrade-Insecure-Requsts:1
# 常见的传递信息的方式
# 1.GET 方法使用的是Query String
# http://www.magedu.com/pathon/index.html?
#