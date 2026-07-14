Necesito un post de **presentación de staff** para Nordic Barber Shop (esto no es un post de "bienvenida a nuevo empleado" específicamente — es una serie de "conocé al equipo" que podemos usar para cualquier miembro del staff, nuevo o no). Te voy a dar una foto real (selfie/foto de celular), el nombre de la persona y su puesto. Quiero que generes el post completo (feed + story, SIEMPRE ambas versiones) siguiendo exactamente este proceso, que ya usamos antes en este repo para un post similar (`posts/instagram/bienvenida-jennifer-host/` — ese nombre de carpeta quedó de la primera vez que lo hicimos, pero de aquí en adelante la serie es "presentación de staff", no "bienvenida"):

**Nombre:** [NOMBRE]
**Puesto:** [PUESTO — ej. Barbero, Host/Recepción, Estilista, Manager, etc.]
**Foto:** [adjunta la foto]

### 1. Retocar la foto (Gemini, no Higgsfield)

Usa `scripts/gemini_image_gen.py` (Gemini `gemini-3-pro-image-preview`, lee `GEMINI_API_KEY` de `scripts/.env`), pasando la foto original como `--image` de referencia. Un solo pase con un prompt que pida, todo junto:

- Preservar 100% la identidad real: mismo rostro, expresión, sonrisa, rasgos — nada de reshapear o "embellecer" facciones.
- Encuadre de medio cuerpo, alejado — NO un close-up directo a la cara. La cara debe ocupar una porción menor del cuadro (a lo mucho un tercio-mitad de la altura), con espacio alrededor, ángulo menos frontal/confrontativo.
- **Vestuario y props: dependen del puesto — decide según el rol antes de escribir el prompt de retoque:**
  - **Barbero/estilista:** vestir la gabardina/capa negra de barbero (el smock clásico de barbería), y opcionalmente ponerle en las manos un objeto acorde a su oficio — tijeras, secadora/blower, máquina de cortar, peine — en una pose natural de "en acción" o sosteniendo la herramienta con confianza. Que se vea como un profesional de la barbería, no un disfraz.
  - **Host/recepción, manager, u otro puesto sin uniforme propio:** vestuario formal pero simple, TODO EN NEGRO (camisa de botón, blusa negra, etc.) — nada de mandil ni herramientas de barbero, porque no aplica a su rol.
  - Si no estás seguro de qué props tiene sentido para un puesto nuevo, pregúntale al usuario antes de generar en vez de asumir.
- Tratamiento de marca: duotono blanco y negro de alto contraste + luz dorada cálida (rim/key light) sobre la persona, fondo de barbería limpio y desenfocado. Nada de fotografía a color.
- Piel: un suavizado sutil tipo filtro de Instagram (parejo, natural, no plástico).
- Salida en alta resolución, orientación vertical (aprox. 4:5).

Revisa el resultado abriéndolo en Preview antes de continuar. Si el encuadre sigue muy cerrado/directo, el vestuario/props no corresponden al rol, o la ropa no cambió, vuelve a intentar con el prompt ajustado — no sigas con una que no cumpla estos puntos.

### 2. Armar el tile de Feed (Option B, hybrid HTML overlay)

Sigue `carousel-tile-generation.md` Opción B, pero usando la foto real retocada como "fondo" en vez de una generada por IA. Carpeta: `posts/instagram/staff-[slug-nombre]-[puesto]/` con `assets/`, `refs/`, `raw/` (copia fuentes y el logo `Nordic-BarberShop-logo-white.svg` de cualquier post existente).

