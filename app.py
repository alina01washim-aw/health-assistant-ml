import os
import pickle
from urllib.parse import quote

import streamlit as st
from streamlit_option_menu import option_menu

# ------------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------------
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

working_dir = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------
# Load the saved models (unchanged)
# ------------------------------------------------------------------
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))


# ------------------------------------------------------------------
# Small helpers
# ------------------------------------------------------------------
def html(s: str) -> str:
    """Strip indentation / blank lines so Streamlit's markdown never
    turns our HTML into a code block."""
    return "\n".join(line.strip() for line in s.strip().splitlines() if line.strip())


def svg_icon(inner: str, color: str = "#b0508a") -> str:
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' "
            f"stroke='{color}' stroke-width='1.8' stroke-linecap='round' "
            f"stroke-linejoin='round'>{inner}</svg>")


# Icons shown inside the input boxes
ICONS = {
    "user":     "<circle cx='12' cy='8' r='4'/><path d='M4 21c0-4 4-7 8-7s8 3 8 7'/>",
    "drop":     "<path d='M12 3C12 3 5 11 5 15a7 7 0 0014 0c0-4-7-12-7-12z'/>",
    "heart":    "<path d='M12 21C5 15 3 11 3 8a4.5 4.5 0 018-2.8A4.5 4.5 0 0121 8c0 3-2 7-9 13z'/>",
    "layers":   "<path d='M12 3l9 5-9 5-9-5 9-5z'/><path d='M3 13l9 5 9-5'/>",
    "syringe":  "<path d='M4 20l6-6'/><path d='M13 5l6 6'/><path d='M11 7l6 6-5 5-6-6z'/>",
    "scale":    "<rect x='4' y='4' width='16' height='16' rx='3'/><path d='M8 10a4 4 0 018 0'/><path d='M12 10l2-2'/>",
    "nodes":    ("<circle cx='6' cy='6' r='2'/><circle cx='18' cy='6' r='2'/><circle cx='6' cy='18' r='2'/>"
                 "<circle cx='18' cy='18' r='2'/><circle cx='12' cy='12' r='2'/>"
                 "<path d='M7.5 7.5l3 3M16.5 7.5l-3 3M7.5 16.5l3-3M16.5 16.5l-3-3'/>"),
    "calendar": "<rect x='4' y='5' width='16' height='16' rx='2'/><path d='M4 10h16M9 3v4M15 3v4'/>",
    "pulse":    "<path d='M3 12h4l3-8 4 16 3-8h4'/>",
}


def icon_uri(key: str) -> str:
    return "data:image/svg+xml," + quote(svg_icon(ICONS[key]), safe="")


# ------------------------------------------------------------------
# Illustrations (inline SVG, no external files needed)
# ------------------------------------------------------------------
LOGO_SVG = """
<svg viewBox="0 0 64 56" width="46" height="40" xmlns="http://www.w3.org/2000/svg">
<path d="M32 52C10 36 3 24 3 15 3 8 9 3 16 3c7 0 12 4 16 10C36 7 41 3 48 3c7 0 13 5 13 12 0 9-7 21-29 37z"
 fill="none" stroke="#d6247f" stroke-width="3.5" stroke-linejoin="round"/>
<path d="M8 28h14l5-12 7 22 5-10h17" fill="none" stroke="#d6247f" stroke-width="3.5"
 stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""

HERO_SVG = """
<svg viewBox="0 0 330 190" xmlns="http://www.w3.org/2000/svg" width="100%">
<defs>
<linearGradient id="hg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#ff6fa8"/><stop offset="1" stop-color="#e8458c"/>
</linearGradient>
</defs>
<ellipse cx="210" cy="150" rx="150" ry="40" fill="#fbd6e8" opacity=".55"/>
<g fill="#f4a3c8" opacity=".85">
<ellipse cx="38" cy="120" rx="10" ry="22" transform="rotate(-30 38 120)"/>
<ellipse cx="62" cy="140" rx="10" ry="22" transform="rotate(-10 62 140)"/>
<ellipse cx="300" cy="70" rx="10" ry="24" transform="rotate(30 300 70)"/>
<ellipse cx="312" cy="105" rx="10" ry="24" transform="rotate(15 312 105)"/>
<ellipse cx="292" cy="140" rx="9" ry="20" transform="rotate(35 292 140)"/>
</g>
<path d="M105 160C38 125 22 92 22 66 22 38 44 22 68 22c18 0 32 10 37 26 5-16 19-26 37-26 24 0 46 16 46 44 0 26-16 59-83 94z"
 transform="translate(10 -10) scale(.95)" fill="url(#hg)"/>
