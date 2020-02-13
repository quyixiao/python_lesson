const a = function add (){
    console.log('a func')
};

const b = function (){
    console.log('b func')
}

const add = function _add(x,y){
    return x + y ;
};




c = add(1,2);
console.log(c);
console.log(add(4,6)) // ReferenceError: _add is not defined


a ();
b();
