# 🧪 Proyecto de Automatización con Selenium - OrangeHRM

## 📌 Descripción
Este proyecto consiste en la automatización de pruebas funcionales sobre la aplicación web OrangeHRM utilizando Selenium WebDriver con Python.

Se implementa el patrón de diseño **Page Object Model (POM)** para mejorar la organización, reutilización y mantenimiento del código.

---

## 🎯 Objetivos
- Automatizar flujos críticos del sistema
- Validar el comportamiento del login
- Verificar acceso a módulos administrativos
- Generar evidencias automáticas (screenshots)
- Generar reportes HTML de ejecución

---

## 🚀 Tecnologías utilizadas
- Python 3
- Selenium WebDriver
- Pytest
- Pytest-HTML

---

## 📂 Estructura del proyecto
selenium_project/
│
├── pages/
│ ├── login_page.py
│ └── user_page.py
│
├── tests/
│ ├── test_login.py
│ └── test_users.py
│
├── utils/
│ ├── driver_setup.py
│ └── screenshot.py
│
├── screenshots/
│
├── reports/
│ └── report.html
│
└── pytest.ini


---

## ✅ Casos de prueba implementados

### 🔐 Login
- Login exitoso con credenciales válidas
- Login con credenciales incorrectas
- Login con campos vacíos

### 👤 Gestión de usuarios
- Acceso al módulo Admin
- Acceso al formulario de creación de usuario
- Validación de navegación para edición de usuario
- Validación de navegación para eliminación de usuario

---

## 🧪 Historias de usuario

### 1. Login exitoso
**Como** usuario  
**Quiero** iniciar sesión  
**Para** acceder al sistema  

**Criterios de aceptación:**
- Usuario válido accede al sistema
- Redirección al dashboard

**Criterios de rechazo:**
- Credenciales inválidas muestran error
- Campos vacíos muestran validación

---

### 2. Acceso a creación de usuario
**Como** administrador  
**Quiero** acceder al formulario de creación  
**Para** registrar nuevos usuarios  

**Criterios de aceptación:**
- Acceso al módulo Admin
- Visualización del formulario "Add User"

---

### 3. Visualización de usuarios
**Como** administrador  
**Quiero** ver la lista de usuarios  
**Para** gestionar la información  

---

### 4. Edición de usuario (simulada)
**Como** administrador  
**Quiero** acceder a la edición  
**Para** modificar datos de usuarios  

---

### 5. Eliminación de usuario (simulada)
**Como** administrador  
**Quiero** acceder a opciones de eliminación  
**Para** remover usuarios del sistema  

---

## ▶️ Ejecución de pruebas

Ejecutar el siguiente comando en la terminal:

```bash
python -m pytest