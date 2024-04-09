#!/usr/bin/node
/* slice is to remove the first 2 default arguments */
const arg = process.argv.slice(2);
/* check mumber of arg is 0 or 1 */
if (arg.length === 0 || arg.length === 1){
	console.log(0);
} else {
	/* arg to integers using map */
	const integers = arg.map(Number);
	/* sort the integers in descending order */
	const sortedIntegers = integers.sort((a, b) => b - a);
	console.log(sortedIntegers[1]);
}
