#!/bin/bash

# Script de actualización para ingenieriasocial
# Por: MidasOrion

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        🔄 Actualización de ingenieriasocial                    ║"
echo "║                   Por: MidasOrion                              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar si estamos en el directorio correcto
if [ ! -f "ingenieriasocial" ]; then
    echo "❌ Error: No se encuentra el archivo 'ingenieriasocial'"
    echo "   Asegúrate de estar en el directorio de ingenieriasocial"
    exit 1
fi

echo "✅ Directorio correcto detectado"
echo ""

# Verificar conexión a internet
echo "🌐 Verificando conexión a internet..."
if ping -c 1 github.com &> /dev/null; then
    echo "✅ Conexión a internet OK"
else
    echo "❌ No hay conexión a internet"
    echo "   Verifica tu conexión e intenta nuevamente"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 Paso 1: Guardando configuración actual..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Hacer backup de capturas si existen
if [ -d "src/templates/phishing" ]; then
    BACKUP_DIR="backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    
    echo "💾 Haciendo backup de capturas..."
    cp -r src/templates/phishing/*/captured_credentials.* "$BACKUP_DIR/" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "✅ Backup guardado en: $BACKUP_DIR"
    else
        echo "⚠️  No se encontraron capturas para respaldar"
    fi
else
    echo "⚠️  No se encontraron capturas"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📥 Paso 2: Descargando última versión..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Guardar cambios locales si los hay
if git diff --quiet; then
    echo "✅ No hay cambios locales"
else
    echo "⚠️  Hay cambios locales, guardándolos..."
    git stash save "Backup antes de actualización $(date +%Y%m%d_%H%M%S)"
fi

# Obtener la versión actual
CURRENT_VERSION=$(git rev-parse --short HEAD 2>/dev/null || echo "desconocida")
echo "📌 Versión actual: $CURRENT_VERSION"

# Actualizar desde GitHub
echo "🔄 Descargando actualizaciones..."
git fetch origin master

if [ $? -ne 0 ]; then
    echo "❌ Error al descargar actualizaciones"
    exit 1
fi

# Verificar si hay actualizaciones
UPDATES=$(git rev-list HEAD..origin/master --count)

if [ "$UPDATES" -eq 0 ]; then
    echo ""
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║          ✅ Ya tienes la última versión                        ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "📌 Versión: $CURRENT_VERSION"
    echo "🎯 No hay actualizaciones disponibles"
    exit 0
fi

echo "📦 Hay $UPDATES actualizaciones disponibles"
echo ""

# Mostrar cambios
echo "📋 Cambios en la nueva versión:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
git log --oneline HEAD..origin/master | head -10
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Preguntar si desea continuar
read -p "¿Deseas actualizar? (s/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[SsYy]$ ]]; then
    echo "❌ Actualización cancelada"
    exit 0
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "⬇️  Paso 3: Instalando actualización..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Aplicar actualización
git pull origin master

if [ $? -ne 0 ]; then
    echo "❌ Error al aplicar actualización"
    echo "   Puedes intentar: git reset --hard origin/master"
    exit 1
fi

NEW_VERSION=$(git rev-parse --short HEAD)
echo "✅ Actualización aplicada"
echo "📌 Nueva versión: $NEW_VERSION"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔧 Paso 4: Configurando permisos..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Dar permisos de ejecución
chmod +x ingenieriasocial 2>/dev/null
chmod +x start_dashboard_simple.sh 2>/dev/null
chmod +x start_dashboard.sh 2>/dev/null
chmod +x upgrade.sh 2>/dev/null
chmod +x install_kali.sh 2>/dev/null

echo "✅ Permisos actualizados"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 Paso 5: Verificando dependencias..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Verificar si hay nuevas dependencias
if [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependencias de Python..."
    pip3 install -r requirements.txt --quiet --upgrade 2>/dev/null
    echo "✅ Dependencias actualizadas"
else
    echo "⚠️  No se encontró requirements.txt"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔄 Paso 6: Restaurando capturas..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Restaurar capturas si existen
if [ -d "$BACKUP_DIR" ]; then
    echo "💾 Restaurando capturas desde backup..."
    cp -r "$BACKUP_DIR"/* src/templates/phishing/ 2>/dev/null
    echo "✅ Capturas restauradas"
else
    echo "⚠️  No hay backup para restaurar"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          ✅ ACTUALIZACIÓN COMPLETADA                           ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "📊 Resumen:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📌 Versión anterior: $CURRENT_VERSION"
echo "  📌 Versión actual:   $NEW_VERSION"
echo "  📦 Actualizaciones:  $UPDATES commits"
if [ -d "$BACKUP_DIR" ]; then
    echo "  💾 Backup guardado:  $BACKUP_DIR"
fi
echo ""
echo "🚀 Para iniciar ingenieriasocial:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  sudo ./ingenieriasocial"
echo ""
echo "📊 Para ver el dashboard:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ./start_dashboard_simple.sh"
echo ""
echo "📋 Para ver los cambios completos:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  git log $CURRENT_VERSION..$NEW_VERSION"
echo ""
echo "© 2025 ingenieriasocial - MidasOrion"
echo ""