<path d="M50 78h28l10-24 14 44 12-26h40" fill="none" stroke="#fff" stroke-width="6"
 stroke-linecap="round" stroke-linejoin="round"/>
<path d="M205 40c0-12 8-20 20-20M265 40c0-12-8-20-20-20" fill="none" stroke="#5b1f5e" stroke-width="5"
 stroke-linecap="round"/>
<path d="M205 40c-6 40 0 78 30 78s36-38 30-78" fill="none" stroke="#5b1f5e" stroke-width="5"
 stroke-linecap="round"/>
<path d="M235 118c0 24 20 38 44 30" fill="none" stroke="#5b1f5e" stroke-width="5" stroke-linecap="round"/>
<circle cx="283" cy="147" r="13" fill="#fff" stroke="#5b1f5e" stroke-width="5"/>
<circle cx="283" cy="147" r="5" fill="#e8458c"/>
<circle cx="205" cy="40" r="5" fill="#5b1f5e"/><circle cx="265" cy="40" r="5" fill="#5b1f5e"/>
</svg>
"""

STETH_SVG = """
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" width="100%">
<g fill="#f4a3c8" opacity=".8">
<ellipse cx="30" cy="120" rx="10" ry="24" transform="rotate(-25 30 120)"/>
<ellipse cx="42" cy="155" rx="9" ry="20" transform="rotate(-10 42 155)"/>
<ellipse cx="172" cy="130" rx="10" ry="24" transform="rotate(25 172 130)"/>
<ellipse cx="160" cy="165" rx="9" ry="20" transform="rotate(15 160 165)"/>
</g>
<path d="M60 20c-6 50 0 88 32 88s38-38 32-88" fill="none" stroke="#6b2d5c" stroke-width="6"
 stroke-linecap="round"/>
<circle cx="60" cy="18" r="6" fill="#6b2d5c"/><circle cx="124" cy="18" r="6" fill="#6b2d5c"/>
<path d="M92 108c0 40 24 55 52 50" fill="none" stroke="#6b2d5c" stroke-width="6" stroke-linecap="round"/>
<circle cx="150" cy="156" r="14" fill="#f9c6dd" stroke="#6b2d5c" stroke-width="6"/>
<circle cx="150" cy="156" r="5" fill="#6b2d5c"/>
</svg>
"""

BIG_HEART_SVG = """
<svg viewBox="0 0 80 70" width="64" height="56" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="bh" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#ffc2dc"/><stop offset="1" stop-color="#f58cbb"/></linearGradient></defs>
<path d="M40 66C12 46 3 32 3 20 3 10 11 3 21 3c8 0 15 5 19 12C44 8 51 3 59 3c10 0 18 7 18 17 0 12-9 26-37 46z" fill="url(#bh)"/>
<path d="M12 33h16l5-12 8 24 6-12h21" fill="none" stroke="#fff" stroke-width="3.5"
 stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""

DROP_BIG = svg_icon(ICONS["drop"], "#c2185b")
HEART_BIG = svg_icon(ICONS["heart"], "#c2185b")
USER_BIG = svg_icon(ICONS["user"], "#c2185b")
BULB = svg_icon("<path d='M9 18h6M10 21h4'/><path d='M12 3a6 6 0 00-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0012 3z'/>", "#b0508a")
BRAIN = svg_icon("<path d='M9 4a3 3 0 00-3 3 3 3 0 00-2 5 3 3 0 002 5 3 3 0 003 3V4z'/>"
                 "<path d='M15 4a3 3 0 013 3 3 3 0 012 5 3 3 0 01-2 5 3 3 0 01-3 3V4z'/>", "#c2185b")
WAVE = svg_icon("<path d='M7 11V6a1.5 1.5 0 013 0v4M10 10V4.5a1.5 1.5 0 013 0V10M13 10V5.5a1.5 1.5 0 013 0V12'/>"
                "<path d='M16 12V9.5a1.5 1.5 0 013 0V15a7 7 0 01-7 7h-1a6 6 0 01-5-3l-2-4a1.5 1.5 0 012.4-1.6L8 15'/>", "#e8458c")


