#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          🎯 Dashboard Web - ingenieriasocial                   ║"
echo "║                   Creado por: MidasOrion                       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar si Python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado"
    exit 1
fi

echo "✅ Python3 encontrado"

# Verificar/instalar dependencias
echo ""
echo "📦 Verificando dependencias..."

if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚙️  Instalando Flask..."
    pip3 install flask flask-cors --quiet
fi

if ! python3 -c "import flask_cors" 2>/dev/null; then
    echo "⚙️  Instalando Flask-CORS..."
    pip3 install flask-cors --quiet
fi

echo "✅ Dependencias instaladas"
echo ""

# Ir al directorio del dashboard
cd "$(dirname "$0")/src/dashboard"

# Iniciar el servidor
echo "🚀 Iniciando Dashboard..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📊 Dashboard: http://localhost:5000"
echo "  🔌 API: http://localhost:5000/api/stats"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  💡 Presiona Ctrl+C para detener el servidor"
echo ""

python3 dashboard.py
