<?php
session_start();
require_once('./db_connect.php');

// 1. DB 연결
$db_conn = new mysqli(DB_INFO::dbURL, DB_INFO::dbid, DB_INFO:: dbpw, DB_INFO:: dbname);

// DB 연결 실패 시
if ($db_conn->connect_errno) {
    $_SESSION['error'] = "DB 연결 실패";
    header("Location: register.php");
    exit;
}

// 2. 값 들고오기
$user_id = trim($_POST['user_id']);
$user_pw = trim($_POST['user_pw']);
$user_name = trim($_POST['user_name']);

// 3. 유효성 검사
// 3-1. 값이 비어 있을 경우
if ($user_id === "" || $user_pw === "" || $user_name === "") {
    $_SESSION['error'] = "회원가입 - 값 비어있음";
    header('Location: register.php');
    exit;
}

// 4. 비밀번호 해싱
$password_hashed = password_hash($user_pw, PASSWORD_DEFAULT);

// excape 처리 -> 문자열 그대로 저장
$user_id = $db_conn->real_escape_string($user_id);
$user_pw = $db_conn->real_escape_string($password_hashed);
$user_name = $db_conn->real_escape_string($user_name);

// DB에 값 저장
$query = "INSERT INTO users (username, password, name) values ('$user_id', '$user_pw', '$user_name')";

// 회원가입 

// 주의점 -> error랑 exception이랑은 다름
// ex) 코드 문법이 틀림 -> error
// ex) 중복 값이 있음 -> error는 아닌 exception임

// 해결 방법
// 1. try, catch문 사용
// 2. 예외 모드 끄기



// 1. try, catch문을 사용했을 경우
try {
    $db_conn->query($query);
    $db_conn->close();
    header("Location: login.php");
    exit;
} catch (mysqli_sql_exception $error) {
    if ($error->getCode() === 1062) {
        $_SESSION['error'] = "중복 아이디";
    } else {
        $_SESSION['error'] = "회원가입 실패";
    }

    header("Location: register.php");
    exit;
}



// // 2. 예외 모드를 껐을 경우
// if ($db_conn->query($query)) {
//     // 회원가입 성공
//     // db 닫기
//     $db_conn->close();
//     header("Location: login.php");
// } else {
//     // 회원가입 실패
//     // 1. 중복 아이디
//     if ($db_conn->errno === 1062) {
//         $_SESSION['error'] = "중복 아이디";
    
//     // 그 외 실패 사유들
//     } else {
//         $_SESSION['error'] = "회원가입 실패";
//     }

//     // DB 닫고 register.php 리다이렉션
//     $db_conn->close();
//     header("Location: register.php");
//     exit;
// }