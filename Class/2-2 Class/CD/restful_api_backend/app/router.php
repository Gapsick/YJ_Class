<?php
// routes: METHOD → path → callable(string 함수명 or [fn, args])
$ROUTES = [
    'GET' => [
        '/students' => 'students_index',
        '/students/{id}' => 'students_show',
    ],
    'POST' => [
        '/students' => 'students_create',
    ],
    'PUT' => [
        '/students/{id}' => 'students_update',
    ],
    'DELETE' => [
        '/students/{id}' => 'students_delete',
    ],
];

function dispatch(array $routes): void
{
    $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
    $path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);

    // 정적 경로 우선
    if (isset($routes[$method][$path])) {
        $fn = $routes[$method][$path];
        if (function_exists($fn)) {
            $fn();
            return;
        }
    }


    // /users/{id} 같은 패턴 매칭
    foreach ($routes[$method] ?? [] as $pattern => $fn) {
        $regex = '#^' . preg_replace('#\{[^/]+\}#', '([^/]+)', $pattern) . '$#';
        if (preg_match($regex, $path, $m)) {
            array_shift($m);
            if (function_exists($fn)) {
                $fn(...$m);
                return;
            }
        }
    }
    json_response(['error' => 'Not Found'], 404);
}