# ------------------------------------------------------------------
# Field definitions: (label, placeholder, icon)
# ------------------------------------------------------------------
DIABETES_FIELDS = [
    ("Number of Pregnancies", "e.g. 3", "user"),
    ("Glucose Level", "e.g. 120", "drop"),
    ("Blood Pressure value", "e.g. 72", "heart"),
    ("Skin Thickness value", "e.g. 23", "layers"),
    ("Insulin Level", "e.g. 85", "syringe"),
    ("BMI value", "e.g. 28.5", "scale"),
    ("Diabetes Pedigree Function value", "e.g. 0.5", "nodes"),
    ("Age of the Person", "e.g. 33", "calendar"),
]

HEART_FIELDS = [
    ("Age", "e.g. 52", "calendar"),
    ("Sex", "1 = male, 0 = female", "user"),
    ("Chest Pain types", "e.g. 0", "heart"),
    ("Resting Blood Pressure", "e.g. 125", "heart"),
    ("Serum Cholestoral in mg/dl", "e.g. 212", "drop"),
    ("Fasting Blood Sugar > 120 mg/dl", "1 = yes, 0 = no", "drop"),
    ("Resting Electrocardiographic results", "e.g. 1", "pulse"),
    ("Maximum Heart Rate achieved", "e.g. 168", "pulse"),
    ("Exercise Induced Angina", "1 = yes, 0 = no", "heart"),
    ("ST depression induced by exercise", "e.g. 1.0", "pulse"),
    ("Slope of the peak exercise ST segment", "e.g. 2", "pulse"),
    ("Major vessels colored by flourosopy", "e.g. 2", "layers"),
    ("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect", "e.g. 3", "nodes"),
]

PARKINSONS_FIELDS = [
    ("MDVP:Fo(Hz)", "e.g. 119.99", "pulse"),
    ("MDVP:Fhi(Hz)", "e.g. 157.30", "pulse"),
    ("MDVP:Flo(Hz)", "e.g. 74.99", "pulse"),
    ("MDVP:Jitter(%)", "e.g. 0.00784", "pulse"),
    ("MDVP:Jitter(Abs)", "e.g. 0.00007", "pulse"),
    ("MDVP:RAP", "e.g. 0.0037", "pulse"),
    ("MDVP:PPQ", "e.g. 0.00554", "pulse"),
    ("Jitter:DDP", "e.g. 0.01109", "pulse"),
    ("MDVP:Shimmer", "e.g. 0.04374", "pulse"),
    ("MDVP:Shimmer(dB)", "e.g. 0.426", "pulse"),
    ("Shimmer:APQ3", "e.g. 0.02182", "pulse"),
    ("Shimmer:APQ5", "e.g. 0.0313", "pulse"),
    ("MDVP:APQ", "e.g. 0.02971", "pulse"),
    ("Shimmer:DDA", "e.g. 0.06545", "pulse"),
    ("NHR", "e.g. 0.02211", "pulse"),
    ("HNR", "e.g. 21.033", "pulse"),
    ("RPDE", "e.g. 0.414783", "pulse"),
    ("DFA", "e.g. 0.815285", "pulse"),
    ("spread1", "e.g. -4.813031", "pulse"),
    ("spread2", "e.g. 0.266482", "pulse"),
    ("D2", "e.g. 2.301442", "pulse"),
    ("PPE", "e.g. 0.284654", "pulse"),
]


# ------------------------------------------------------------------
# CSS
# ------------------------------------------------------------------
def build_css() -> str:
    all_fields = DIABETES_FIELDS + HEART_FIELDS + PARKINSONS_FIELDS
    icon_rules = ""
    for label, _, icon in all_fields:
        safe = label.replace('"', '\\"')
        icon_rules += (f'[data-testid="stTextInput"] input[aria-label="{safe}"]'
                       f'{{background-image:url("{icon_uri(icon)}");}}\n')

    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Caveat:wght@500;600&display=swap');

:root {{
  --plum: #4a0e4e;
  --plum-soft: #6b2d5c;
  --pink: #d6609a;
  --pink-light: #fde4f0;
  --border: #f1c9dd;
}}

html, body, [class*="css"], .stApp {{
  font-family: 'Plus Jakarta Sans', sans-serif;
}}

