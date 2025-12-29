# 📁 Organizador de Archivos de Pacientes

Programa en Python para organizar automáticamente archivos médicos en carpetas individuales por paciente.

## ✨ Características

- **📋 Extracción automática de datos**: Lee archivos con formato `TIPO-CEDULA-NOMBRE.extensión` y extrae la cédula y el nombre que están después del primer guion

- **📂 Creación automática de carpetas**: Genera carpetas con el formato `CEDULA-NOMBRE`  
  Ejemplo: `34345344-DIDIER MAURICIO ESPINEL SUAREZ`

- **🚀 Movimiento de archivos**: Coloca cada archivo dentro de su carpeta correspondiente automáticamente

- **⚠️ Manejo de errores**: Informa sobre archivos que no tienen el formato correcto y continúa con los demás

## 🔧 Instalación
```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/organizador-archivos-pacientes.git

# Navega al directorio
cd organizador-archivos-pacientes
```

## 💻 Uso

### Método 1: Especificar ruta de archivos

Edita el archivo y cambia la ruta en la línea:
```python
carpeta = "C:/Ruta/A/Tus/Archivos"
```

### Método 2: Usar carpeta actual

Usa la carpeta donde ejecutas el script:
```python
carpeta = "."
```

### Ejecutar el programa
```bash
python organizador_archivos.py
```

## 📝 Ejemplo

**Antes:**
```
📁 Mis Archivos
├── CUADRO HEMATICO-34345344-DIDIER MAURICIO ESPINEL SUAREZ.pdf
├── RADIOGRAFIA-12345678-MARIA LOPEZ GARCIA.jpg
└── ECOGRAFIA-87654321-JUAN PEREZ MARTINEZ.pdf
```

**Después:**
```
📁 Mis Archivos
├── 📁 34345344-DIDIER MAURICIO ESPINEL SUAREZ
│   └── CUADRO HEMATICO-34345344-DIDIER MAURICIO ESPINEL SUAREZ.pdf
├── 📁 12345678-MARIA LOPEZ GARCIA
│   └── RADIOGRAFIA-12345678-MARIA LOPEZ GARCIA.jpg
└── 📁 87654321-JUAN PEREZ MARTINEZ
    └── ECOGRAFIA-87654321-JUAN PEREZ MARTINEZ.pdf
```

## 📋 Formato de archivos requerido

Los archivos deben seguir este patrón:
```
TIPO_EXAMEN-CEDULA-NOMBRE_COMPLETO.extensión
```

- **TIPO_EXAMEN**: Descripción del documento (ej: CUADRO HEMATICO, RADIOGRAFIA)
- **CEDULA**: Número de identificación del paciente
- **NOMBRE_COMPLETO**: Nombre completo del paciente
- **extensión**: .pdf, .jpg, .png, etc.

## 🛠️ Requisitos

- Python 3.6 o superior
- Módulos estándar: `os`, `shutil`, `re` (incluidos en Python)

## 📄 Licencia

MIT License - Siéntete libre de usar y modificar este código

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 👨‍💻 Autor

Tu Nombre - [@tu_usuario](https://github.com/diegun99)

## 📞 Soporte

¿Tienes algún problema? [Abre un issue](https://github.com/tu-usuario/organizador-archivos-pacientes/issues)