Canvas 1080×1350 (4:5). Layout (ya validado con el usuario, replicar tal cual):
- Foto a ancho completo (1080px, alto automático), anclada arriba, sin recortar de nuevo.
- Logo Nordic en la esquina **superior derecha**, a **120px de alto** (el doble del tamaño base de 60px que se usa en otros posts).
- Bloque de texto (pill + headline + rol + caption) anclado como un solo grupo en la parte de **abajo** del tile (no arriba), con `display:flex; flex-direction:column; gap:18px` dentro de un contenedor `position:absolute; left/right:64px; bottom:64px`.
- Pill: **"NUESTRO EQUIPO"** (no "BIENVENIDA" — la serie ya no es de bienvenida) — amarillo `#FFD200`, texto Fira Sans Condensed 800. Si un post puntual sí es de alguien recién contratado, confirma con el usuario si prefiere "BIENVENIDA" para ese caso específico.
- Headline en Lost in South: "TE PRESENTAMOS A [NOMBRE]" con el nombre en amarillo (`.hl`).
- Rol: "[PUESTO]" en mayúsculas, Fira Sans Condensed 800, amarillo, tamaño ~30px.
- Caption: tono cálido/amigable pero corto — NO uses frases tipo "con toda la buena onda" (sonó forzado/raro cuando lo probamos). Escribe algo específico al rol (ej. para un barbero: "El fade que estabas buscando, en sus manos." — para host: "Ella te recibirá con una sonrisa apenas llegués a Nordic."). Ajusta el verbo/persona según corresponda.
- Scrim (gradiente oscuro) arriba (para legibilidad del logo) y abajo (para legibilidad del texto).

Renderiza con headless Chrome a `00-portada.png` (2160×2700, `--force-device-scale-factor=2`, `--window-size=1080,1350`).

### 3. Versión Story (mismo tile, sin recortar la foto de nuevo)

`index-story.html`, canvas 1080×1920. Reglas clave (ya afinadas con el usuario en varias rondas, no las repitas desde cero):

- La foto va con **ancho fijo 1080px, alto automático, anclada arriba** — NO uses `object-fit:cover` a pantalla completa (eso recortaría la foto otra vez, que el usuario no quiere).
- El alto natural de la foto (normalmente ~1300-1350px) deja un área inferior en el fondo oscuro de marca (`#101010`) — ahí vive el bloque de texto.
- Logo top-right igual que en el feed (120px), pero bajado a `top:270px` para respetar la zona segura de Instagram Stories (documentada en `design-system.md` §8: despejar los primeros ~250px y los últimos ~220px).
- Bloque de texto anclado abajo con `bottom:240px` (mismo patrón flex-column que el feed), fuentes un poco más grandes que en feed (headline ~92px, rol ~34px, caption ~36px).
- **El fade entre la foto y el fondo negro es lo más delicado — no lo hagas a ojo, usa este gradiente ya validado:** `scrim-bottom` con `height:1250px` y este gradiente exacto (`to top`):
  ```
  rgba(16,16,16,1) 0%,
  rgba(16,16,16,1) 50%,
  rgba(16,16,16,.55) 70%,
  rgba(16,16,16,.22) 85%,
  rgba(16,16,16,0) 100%
  ```
  La clave: el tramo 100% opaco (0%–50%) debe llegar hasta justo el borde real de abajo de la foto (para tapar el corte rectangular de la imagen), y el fade a transparente ocurre más arriba, dentro de la foto visible, en un tramo largo — así no se ve una línea dura entre la foto y el negro. Si cambia el alto de la foto retocada, recalculá el % donde cae el borde real (`(1920 - y_borde) / height_scrim`) y ajustá el primer stop opaco para que caiga ahí, no antes.

Renderiza a `00-story.png` (2160×3840).

### 4. Checklist de cierre (obligatorio, no esperes que te lo pidan)

1. Abre ambos PNG finales en Preview (`open -a Preview ...`).
2. Escribe `copy.json` (pill, headline, headline_highlight, role, caption_on_image, instagram_caption con tono cálido, build_method explicando el proceso, incluyendo qué vestuario/props se usaron y por qué).
3. Agrega DOS entradas al arreglo `POSTS` en el `index.html` raíz (una `label:'Versión: Feed'`, otra `label:'Versión: Story'`, mismo `copyJson`), y confirma con un screenshot headless que las tarjetas nuevas se ven bien en el showcase.
4. Commit de todo (fotos, html, copy.json, index.html) en un solo commit por unidad de trabajo lógica.

### Notas de tono (aplican a este y a cualquier post nuevo)

El tono de marca se actualizó a "confident, short, **warm**" (antes "a little dry") — ver `design-system.md` §9. Habla a la gente como un amigo que llega a la barbería, no como un aviso frío. Evita también sonar demasiado informal/forzado (nada de "buena onda" u otras muletillas que suenen impostadas).
