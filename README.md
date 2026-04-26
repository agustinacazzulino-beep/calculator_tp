# Calculadora Básica + Pruebas Automatizadas y Pipeline CI/CD

## Descripción del Proyecto
Este repositorio contiene una calculadora básica desarrollada en Python como parte del TPO 2 de la materia Testing de Aplicaciones.

Se implementaron:
- 4 casos de prueba automatizados con **pytest** (caso exitoso, caso de error y casos borde).
- Pipeline de **integración continua (CI/CD)** con **GitHub Actions** que se ejecuta automáticamente en cada push.
- Generación automática de un reporte HTML (`report.html`).

## Estructura del Proyecto
calculator_tp/
├── app/
│   └── calculadora.py              # Funciones principales de la calculadora
├── test/
│   └── test_calculator.py          # Tests automatizados con pytest
├── .github/workflows/
│   └── testyml                     # Pipeline de GitHub Actions
├── requirements.txt
├── pytest.ini
└── README.md

## Instalar dependencias:
```bash
pip install -r requirements.txt
