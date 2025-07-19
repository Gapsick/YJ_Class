<?php session_start() ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php if (isset($_SESSION['error']))
        echo "<p style='color:red'>".htmlspecialchars($_SESSION['error'])."</p>";
        unset($_SESSION['error']);
    ?>
    
    <h1>회원가입</h1>

    <form action="register_check.php" method="post">
        ID: <input type="text" name="user_id"><br>
        PW: <input type="text" name="user_pw"><br>
        이름: <input type="text" name="user_name"><br>
        <input type="submit" value="회원가입">
    </form>


</body>
</html>