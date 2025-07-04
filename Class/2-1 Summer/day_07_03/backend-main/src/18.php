<?php 
# 값 저장
$listValue = [$_POST['value1'], $_POST['value2'], $_POST['value3'], $_POST['value4'], $_POST['value5']];
$avg = array_sum($listValue) / 5;

// 전역변수 선언
global $vx;

// 표본분산 계산
foreach ($listValue as $value) {
    $vx += (pow($value - $avg, 2) / 4);
}

// 표본표준편차 계산
$ax = round(sqrt($vx),2);

// 출력
echo "입력값 : {$listValue[0]} {$listValue[1]} {$listValue[2]} {$listValue[3]} {$listValue[4]}" . "<br>";
echo "평균 : {$avg}" . "<br>";
echo "분산 : {$vx}" . "<br>";
echo "표준편차 : $ax"
?>