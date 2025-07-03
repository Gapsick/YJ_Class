<?php 

// 변수 선언
// 변수 자료형
// 점근 범위
// 생명 주기

// hoisting

// 변수의 접근 범위
// 변수의 생명 주기
// - 출생 - 소멸
//   선언   전역, 지역

$bar = "hello";

function foo() {
    global $bar;
    
    print $bar;
}

foo();



// 자바 -> 블럭 기반
// python -> 함수 기반
// php -> 함수 기반






?>