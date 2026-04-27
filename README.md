# Calculadora Básica + Pruebas Automatizadas y Pipeline CI/CD

Se implementaron:
- 4 casos de prueba automatizados con **pytest** (casos exitosos, caso de error y caso borde).
- Pipeline de **integración continua (CI/CD)** con **GitHub Actions** que se ejecuta automáticamente en cada push.
- Generación automática de un reporte HTML (`report.html`).

## Estructura del Proyecto
calculator_tp/
├── app/
│   └── calculator.py              # Funciones principales de la calculadora
├── test/
│   └── test_calculator.py          # Tests automatizados con pytest
├── .github/workflows/
│   └── test.yml                     # Pipeline de GitHub Actions
├── requirements.txt
└── README.md

## Instalar dependencias:
```bash
pip install -r requirements.txt
