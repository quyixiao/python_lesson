// 字面式声明方式
// 这种方法也称作字面值创建对象
// ES6之前，构造器
// 1.定义一个函数构造器对象，函数名首字母大写
// 2.使用this定义属性
// 3. 使用new和构造器创建一个新的对象
// this 指代当前实例本身 ,当前实例本身
// 
var obj={ // 定义类
    'a':100,
    'b':200,
    'show':function(){
        console.log('show')
    }
}

var obj1 = new Object();
var obj2 = new Date();
function Point(x,y){
    this.x = x ;
    this.y = y ;
    console.log(33333333,this);
    this.show = function(){
        console.log(4444,this,this.x,this.y);
    }

}
console.log('------------------------------------------------')
var obj3 = Point(4,5);
console.log('++++++++++++++++++++++++++++++++++++++++++')
console.log(typeof obj3);
console.log('------------------------------------------------')
//console.log(obj3.x);   console.log(obj3.x);

var obj4 = new Point(5,6);
console.log(typeof obj4);
console.log(obj4.x);
obj4.show();
var obj5 = new Point(5,6);
console.log(obj4.show === obj5.show); //每次new 的时候


function Point1(x,y){
    this.x = x ;
    this.y = y ;
    console.log(33333333,this);
    this.show = show;

}

console.log('************************************************************')
function show(){
    console.log(this,this.x,this.y);
}
var obj6 = new Point1(5,6);
var obj7 = new Point1(5,6);
console.log(obj6.show === obj7.show); //每次new 的时候
console.log('-----------------------------------------')
//继承 
function Point3D(x,y,z){
    Point.call(this,x,y);//传递this 动态的增加了x,动态增加了y,动态增加了show方法,用于继承
    this.z = z ;
    this.show = ()=>{
        console.log(this,this.x,this.y,this.z);
    }
}
p3d = new Point3D(6,6,8);
p3d.show();
// new 是构建一个新的通用的对象，new操作符会将新的对象的this传递给Point3D 构造器函数，函数为这个对象创建z属性，
// 从上面的句话就知道，new后得到了一个对象，使用这个对象，使用这个对象的this来调用构造器，那么如何执行基类的构造器方法呢？
// 






