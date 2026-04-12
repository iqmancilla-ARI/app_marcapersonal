"""
Portfolio Personal — J. Daniel Mancilla Malvaez
Data Scientist | Operations Analytics Specialist
"""

import streamlit as st

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="J. Daniel Mancilla — Data Scientist",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CUSTOM CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    /* Global */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* Hide Streamlit default elements */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1100px; }

    /* Hero name */
    .hero-name {
        font-family: 'DM Serif Display', serif;
        font-size: 3.8rem;
        font-weight: 400;
        color: #0D1F2D;
        line-height: 1.05;
        margin-bottom: 0.2rem;
    }
    .hero-name span { color: #1B6CA8; }

    /* Section headers */
    .section-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #2ABEBC;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }
    .section-title {
        font-family: 'DM Serif Display', serif;
        font-size: 2.2rem;
        color: #0D1F2D;
        margin-bottom: 1.5rem;
        line-height: 1.2;
    }

    /* Divider */
    .custom-divider {
        height: 3px;
        background: linear-gradient(to right, #1B6CA8, #2ABEBC, transparent);
        border: none;
        margin: 2rem 0;
        border-radius: 2px;
    }

    /* Stat cards */
    .stat-card {
        background: linear-gradient(135deg, #0D1F2D 0%, #1A3448 100%);
        border-radius: 10px;
        padding: 1.4rem;
        text-align: center;
        border: 1px solid rgba(42,190,188,0.2);
    }
    .stat-number {
        font-family: 'DM Serif Display', serif;
        font-size: 2.8rem;
        color: #2ABEBC;
        display: block;
        line-height: 1;
        margin-bottom: 0.4rem;
    }
    .stat-label {
        font-size: 0.78rem;
        color: #8BA3B8;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    /* Project cards */
    .project-card {
        background: #F8FAFE;
        border: 1px solid #E0E8F0;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #1B6CA8;
        transition: all 0.2s;
    }
    .project-num {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        color: #2ABEBC;
        letter-spacing: 0.15em;
        margin-bottom: 0.5rem;
    }
    .project-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #0D1F2D;
        margin-bottom: 0.5rem;
    }
    .project-desc {
        font-size: 0.88rem;
        color: #555;
        line-height: 1.7;
        margin-bottom: 0.8rem;
    }

    /* Tag pills */
    .tag-pill {
        display: inline-block;
        background: #E8F4FD;
        color: #1B6CA8;
        border: 1px solid #B8D8F0;
        border-radius: 4px;
        padding: 2px 10px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        margin: 2px;
    }
    .tag-pill-teal {
        background: #E0F7F5;
        color: #0F6E56;
        border-color: #9FE1CB;
    }
    .tag-pill-gold {
        background: #FEF9E7;
        color: #854F0B;
        border-color: #FAC775;
    }

    /* Skill bars */
    .skill-label {
        font-size: 0.85rem;
        font-weight: 500;
        color: #0D1F2D;
        margin-bottom: 3px;
    }

    /* Timeline */
    .timeline-item {
        border-left: 2px solid #1B6CA8;
        padding-left: 1.2rem;
        margin-bottom: 1.5rem;
        position: relative;
    }
    .timeline-dot {
        width: 10px;
        height: 10px;
        background: #2ABEBC;
        border-radius: 50%;
        position: absolute;
        left: -6px;
        top: 4px;
    }
    .timeline-date {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #2ABEBC;
        margin-bottom: 3px;
    }
    .timeline-role {
        font-size: 1rem;
        font-weight: 600;
        color: #0D1F2D;
        margin-bottom: 2px;
    }
    .timeline-company {
        font-size: 0.85rem;
        color: #E8C547;
        font-style: italic;
        margin-bottom: 5px;
    }
    .timeline-desc {
        font-size: 0.85rem;
        color: #555;
        line-height: 1.65;
    }

    /* Contact card */
    .contact-card {
        background: linear-gradient(135deg, #0D1F2D, #1A3448);
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid rgba(42,190,188,0.2);
    }
    .contact-card h3 {
        font-family: 'DM Serif Display', serif;
        color: white;
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .contact-card p { color: #8BA3B8; font-size: 0.9rem; line-height: 1.7; }

    /* Nav tabs override */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #F0F6FC;
        border-radius: 8px;
        padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 6px;
        font-weight: 500;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background: #1B6CA8 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════
col_hero, col_space = st.columns([3, 1])

with col_hero:
    st.markdown("""
    <div style="margin-bottom: 0.5rem;">
        <span style="font-family:'JetBrains Mono',monospace; font-size:0.78rem;
                     color:#2ABEBC; letter-spacing:0.15em;
                     background:#E0F7F5; padding:4px 12px;
                     border-radius:4px; border:1px solid rgba(42,190,188,0.3);">
            // disponible para nuevas oportunidades
        </span>
    </div>
    <div class="hero-name">J. Daniel<br><span>Mancilla</span></div>
    <div style="font-family:'DM Serif Display',serif; font-size:1.5rem;
                color:#E8C547; font-style:italic; margin-bottom:1rem;">
        Data Scientist & Operations Specialist
    </div>
    <p style="font-size:1rem; color:#555; line-height:1.75; max-width:580px; margin-bottom:1.5rem;">
        <strong>Ingeniero Químico con +15 años en operaciones industriales</strong> —
        manufactura, construcción MEP, agroindustria — en transición estratégica hacia
        Data Science aplicado. Convierto datos operativos en decisiones de negocio
        de alto impacto.
    </p>
    """, unsafe_allow_html=True)

    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    with col_btn1:
        st.link_button("💼 LinkedIn", "https://linkedin.com/in/pmomancilla", use_container_width=True)
    with col_btn2:
        st.link_button("💻 GitHub", "https://github.com/iqmancilla-ARI", use_container_width=True)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# STATS
# ══════════════════════════════════════════════════════════════
c1, c2, c3, c4 = st.columns(4)

stats = [
    ("+15", "Años en operaciones industriales"),
    ("+55%", "Incremento de productividad logrado"),
    ("4", "Proyectos DS desplegados"),
    ("3", "Sectores industriales liderados"),
]

for col, (num, label) in zip([c1, c2, c3, c4], stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <span class="stat-number">{num}</span>
            <span class="stat-label">{label}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TABS NAVIGATION
# ══════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "⚙️  Sobre mí",
    "📊  Proyectos DS",
    "🏭  Experiencia",
    "📬  Contacto",
])


# ────────────────────────────────────────────────────────────
# TAB 1 — SOBRE MÍ
# ────────────────────────────────────────────────────────────
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    col_bio, col_skills = st.columns([1.1, 1])

    with col_bio:
        st.markdown('<p class="section-tag">// 01. sobre mí</p>', unsafe_allow_html=True)
        st.markdown('<h2 class="section-title">El profesional<br>detrás del perfil</h2>', unsafe_allow_html=True)

        st.markdown("""
        <p style="color:#444; line-height:1.85; margin-bottom:1rem;">
            Combino <strong>experiencia operativa real en piso de planta</strong> con herramientas
            modernas de Data Science. Eso significa que no solo construyo modelos —
            entiendo los procesos que generan los datos, las preguntas que realmente
            importan y cómo comunicar los hallazgos a quienes toman decisiones.
        </p>
        <p style="color:#444; line-height:1.85; margin-bottom:1rem;">
            Trabajé en manufactura metalmecánica y alimentos, coordiné proyectos MEP en
            sectores farmacéutico, hotelero e industrial, y hoy construyo dashboards,
            pipelines de datos y aplicaciones analíticas desde mi consultora <strong>ARI</strong>.
        </p>
        <p style="color:#444; line-height:1.85;">
            Actualmente cursando el <strong>Bootcamp de Data Science de TripleTen</strong>,
            consolidando Python, SQL, Machine Learning y despliegue de aplicaciones sobre
            mi base de ingeniería industrial.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Especialidades:**")
        tags_ops = ["OEE", "TPM", "Lean Manufacturing", "Kaizen", "HACCP", "ISO 9001", "BIM/ISO 19650", "EVM/S-Curve"]
        pills_html = " ".join([f'<span class="tag-pill-teal">{t}</span>' for t in tags_ops])
        st.markdown(pills_html, unsafe_allow_html=True)

    with col_skills:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("**Stack técnico**")

        skills_code = {
            "Python (pandas · scipy · matplotlib)": 80,
            "SQL (PostgreSQL · SQLite)": 75,
            "EDA & Análisis Estadístico": 85,
            "Streamlit & Plotly": 75,
            "Machine Learning (en formación)": 45,
            "APIs REST & Web Scraping": 65,
        }

        skills_ops = {
            "OEE & KPIs de Producción": 95,
            "Lean Manufacturing & TPM": 95,
            "Gestión de Proyectos MEP": 90,
            "BIM / ArchiCAD": 80,
            "EVM / S-Curve": 85,
        }

        st.markdown("*Data Science:*")
        for skill, pct in skills_code.items():
            st.markdown(f'<div class="skill-label">{skill}</div>', unsafe_allow_html=True)
            st.progress(pct / 100)

        st.markdown("<br>*Operaciones Industriales:*", unsafe_allow_html=True)
        for skill, pct in skills_ops.items():
            st.markdown(f'<div class="skill-label">{skill}</div>', unsafe_allow_html=True)
            st.progress(pct / 100)

        st.markdown("<br>**Idiomas:**")
        st.markdown("""
        <span class="tag-pill">🇲🇽 Español — Nativo</span>
        <span class="tag-pill">🇺🇸 Inglés — C1 Advanced</span>
        <span class="tag-pill-gold">Visa US vigente</span>
        """, unsafe_allow_html=True)


# ────────────────────────────────────────────────────────────
# TAB 2 — PROYECTOS DS
# ────────────────────────────────────────────────────────────
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-tag">// 02. proyectos</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Data Science en acción</h2>', unsafe_allow_html=True)

    projects = [
        {
            "num": "01 / DS",
            "title": "Análisis de Planes Tarifarios — Megaline",
            "desc": "Determiné el plan tarifario más rentable para 500 clientes de telecomunicaciones. Apliqué EDA completo y prueba de hipótesis Welch's t-test para validar diferencias estadísticamente significativas con 95% de confianza — recomendación accionable para equipo comercial.",
            "tags": ["Python", "pandas", "scipy", "EDA", "Hipótesis", "seaborn"],
            "resultado": "✅ Identificé el plan más rentable con 95% de confianza",
            "link": "https://github.com/iqmancilla-ARI",
        },
        {
            "num": "02 / DS",
            "title": "Análisis de Ventas Globales de Videojuegos",
            "desc": "Procesé 16,715 registros históricos para identificar patrones de éxito comercial por plataforma, género y región. Construí perfiles de usuario diferenciados para NA, EU y JP para orientar estrategias de lanzamiento.",
            "tags": ["Python", "pandas", "scipy", "matplotlib", "Segmentación", "EDA"],
            "resultado": "✅ Perfiles regionales para 3 mercados distintos",
            "link": "https://github.com/iqmancilla-ARI",
        },
        {
            "num": "03 / DS · DEPLOYED",
            "title": "App Interactiva de Análisis de Vehículos",
            "desc": "Aplicación web interactiva desplegada en producción para exploración de dataset de vehículos usados. Tema visual personalizado con CSS, session state y filtros dinámicos. Disponible públicamente en Render.",
            "tags": ["Streamlit", "Plotly", "Render", "Python", "pandas", "CSS"],
            "resultado": "🚀 App en producción — disponible públicamente",
            "link": "https://github.com/iqmancilla-ARI",
        },
        {
            "num": "04 / REAL OPS",
            "title": "Sistema de Gestión de Licitaciones MEP — SQLite",
            "desc": "Base de datos relacional para seguimiento de pipeline comercial de ingeniería. Implementado en ARI Consulting con Python y SQLite — caso de uso real que redujo tiempos de gestión documental en +60%.",
            "tags": ["Python", "SQLite", "SQL", "Terminal", "Ops Real"],
            "resultado": "✅ Reducción +60% en tiempos de gestión",
            "link": "https://github.com/iqmancilla-ARI",
        },
    ]

    col_left, col_right = st.columns(2)

    for i, proj in enumerate(projects):
        target_col = col_left if i % 2 == 0 else col_right
        with target_col:
            tags_html = " ".join([f'<span class="tag-pill">{t}</span>' for t in proj["tags"]])
            st.markdown(f"""
            <div class="project-card">
                <div class="project-num">{proj['num']}</div>
                <div class="project-title">{proj['title']}</div>
                <div class="project-desc">{proj['desc']}</div>
                <div style="margin-bottom:0.8rem;">{tags_html}</div>
                <div style="font-size:0.82rem; color:#0F6E56; font-weight:500; margin-bottom:0.6rem;">{proj['resultado']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("→ Ver en GitHub", proj["link"], use_container_width=False)
            st.markdown("<br>", unsafe_allow_html=True)


# ────────────────────────────────────────────────────────────
# TAB 3 — EXPERIENCIA
# ────────────────────────────────────────────────────────────
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-tag">// 03. experiencia</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Trayectoria profesional</h2>', unsafe_allow_html=True)

    experience = [
        {
            "date": "01/2026 — Actualidad",
            "role": "Consultor Técnico MEP | Operations Data Analyst",
            "company": "ARI — Auditoría Técnica MEP (Consultoría Propia)",
            "desc": "Auditoría técnica MEP, licitaciones de ingeniería y herramientas de análisis operativo. Implementé sistema SQLite + Python para seguimiento de pipeline de licitaciones, reduciendo tiempos de gestión en +60%.",
        },
        {
            "date": "01/2020 — 12/2025",
            "role": "Gerente de Operaciones",
            "company": "Frimax S.A. de C.V. — Manufactura (Paneles de Poliuretano, FMCG)",
            "desc": "+55% de productividad mediante sistema de KPIs basado en OEE, análisis de causa raíz y proyectos Lean/TPM. Gestión CAPEX con control EVM. Operación de manufactura compleja.",
        },
        {
            "date": "01/2010 — 12/2019",
            "role": "Gerente de Proyectos MEP / Coordinador de Ingeniería",
            "company": "Proyectos Industriales y Construcción — Multisectorial",
            "desc": "Proyectos de hasta $50M MXN aplicando BIM/ISO 19650 y EVM/S-Curve. Equipos de hasta 40 ingenieros en sectores farmacéutico, hotelero, alimentario e industrial.",
        },
    ]

    col_exp, col_cert = st.columns([1.2, 1])

    with col_exp:
        st.markdown("**Experiencia laboral**")
        st.markdown("<br>", unsafe_allow_html=True)
        for exp in experience:
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-date">{exp['date']}</div>
                <div class="timeline-role">{exp['role']}</div>
                <div class="timeline-company">{exp['company']}</div>
                <div class="timeline-desc">{exp['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

    with col_cert:
        st.markdown("**Formación académica**")
        st.info("🎓 **Ingeniería Química**\nUniversidad de Guadalajara — CUCEI\nTitulado")
        st.info("📊 **Data Science Bootcamp** (en curso)\nTripleTen (Practicum) — 2024 a la fecha\nPython · SQL · ML · Streamlit · APIs")

        st.markdown("<br>**Certificaciones**", unsafe_allow_html=True)

        certs = [
            "📋 Project Management Professional (PMI/PMBOK)",
            "🏭 Lean Manufacturing & TPM",
            "🍽️ HACCP — Inocuidad alimentaria",
            "✅ ISO 9001:2015",
            "🏗️ BIM / ISO 19650",
            "🔥 NFPA 13, 14, 2001",
        ]
        for cert in certs:
            st.markdown(f"""
            <div style="background:#F8FAFE; border:1px solid #E0E8F0;
                        border-radius:6px; padding:8px 14px; margin-bottom:6px;
                        font-size:0.85rem; color:#333;">
                {cert}
            </div>
            """, unsafe_allow_html=True)


# ────────────────────────────────────────────────────────────
# TAB 4 — CONTACTO
# ────────────────────────────────────────────────────────────
with tab4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-tag">// 04. contacto</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">¿Hablamos?</h2>', unsafe_allow_html=True)

    col_contact, col_form = st.columns([1, 1.2])

    with col_contact:
        st.markdown("""
        <div class="contact-card">
            <h3>J. Daniel Mancilla M.</h3>
            <p>Estoy abierto a roles en <strong style="color:#2ABEBC">analítica industrial</strong>,
            <strong style="color:#2ABEBC">Data Science</strong> y
            <strong style="color:#2ABEBC">ConTech</strong>.</p>
            <br>
            <p>📍 Zapopan, Jalisco — México<br>
            🔄 Disponibilidad de relocalización nacional inmediata<br>
            🇺🇸 Visa US vigente<br>
            🌐 Inglés C1 Advanced</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.link_button("✉️  iq.mancilla@gmail.com", "mailto:iq.mancilla@gmail.com", use_container_width=True)
        st.link_button("💼  linkedin.com/in/pmomancilla", "https://linkedin.com/in/pmomancilla", use_container_width=True)
        st.link_button("💻  github.com/iqmancilla-ARI", "https://github.com/iqmancilla-ARI", use_container_width=True)

    with col_form:
        st.markdown("**Envíame un mensaje directo:**")
        nombre = st.text_input("Tu nombre")
        email = st.text_input("Tu email")
        asunto = st.selectbox("Asunto", [
            "Oportunidad laboral",
            "Proyecto de consultoría",
            "Colaboración técnica",
            "Otro",
        ])
        mensaje = st.text_area("Mensaje", height=130)

        if st.button("Enviar mensaje →", use_container_width=True, type="primary"):
            if nombre and email and mensaje:
                st.success(f"✅ Gracias **{nombre}**. Te respondo a la brevedad a **{email}**.")
                st.balloons()
            else:
                st.warning("Por favor completa todos los campos.")

# ── FOOTER ───────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center;
            font-family:'JetBrains Mono',monospace; font-size:0.75rem; color:#8BA3B8;">
    <span>© 2026 J. Daniel Mancilla Malvaez</span>
    <span>Zapopan, Jalisco — México</span>
    <span>Construido con Python + Streamlit</span>
</div>
""", unsafe_allow_html=True)
