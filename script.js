arr = ['apple', 'banana', 'grapes', 12, 23, 55, 67, 43]

let [apple, banana, grapes, ...other] = arr

console.log(apple);
console.log(banana);
console.log(grapes);
console.log(other);