const arr = [1,[2,3],4];
const [a,[b,c],d] = arr;//1 2 3 4
console.log(a,b,c,d);

const [e,...f] = arr;//1 [ [ 2, 3 ], 4 ]
console.log(e,f);