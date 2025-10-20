#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     🧪 PRUEBA DE TEMPLATES DE PHISHING - ingenieriasocial     ║"
echo "║                   Creado por: MidasOrion                       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

TEMPLATES=("instagram" "whatsapp" "metamask")
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Función para verificar archivo
check_file() {
    local file=$1
    local name=$2
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    if [ -f "$file" ]; then
        size=$(wc -c < "$file" | tr -d ' ')
        lines=$(wc -l < "$file" | tr -d ' ')
        echo "  ✅ $name existe"
        echo "     📊 Tamaño: $size bytes | Líneas: $lines"
        PASSED_TESTS=$((PASSED_TESTS + 1))
        return 0
    else
        echo "  ❌ $name NO existe"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        return 1
    fi
}

# Función para verificar contenido HTML
check_html_content() {
    local file=$1
    local template=$2
    
    echo "  🔍 Verificando contenido HTML..."
    
    # Verificar DOCTYPE
    if grep -q "<!DOCTYPE html>" "$file"; then
        echo "     ✅ DOCTYPE correcto"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ DOCTYPE faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar formulario
    if grep -q '<form' "$file" && grep -q 'method="POST"' "$file"; then
        echo "     ✅ Formulario POST presente"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ Formulario POST faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar action post.php
    if grep -q 'action="post.php"' "$file"; then
        echo "     ✅ Action post.php configurado"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ Action post.php faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar JavaScript
    if grep -q '<script>' "$file"; then
        echo "     ✅ JavaScript presente"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ JavaScript faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar CSS
    if grep -q '<style>' "$file"; then
        echo "     ✅ CSS presente"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ CSS faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
}

# Función para verificar PHP
check_php_content() {
    local file=$1
    
    echo "  🔍 Verificando contenido PHP..."
    
    # Verificar apertura PHP
    if grep -q '<?php' "$file"; then
        echo "     ✅ Tag PHP presente"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ Tag PHP faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar captura de POST
    if grep -q '$_POST' "$file"; then
        echo "     ✅ Captura de POST configurada"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ Captura de POST faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar file_put_contents
    if grep -q 'file_put_contents' "$file"; then
        echo "     ✅ Guardado de datos configurado"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ Guardado de datos faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar JSON
    if grep -q 'json_encode' "$file"; then
        echo "     ✅ Exportación JSON configurada"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "     ❌ Exportación JSON faltante"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
}

# Probar cada template
for template in "${TEMPLATES[@]}"; do
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📱 PROBANDO: $template"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    template_dir="src/templates/phishing/$template"
    
    if [ ! -d "$template_dir" ]; then
        echo "  ❌ Directorio no existe: $template_dir"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        TOTAL_TESTS=$((TOTAL_TESTS + 1))
        continue
    fi
    
    echo "  ✅ Directorio existe"
    PASSED_TESTS=$((PASSED_TESTS + 1))
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    # Verificar archivos
    echo ""
    echo "  📄 Verificando archivos..."
    check_file "$template_dir/index.html" "index.html"
    check_file "$template_dir/post.php" "post.php"
    
    # Verificar contenido HTML
    if [ -f "$template_dir/index.html" ]; then
        echo ""
        check_html_content "$template_dir/index.html" "$template"
    fi
    
    # Verificar contenido PHP
    if [ -f "$template_dir/post.php" ]; then
        echo ""
        check_php_content "$template_dir/post.php"
    fi
done

# Verificar README
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📚 VERIFICANDO DOCUMENTACIÓN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_file "src/templates/phishing/README.md" "README.md"

# Resumen final
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                      📊 RESUMEN DE PRUEBAS                     ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "  Total de pruebas:    $TOTAL_TESTS"
echo "  ✅ Pruebas exitosas: $PASSED_TESTS"
echo "  ❌ Pruebas fallidas: $FAILED_TESTS"
echo ""

# Calcular porcentaje
if [ $TOTAL_TESTS -gt 0 ]; then
    percentage=$((PASSED_TESTS * 100 / TOTAL_TESTS))
    echo "  📈 Tasa de éxito: $percentage%"
    echo ""
    
    if [ $percentage -eq 100 ]; then
        echo "  🎉 ¡TODOS LOS TESTS PASARON! Templates 100% funcionales"
        exit 0
    elif [ $percentage -ge 80 ]; then
        echo "  ✅ Templates mayormente funcionales"
        exit 0
    else
        echo "  ⚠️  Se encontraron problemas en los templates"
        exit 1
    fi
else
    echo "  ❌ No se ejecutaron pruebas"
    exit 1
fi
