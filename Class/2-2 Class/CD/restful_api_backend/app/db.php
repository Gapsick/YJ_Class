<?php
require_once __DIR__ . '/config.php';

function get_db(): mysqli {
    try {
        $db = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        $db->set_charset('utf8mb4');
        return $db;
    } catch (Throwable $e) {
        if (session_status() === PHP_SESSION_NONE) session_start();
        $_SESSION['error'] = 'DB 연결 오류';
        error_log('[DB] ' . $e->getMessage());
        throw $e; // 상위에서 500 JSON 처리
    }
}
