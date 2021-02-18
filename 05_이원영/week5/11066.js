//22-1 11066

const process = require('process');
const argv = (() => {
	const obj = {};

	obj.source = '';
	obj.append = str => (obj.source += str);
	obj.end = () => (obj.data = obj.source.split(/ |(?:\r?\n)/));

	obj.data = [];
	obj.cursor = 0;
	obj.getNumber = () => Number(obj.data[obj.cursor++]);

	return obj;
})();

process.stdin.setEncoding('utf8');
process.stdin.on('data', data => argv.append(data));

process.stdin.on('end', () => {
	argv.end();

	const T = argv.getNumber();
	for (let t = 0; t < T; t++) {
		const N = argv.getNumber();
		const novel = new Array(N);
		for (let n = 0; n < N; n++) novel[n] = argv.getNumber();
		console.log(solution(novel));
	}
});

function solution(novel) {
	const dp = new Array(novel.length);
	for (let i = 0; i < novel.length; i++) {
		dp[i] = new Array(novel.length - i);
		for (let j = 0; j < novel.length - i; j++) dp[i][j] = undefined;
	}

	for (let i = 0; i < novel.length; i++) dp[i][novel.length - i - 1] = 0;

	const combine = (start, end) => {
		if (dp[start][novel.length - end] !== undefined) return dp[start][novel.length - end];

		dp[start][novel.length - end] = 0;
		for (let i = start; i < end; i++) dp[start][novel.length - end] += novel[i];

		if (end - start > 2) {
			let appropriateWay = 123456789;
			for (let i = 1; i < end - start; i++) {
				const way = combine(start, start + i) + combine(start + i, end);
				if (way < appropriateWay) appropriateWay = way;
			}

			dp[start][novel.length - end] += appropriateWay;
		}

		return dp[start][novel.length - end];
	};

	return combine(0, novel.length);
}
