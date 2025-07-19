<?php
session_start();

require ('./db_connect.php');

// DB 연결
$db_conn = new mysqli(DB_INFO::dbURL, DB_INFO::dbid, DB_INFO:: dbpw, DB_INFO:: dbname);

// DB 연결 실패 시
if ($db_conn->connect_errno) {
    $_SESSION['error'] = "DB 연결 실패";
    header("Location: login.php");
    exit;
}

// POST값 받음
$user_id = $_POST["user_id"];
$user_pw = $_POST["user_pw"];
$user_name = $_POST["user_name"];

// 유효성 검사
// 1. 값이 비어 있을 경우
if ($user_id === "" || $user_pw === "" || $user_name === "") {
    $_SESSION['error'] = "값이 비어있음";
    header('Location: login.php');
    exit;
}

// DB에 값이 있는지 확인
$query = "SELECT * FROM users WHERE username = '$user_id'";
$result = $db_conn->query($query);

// DB 연결 종료 (리소스 반환)
$db_conn->close();

// 조회 결과 로직
if ($result && $row = $result->fetch_assoc()) {

    // 비밀번호 확인
    if(($user_pw === $row['password'])) {
        // 맞으면 로그인 성공
        $_SESSION['user_id'] = $row['id'];
        $_SESSION['user_name'] = $row['name'];
        header("Location: main.php");
        exit;
    } else {
        // 비밀번호 안맞음
        $_SESSION['error'] = "비밀번호 안맞음";
        header("Location: login.php");
        exit;
    }

} else {
    // 사용자 값이 없음
    $_SESSION['error'] = "아이디가 없음";
    header("Location: login.php");
    exit;
}








