# Guía de Instalación

Este documento describe las diferentes opciones para configurar su entorno de desarrollo para el curso de MicroPython con LEGO SPIKE Education.

## Opción 1: Entorno Web (Recomendado para estudiantes)

### Pybricks Code IDE
1. Visite https://code.pybricks.com/
2. Conecte su hub SPIKE vía Bluetooth o USB
3. Comience a programar inmediatamente

Ventajas:
- No requiere instalación local
- Siempre tiene la última versión estable
- Funciona en cualquier sistema operativo con navegador moderno
- Incluye simulador de hub para pruebas iniciales

## Opción 2: Entorno Local Virtual (Para pruebas sin hardware)

### Requisitos
- Python 3.12+
- Git
- Conexión a internet

### Pasos de instalación

```bash
# 1. Clonar este repositorio
git clone <URL_DESTE_REPOSITORIO>
cd Micro_Python

# 2. Configurar entorno virtual para pruebas
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias básicas
pip install --upgrade pip
pip install pyserial  # Para comunicación serial si se necesita

# 4. Configurar pybricks-micropython para pruebas virtuales
cd ../pybricks-micropython  # Asumiendo que está al mismo nivel
make mpy-cross -j
./test-virtualhub.sh  # Ejecuta tests en entorno virtual
```

## Opción 3: Entorno de Desarrollo Completo (Para instructores y contribuyentes)

> ⚠️ Nota: Esta opción puede presentar desafíos técnicos en macOS ARM64 debido a limitaciones del toolchain ARM.

### Requisitos adicionales
- GNU ARM Embedded Toolchain (arm-none-eabi-gcc)
- GNU Make
- Git
- Python 3.12+
- Poetry (para gestión de dependencias de Python)

### Instalación del toolchain ARM

#### En Linux (Ubuntu/Debian recomendado):
```bash
sudo apt update
sudo apt install git python3 python3-pip gcc make binutils bzip2 perl
pip install poetry
poetry install  # En el directorio pybricks-micropython
```

#### En macOS (Intel x86_64):
```bash
brew install pipx
pipx install poetry
brew install gcc-arm-embedded  # o usar xPack alternatives
```

#### En macOS (Apple Silicon ARM64):
Las descargas oficiales de ARM toolchain pueden fallar. Alternativas:
1. Usar Rosetta2 con binarios x86_64
2. Usar entornos de Linux virtual (Docker, UTM, Parallels)
3. Usar el enfoque virtual hub o web IDE

### Verificación de instalación
```bash
arm-none-eabi-gcc --version
# Debería mostrar algo como:
# arm-none-eabi-gcc (GNU Arm Embedded Toolchain 15.2.Rel1) 15.2.0 20240910
```

## Verificación del entorno

Después de instalar, verifique que puede:
1. Compilar el virtualhub: `make -C bricks/virtualhub`
2. Ejecutar los tests: `./test-virtualhub.sh`
3. Accedir al REPL de MicroPython en el virtualhub

## Solución de problemas comunes

Consulte `docs/TROUBLESHOOTING.md` para solucionar problemas de instalación específica.

---
*Última actualización: Abril 2026*