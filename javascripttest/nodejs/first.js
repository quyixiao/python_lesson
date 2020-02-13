
console.log('我是瞿贻晓')

console.log('我们测试他们东西')

// 你的环境变量是不是正确
// node js 的东西是不是在服务器中执行
// 

// 注释
// 和C,Java 一样
// 单行注释
// 注释，多行注释，也可以用在语句中

str = 'hello' + /*commnet */ 'magedu'
console.log(str)    

// 常量和变量
// 标识符 
// 标识符必须是字母，下划线，美元符号和数字，但必须是字母，下划线，美元符号开头，依然是不是能数字开头就行
// 标识符区分大小写
// 声明
// var 声明一个变量
// let 声明一个块作用域的局部变量
// const 声明一个常量
// JS 中的变量声明和初始化是可以分开的
// 

var a = 1 ; // 
let b ;
const c =20 ; // 声明一个常量
d = 5 ; 
b = 10 ;

console.log(a,b,c)

var y ; // 只是声明，y 的值是undefined 
var x ;     // 规范的声明并初始化，声明个事情或者局部的变量
x = 6 ;// 不规范的初始化，不推荐，在严格的模式下会产生异常，在赋值之前不能引用，因为它没有声明，一旦这样的赋值京是全局作用域 
// 
function hello(){
    f = 100;
}
hello();
var f = 20
console.log(f) //
// console.log(a) // 声明变量
// 常量和变量的选择
// 如果明确知道一个标识符定义后不再修改，应该尽量的声明成const常量 ，减少修改的风险，减少Bug
// 数据类型
// 常量对应的应用的内存地址不能变，但是引用的对象的属性是能变的
// number  数值型，包括整形和浮点型
// boolean  布尔型 ,true和false
// string   字符串
// null     只有一个值null
// undefined    变量的声明未赋值的，对象的未定义的属性
// symbol       ES6 新引入的类型
// object类型   是以上基本类型的复合类型，是容器
// ES 是动态语言，弱类型的语言
// 虽然先声明了变量，但是变量可以重新赋值任何类型
// 类型转换
// 弱类型
// 


console.log('============string======================')
console.log(a=3 + 'magedu',typeof(a))
console.log(a = null + ' magedu',typeof(a))
console.log(a = undefined + ' mage du ',typeof(a))
console.log(a = true + ' mage du ',typeof(a))

console.log('============boolean======================')
console.log(a = null + true ,typeof(a))
console.log(a = null + false ,typeof(a))
console.log(a = undefined + true ,typeof(a)) // undefined 没法转换成一个对应的数字 
console.log(a = undefined + false,typeof(a))
console.log(a = null & true ,typeof(a))

console.log('============boolean======================')
console.log(a =null && true ,typeof(a))  //逻辑运算符，null ,直接就是false 
console.log(a =false && true ,typeof(a)) // 逻辑运算符，false 就是短路返回false 
console.log(a = false && 'magedu.com' ,typeof(a)) // boolean 
console.log(a = true && 'mage',typeof(a))  // 字符串
console.log(a = true && '',typeof(a)) // 字符串
// 弱类型，不需要强制类型转换，会隐式类型转换
// NaN ，not a number ，转换数字失败
// 总结 ，遇到字符串，加号就是拼接字符串，所有的非字符串隐式转换为字符串
// 如果没有字符串，加号把其他的所有的类型都当数字处理，非数字类型隐式的转换成数字，undefined 特殊，因它都没有定义值
//let a = 'abc';
//var b = '123';
//let c = `x
//${a} 
//y 
//${b}
//z`

// \0    Nll字节
// \b    退格符
// \n       换行符
// 
console.log('-----------------------------------------------------------')
let school = 'magedu'
console.log(school.charAt(2))//g 
console.log(school[2])
console.log(school.toUpperCase())
console.log(school.concat('.com'))
console.log(school.slice(3))
console.log(school.slice(3,5))
console.log(school.slice(-2,-1))
console.log(school.slice(-2))
console.log('-----------------------------------------------------------')
let test = 'www.magedu.com'
console.log(test.split('.'))
console.log(test.substring(7,2))
console.log(test.substring(10,20))

console.log('-----------------------------------------------------------')
let s = 'magedu.edu'
console.log(s.indexOf('ed')) //3 
console.log(s.indexOf('ed',4))
console.log(s.replace('.edu','com'))
s='\tmage edu \r\n'
console.log(s.trim()) // 去除两端的空白字符，trimLeft ，trimRight 是非标函数，不要用
// 数值型
// 在JS 中数据均为双精度浮点型范围只能在-(2^53-1) 和2^53-1 之间，整型也不例外
// 数值类型还有三种符号值:+Infinity(正无穷),-Infinity(负无穷),和NAN(not-a-number非数字)
// 二进制0b0010,0B110
// 八进制0755,注意0855,被认作是十进制，因为8不在八进制中，
var bigestNum = Number.MAX_VALUE
var smallestNum = Number.MIN_VALUE
var infiniteNum = Number.POSITIVE_INFINITY
var negInfiniteNum = Number.NEGATIVE_INFINITY
var notANum = Number.NaN
console.log('------------------------------------------')
console.log(bigestNum)
console.log(smallestNum)
console.log(infiniteNum)
console.log(negInfiniteNum)
console.log(notANum)

console.log(1/0)


console.log('------------------------------------------')
console.log(a = Number.parseInt('123'),typeof(a))
console.log(a = parseFloat('123.32'),typeof(a))
// 这些Math 函数
console.log(Math.PI)
console.log(Math.abs(-10))
console.log(Math.random())

console.log(1/2)
console.log(parseInt(1/2))
console.log(Math.floor(3/2))
console.log(Math.ceil(3/2))
console.log(Math.round(1/2))
console.log(Math.round(3/2))






let i = 0 ;
let a = i ++
console.log(a,i)        //打印什么
console.log(a ,i++) // 打印什么
a = ++i 
console.log(a ,i) // 打印什么


















