<?php
session_start();

if(session_id() !== '') {
    echo "세션 시작 중";
}

if (session_status() == PHP_SESSION_ACTIVE) {
    echo "<br>세션 활동 중";
}

// Create, update
$_SESSION['std_info'] = [
    "id" => 2423009, "name" => "김성식"
];

if (isset($_SESSION['std_info'])) {
    $_SESSION['std_info'] = [
        "id" => 2423009, "name" => "김성관"
    ];
} else {
    echo "학생 정보 없음";
}


?>