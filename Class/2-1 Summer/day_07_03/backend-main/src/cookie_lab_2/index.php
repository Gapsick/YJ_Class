<?php 
if (isset($_COOKIE['username'])) {
    $username = htmlspecialchars($_COOKIE['username']);
    $latte = htmlspecialchars($_COOKIE['latte']);
    $icecoffee = htmlspecialchars($_COOKIE['icecoffee']);
    echo "{$username}님의 주문내용";
    echo "<li> 라떼 수량: {$latte}잔 </li>";
    echo "<li> 아이스 아메리카노 수량: {$icecoffee}잔 </li>";
    echo "<a href=edit_order.php>주문 수정</a> <br>";
    echo "<a href=delete_cookie.php>주문 초기화</a> <br>";
} else {
    echo "<form method='post' action='set_cookie.php'>
            이름: <input type='text' name='username'> <br>
            라떼 수량: <input type='text' name='latte'> <br>
            아이스 아메리카노 수량: <input type='text' name='icecoffee'> <br>
            <button type='submit'>주문하기</button>
    </form>";
}




?>