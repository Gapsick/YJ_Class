<?php session_start() ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Login</h1>

    <?php if (isset($_SESSION['error']))
    echo "<p style='color:red'>".htmlspecialchars($_SESSION['error'])."</p>";
    unset($_SESSION['error']);
    ?>

    <form action="login_check.php" method="post">
        ID: <input type="text" name="user_id"><br>
        PW: <input type="text" name="user_pw"><br>
        이름: <input type="text" name="user_name"><br>
        <input type="submit" value="로그인">
    </form>

    
    <h2>혹시 계정이 없으시다면</h2>
    <button>
        <a href="register.php">회원가입</a>
    </button>


</body>
</html>