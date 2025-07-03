<?php 
if(isset($_POST['user_name']) && isset($_POST['user_age'])) {

    $name = $_POST['user_name'];
    $age = $_POST['user_age'];
} else {
    echo "잘못된 접근!!";
}

echo "{$name}님 환영합니다.";
echo "{$age}살 입니다";


?>