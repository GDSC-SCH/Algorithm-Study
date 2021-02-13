//17-1 10828
const fs = require('fs');
//const input = fs.readFileSync('/dev/stdin').toString().split('\n'); //임시 할당

var num = 7;
var command = ['pop', 'pop', 'push 123', 'top', 'pop', 'top', 'pop'];
var stack = [];

for (let i = 1; i <= num; i++) {
    if (command[i] === 'top') {    //top
        if (stack.length === 0) {
            console.log(-1);
        }

        else {
            console.log(stack[stack.length - 1]);
        }
    }

    else if (command[i] === 'size') {  // size
        console.log(stack.length);
    }

    else if (command[i] === 'empty') {    //empty
        if (stack.length === 0) {
            console.log(1);
        }

        else {
            console.log(0);
        }
    } 
    
    else if (command[i] === 'pop') {   //pop
        if (stack.length === 0) {
            console.log(-1);
        }

        else {
            console.log(stack.pop());
        }
    }

    else {  //push
        stack.push(Number(command[i].split(' ')[1]));
    }
}
