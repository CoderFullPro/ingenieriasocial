# 🔄 Guía de Actualización - ingenieriasocial

## Por: MidasOrion

---

## 🚀 Actualización Rápida

```bash
cd /opt/ingieriasocial
./upgrade.sh
```

¡Eso es todo! El script se encarga de todo automáticamente.

---

## 📋 ¿Qué hace el script de actualización?

### **1. Verificaciones Iniciales** ✅
- Verifica que estés en el directorio correcto
- Comprueba la conexión a internet
- Detecta la versión actual

### **2. Backup Automático** 💾
- Guarda todas tus capturas en un directorio de backup
- Formato: `backup_YYYYMMDD_HHMMSS/`
- Incluye archivos `.txt` y `.json`

### **3. Descarga de Actualizaciones** 📥
- Conecta con GitHub
- Descarga la última versión
- Muestra los cambios disponibles

### **4. Confirmación** ❓
- Te muestra los últimos 10 commits
- Pregunta si deseas continuar
- Puedes cancelar en cualquier momento

### **5. Instalación** ⬇️
- Aplica las actualizaciones
- Actualiza dependencias de Python
- Configura permisos automáticamente

### **6. Restauración** 🔄
- Restaura tus capturas guardadas
- Mantiene tu configuración
- Todo vuelve a funcionar como antes

---

## 📊 Ejemplo de Uso

```bash
$ cd /opt/ingieriasocial
$ ./upgrade.sh

╔════════════════════════════════════════════════════════════════╗
║        🔄 Actualización de ingenieriasocial                    ║
║                   Por: MidasOrion                              ║
╚════════════════════════════════════════════════════════════════╝

✅ Directorio correcto detectado
✅ Conexión a internet OK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Paso 1: Guardando configuración actual...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💾 Haciendo backup de capturas...
✅ Backup guardado en: backup_20250120_103000

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📥 Paso 2: Descargando última versión...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 Versión actual: a77012c
📦 Hay 5 actualizaciones disponibles

📋 Cambios en la nueva versión:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
b23456a Agregado nuevo template de Discord
c34567b Mejorado dashboard con gráficos
d45678c Corrección de bugs en WhatsApp
e56789d Actualizado README
f67890e Optimización de rendimiento
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

¿Deseas actualizar? (s/n): s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⬇️  Paso 3: Instalando actualización...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Actualización aplicada
📌 Nueva versión: f67890e

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔧 Paso 4: Configurando permisos...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Permisos actualizados

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Paso 5: Verificando dependencias...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Dependencias actualizadas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 Paso 6: Restaurando capturas...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Capturas restauradas

╔════════════════════════════════════════════════════════════════╗
║          ✅ ACTUALIZACIÓN COMPLETADA                           ║
╚════════════════════════════════════════════════════════════════╝

📊 Resumen:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📌 Versión anterior: a77012c
  📌 Versión actual:   f67890e
  📦 Actualizaciones:  5 commits
  💾 Backup guardado:  backup_20250120_103000
```

---

## 🔧 Actualización Manual

Si prefieres actualizar manualmente:

```bash
# 1. Ir al directorio
cd /opt/ingieriasocial

# 2. Backup de capturas
mkdir -p ~/backup_ingenieriasocial
cp -r src/templates/phishing/*/captured_credentials.* ~/backup_ingenieriasocial/

# 3. Ver cambios disponibles
git fetch origin master
git log HEAD..origin/master --oneline

# 4. Actualizar
git pull origin master

# 5. Restaurar capturas
cp ~/backup_ingenieriasocial/captured_credentials.* src/templates/phishing/*/

# 6. Actualizar permisos
chmod +x ingenieriasocial
chmod +x *.sh

# 7. Actualizar dependencias (opcional)
pip3 install -r requirements.txt --upgrade
```

---

## ❓ Preguntas Frecuentes

### **¿Perderé mis capturas al actualizar?**
No. El script hace backup automático de todas tus capturas y las restaura después.

### **¿Puedo cancelar la actualización?**
Sí. El script te pregunta antes de aplicar cambios. Puedes cancelar en cualquier momento.

### **¿Qué pasa si algo sale mal?**
Tus capturas están guardadas en el directorio `backup_YYYYMMDD_HHMMSS/`. Puedes restaurarlas manualmente.

### **¿Con qué frecuencia debo actualizar?**
Recomendamos actualizar cada 1-2 semanas para tener las últimas mejoras y correcciones.

### **¿Necesito ser root para actualizar?**
No. La actualización no requiere permisos de root.

### **¿Se actualizan los templates en Apache?**
No automáticamente. Si usas Apache, debes copiar los templates nuevamente:
```bash
sudo cp -r src/templates/phishing/* /var/www/html/
sudo systemctl restart apache2
```

---

## 🔍 Verificar Versión Actual

```bash
cd /opt/ingieriasocial
git log -1 --oneline
```

O ver el hash completo:
```bash
git rev-parse HEAD
```

---

## 📜 Ver Historial de Cambios

```bash
# Últimos 10 commits
git log -10 --oneline

# Cambios detallados
git log -5 --stat

# Cambios desde una versión específica
git log a77012c..HEAD --oneline
```

---

## 🔄 Revertir a Versión Anterior

Si algo no funciona después de actualizar:

```bash
# Ver versiones disponibles
git log --oneline

# Volver a una versión específica
git checkout a77012c

# O volver a la versión anterior
git checkout HEAD~1

# Para volver a la última versión
git checkout master
git pull origin master
```

---

## 🆘 Solución de Problemas

### **Error: "Already up to date"**
Ya tienes la última versión. No hay actualizaciones disponibles.

### **Error: "Your local changes would be overwritten"**
Tienes cambios locales. Opciones:
```bash
# Guardar cambios
git stash

# O descartar cambios
git reset --hard origin/master
```

### **Error: "fatal: not a git repository"**
No estás en el directorio correcto o no es un repositorio git:
```bash
cd /opt/ingieriasocial
git status
```

### **Error: "Permission denied"**
Falta permiso de ejecución:
```bash
chmod +x upgrade.sh
```

---

## 📊 Comandos Útiles

```bash
# Ver estado actual
git status

# Ver rama actual
git branch

# Ver remoto configurado
git remote -v

# Limpiar archivos no rastreados
git clean -fd

# Forzar actualización (¡cuidado!)
git reset --hard origin/master
git pull origin master
```

---

## 🎯 Después de Actualizar

1. **Verificar que funciona:**
   ```bash
   sudo ./ingenieriasocial
   ```

2. **Actualizar Apache (si lo usas):**
   ```bash
   sudo cp -r src/templates/phishing/* /var/www/html/
   sudo systemctl restart apache2
   ```

3. **Probar el dashboard:**
   ```bash
   ./start_dashboard_simple.sh
   ```

4. **Leer los cambios:**
   ```bash
   cat CHANGELOG.md  # Si existe
   ```

---

## 📚 Recursos Adicionales

- **Instalación:** `INSTALL_KALI.md`
- **README:** `README.md`
- **GitHub:** https://github.com/CoderFullPro/ingieriasocial
- **Issues:** https://github.com/CoderFullPro/ingieriasocial/issues

---

**© 2025 ingenieriasocial - MidasOrion**

*Mantén tu herramienta actualizada para tener las últimas mejoras y correcciones de seguridad.*
