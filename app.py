"""
Portfolio Personal — J. Daniel Mancilla Malvaez
Data Scientist | Operations Analytics Specialist
Blueprint palette + IBM Plex Sans
"""

import streamlit as st

st.set_page_config(
    page_title="Daniel Mancilla",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'IBM Plex Sans', sans-serif !important;
    background-color: #F6F4EF !important;
    color: #12233A !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 2.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1080px !important;
}

.hero-badge {
    display: inline-block;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #1458A8;
    background: #E8F1FB;
    border: 1.5px solid #2B7FD4;
    border-radius: 3px;
    padding: 5px 14px;
    margin-bottom: 1.2rem;
}
.hero-name {
    font-weight: 700;
    font-size: clamp(2.6rem, 5vw, 4.2rem);
    color: #12233A;
    line-height: 1.05;
    margin-bottom: 0.3rem;
}
.hero-name span { color: #1458A8; }
.hero-role {
    font-weight: 300;
    font-size: 1.3rem;
    color: #2B7FD4;
    margin-bottom: 1.2rem;
    letter-spacing: 0.02em;
}
.hero-desc {
    font-size: 0.98rem;
    color: #4B6A8A;
    line-height: 1.8;
    max-width: 560px;
}
.hero-desc strong { color: #12233A; font-weight: 600; }

.bp-divider {
    height: 2px;
    background: linear-gradient(to right, #1458A8 0%, #2B7FD4 40%, #E8F1FB 100%);
    border: none;
    margin: 2rem 0;
    border-radius: 2px;
}

.stat-card {
    background: #FFFFFF;
    border: 1px solid #D0E2F4;
    border-top: 4px solid #1458A8;
    border-radius: 6px;
    padding: 1.4rem 1rem;
    text-align: center;
}
.stat-num {
    font-weight: 700;
    font-size: 2.3rem;
    color: #1458A8;
    display: block;
    line-height: 1;
    margin-bottom: 0.5rem;
}
.stat-lbl {
    font-size: 0.76rem;
    color: #4B6A8A;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 500;
    line-height: 1.45;
}

.sec-tag {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    color: #2B7FD4;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    display: block;
    margin-bottom: 0.4rem;
}
.sec-title {
    font-weight: 700;
    font-size: 2rem;
    color: #12233A;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}
.sec-title span { color: #1458A8; }

.proj-card {
    background: #FFFFFF;
    border: 1px solid #D0E2F4;
    border-radius: 8px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
    border-left: 5px solid #1458A8;
}
.proj-num {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.68rem;
    color: #2B7FD4;
    letter-spacing: 0.15em;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
}
.proj-title {
    font-weight: 600;
    font-size: 1rem;
    color: #12233A;
    margin-bottom: 0.5rem;
    line-height: 1.3;
}
.proj-desc {
    font-size: 0.87rem;
    color: #4B6A8A;
    line-height: 1.75;
    margin-bottom: 0.9rem;
}
.proj-result {
    font-size: 0.82rem;
    color: #1A6B3A;
    font-weight: 600;
    background: #EAF7EE;
    border: 1px solid #B0DFC0;
    border-radius: 4px;
    padding: 5px 12px;
    display: inline-block;
    margin-top: 0.6rem;
}

.tag {
    display: inline-block;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    padding: 3px 9px;
    border-radius: 3px;
    margin: 2px 2px 2px 0;
    font-weight: 500;
}
.tag-blue  { background: #E8F1FB; color: #1458A8; border: 1px solid #B8D4F0; }
.tag-slate { background: #EEF2F7; color: #4B6A8A; border: 1px solid #C8D8E8; }
.tag-green { background: #EAF7EE; color: #1A6B3A; border: 1px solid #B0DFC0; }

.tl-item {
    border-left: 2px solid #D0E2F4;
    padding-left: 1.3rem;
    margin-bottom: 2rem;
    position: relative;
}
.tl-dot {
    width: 11px; height: 11px;
    background: #1458A8;
    border-radius: 50%;
    position: absolute;
    left: -6.5px; top: 3px;
    border: 2px solid #F4F7FB;
}
.tl-dot-active { background: #2B7FD4; box-shadow: 0 0 0 3px #E8F1FB; }
.tl-date {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    color: #2B7FD4;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
}
.tl-role  { font-weight: 600; font-size: 1rem; color: #12233A; margin-bottom: 2px; line-height: 1.3; }
.tl-company { font-size: 0.85rem; color: #1458A8; font-weight: 500; margin-bottom: 6px; }
.tl-desc  { font-size: 0.85rem; color: #4B6A8A; line-height: 1.7; }
.tl-desc strong { color: #12233A; }

.sk-label {
    font-size: 0.85rem;
    font-weight: 500;
    color: #12233A;
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
}
.sk-label span { color: #4B6A8A; font-weight: 400; font-size: 0.78rem; }

.stProgress > div > div > div > div { background: #1458A8 !important; }

.contact-card {
    background: #12233A;
    border-radius: 10px;
    padding: 2rem;
}
.contact-card h3 { font-weight: 700; font-size: 1.4rem; color: #FFFFFF; margin-bottom: 0.5rem; }
.contact-card p { color: #A8C0D8; font-size: 0.9rem; line-height: 1.8; }
.contact-card strong { color: #2B7FD4; }

.cert-pill {
    background: #FFFFFF;
    border: 1px solid #D0E2F4;
    border-left: 4px solid #2B7FD4;
    border-radius: 5px;
    padding: 8px 14px;
    margin-bottom: 7px;
    font-size: 0.84rem;
    color: #12233A;
    font-weight: 500;
}

.stTabs [data-baseweb="tab-list"] {
    background: #FFFFFF !important;
    border-bottom: 2px solid #D0E2F4 !important;
    gap: 0 !important;
    padding: 0 !important;
    border-radius: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    color: #4B6A8A !important;
    padding: 0.75rem 1.5rem !important;
    border-radius: 0 !important;
    border-bottom: 3px solid transparent !important;
    margin-bottom: -2px !important;
}
.stTabs [aria-selected="true"] {
    color: #1458A8 !important;
    border-bottom: 3px solid #1458A8 !important;
    background: transparent !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════
col_h, _ = st.columns([3, 1])
with col_h:
    st.markdown("""
    <div class="hero-badge">// Disponible para nuevas oportunidades</div>
    <div class="hero-name">JDMM | <span>Daniel Mancilla</span></div>
    <div class="hero-role">Operations|Data Scientist|MEP Construction<br>|Lean &amp; Process Optimization</div>
    <p class="hero-desc">
        <strong>Líder en Operaciones con +15 años en manufactura &amp; construcción MEP</strong> —
        Transformo operaciones en resultados mediante LEAN, AGILE, analítica y digitalización.
        Conecto estrategia, ciencia de datos y ejecución para maximizar rentabilidad y lograr crecimiento.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1.2, 1.2, 2])
    with b1:
        st.link_button(
            "💼 LinkedIn", "https://linkedin.com/in/pmomancilla", use_container_width=True)
    with b2:
        st.link_button(
            "💻 GitHub", "https://github.com/iqmancilla-ARI", use_container_width=True)

st.markdown('<div class="bp-divider"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# STATS
# ══════════════════════════════════════════════════════════════
s1, s2, s3, s4 = st.columns(4)
for col, (num, lbl) in zip(
    [s1, s2, s3, s4],
    [("+15", "Años en operaciones industriales"), ("+55%", "Incremento de productividad logrado"),
     ("4", "Proyectos DS desplegados"), ("3", "Sectores industriales liderados")]
):
    with col:
        st.markdown(f'<div class="stat-card"><span class="stat-num">{num}</span><span class="stat-lbl">{lbl}</span></div>',
                    unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs(
    ["⚙️  Sobre mí", "📊  Proyectos DS", "🏭  Experiencia", "📬  Contacto"])


# ── TAB 1 ────────────────────────────────────────────────────
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    c_bio, c_sk = st.columns([1.1, 1])

    with c_bio:
        st.markdown('<span class="sec-tag">// 01. sobre mí</span>',
                    unsafe_allow_html=True)
        st.markdown(
            '<div class="sec-title">El profesional<br><span>detrás del perfil</span></div>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color:#4B6A8A;line-height:1.85;margin-bottom:1rem;font-size:0.97rem;">
        Combino <strong style="color:#12233A">experiencia operativa real en piso de planta</strong>
        con herramientas modernas de Data Science. No solo construyo modelos —
        entiendo los procesos que generan los datos y cómo comunicar hallazgos
        a quienes toman decisiones.
        </p>
        <p style="color:#4B6A8A;line-height:1.85;margin-bottom:1rem;font-size:0.97rem;">
        Trabajé en manufactura metalmecánica y alimentos, coordiné proyectos MEP
        en sectores farmacéutico, hotelero e industrial, y hoy construyo dashboards
        y pipelines de datos desde mi consultora <strong style="color:#12233A">ARI</strong>.
        </p>
        <p style="color:#4B6A8A;line-height:1.85;font-size:0.97rem;">
        Cursando el <strong style="color:#12233A">Bootcamp de Data Science de TripleTen</strong>
        — Python, SQL, Machine Learning y despliegue de aplicaciones.
        </p><br>
        """, unsafe_allow_html=True)
        st.markdown("**Operaciones industriales:**")
        st.markdown(" ".join([f'<span class="tag tag-slate">{t}</span>' for t in
                              ["OEE", "TPM", "Lean Manufacturing", "Kaizen", "HACCP", "ISO 9001", "BIM/ISO 19650", "EVM/S-Curve"]]),
                    unsafe_allow_html=True)
        st.markdown("<br>**Stack técnico:**", unsafe_allow_html=True)
        st.markdown(" ".join([f'<span class="tag tag-blue">{t}</span>' for t in
                              ["Python", "pandas", "scipy", "matplotlib", "SQL", "PostgreSQL", "SQLite", "Streamlit", "Plotly", "GitHub"]]),
                    unsafe_allow_html=True)

    with c_sk:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Data Science:**")
        for sk, pct in [("Python (pandas · scipy · matplotlib)", 80), ("SQL (PostgreSQL · SQLite)", 75),
                        ("EDA & Análisis Estadístico",
                         85), ("Streamlit & Plotly", 75),
                        ("Machine Learning (scikit-learn)", 45), ("APIs REST & Web Scraping", 65)]:
            st.markdown(
                f'<div class="sk-label">{sk}<span>{pct}%</span></div>', unsafe_allow_html=True)
            st.progress(pct/100)
        st.markdown("<br>**Operaciones Industriales:**")
        for sk, pct in [("OEE & KPIs de Producción", 95), ("Lean Manufacturing & TPM", 95),
                        ("Gestión de Proyectos MEP", 90), ("BIM / ArchiCAD", 80), ("EVM / S-Curve", 85)]:
            st.markdown(
                f'<div class="sk-label">{sk}<span>{pct}%</span></div>', unsafe_allow_html=True)
            st.progress(pct/100)
        st.markdown("<br>**Idiomas:**")
        st.markdown("""
        <span class="tag tag-blue">🇲🇽 Español — Nativo</span>
        <span class="tag tag-blue">🇺🇸 Inglés — C1 Advanced</span>
        <span class="tag tag-green">Visa US vigente</span>
        <span class="tag tag-green">Relocalización inmediata</span>
        """, unsafe_allow_html=True)


# ── TAB 2 ────────────────────────────────────────────────────
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<span class="sec-tag">// 02. proyectos</span>',
                unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Data Science <span>en acción</span></div>',
                unsafe_allow_html=True)

    projs = [
        ("01 / Data Science", "Análisis de Planes Tarifarios — Megaline",
         "Determiné el plan tarifario más rentable para 500 clientes mediante EDA y prueba de hipótesis Welch's t-test con 95% de confianza.",
         ["Python", "pandas", "scipy", "EDA", "Hipótesis"], "✅ Plan más rentable — 95% confianza"),
        ("02 / Data Science", "Análisis de Ventas Globales de Videojuegos",
         "Procesé 16,715 registros para identificar patrones por plataforma, género y región. Perfiles diferenciados para NA, EU y JP.",
         ["Python", "pandas", "scipy", "matplotlib", "Segmentación"], "✅ Perfiles para 3 mercados"),
        ("03 / DS · Deployed", "App Interactiva de Análisis de Vehículos",
         "Aplicación web interactiva en producción. CSS personalizado, session state y filtros dinámicos desplegada en Render.",
         ["Streamlit", "Plotly", "Render", "Python", "pandas"], "🚀 App pública en producción"),
        ("04 / Ops Real", "Sistema de Gestión de Licitaciones MEP",
         "Base de datos relacional SQLite para pipeline comercial de ARI Consulting. Gestión de convocatorias y seguimiento en tiempo real.",
         ["Python", "SQLite", "SQL", "Terminal"], "✅ Reducción +60% tiempos de gestión"),
    ]

    cl, cr = st.columns(2)
    for i, (num, title, desc, tags, res) in enumerate(projs):
        with (cl if i % 2 == 0 else cr):
            tags_html = " ".join(
                [f'<span class="tag tag-blue">{t}</span>' for t in tags])
            st.markdown(f"""
            <div class="proj-card">
                <div class="proj-num">{num}</div>
                <div class="proj-title">{title}</div>
                <div class="proj-desc">{desc}</div>
                {tags_html}
                <div class="proj-result">{res}</div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("→ Ver en GitHub",
                           "https://github.com/iqmancilla-ARI")
            st.markdown("<br>", unsafe_allow_html=True)


# ── TAB 3 ────────────────────────────────────────────────────
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    ct, ce = st.columns([1.2, 1])

    with ct:
        st.markdown('<span class="sec-tag">// 03. experiencia</span>',
                    unsafe_allow_html=True)
        st.markdown(
            '<div class="sec-title">Trayectoria <span>profesional</span></div>', unsafe_allow_html=True)
        for date, role, company, desc, active in [
            ("01/2026 — Actualidad", "Consultor Técnico MEP | Operations Data Analyst",
             "ARI — Consultoría Técnica MEP",
             "Auditoría MEP y herramientas de análisis operativo. <strong>Sistema SQLite + Python</strong> redujo tiempos de gestión en +60%.", True),
            ("01/2020 — 12/2025", "Gerente de Operaciones",
             "Frimax S.A. de C.V. — Manufactura FMCG",
             "<strong>+55% productividad</strong> mediante OEE, causa raíz y Lean/TPM. Gestión CAPEX con control EVM.", False),
            ("01/2010 — 12/2019", "Gerente de Proyectos MEP / Coordinador de Ingeniería",
             "Proyectos Industriales y Construcción — Multisectorial",
             "Proyectos de hasta <strong>$50M MXN</strong> con BIM/ISO 19650 y EVM. Equipos de hasta 40 ingenieros.", False),
        ]:
            dot = "tl-dot tl-dot-active" if active else "tl-dot"
            st.markdown(f"""
            <div class="tl-item">
                <div class="{dot}"></div>
                <div class="tl-date">{date}</div>
                <div class="tl-role">{role}</div>
                <div class="tl-company">{company}</div>
                <div class="tl-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)

    with ce:
        st.markdown('<span class="sec-tag">// formación</span>',
                    unsafe_allow_html=True)
        st.markdown(
            '<div class="sec-title" style="font-size:1.6rem;">Educación &<br><span>Certificaciones</span></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="proj-card" style="border-left-color:#2B7FD4;">
            <div class="proj-num">Universidad de Guadalajara — CUCEI</div>
            <div class="proj-title">Ingeniería Química — Titulado</div>
        </div>
        <div class="proj-card">
            <div class="proj-num">TripleTen (Practicum) · 2024 — Actualidad</div>
            <div class="proj-title">Data Science Bootcamp</div>
            <div class="proj-desc" style="margin-bottom:0.5rem;">Python · SQL · ML · Streamlit · APIs</div>
            <span class="tag tag-green">En curso</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("**Certificaciones:**")
        for c in ["📋 Project Management Professional (PMI/PMBOK)", "🏭 Lean Manufacturing & TPM",
                  "🍽️ HACCP — Inocuidad alimentaria", "✅ ISO 9001:2015", "🏗️ BIM / ISO 19650", "🔥 NFPA 13, 14, 2001"]:
            st.markdown(
                f'<div class="cert-pill">{c}</div>', unsafe_allow_html=True)


# ── TAB 4 ────────────────────────────────────────────────────
with tab4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<span class="sec-tag">// 04. contacto</span>',
                unsafe_allow_html=True)
    st.markdown('<div class="sec-title">¿<span>Hablamos</span>?</div>',
                unsafe_allow_html=True)

    ci, cf = st.columns([1, 1.2])
    with ci:
        st.markdown("""
        <div class="contact-card">
            <h3>J. Daniel Mancilla M.</h3>
            <p>Abierto a roles en<br>
            <strong>analítica industrial</strong>, <strong>Data Science</strong> y <strong>ConTech</strong>.</p>
            <br>
            <p>📍 Zapopan, Jalisco — México<br>
            🔄 Relocalización nacional inmediata<br>
            🇺🇸 Visa US vigente<br>
            🌐 Inglés C1 Advanced</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("✉️  iq.mancilla@gmail.com",
                       "mailto:iq.mancilla@gmail.com", use_container_width=True)
        st.link_button("💼  linkedin.com/in/pmomancilla",
                       "https://linkedin.com/in/pmomancilla", use_container_width=True)
        st.link_button("💻  github.com/iqmancilla-ARI",
                       "https://github.com/iqmancilla-ARI", use_container_width=True)

    with cf:
        st.markdown("**Envíame un mensaje:**")
        nombre = st.text_input("Nombre")
        email_ = st.text_input("Email")
        asunto = st.selectbox("Asunto", [
                              "Oportunidad laboral", "Proyecto de consultoría", "Colaboración técnica", "Otro"])
        mensaje = st.text_area("Mensaje", height=140,
                               placeholder="Cuéntame sobre la oportunidad...")
        if st.button("Enviar mensaje →", use_container_width=True, type="primary"):
            if nombre and email_ and mensaje:
                st.success(
                    f"✅ Gracias **{nombre}** — te respondo a **{email_}** a la brevedad.")
                st.balloons()
            else:
                st.warning("Completa todos los campos.")


# ── FOOTER ───────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="bp-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="display:flex;justify-content:space-between;
            font-family:'IBM Plex Mono',monospace;
            font-size:0.72rem;color:#4B6A8A;padding:0.5rem 0;">
    <span>© 2026 J. Daniel Mancilla Malvaez</span>
    <span>Zapopan, Jalisco — México</span>
    <span>Python · Streamlit</span>
</div>
""", unsafe_allow_html=True)
