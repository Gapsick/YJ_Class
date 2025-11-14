<?php
declare(strict_types=1);

session_start();

require_once __DIR__ . '/../app/http.php';
require_once __DIR__ . '/../app/router.php';
require_once __DIR__ . '/../app/controllers/students.php';

apply_cors();

// 프리플라이트
if ($method === 'OPTIONS') {
        http_response_code(204);
        return;
}

// routes 배열 가져와서 디스패치
global $ROUTES;
dispatch($ROUTES);
