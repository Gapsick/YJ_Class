<?php 
// 쿠키 있는지 확인
if (!isset($_COOKIE['username'])) {
    $username = trim($_POST['username']);
    setcookie('username', $username, time() +3600, '/');
    header("Location: index.php");
    exit;
}
?>