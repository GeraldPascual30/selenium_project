# Pruebas de interfaz con Selenium y Python

Proyecto académico de automatización sobre la demo web **OrangeHRM**, organizado con **Page Object Model**, Selenium WebDriver y pytest. Incluye capturas de evidencia y un reporte HTML.

## Alcance de las pruebas actuales

| Caso | Qué comprueba el código |
| --- | --- |
| Login válido | Espera la carga del dashboard y comprueba su presencia. |
| Login incorrecto | Busca el mensaje de credenciales inválidas. |
| Campos de login vacíos | Comprueba el mensaje de campos requeridos. |
| Formulario de alta | Navega al módulo Admin, abre Add User y comprueba el formulario. |
| Caso llamado update user | Comprueba el acceso a una URL del módulo Admin. |
| Caso llamado delete user | Comprueba el acceso a una URL del módulo Admin. |

Los dos últimos casos son ejercicios de navegación. No modifican ni eliminan usuarios, y el caso de alta no guarda un nuevo usuario.

## Tecnologías y organización

- Python, Selenium WebDriver, pytest y pytest-html.
- `pages/`: objetos de página para login y usuarios.
- `tests/`: casos de prueba.
- `utils/`: creación del navegador y capturas de pantalla.
- `reports/`: reporte HTML y evidencias.
- `pytest.ini`: configuración del reporte.

## Preparar y ejecutar

Se necesita Python, Google Chrome y acceso a Internet para abrir la demo.

```bash
git clone https://github.com/GeraldPascual30/selenium_project.git
cd selenium_project
python -m venv .venv
```

Activar el entorno en Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instalar las dependencias y ejecutar desde la raíz del repositorio:

```bash
python -m pip install selenium pytest pytest-html
python -m pytest
```

`utils/driver_setup.py` crea una instancia de Chrome. Selenium puede necesitar descargar un controlador compatible la primera vez.

El archivo existente `requeriments.txt` está vacío; por eso se muestra la instalación explícita de dependencias.

## Evidencias

La configuración de pytest genera [reports/report.html](reports/report.html). Las capturas se encuentran en [reports/screenshots](reports/screenshots).

Las evidencias guardadas corresponden a ejecuciones anteriores. El resultado de una nueva ejecución depende del estado de la demo y de los localizadores de la interfaz.

## Recorrido para revisar el proyecto

1. Leer [la página de login](pages/login_page.py).
2. Revisar [las tres pruebas de login](tests/test_login.py).
3. Revisar [las pruebas de navegación administrativa](tests/test_users.py).
4. Abrir el reporte HTML y comparar sus evidencias.

## Próximas mejoras

- Completar flujos reales de alta, edición y eliminación con datos de prueba aislados.
- Añadir esperas explícitas a las pruebas negativas.
- Fijar versiones de dependencias y excluir archivos de caché del repositorio.

---

[Gerald Pascual](https://github.com/GeraldPascual30) · Práctica académica de QA
