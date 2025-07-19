<?php 
session_start();

// 세션 데이터 삭제
session_destroy();

// 세션 쿠키 삭제
if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie(
        session_name(), '', time() - 42000,
        $params["path"], $params["domain"], $params["secure"], $params["httponly"]
    );
}

// 다시 로그인 페이지 리다이렉트
header("Location: login.php");
exit;