/* ---------- App background ---------- */
.stApp {{
  background: linear-gradient(180deg, #fff9fc 0%, #fdeef6 100%);
}}
[data-testid="stHeader"] {{ background: transparent; }}
[data-testid="stToolbar"], #MainMenu, footer {{ display: none !important; }}
.block-container {{
  padding-top: 1rem !important;
  padding-bottom: 2rem !important;
  max-width: 1250px;
}}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {{
  background: linear-gradient(180deg, #fde9f3 0%, #fbd3e6 100%);
  border-right: 1px solid #f6d3e4;
}}
section[data-testid="stSidebar"] > div {{ background: transparent; }}
section[data-testid="stSidebar"] .block-container {{ padding-top: 1rem !important; }}

.brand {{ display:flex; align-items:center; gap:.8rem; margin:.2rem 0 1.6rem .2rem; }}
.brand .name {{ font-size:1.55rem; font-weight:800; color:var(--plum); line-height:1.1; }}
.brand .tag  {{ font-size:.68rem; color:#7a5a74; margin-top:.2rem; }}

.sys-title {{
  display:flex; align-items:center; gap:.7rem;
  background: linear-gradient(135deg, #6b2d5c, #5a2150);
  color:#fff; font-weight:700; font-size:1.02rem; line-height:1.25;
  padding:.95rem 1rem; border-radius:14px; margin-bottom:.6rem;
  box-shadow: 0 6px 16px rgba(107,45,92,.28);
}}
.sys-title .ic {{
  width:38px; height:38px; border-radius:10px; background:rgba(255,255,255,.14);
  display:flex; align-items:center; justify-content:center; font-size:1.3rem;
}}

.side-quote {{ margin-top:3.5rem; padding:0 .6rem; }}
.side-quote .q {{
  font-family:'Caveat', cursive; font-size:1.7rem; color:#c2185b; line-height:1.05;
}}
.side-quote .art {{ width:70%; margin-top:.4rem; }}

/* ---------- Top bar + hero ---------- */
.topbar {{ display:flex; justify-content:flex-end; margin-bottom:.2rem; }}
.chip {{
  display:flex; align-items:center; gap:.6rem; background:#fff; border:1px solid var(--border);
  border-radius:999px; padding:.35rem .9rem .35rem .4rem; font-size:.85rem; color:var(--plum);
  font-weight:600; box-shadow:0 2px 8px rgba(214,96,154,.12);
}}
.chip .av {{
  width:32px; height:32px; border-radius:50%; background:var(--pink-light);
  display:flex; align-items:center; justify-content:center;
}}
.chip .av svg {{ width:18px; height:18px; }}

.hero {{
  display:grid; grid-template-columns: 1.35fr .95fr .9fr; gap:1rem; align-items:center;
  margin-bottom:1.1rem;
}}
.hero h1 {{
  font-size:2.35rem; font-weight:800; color:var(--plum); line-height:1.12; margin:0; padding:0;
}}
.hero h1 svg {{ width:34px; height:34px; vertical-align:middle; margin-left:.4rem; }}
.hero p {{ color:#6b4a66; font-size:.98rem; margin:.7rem 0 0 0; line-height:1.55; }}
.pill {{
  display:flex; align-items:center; gap:.8rem; background:rgba(255,255,255,.7);
  border:1px solid var(--border); border-radius:16px; padding:.8rem 1rem;
}}
.pill svg {{ width:36px; height:36px; flex:none; }}
.pill b {{ display:block; color:var(--plum); font-size:.88rem; }}
.pill span {{ color:#8a6a84; font-size:.74rem; }}

/* ---------- The card (st.form) ---------- */
[data-testid="stForm"] {{
  background:#fff; border:1px solid #f6dce9; border-radius:22px; padding:1.6rem 1.8rem 1.8rem;
  box-shadow:0 10px 30px rgba(214,96,154,.12);
}}
.card-head {{
  display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding-bottom:1.1rem; margin-bottom:.9rem; border-bottom:1px solid #f8e6ef;
}}
.card-head .l {{ display:flex; align-items:center; gap:1rem; }}
.card-head .badge {{
  width:60px; height:60px; border-radius:50%; background:#fde0ee;
  display:flex; align-items:center; justify-content:center; flex:none;
}}
.card-head .badge svg {{ width:30px; height:30px; }}
.card-head h2 {{ margin:0; padding:0; font-size:1.7rem; font-weight:800; color:var(--plum); }}
.card-head p {{ margin:.25rem 0 0 0; color:#7a5a74; font-size:.95rem; }}
.tip {{
  display:flex; gap:.7rem; align-items:flex-start; background:#fff8fb; border:1px solid var(--border);
  border-radius:14px; padding:.8rem 1rem; color:var(--plum); font-size:.85rem; min-width:230px;
}}
.tip svg {{ width:22px; height:22px; flex:none; }}
.tip i {{ display:block; font-family:'Caveat',cursive; font-style:normal; color:#c2185b;
  font-size:1.1rem; text-align:right; }}

/* ---------- Inputs ---------- */
[data-testid="stTextInput"] label p {{
  font-size:.9rem; font-weight:500; color:var(--plum);
}}
[data-testid="stTextInput"] div[data-baseweb="input"] {{
  background:#fffafd; border:1px solid var(--border); border-radius:12px; overflow:hidden;
}}
[data-testid="stTextInput"] div[data-baseweb="input"] > div {{ background:transparent; }}
[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {{
  border-color:var(--pink); box-shadow:0 0 0 3px rgba(214,96,154,.18);
}}
[data-testid="stTextInput"] input {{
  color:var(--plum); height:2.35rem; padding-left:2.7rem !important;
  background-repeat:no-repeat; background-position:.85rem center; background-size:20px 20px;
  background-image:url("{icon_uri('pulse')}");
}}
[data-testid="stTextInput"] input::placeholder {{ color:#c4a7bc; opacity:1; }}
{icon_rules}

/* ---------- Gradient button ---------- */
[data-testid="stForm"] button {{
  width:100%; border:none; border-radius:12px; padding:.8rem 1rem; font-weight:700;
  font-size:1rem; color:#fff; background:linear-gradient(90deg, #c9559a, #ef7fb0);
  box-shadow:0 8px 18px rgba(201,85,154,.35); transition:transform .15s, box-shadow .15s;
}}
[data-testid="stForm"] button p {{ color:#fff; font-weight:700; }}
[data-testid="stForm"] button:hover {{
  transform:translateY(-1px); box-shadow:0 12px 22px rgba(201,85,154,.45); color:#fff;
  background:linear-gradient(90deg, #bb4a8e, #ea6fa6);
}}
[data-testid="stForm"] button:focus {{ color:#fff; }}

/* ---------- Result box ---------- */
.res {{
  display:flex; align-items:center; gap:1.4rem; border-radius:16px; padding:1.1rem 1.6rem;
  margin-top:.9rem; border:1px dashed #f2cfe0; background:linear-gradient(90deg,#fff6fa,#fdeaf3);
}}
.res .t {{ flex:1; text-align:center; }}
.res .t b {{ display:block; font-size:1.05rem; color:var(--plum); }}
.res .t span {{ color:#8a6a84; font-size:.88rem; }}
.res.ok   {{ border:1px solid #bfe6cf; background:linear-gradient(90deg,#f3fbf6,#e5f6ec); }}
.res.ok .t b {{ color:#1e6b43; }}
.res.risk {{ border:1px solid #f5b5c8; background:linear-gradient(90deg,#fff3f6,#ffe3ec); }}
.res.risk .t b {{ color:#a3123f; }}
.disclaimer {{ text-align:center; color:#a58aa0; font-size:.75rem; margin-top:.6rem; }}

@media (max-width: 900px) {{
  .hero {{ grid-template-columns: 1fr; }}
  .card-head {{ flex-direction:column; align-items:flex-start; }}
}}
</style>
"""


st.markdown(build_css(), unsafe_allow_html=True)


# ------------------------------------------------------------------
# UI building blocks
# ------------------------------------------------------------------
def render_hero():
    st.markdown(html(f"""
    <div class="topbar"><div class="chip"><span class="av">{USER_BIG}</span>Health Assistant &#8964;</div></div>
    <div class="hero">
      <div>
        <h1>Hello! {WAVE}<br>Let's predict your health risk</h1>
        <p>Choose a disease from the sidebar and enter the required details.<br>
        Our ML model will help you get an early prediction.</p>
      </div>
      <div class="pill">{BRAIN}<div><b>Powered by Machine Learning</b>
        <span>Fast &nbsp;•&nbsp; Reliable &nbsp;•&nbsp; Easy to Use</span></div></div>
      <div>{HERO_SVG}</div>
    </div>
    """), unsafe_allow_html=True)


def card_header(title: str, subtitle: str, icon_svg: str):
    st.markdown(html(f"""
    <div class="card-head">
      <div class="l"><div class="badge">{icon_svg}</div>
        <div><h2>{title}</h2><p>{subtitle}</p></div></div>
      <div class="tip">{BULB}<div>Early detection can make a big difference.<i>Take care ♡</i></div></div>
    </div>
    """), unsafe_allow_html=True)


def result_box(kind: str, title: str, subtitle: str) -> str:
    return html(f"""
    <div class="res {kind}">{BIG_HEART_SVG}
      <div class="t"><b>{title}</b><span>{subtitle}</span></div></div>
    <div class="disclaimer">This tool is for educational purposes only and is not a medical diagnosis.</div>
    """)


IDLE_BOX = result_box("", "Your prediction result will appear here",
                      "Fill in the details above and click the button to get your result.")


def render_form(key, title, subtitle, icon_svg, fields, n_cols, button_label,
                model, pos_text, neg_text):
    """Draws one prediction page and runs the model on submit."""
    with st.form(key):
        card_header(title, subtitle, icon_svg)

        cols = st.columns(n_cols)
        values = []
        for i, (label, placeholder, _) in enumerate(fields):
            with cols[i % n_cols]:
                values.append(st.text_input(label, placeholder=placeholder, key=f"{key}_{i}"))

        submitted = st.form_submit_button(f"✦   {button_label}   →", use_container_width=True)
        slot = st.empty()
        slot.markdown(IDLE_BOX, unsafe_allow_html=True)

        if submitted:
            try:
                user_input = [float(v) for v in values]
            except ValueError:
                slot.markdown(result_box("risk", "Please check your inputs",
                                         "Every field is required and must be a number."),
                              unsafe_allow_html=True)
                return

            prediction = model.predict([user_input])
            if prediction[0] == 1:
                slot.markdown(result_box("risk", pos_text, "Please consult a doctor for a proper check-up."),
                              unsafe_allow_html=True)
            else:
                slot.markdown(result_box("ok", neg_text, "Keep up the healthy habits!"),
                              unsafe_allow_html=True)


# ------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown(html(f"""
    <div class="brand">{LOGO_SVG}<div><div class="name">Health Assistant</div>
    <div class="tag">Better Data &nbsp;•&nbsp; Healthier Tomorrows</div></div></div>
    <div class="sys-title"><div class="ic">🏥</div><div>Multiple Disease<br>Prediction System</div></div>
    """), unsafe_allow_html=True)

    selected = option_menu(
        None,
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['droplet', 'heart', 'person'],
        default_index=0,
        styles={
            "container": {"padding": "0", "background-color": "transparent"},
            "icon": {"color": "#4a0e4e", "font-size": "18px"},
            "nav-link": {"font-size": "15px", "font-weight": "500", "color": "#4a0e4e",
                         "border-radius": "12px", "margin": "4px 0", "padding": "12px 14px",
                         "--hover-color": "#fbd3e6"},
            "nav-link-selected": {"background": "linear-gradient(90deg,#fbc3de,#fdd9ea)",
                                  "color": "#4a0e4e", "font-weight": "700"},
        },
    )

    st.markdown(html(f"""
    <div class="side-quote"><div class="q">Small steps<br>towards a<br>healthier you ♡</div>
    <div class="art">{STETH_SVG}</div></div>
    """), unsafe_allow_html=True)


# ------------------------------------------------------------------
# Pages
# ------------------------------------------------------------------
render_hero()

if selected == 'Diabetes Prediction':
    render_form("diabetes", "Diabetes Prediction using ML",
                "Enter the following details about the person to check the diabetes risk.",
                DROP_BIG, DIABETES_FIELDS, 3, "Diabetes Test Result",
                diabetes_model, "The person is diabetic", "The person is not diabetic")

if selected == 'Heart Disease Prediction':
    render_form("heart", "Heart Disease Prediction using ML",
                "Enter the following details about the person to check the heart disease risk.",
                HEART_BIG, HEART_FIELDS, 3, "Heart Disease Test Result",
                heart_disease_model, "The person is having heart disease",
                "The person does not have any heart disease")

if selected == 'Parkinsons Prediction':
    render_form("parkinsons", "Parkinson's Disease Prediction using ML",
                "Enter the following voice measurements to check the Parkinson's risk.",
                USER_BIG, PARKINSONS_FIELDS, 4, "Parkinson's Test Result",
                parkinsons_model, "The person has Parkinson's disease",
                "The person does not have Parkinson's disease")