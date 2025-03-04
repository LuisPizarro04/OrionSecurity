# **Especificación de Requerimientos del Sistema de Guardias de Seguridad para Obras de Construcción**

## **1. Introducción**
### **1.1 Propósito**
Este documento define los requerimientos funcionales y no funcionales del sistema de guardias de seguridad para una obra de construcción. El sistema se desarrollará utilizando Django y permitirá gestionar la administración de guardias, turnos, control de acceso, reportes de incidentes y más.

### **1.2 Alcance**
El sistema estará diseñado para:
- Administrar guardias de seguridad.
- Gestionar turnos y asistencia.
- Registrar accesos a la obra.
- Reportar incidentes en tiempo real.
- Proporcionar informes y auditoría de actividades.

## **2. Requerimientos Funcionales**

### **2.1 Gestión de Usuarios**
- Registro y autenticación de usuarios.
- Roles de usuario:
  - **Administrador:** Control total del sistema.
  - **Supervisor de Seguridad:** Supervisa y asigna turnos.
  - **Guardia de Seguridad:** Reporta novedades y cumple turnos.
- Recuperación de contraseña.
- Control de permisos según el rol.

### **2.2 Gestión de Guardias de Seguridad**
- Registro de guardias con información personal:
  - Nombre, identificación, contacto, dirección.
  - Tipo de contrato, certificaciones, exámenes médicos.
- Asignación de equipamiento (radio, uniforme, etc.).
- Historial de asistencia y evaluación de desempeño.
- Registro de capacitaciones y entrenamientos.

### **2.3 Gestión de Turnos**
- Creación de turnos por fecha y horario.
- Asignación de guardias a turnos.
- Registro de cambios y reemplazos de turno.
- Control de asistencia con marcación de entrada y salida.
- Generación automática de horarios rotativos.

### **2.4 Control de Acceso a la Obra**
- Registro de entrada y salida de:
  - Empleados.
  - Proveedores.
  - Visitantes.
- Verificación de identidad con QR, PIN o credencial.
- Registro de acceso de vehículos.
- Control de horarios y restricciones de acceso.

### **2.5 Reportes y Novedades**
- Registro de incidentes con descripción y tipo de evento.
- Adjuntar evidencia (fotos, videos, notas).
- Notificación automática a supervisores.
- Historial de reportes con clasificación de incidentes.
- Registro de observaciones y mejoras en seguridad.

### **2.6 Panel de Administración y Reportes**
- Dashboard con métricas clave.
- Reportes exportables en PDF o Excel.
- Auditoría de acciones y logs del sistema.
- Historial de accesos y actividades del sistema.

### **2.7 Notificaciones y Alertas**
- Alertas en tiempo real para:
  - Cambios de turno.
  - Incidentes.
  - Accesos no autorizados.
- Notificaciones vía correo electrónico o SMS.
- Alertas automáticas si un guardia no se presenta al turno.
- Recordatorios de turnos próximos.

### **2.8 Integración con Dispositivos de Seguridad (Opcional)**
- Registro de eventos de cámaras de seguridad.
- Alertas automáticas por detección de movimientos sospechosos.
- Registro de activación de alarmas de seguridad.
- Monitoreo en tiempo real de cámaras.

## **3. Requerimientos No Funcionales**

### **3.1 Seguridad**
- Autenticación con JWT o OAuth2.
- Encriptación de datos sensibles.
- Auditoría de actividades de usuario.
- Implementación de firewall y control de acceso.

### **3.2 Rendimiento y Escalabilidad**
- Arquitectura basada en microservicios para futuras expansiones.
- Optimización de consultas SQL y caché para rendimiento.
- Escalabilidad horizontal y vertical del sistema.

### **3.3 Disponibilidad y Fiabilidad**
- Sistema disponible 24/7.
- Copias de seguridad periódicas de la base de datos.
- Plan de recuperación ante fallos o desastres.

### **3.4 Compatibilidad**
- Accesible desde navegadores web y dispositivos móviles.
- API REST para integraciones futuras.
- Interfaz responsiva y accesible para diferentes dispositivos.

## **4. Consideraciones Finales**
Este documento define las bases del sistema a desarrollar. Se podrán realizar ajustes según los requerimientos del cliente y pruebas en la fase de desarrollo. Se recomienda realizar validaciones periódicas con los usuarios para asegurar que el sistema cumpla con sus necesidades y expectativas.

