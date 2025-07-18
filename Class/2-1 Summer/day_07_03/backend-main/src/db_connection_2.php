<?php
require_once("./db_conf.php");

// 1. 연결 설정
$db_conn = new mysqli(DB_INFO::DB_HOST, DB_INFO::DB_USER, DB_INFO::DB_PASS, DB_INFO::DB_NAME);

if($db_conn->connect_errno) {
    echo "DB Error: " . $db_conn -> connect_error;
    exit;
}

// 2. 연결 설정
$sql = "select * from student";
$result = $db_conn->query($sql);

// mysqli_result -> fetch_filed(), fetch_fields();
$field_info = $result->fetch_field();
foreach ($field_info as $key => $field) {
    echo $key.":".$field."<br>";
}

echo "<hr>";




if(!$result) {
    echo "Query Error: ".$db_conn->error;
    exit;
}


$db_conn->close();