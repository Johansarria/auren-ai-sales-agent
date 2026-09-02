# Arquitectura — Agente de Ventas AUREN

Documento de soporte del case study público. Describe el diseño a nivel conceptual, sin código, rutas ni credenciales. El autor diseñó e implementó el ecosistema completo: storefront Shopify (tema a medida), esquema Supabase con RLS y el agente autónomo.

## Vista de componentes

```
                        ┌──────────────────────┐
                        │   CLIENTE FINAL      │
                        │   (WhatsApp)         │
                        └──────────┬───────────┘
                                   │
                        ┌──────────▼───────────┐
                        │  WhatsApp Cloud API  │
                        │  (Meta · WABA)       │
                        └──────────┬───────────┘
                                   │ mensajes enviados
                                   │ webhooks de estado
┌──────────────────────┐           │
│  SHOPIFY (tienda)    │           │
│  aurenstore.store    │           │
│                      │           │
│  webhooks de pedidos │           │
└──────────┬───────────┘           │
           │                       │
           ▼                       ▼
   ┌───────────────────────────────────────┐
   │          AGENTE AUTÓNOMO              │
   │                                       │
   │  ┌────────────┐   ┌───────────────┐   │
   │  │ Orquestador │──▶│   LLM        │   │
   │  │ (Hermes)    │   │ (razonamiento)│   │
   │  └─────┬──────┘   └───────────────┘   │
   │        │                              │
   │  decide y ejecuta                     │
   └───┬──────────────┬────────────────────┘
       │              │
       ▼              ▼
┌──────────────┐ ┌──────────────────────────┐
│  SUPABASE    │ │  SHOPIFY ADMIN API       │
│  Postgres    │ │  (pedidos, stock,        │
│  + RLS       │ │   fulfillment)           │
└──────────────┘ └──────────────────────────┘
```

## Flujos principales

### 1. Notificación de guía (transaccional)
1. El transportista (Interrapísimo) genera la guía → la tienda marca el pedido `fulfilled` en Shopify.
2. Shopify emite el webhook `orders/fulfilled`.
3. El agente valida la firma del webhook (HMAC), consulta el detalle del pedido y el teléfono del cliente.
4. El agente envía una plantilla transaccional aprobada por Meta con la guía.
5. Resultado: el cliente recibe su número de seguimiento en segundos, 24/7, sin personal.

### 2. Escalera de recuperación de carritos
1. Shopify reporta un checkout abandonado (o el lead no completó compra).
2. El agente agenda la escalera: **toque 1** recordatorio → **toque 2** descuento (tier 1) → **toque 3** descuento (tier 2).
3. Cada toque usa una plantilla promocional aprobada con CTA de compra.
4. El CTA abre el checkout con el cupón ya aplicado (enlace con descuento), reduciendo fricción a un clic.
5. La conversión de cada toque se registra para medir el ROI de la escalera.

### 3. Captura de leads con atribución
1. El usuario hace clic en "WhatsApp" desde la web → un miniformulario pide su número antes de abrir el chat.
2. El teléfono y los parámetros UTM (campaña, medio, fuente) se registran en Supabase.
3. Atribución: cada lead sabe de qué campaña vino → el gasto en ads se audita contra ventas reales.

## Decisiones de diseño

| Decisión | Por qué |
|---|---|
| **Webhooks + agente, no polling** | Reacción en segundos; el agente solo trabaja cuando hay eventos reales |
| **Supabase con RLS** | Datos de clientes aislados por fila; un compromiso no expone la base completa |
| **Plantillas Meta aprobadas** | Único canal legítimo para mensajes proactivos en WhatsApp Business; protege la calidad del número |
| **Sistema privado + narrativa pública** | El valor del caso es demostrable sin exponer la operación |
| **Enlace de descuento directo al checkout** | Elimina la fricción "copiar cupón" — la conversión sube con menos pasos |

## Superficie de ataque controlada

- Firma HMAC en webhooks entrantes (solo eventos legítimos de Shopify).
- Secretos en variables de entorno del contenedor, nunca en el repositorio.
- Principio de mínimos privilegios en los tokens de API (scopes acotados a lo que el agente ejecuta).
- RLS activo en toda tabla con datos de personas.
