# [Gold V] 소수상근수 - 9421 

[문제 링크](https://www.acmicpc.net/problem/9421) 

### 성능 요약

메모리: 128512 KB, 시간: 716 ms

### 분류

수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>양의 정수 n의 각 자리수의 제곱의 합을 계산한다. 그렇게 해서 나온 합도 각 자리수의 제곱의 합을 계산한다. 이렇게 반복해서 1이 나온다면, n을 상근수라고 한다.</p>

<p>700은 상근수이다.</p>

<ul>
	<li>7<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 49</li>
	<li>4<sup>2</sup> + 9<sup>2</sup> = 97</li>
	<li>9<sup>2</sup> + 7<sup>2</sup> = 130</li>
	<li>1<sup>2</sup> + 3<sup>2</sup> + 0<sup>2</sup> = 10</li>
	<li>1<sup>2</sup> + 0<sup>2</sup> = 1</li>
</ul>

<p>2는 상근수가 아니다.</p>

<ul>
	<li>2<sup>2</sup> = 4</li>
	<li>4<sup>2</sup> = 16</li>
	<li>1<sup>2</sup> + 6<sup>2</sup> = 37</li>
	<li>3<sup>2</sup> + 7<sup>2</sup> = 58</li>
	<li>5<sup>2</sup> + 8<sup>2</sup> = 89</li>
	<li>8<sup>2</sup> + 9<sup>2</sup> = 145</li>
	<li>1<sup>2</sup> + 4<sup>2</sup> + 5<sup>2</sup> = 42</li>
	<li>4<sup>2</sup> + 2<sup>2</sup> = 20</li>
	<li>2<sup>2</sup> + 0<sup>2</sup> = 4</li>
	<li>4<sup>2</sup> = 16</li>
	<li>... 끝나지 않는다</li>
</ul>

<p>소수는 1과 자기자신을 제외하고 약수가 없는 수이다. 2, 3, 5, 7, 11, 13, 17, 19, ... 는 소수이다.</p>

<p>소수상근수는 소수이면서 상근수인 숫자이다. 7, 13, 19, ... 는 소수 상근수이다.</p>

<p>n이 주어졌을 때, n보다 작거나 같은 모든 소수상근수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 n (10 ≤ n ≤ 1000000)이 주어진다.</p>

### 출력 

 <p>n보다 작거나 같은 소수상근수를 한 줄에 하나씩 오름차순으로 출력한다.</p>

