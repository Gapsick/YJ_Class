<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    $_SESSION['error'] = "잘못된 접근 입니다.";
    header("Location: login.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>환영합니다, <?= htmlspecialchars($_SESSION['user_name']) ?>님!  </h2>
    <a href="logout.php">로그아웃</a>
</body>
</html>