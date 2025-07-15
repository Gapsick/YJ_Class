<?php
session_start();

// Read
$name = $_SESSION['std_info']['name'];
echo $name;

// Delete
unset($_SESSION['std_info']['name']);

// Delete All

// 메모리상 삭제 (세션 변수 초기화)
$_SESSION = [];

// 세션 파일 삭제
session_destroy();

if (ini_get("session.use_cookies")) {
    // 현재 세션 쿠키의 설정 정보 가져오기
    $params = session_get_cookie_params();

    // 세션 쿠키 삭제 (만료 시간: 과거)
    setcookie(session_name(), '', [
        'expires' => time() - 3600,
        'path' => $params['path'],
        'domain' => $params['domain'],
        'secure' => $params['secure'],
        'httponly' => $params['httponly'],
        'samesite' => $params['samesite'] ?? 'Lax'
    ]);
}




print_r($_SESSION);

?>