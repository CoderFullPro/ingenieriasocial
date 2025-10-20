#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          🎯 Dashboard Simple - ingenieriasocial                ║"
echo "║                   Creado por: MidasOrion                       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Ir al directorio del proyecto
cd "$(dirname "$0")"

# Iniciar servidor HTTP simple
echo "🚀 Iniciando servidor HTTP..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📊 Dashboard: http://localhost:8000/dashboard_simple.html"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  💡 El dashboard se actualizará automáticamente cada 5 segundos"
echo "  💡 Presiona Ctrl+C para detener el servidor"
echo ""

# Abrir navegador automáticamente
sleep 2 && open http://localhost:8000/dashboard_simple.html &

# Iniciar servidor Python
python3 -m http.server 8000
