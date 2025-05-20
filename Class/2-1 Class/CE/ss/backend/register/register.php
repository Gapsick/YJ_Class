<?php
include "../db/db.php";

$user_id = $_POST['user_id'] ?? '';
$password = $_POST['password'] ?? '';
$check_password = $_POST['check_password'] ?? '';

// 1. 공백 확인
if (!$user_id || !$password || !$check_password) {
    die("모든 값을 입력해주세요.");
}

// 2. 비밀번호 일치 확인
if ($password !== $check_password) {
    die("비밀번호가 일치하지 않습니다.");
}

// 3. 아이디 중복 확인
$stmt = $conn->prepare("SELECT id FROM users WHERE user_id = ?");
$stmt->bind_param("s", $user_id);
$stmt->execute();
$stmt->store_result();

if ($stmt->num_rows > 0) {
    die("이미 존재하는 아이디입니다.");
}

// 4. 비밀번호 암호화 및 저장
$hashed_password = password_hash($password, PASSWORD_DEFAULT);
$insert = $conn->prepare("INSERT INTO users (user_id, password) VALUES (?, ?)");
$insert->bind_param("ss", $user_id, $hashed_password);
$insert->execute();

echo "회원가입 성공! <a href='../../login/index.html'>로그인 하러가기</a>";
?>
