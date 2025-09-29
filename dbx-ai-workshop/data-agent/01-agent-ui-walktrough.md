# Agent Bricks – UI Walkthrough

## ¿Qué es Agent Bricks?
Agent Bricks es la funcionalidad de Databricks que permite crear **agentes de IA** que entienden tu **Lakehouse**.  
Los agentes pueden responder en lenguaje natural, generar SQL seguro y respetar permisos de Unity Catalog.

## ¿Por qué usarlo?
- **Democratización**: usuarios no técnicos pueden consultar datos sin aprender SQL.  
- **Seguridad**: solo muestra lo que el usuario tiene permiso de ver en UC.  
- **Rapidez**: reduce tiempo en análisis exploratorio.  

### Ejemplo de caso de uso:
Un analista de ventas en retail puede preguntar directamente:  
> “¿Cuáles son los 5 clientes con más gasto en el último mes?”  
y obtener el resultado en segundos, sin depender del equipo de BI.

---

## Demo – Crear un agente

1. Abre **Genie / Agent Bricks** en la barra lateral de Databricks.  
2. Haz clic en **Create new Agent / Space** y llama al agente `Sales-Agent-Demo`.  
3. Conecta datasets: selecciona las tablas `customers`, `products`, `orders` de tu esquema (`main.demo_llm`).  
4. Añade un contexto descriptivo:  
   > “Datos ficticios de retail: clientes, órdenes y productos.”  
5. Prueba estas preguntas (puedes copiarlas de `sample_queries.md`):  
   - “Top 5 customers by total spend last 7 days”  
   - “Orders by status”  
   - “Revenue by product category”  
6. Muestra la traducción SQL que genera el agente → explica que es **transparente y auditable**.  

👉 **Resultado esperado**: un agente que responde en lenguaje natural con SQL seguro, demostrando el poder de democratizar datos sin perder control.
