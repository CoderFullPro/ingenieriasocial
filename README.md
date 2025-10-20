# 🎯 ingenieriasocial
### Herramienta Avanzada de Ingeniería Social

* **Creado por:** MidasOrion
* **Versión:** 8.0.3
* **Nombre código:** 'Maverick'
* **Basado en:** The Social-Engineer Toolkit (SET) de TrustedSec

---

## 📖 Descripción

**ingenieriasocial** es una herramienta avanzada de pruebas de penetración diseñada específicamente para ingeniería social. Esta versión ha sido completamente traducida al español y mejorada con nuevas funcionalidades, templates modernos y un dashboard web en tiempo real.

La herramienta incluye múltiples vectores de ataque personalizados que te permiten crear ataques realistas de forma rápida y efectiva.

### ⚠️ DESCARGO DE RESPONSABILIDAD

Esta herramienta es **SOLO** para propósitos de pruebas y educación. Solo puede ser utilizada donde se haya dado consentimiento estricto. **NO** uses esta herramienta para propósitos ilegales.

**Uso exclusivo para:**
- ✅ Pruebas de penetración autorizadas
- ✅ Educación y capacitación en ciberseguridad
- ✅ Investigación de seguridad
- ❌ **NO** para actividades ilegales

---

## 🚀 Características Principales

### 🎨 **Interfaz Completamente en Español**
- Todos los menús y mensajes traducidos
- 10 banners ASCII personalizados
- Interfaz moderna y profesional

### 🎭 **Templates de Phishing Modernos**
- **Instagram** - Diseño idéntico al original
- **WhatsApp Web** - Interfaz actualizada 2024
- **MetaMask** - Wallet de criptomonedas

### 📊 **Dashboard Web en Tiempo Real**
- Visualización de capturas en vivo
- Estadísticas por plataforma
- Exportación de datos (JSON, CSV, TXT)
- Auto-refresh cada 5 segundos

### 🔧 **Sistema de Actualización**
- Script de actualización automática
- Backup de capturas
- Restauración de datos

---

## 💻 Plataformas Soportadas

- ✅ **Kali Linux** (Recomendado)
- ✅ **Parrot OS**
- ✅ **Ubuntu/Debian**
- ✅ **Mac OS X** (Experimental)

---

## 📦 Instalación

### **Instalación Rápida en Kali Linux**

```bash
# Clonar el repositorio
git clone https://github.com/CoderFullPro/ingenieriasocial.git

# Entrar al directorio
cd ingenieriasocial

# Ejecutar instalador automático
sudo chmod +x install_kali.sh
sudo ./install_kali.sh

# Iniciar la herramienta
sudo ./ingenieriasocial
```

### **Instalación Manual**

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y python3 python3-pip git apache2 php

# Instalar dependencias de Python
sudo pip3 install pexpect pycrypto pyopenssl pefile impacket flask flask-cors

# Clonar repositorio
git clone https://github.com/CoderFullPro/ingenieriasocial.git
cd ingenieriasocial

# Dar permisos
chmod +x ingenieriasocial

# Ejecutar
sudo ./ingenieriasocial
```

---

## 🎯 Uso Básico

### **Iniciar ingenieriasocial:**
```bash
sudo ./ingenieriasocial
```

### **Iniciar Dashboard:**
```bash
./start_dashboard_simple.sh
```
Luego abre tu navegador en: `http://localhost:8000/dashboard_simple.html`

### **Actualizar la herramienta:**
```bash
./upgrade.sh
```

---

## 📚 Documentación

- **Instalación completa:** [INSTALL_KALI.md](INSTALL_KALI.md)
- **Guía de actualización:** [UPGRADE.md](UPGRADE.md)
- **Templates de phishing:** [src/templates/phishing/README.md](src/templates/phishing/README.md)
- **Dashboard:** [src/dashboard/README.md](src/dashboard/README.md)

---

## 🌐 Vectores de Ataque Disponibles

### **1. Ataques de Ingeniería Social**
- Ataques de Spear-Phishing
- Vectores de ataque web
- Ataques de correo masivo
- Ataques de QRCode
- Ataques de PowerShell

### **2. Templates de Phishing**
- Instagram (Captura usuario/contraseña)
- WhatsApp Web (Captura código QR)
- MetaMask (Captura seed phrase)

### **3. Dashboard de Monitoreo**
- Visualización en tiempo real
- Estadísticas por plataforma
- Exportación de datos
- Búsqueda y filtrado

---

## 🔄 Actualización

Para actualizar a la última versión:

```bash
cd ingenieriasocial
./upgrade.sh
```

O manualmente:
```bash
git pull origin master
chmod +x ingenieriasocial
```

---

## 🐛 Reportar Bugs

Si encuentras algún bug o tienes sugerencias, por favor abre un [issue](https://github.com/CoderFullPro/ingenieriasocial/issues).

---

## 🎓 Créditos

### **Desarrollador Principal:**
- **MidasOrion** - Traducción, mejoras y nuevas funcionalidades

### **Basado en:**
- **The Social-Engineer Toolkit (SET)** por David Kennedy (ReL1K)
- **TrustedSec** - https://www.trustedsec.com

### **Agradecimientos Especiales:**
- A la comunidad de seguridad informática
- A todos los contribuidores del proyecto original SET
- A los testers y usuarios que reportan bugs

---

## 📜 Licencia

Esta herramienta mantiene la licencia original de SET.

**Recuerda:** Esta herramienta es para uso ético y educativo solamente.

---

## 📞 Contacto

- **GitHub:** https://github.com/CoderFullPro/ingenieriasocial
- **Issues:** https://github.com/CoderFullPro/ingenieriasocial/issues

---

## ⭐ Características Únicas de ingenieriasocial

### **Mejoras sobre SET original:**

1. ✅ **100% en Español** - Toda la interfaz traducida
2. ✅ **Templates Modernos** - Diseños actualizados 2024
3. ✅ **Dashboard Web** - Monitoreo en tiempo real
4. ✅ **Sistema de Actualización** - Upgrade automático
5. ✅ **Banners Personalizados** - 10 diseños únicos
6. ✅ **Documentación Completa** - Guías en español
7. ✅ **Instalador Automático** - Setup en un comando

---

**© 2025 ingenieriasocial - Por MidasOrion**

*Usa esta herramienta de forma ética y responsable.*
