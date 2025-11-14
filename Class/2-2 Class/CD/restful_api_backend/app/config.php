<?php
// DB/경로 상수 + mysqli 예외 모드 설정(연결은 여기서 하지 않음)
define('DB_HOST', 'db');
define('DB_USER', 'root');
define('DB_PASS', 'root');
define('DB_NAME', 'gsc');


mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
