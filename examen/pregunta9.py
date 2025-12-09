# ¿Cual es la opción correcta sobre arquitecturas distribuidas? (1 Punto) A) Son más simples que las arquitecturas monolíticas. B) Se caracterizan por presentar varias bases de datos independientes (como minimo una por cada servicio), sin comunicación externa o entre servicios para preservar la idempotencia de los servicios. C) Son la opción adecuada para software complejo, que requiere de alta escalabilidad, protección a fallos y modularidad. D) Presentan un alto grado de conescencia y abstracción, haciendo que el acoplamiento se mantenga al mínimo. Esto es perfecto para asegurar la modularidad. Y se caracterizan por presentar varias bases de datos para mantener la cohesión, especialmente la cohesión estructural.
# ✅ La opción correcta es: C) Son la opción adecuada para software complejo, que requiere de alta escalabilidad, protección a fallos y modularidad.

# 🧠 Explicación técnica
# Las arquitecturas distribuidas (ej. microservicios, sistemas event‑driven, arquitecturas basadas en colas) se utilizan cuando el software necesita:

# Alta escalabilidad → cada servicio puede escalarse de forma independiente.

# Protección ante fallos → un error en un servicio no tumba todo el sistema.

# Modularidad → cada servicio cumple una función clara, favoreciendo cohesión y reduciendo acoplamiento.

# Adecuadas para software complejo → especialmente cuando se requiere resiliencia, elasticidad y despliegues independientes.

# ❌ Por qué las otras opciones no son correctas
# A) Incorrecta: son más complejas que las monolíticas, requieren orquestación, comunicación entre servicios y gestión distribuida.

# B) Incorrecta: aunque es común que cada servicio tenga su propia base de datos, sí existe comunicación entre servicios (APIs, colas, eventos). No se evita la comunicación externa.

# D) Incorrecta: mezcla conceptos de cohesión y bases de datos, pero está redactada de forma confusa y no refleja la definición estándar de arquitecturas distribuidas.