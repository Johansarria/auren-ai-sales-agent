# AUREN · Agente de Ventas Autónomo con IA

![Producción en vivo](https://img.shields.io/badge/Estado-Producci%C3%B3n%20en%20vivo-success)
![Shopify](https://img.shields.io/badge/Shopify-Admin%20API-7AB55C)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Business%20API-25D366)
![Meta](https://img.shields.io/badge/Meta-Business%20%26%20WABA-0866FF)
![Stack](https://img.shields.io/badge/Python%20%7C%20Docker%20%7C%20Supabase-3776AB)

> **Case study de un agente de IA autónomo operando una tienda real en producción** — no un chatbot, sino un agente que observa, decide y ejecuta.

**AUREN** ([aurenstore.store](https://aurenstore.store)) es una tienda de calzado en Colombia construida sobre Shopify. Su operación comercial y de posventa por WhatsApp está automatizada por un **agente de IA autónomo**: el agente escucha eventos de la tienda, razona con contexto de negocio y ejecuta acciones con efectos reales — notificar envíos, recuperar carritos abandonados y capturar leads con atribución.

---

## 📖 English Summary

> **An autonomous AI sales agent running a real store in production** — not a chatbot. It reacts to store events, reasons with business context, and executes real actions end-to-end over WhatsApp Business.

- 🛒 **Store:** [AUREN](https://aurenstore.store) — a footwear e-commerce in Colombia built on Shopify.
- 🤖 **What the agent does:** notifies customers of shipping guides the moment an order is fulfilled · recovers abandoned checkouts with a 3-touch discount ladder (CTA opens checkout with the coupon pre-applied) · captures leads with UTM attribution.
- 📱 **Meta Business:** WhatsApp Business Platform (WABA) with Meta-approved templates (transactional + promotional) and Meta Pixel conversion tracking.
- 🧱 **Stack:** Python · Docker · autonomous agent orchestration (Hermes) · LLM reasoning · Shopify Admin API · Supabase (PostgreSQL + RLS) · Interrapísimo shipping.
- 🔒 **Privacy by design:** this repo is public narrative only — no production code, credentials, routes, or customer data. The live system stays private.

_El caso completo continúa en español a continuación._

## 🤖 ¿Por qué un *agente* y no un chatbot?

| | Chatbot clásico | Agente autónomo |
|---|---|---|
| **Entrada** | El cliente inicia y pregunta | La tienda misma genera eventos (webhooks) |
| **Acción** | Responde texto | Ejecuta: consulta APIs, envía mensajes, aplica descuentos |
| **Contexto** | Conversación | Estado real del negocio: pedidos, stock, historial |
| **Horario** | Limitado al humano | 24/7 sin intervención |

El agente no espera a que le pregunten: **cuando un pedido pasa a enviado, el cliente ya recibió su guía por WhatsApp** — sin que nadie lo escriba.

---

## 🎯 El problema

- Seguimiento de pedidos y notificación de guías 100% manual.
- Carritos abandonados (>70% en e-commerce) sin ningún mecanismo de recuperación.
- Atención al cliente limitada a horario comercial.
- Cero trazabilidad del ciclo *clic → lead → pedido → entrega*.

## ⚙️ La solución: arquitectura

<p align="center">
  <img src="assets/architecture.svg" alt="Arquitectura del agente de ventas IA de AUREN" width="820">
</p>

**Evento → Acción del agente:**

| Evento de la tienda | Acción autónoma del agente |
|---|---|
| Pedido marcado como enviado (con guía Interrapísimo) | WhatsApp transaccional al cliente: confirmación + número de guía, sin intervención humana |
| Checkout abandonado | **Escalera de recuperación**: recordatorio → descuento progresivo (toque 2 y 3) con CTA que abre el checkout con el cupón ya aplicado |
| Lead nuevo (formulario flotante con UTM) | Registro en Supabase con atribución de origen (campaña/medio) |
| Consulta de disponibilidad | Respuesta con stock real vía API, no catálogo estático |

---

## 📱 Meta Business en el centro de la operación

- **WhatsApp Business Platform (WABA)** con plantillas aprobadas por Meta: mensajes *transaccionales* (guías, confirmaciones) y *promocionales* (escalera de descuentos) — siempre con plantillas aprobadas, cumpliendo las políticas de calidad de Meta.
- **Pixel de Meta** para medición de conversión del tráfico pagado y orgánico.
- **Embudo medible**: cada lead queda etiquetado con su origen UTM para saber qué campaña realmente vende.

## 🧱 Componentes clave

| Componente | Rol |
|---|---|
| **Agente Hermes** (Nous Research) | Orquestación autónoma del agente en bucle |
| **LLM** | Razonamiento con contexto de negocio |
| **Shopify Admin API** | Lectura/escritura de pedidos y stock |
| **Supabase (PostgreSQL + RLS)** | Clientes, pedidos, eventos — acceso por fila |
| **Python + Docker** | Servicio del agente en VPS Linux |
| **WhatsApp Cloud API** | Canal de comunicación (WABA) |
| **Interrapísimo** | Logística de envíos (guías) |

## 🔒 Blindaje de datos

Este repositorio es **narrativa pública**: no contiene código de producción, credenciales, rutas internas ni datos de clientes. Los datos reales (teléfonos, pedidos) viven únicamente en Supabase con Row Level Security; el sistema operativo permanece en un repositorio privado. La privacidad del cliente final es parte del diseño, no un añadido.

## 📈 Resultados

> Sección reservada para métricas agregadas reales de operación (por confirmar con el autor).

---

## 👤 Autor

**Johan Sarria** — Data Science & IA · Automatización de negocios con agentes

[GitHub](https://github.com/Johansarria) · [LinkedIn](https://www.linkedin.com/in/johansarria/)
