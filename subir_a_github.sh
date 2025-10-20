#!/bin/bash

echo "=========================================="
echo "Script para subir ingenieriasocial a GitHub"
echo "=========================================="
echo ""

# Ir al directorio del proyecto
cd /Users/coderfull/Desktop/setoolkit/social-engineer-toolkit

# Verificar si ya hay cambios commiteados
echo "✓ Verificando estado de git..."
git status

echo ""
echo "=========================================="
echo "OPCIONES DE AUTENTICACIÓN:"
echo "=========================================="
echo ""
echo "Opción 1: Usar GitHub CLI (Recomendado)"
echo "  1. Instala: brew install gh"
echo "  2. Ejecuta: gh auth login"
echo "  3. Sigue las instrucciones en pantalla"
echo ""
echo "Opción 2: Usar Token de Acceso Personal"
echo "  1. Ve a: https://github.com/settings/tokens"
echo "  2. Click en 'Generate new token (classic)'"
echo "  3. Dale permisos de 'repo'"
echo "  4. Copia el token"
echo ""
echo "=========================================="
echo ""

# Preguntar qué método quiere usar
read -p "¿Qué método quieres usar? (1=GitHub CLI, 2=Token): " metodo

if [ "$metodo" = "1" ]; then
    echo ""
    echo "Verificando si GitHub CLI está instalado..."
    if ! command -v gh &> /dev/null; then
        echo "GitHub CLI no está instalado."
        read -p "¿Quieres instalarlo ahora? (y/n): " instalar
        if [ "$instalar" = "y" ]; then
            echo "Instalando GitHub CLI..."
            brew install gh
        else
            echo "No se puede continuar sin GitHub CLI."
            exit 1
        fi
    fi
    
    echo ""
    echo "Autenticándote con GitHub..."
    gh auth login
    
    echo ""
    echo "Subiendo código a GitHub..."
    git push -u origin master
    
elif [ "$metodo" = "2" ]; then
    echo ""
    read -p "Ingresa tu token de GitHub: " token
    
    if [ -z "$token" ]; then
        echo "Error: No ingresaste un token."
        exit 1
    fi
    
    echo ""
    echo "Configurando remote con token..."
    git remote set-url origin https://$token@github.com/CoderFullPro/ingenieriasocial.git
    
    echo ""
    echo "Subiendo código a GitHub..."
    git push -u origin master
    
    # Limpiar el token del remote por seguridad
    echo ""
    echo "Limpiando configuración de token..."
    git remote set-url origin https://github.com/CoderFullPro/ingenieriasocial.git
    
else
    echo "Opción no válida."
    exit 1
fi

echo ""
echo "=========================================="
echo "✓ ¡Código subido exitosamente!"
echo "=========================================="
echo ""
echo "Tu repositorio está en:"
echo "https://github.com/CoderFullPro/ingenieriasocial"
echo ""
