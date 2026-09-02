# -*- coding: utf-8 -*-
"""Edita C:\\brochure\\portfolio\\src\\App.jsx:
1) Inserta AUREN AI SALES como caso #1 (id 01) y renumerar 01-06 -> 02-07.
2) Reescribe la tarjeta de capacidades 'IA & Machine Learning' -> 'Agentes IA & Meta Business'.
Preserva los 6 proyectos originales byte a byte (solo cambia sus ids).
"""
import re

p = r'C:\brochure\portfolio\src\App.jsx'
src = open(p, encoding='utf-8').read()

# ---------- 1) Array projects ----------
start = src.index('const projects = [')
end = src.index('];', start) + 2
body = src[start:end]

# Renumerar ids existentes 01..06 -> 02..07 (en orden de aparición)
counter = [0]
def bump(m):
    counter[0] += 1
    return "id: '%02d'" % (counter[0] + 1)
body_new = re.sub(r"id: '\d\d'", bump, body)

auren_obj = """    {
      id: '01',
      title: 'AUREN AI SALES',
      area: 'AUTONOMOUS AI AGENTS',
      metric: 'Producción real · 24/7',
      description: 'Agente de ventas autónomo operando una tienda Shopify real (AUREN). Ejecuta posventa, recuperación de carritos y captura de leads sobre WhatsApp Business, sin intervención humana.',
      tags: ['Python', 'Docker', 'LLM', 'WhatsApp Business', 'Supabase'],
      challenge: 'Una tienda de calzado real sobre Shopify perdía ventas por carritos abandonados sin recuperación, notificaba guías de envío manualmente en horario laboral y no podía rastrear qué campañas generaban leads reales.',
      solution: 'Diseñé un agente autónomo (no un chatbot) que escucha los webhooks de la tienda, razona con contexto de negocio vía LLM y ejecuta: notificación inmediata de guías de envío por WhatsApp, escalera de recuperación de carritos con descuentos progresivos que aplican el cupón directamente en el checkout, y registro de cada lead con atribución UTM en Supabase con Row Level Security.',
      impactList: [
        'Posventa 24/7: cada cliente recibe su guía de envío en segundos, sin personal.',
        'Escalera de carritos automatizada: recordatorio + descuentos progresivos con CTA directo al checkout.',
        'Meta Business integrado: plantillas WABA aprobadas y mensurabilidad real de campañas por UTM.'
      ]
    },
"""

# Insertar AUREN justo después del '[' de apertura del array
open_bracket = body_new.index('[') + 1
body_final = body_new[:open_bracket] + '\n' + auren_obj + body_new[open_bracket:]

src = src[:start] + body_final + src[end:]

# ---------- 2) Tarjeta de capacidades ----------
old_card = """<h4 className="text-2xl font-bold tracking-tight uppercase">IA & Machine Learning</h4>
            <p className="text-white/40 font-light leading-relaxed">
              Integración de modelos predictivos y agentes LLM locales para automatización de procesos y análisis de datos sin exposición a la nube.
            </p>"""
new_card = """<h4 className="text-2xl font-bold tracking-tight uppercase">Agentes IA & Meta Business</h4>
            <p className="text-white/40 font-light leading-relaxed">
              Creación de agentes autónomos que operan negocios reales: WhatsApp Business (WABA) con plantillas aprobadas, embudos de conversión con descuentos automáticos y pipelines LLM locales o en la nube sin fuga de datos.
            </p>"""
assert old_card in src, 'tarjeta IA no encontrada'
src = src.replace(old_card, new_card)

open(p, 'w', encoding='utf-8', newline='\n').write(src)
print('OK: AUREN insertado como 01, ids renumerados 02-07, tarjeta reescrita')
print('ids en array:', re.findall(r"id: '\d\d'", src[src.index('const projects'):src.index('];', src.index('const projects'))]))
