// 虽然JS 和C++ ,Java 一样的有this ，但是Js表现是不同的
// 原因在于C++,Java是静态编译型语言，this 是在编译期绑定的，而JS是动态语言，运行期动态绑定的
// 注意
// 静态的概念和Python静态不同，相当于Python 中的类变量
// js本身这些版本之间都有这么多的问题。bind方法
// 

var school = {
    name :'magedu',
    getNameFunc : function(){
        console.log(this.name);
        console.log(this);
        return function(){
            console.log(1,this == global); // this 是否是global对象
            console.log(2,school === this);
            return this.name;
        }
    }
}

var school1 = {
    name :'hahahah',
}


var school2 = {
    name :'magedu',
    getNameFunc : function(){
        console.log(this.name);
        console.log(this);
        return function(x,y){
            console.log(1,this == global); // this 是否是global对象
            console.log(2,school === this);
            console.log(x,y);
            return this.name;
        }
    }
}


var school3 = {
    name :'magedu',
    getNameFunc : function(){
        console.log(this.name);
        console.log(this);
        return function(that){
            console.log(1,that == global); // this 是否是global对象window()
            console.log(2,school3 === that);
            return that.name;
        }
    }
}


var school4 = {
    name :'magedu',
    getNameFunc : function(){
        console.log(this.name);
        console.log(this);
        return () => {
            console.log(1,this == global); // this 是否是global对象window()
            console.log(2,school4 === this);
            return this.name;
        }
    }
}


func = school.getNameFunc();
func() ;    // this 表示的是全局变量
console.log(3,school.getNameFunc()());
console.log('==================================================================')
console.log(4,school.getNameFunc().call(school));
console.log('****************************************************')
console.log(5,school.getNameFunc().apply(school));
console.log('****************************************************')
console.log(5,school.getNameFunc().apply(school1));
console.log('****************************************************')
console.log(6,school2.getNameFunc().call(school,4,5));
console.log('****************************************************')
console.log(7,school2.getNameFunc().apply(school,[4,5]));
// that 
console.log('****************************************************')
console.log(8,school3.getNameFunc()(school3));
console.log('****************************************************')
console.log(9,school.getNameFunc().bind(school));//bind 之后返回的是一个新函数，新函数绑定了你指定的this
console.log('------------------------------------------------------------')
console.log(10,school.getNameFunc().bind(school)());// 
// 
newfunc = school.getNameFunc().bind(school);// 
newfunc();
console.log('------------------------------------------------------------')
console.log(10,school4.getNameFunc()());// 为了以防万一，我们临时的使用这个方法来实现
// 


