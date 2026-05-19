"""
BUI QABUL SIMULYATORI — Ma'lumot Kiritish Veb-Forması
=====================================================
Ishga tushirish: streamlit run app.py
Brauzerda: http://localhost:8501
"""

import streamlit as st
import json
import os
import base64
import requests
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "bui_data.json")

# GitHub config — Secrets orqali yoki to'g'ridan-to'g'ri
GITHUB_REPO = "plux96/bui-admission-simulator"
GITHUB_FILE = "bui_data.json"

def get_github_token():
    """GitHub token olish (Streamlit secrets yoki env)."""
    try:
        return st.secrets["GITHUB_TOKEN"]
    except Exception:
        return os.environ.get("GITHUB_TOKEN", "")

# ─── Yordamchi funksiyalar ───
def load_from_github():
    """GitHub repo'dan bui_data.json ni o'qish."""
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE}"
        token = get_github_token()
        headers = {"Accept": "application/vnd.github.v3+json"}
        if token:
            headers["Authorization"] = f"token {token}"
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            content = base64.b64decode(resp.json()["content"]).decode("utf-8")
            return json.loads(content), resp.json().get("sha", "")
        return {}, ""
    except Exception:
        return {}, ""

def save_to_github(data):
    """GitHub repo'ga bui_data.json ni saqlash."""
    token = get_github_token()
    if not token:
        return False, "GitHub token topilmadi. Secrets'ga GITHUB_TOKEN qo'shing."
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE}"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        # Avval SHA olish
        resp = requests.get(url, headers=headers, timeout=10)
        sha = resp.json().get("sha", "") if resp.status_code == 200 else ""

        content = base64.b64encode(
            json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        ).decode("utf-8")

        payload = {
            "message": f"Data updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "content": content,
        }
        if sha:
            payload["sha"] = sha

        resp = requests.put(url, headers=headers, json=payload, timeout=15)
        if resp.status_code in (200, 201):
            return True, "GitHub'ga saqlandi!"
        return False, f"Xatolik: {resp.status_code}"
    except Exception as e:
        return False, str(e)

def load_data():
    """Avval lokal, keyin GitHub'dan yuklash."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            local_data = json.load(f)
            if local_data:
                return local_data
    # Lokal bo'sh — GitHub'dan olish
    gh_data, _ = load_from_github()
    if gh_data:
        # Lokal cache'ga ham yozib qo'y
        save_data_local(gh_data)
        return gh_data
    return {}

def save_data_local(data):
    """Lokal faylga saqlash."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_data(data):
    """Lokal + GitHub'ga saqlash."""
    save_data_local(data)

def get_val(key, default=None):
    keys = key.split(".")
    d = st.session_state.get("data", {})
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, default)
        else:
            return default
    return d if d is not None else default

def set_val(key, value):
    keys = key.split(".")
    d = st.session_state["data"]
    for k in keys[:-1]:
        if k not in d:
            d[k] = {}
        d = d[k]
    d[keys[-1]] = value

def num(label, key, help_text="", min_val=0, max_val=None, step=1, is_float=False):
    """Raqam kiritish maydoni."""
    default = get_val(key, 0.0 if is_float else 0)
    if is_float:
        val = st.number_input(label, value=float(default), min_value=0.0,
                              step=0.1, help=help_text, key=f"w_{key}")
    else:
        kw = {"label": label, "value": int(default), "min_value": min_val,
              "step": step, "help": help_text, "key": f"w_{key}"}
        if max_val is not None:
            kw["max_value"] = max_val
        val = st.number_input(**kw)
    set_val(key, val)
    return val

def txt(label, key, help_text=""):
    """Matn kiritish maydoni."""
    default = get_val(key, "")
    val = st.text_input(label, value=str(default), help=help_text, key=f"w_{key}")
    set_val(key, val)
    return val

def txtarea(label, key, help_text=""):
    """Ko'p qatorli matn."""
    default = get_val(key, "")
    val = st.text_area(label, value=str(default), help=help_text, key=f"w_{key}")
    set_val(key, val)
    return val

def yn(label, key, help_text=""):
    """Ha/Yo'q."""
    default = get_val(key, False)
    val = st.checkbox(label, value=bool(default), help=help_text, key=f"w_{key}")
    set_val(key, val)
    return val

def slider(label, key, min_v=0, max_v=10, help_text=""):
    """Slider 0-10."""
    default = get_val(key, 0)
    val = st.slider(label, min_v, max_v, int(default), help=help_text, key=f"w_{key}")
    set_val(key, val)
    return val

def tags(label, key, help_text=""):
    """Vergul bilan ajratilgan ro'yxat."""
    default = get_val(key, [])
    if isinstance(default, list):
        default = ", ".join(str(x) for x in default)
    val = st.text_input(label, value=str(default), help=help_text + " (vergul bilan ajrating)", key=f"w_{key}")
    result = [x.strip() for x in val.split(",") if x.strip()] if val else []
    set_val(key, result)
    return result

def pct(label, key, help_text=""):
    """Foiz kiritish 0-100."""
    default = get_val(key, 0)
    val = st.number_input(label, value=int(default), min_value=0, max_value=100,
                          step=1, help=help_text, key=f"w_{key}")
    set_val(key, val)
    return val

def money(label, key, help_text=""):
    """Pul summasi."""
    default = get_val(key, 0)
    val = st.number_input(label, value=int(default), min_value=0,
                          step=100000, help=help_text + " (so'mda)", key=f"w_{key}")
    set_val(key, val)
    return val


# ─── Sahifa sozlamalari ───
st.set_page_config(
    page_title="BUI Qabul Simulyatori",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ma'lumotlarni yuklash
if "data" not in st.session_state:
    st.session_state["data"] = load_data()

# ─── Sidebar ───
with st.sidebar:
    st.title("BUI Simulyator")
    st.markdown("---")

    # Progress
    data = st.session_state["data"]
    total_fields = 0
    filled_fields = 0
    def count_filled(d):
        global total_fields, filled_fields
        if isinstance(d, dict):
            for v in d.values():
                count_filled(v)
        elif isinstance(d, list):
            total_fields += 1
            if len(d) > 0: filled_fields += 1
        elif isinstance(d, bool):
            total_fields += 1; filled_fields += 1
        elif isinstance(d, (int, float)):
            total_fields += 1
            if d != 0: filled_fields += 1
        elif isinstance(d, str):
            total_fields += 1
            if d.strip(): filled_fields += 1
    count_filled(data)
    pct_done = (filled_fields / max(total_fields, 1)) * 100

    st.metric("To'ldirilgan", f"{filled_fields}/{total_fields}")
    st.progress(pct_done / 100)
    st.caption(f"{pct_done:.0f}% tayyor")

    st.markdown("---")

    # SAQLASH — lokal + GitHub
    if st.button("SAQLASH", type="primary", use_container_width=True):
        save_data(st.session_state["data"])
        ok, msg = save_to_github(st.session_state["data"])
        if ok:
            st.success("Saqlandi! (lokal + GitHub)")
        else:
            st.warning(f"Lokal saqlandi. GitHub: {msg}")

    # JSON YUKLAB OLISH
    st.download_button(
        "JSON yuklab olish",
        data=json.dumps(st.session_state["data"], ensure_ascii=False, indent=2),
        file_name="bui_data.json",
        mime="application/json",
        use_container_width=True,
    )

    # JSON YUKLASH (import)
    uploaded = st.file_uploader("JSON yuklash (import)", type=["json"], key="json_upload")
    if uploaded is not None:
        try:
            imported = json.load(uploaded)
            st.session_state["data"] = imported
            save_data(imported)
            st.success(f"Yuklandi! {len(str(imported))} bayt")
            st.rerun()
        except Exception as e:
            st.error(f"Xato: {e}")

    # GitHub'dan yangilash
    if st.button("GitHub'dan yuklash", use_container_width=True):
        gh_data, _ = load_from_github()
        if gh_data:
            st.session_state["data"] = gh_data
            save_data_local(gh_data)
            st.success("GitHub'dan yuklandi!")
            st.rerun()
        else:
            st.warning("GitHub'da ma'lumot topilmadi.")

    st.markdown("---")
    section = st.radio("Bo'limni tanlang:", [
        "1. Universitet profili",
        "2. Ta'lim yo'nalishlari",
        "3. Narxlash",
        "4. Marketing",
        "5. Abituriyent profili",
        "6. Raqobatchilar",
        "7. Infratuzilma",
        "8. Xalqaro hamkorlik",
        "9. Qabul jarayoni",
        "10. Moliya",
        "11. Hududiy bozor",
        "12. Mavsumiylik",
        "13. Texnologiya",
        "14. Tashqi omillar",
        "15. Kadrlar",
        "16. Alumni",
        "17. Talaba hayoti",
        "18. Brend",
        "19. Hamkorliklar",
        "20. Qonunchilik",
        "21. Qabul funnel",
        "22. Raqamli aktivlar",
        "23. Ijtimoiy ta'sir",
        "24. Kelajak rejalari",
        "25. Simulyatsiya maqsadlari",
    ])

sec_num = int(section.split(".")[0])

# ═══════════════════════════════════════════════════════════════
# BO'LIMLAR
# ═══════════════════════════════════════════════════════════════

if sec_num == 1:
    st.header("🏫 Universitet Profili")

    st.subheader("Asosiy ma'lumotlar")
    c1, c2 = st.columns(2)
    with c1:
        txt("Universitet nomi", "uni.nomi")
        txt("Qisqa nomi", "uni.qisqa_nomi")
        num("Tashkil etilgan yil", "uni.tashkil_yil")
        txt("Litsenziya turi", "uni.litsenziya_turi", "Davlat / Nodavlat")
        txt("Litsenziya raqami", "uni.litsenziya_raqami")
        txt("Rektor F.I.O.", "uni.rektor")
    with c2:
        txt("Rektor ilmiy darajasi", "uni.rektor_daraja")
        num("Prorektor soni", "uni.prorektor_soni")
        yn("Akkreditatsiya bor", "uni.akkreditatsiya")
        txt("Akkreditatsiya darajasi", "uni.akkreditatsiya_daraja")
        txt("Akkreditatsiya organi", "uni.akkreditatsiya_organ")
        txt("Akkreditatsiya muddati", "uni.akkreditatsiya_muddat", "2030-01-01")

    st.subheader("Joylashuv")
    c1, c2, c3 = st.columns(3)
    with c1:
        txt("Shahar", "uni.shahar")
        txt("Viloyat", "uni.viloyat")
        txt("To'liq manzil", "uni.manzil")
    with c2:
        txt("Pochta indeksi", "uni.pochta")
        num("Shahar markazidan (km)", "uni.markaz_km")
        num("Aeroportdan (km)", "uni.aeroport_km")
    with c3:
        num("Temir yo'ldan (km)", "uni.temir_yol_km")
        num("Avtovokzaldan (km)", "uni.avtovokzal_km")

    st.subheader("Veb va aloqa")
    c1, c2, c3 = st.columns(3)
    with c1:
        txt("Veb-sayt", "uni.sayt")
        txt("Qabul sayti", "uni.qabul_sayt")
        txt("Email", "uni.email")
    with c2:
        txt("Telefon (asosiy)", "uni.telefon")
        txt("Telefon (qabul)", "uni.telefon_qabul")
        txt("Telegram kanal", "uni.telegram")
    with c3:
        txt("Instagram", "uni.instagram")
        txt("YouTube", "uni.youtube")
        txt("TikTok", "uni.tiktok")

    st.subheader("Reyting va nufuz (1-10 shkala)")
    c1, c2 = st.columns(2)
    with c1:
        slider("Mahalliy reyting", "uni.reyting_mahalliy")
        slider("Xalqaro reyting", "uni.reyting_xalqaro")
        slider("Ish beruvchi ishonchi", "uni.ish_beruvchi_ishonch")
        slider("Talabalar qoniqishi", "uni.talaba_qoniqish")
    with c2:
        slider("Ota-ona ishonchi", "uni.ota_ona_ishonch")
        slider("Media ko'rinishi", "uni.media_korinish")
        slider("Brend tanilganligi (Buxoro)", "uni.brend_buxoro")
        slider("Brend tanilganligi (O'zbekiston)", "uni.brend_uzb")

    num("Google reyting (1.0-5.0)", "uni.google_reyting", is_float=True)
    num("Google sharhlar soni", "uni.google_sharh")

    st.subheader("Umumiy raqamlar")
    c1, c2, c3 = st.columns(3)
    with c1:
        num("Joriy talabalar soni", "uni.talabalar")
        num("Bakalavr", "uni.bakalavr")
        num("Magistr", "uni.magistr")
        num("PhD", "uni.phd")
        num("Sirtqi", "uni.sirtqi")
    with c2:
        num("Xorijiy talabalar", "uni.xorijiy_talaba")
        num("Fakultetlar soni", "uni.fakultetlar")
        num("Kafedralar soni", "uni.kafedralar")
        num("Professor-o'qituvchilar", "uni.professorlar")
        num("Xalqaro professorlar", "uni.xalqaro_prof")
    with c3:
        pct("PhD li professor %", "uni.phd_foiz")
        num("DSc li professorlar", "uni.dsc_soni")
        num("Talaba:O'qituvchi nisbati", "uni.talaba_oqituvchi")
        num("Jami bitiruvchilar", "uni.bitiruvchilar")


elif sec_num == 2:
    st.header("📚 Ta'lim Yo'nalishlari")
    st.info("Har bir yo'nalishni alohida qo'shing. Kamida 5-10 ta kerak.")

    # Nechta yo'nalish bor
    yon_count = get_val("yon_count", 1)
    yon_count = st.number_input("Yo'nalishlar soni", value=int(yon_count),
                                min_value=1, max_value=50, key="w_yon_count")
    set_val("yon_count", yon_count)

    for i in range(int(yon_count)):
        prefix = f"yon.{i}"
        yon_nomi = get_val(f"{prefix}.nomi", "Yangi yonalish")
        with st.expander(f"Yonalish #{i+1}: {yon_nomi}", expanded=(i==0)):
            c1, c2, c3 = st.columns(3)
            with c1:
                txt("Nomi", f"{prefix}.nomi")
                txt("Inglizcha nomi", f"{prefix}.nomi_en")
                txt("Fakultet", f"{prefix}.fakultet")
                txt("Kafedra", f"{prefix}.kafedra")
                txt("Ta'lim turi", f"{prefix}.talim_turi", "Bakalavr / Magistratura / PhD")
            with c2:
                txt("Ta'lim tili", f"{prefix}.talim_tili", "O'zbek / Rus / Ingliz")
                txt("Ta'lim shakli", f"{prefix}.talim_shakli", "Kunduzgi / Sirtqi / Kechki")
                num("Ta'lim muddati (yil)", f"{prefix}.muddat")
                num("Kreditlar soni", f"{prefix}.kreditlar")
                num("Amaliyot (oy)", f"{prefix}.amaliyot_oy")
            with c3:
                yn("Davlat granti bor", f"{prefix}.grant_bor")
                num("Grant kvota", f"{prefix}.grant_kvota")
                num("Kontrakt kvota", f"{prefix}.kontrakt_kvota")
                num("Jami kvota", f"{prefix}.jami_kvota")
                num("Minimal ball (DTM)", f"{prefix}.min_ball")

            st.markdown("**O'tgan yil statistikasi:**")
            c1, c2, c3 = st.columns(3)
            with c1:
                num("Ariza soni (2025)", f"{prefix}.ariza_2025")
                num("Qabul qilingan", f"{prefix}.qabul_2025")
                num("Hujjat topshirgan", f"{prefix}.kelgan_2025")
            with c2:
                num("To'lov boshlagan", f"{prefix}.tolov_2025")
                num("1-semestr ketgan", f"{prefix}.ketgan_2025")
                num("O'rtacha qabul bali", f"{prefix}.ortacha_ball")
            with c3:
                money("Kontrakt narxi (yillik)", f"{prefix}.narx")
                money("O'tgan yilgi narx", f"{prefix}.narx_2025")
                money("Sirtqi narxi", f"{prefix}.sirtqi_narx")

            st.markdown("**Ish bilan bandlik:**")
            c1, c2 = st.columns(2)
            with c1:
                pct("Ish bilan bandlik %", f"{prefix}.ish_bandlik")
                money("O'rtacha maosh (1-yil)", f"{prefix}.maosh_1yil")
                money("O'rtacha maosh (3-yil)", f"{prefix}.maosh_3yil")
            with c2:
                num("Ish beruvchi hamkorlar", f"{prefix}.ish_beruvchi_soni")
                tags("Top ish beruvchilar", f"{prefix}.top_ish_beruvchi")
                yn("Stajировка imkoniyati", f"{prefix}.staj_bor")

            tags("Kuchli tomonlari", f"{prefix}.kuchli")
            tags("Zaif tomonlari", f"{prefix}.zaif")
            txt("USP (noyob afzallik)", f"{prefix}.usp")
            slider("Mashhurlik darajasi", f"{prefix}.mashhurlik")


elif sec_num == 3:
    st.header("💰 Narxlash Strategiyasi")

    st.subheader("Joriy narx diapazoni")
    c1, c2, c3 = st.columns(3)
    with c1:
        money("Eng arzon kontrakt", "narx.eng_arzon")
        money("Eng qimmat kontrakt", "narx.eng_qimmat")
        money("O'rtacha kontrakt", "narx.ortacha")
    with c2:
        money("2023 narxi", "narx.narx_2023")
        money("2024 narxi", "narx.narx_2024")
        money("2025 narxi", "narx.narx_2025")
    with c3:
        money("2026 rejali narx", "narx.narx_2026")
        pct("Yillik o'sish %", "narx.yillik_osish")

    st.subheader("Chegirmalar")
    c1, c2 = st.columns(2)
    with c1:
        pct("Early bird chegirma %", "narx.early_bird")
        txt("Early bird deadline", "narx.early_bird_deadline", "2026-06-01")
        num("Early bird foydalanganlar (2025)", "narx.early_bird_2025")
        pct("Bir yillik to'lash chegirma %", "narx.bir_yillik")
        pct("Aka-uka chegirma %", "narx.aka_uka")
        pct("Oltin medal chegirma %", "narx.oltin_medal")
        pct("Kumush medal chegirma %", "narx.kumush_medal")
    with c2:
        pct("Sport chegirma %", "narx.sport")
        pct("Ijtimoiy chegirma %", "narx.ijtimoiy")
        pct("Hamkor maktab chegirma %", "narx.hamkor_maktab")
        pct("Xodim farzandi chegirma %", "narx.xodim_farzand")
        pct("Talaba tavsiya (referral) %", "narx.referral")
        pct("Olimpiada (oltin) chegirma %", "narx.olimp_gold")
        pct("Guruh chegirma (3+ kishi) %", "narx.guruh")

    st.subheader("Stipendiyalar")
    c1, c2 = st.columns(2)
    with c1:
        num("To'liq grant soni", "narx.toliq_grant")
        num("Yarim grant soni", "narx.yarim_grant")
        num("Chorak grant soni", "narx.chorak_grant")
    with c2:
        num("Rektorat stipendiya soni", "narx.rektorat_stip")
        money("Rektorat stipendiya (oylik)", "narx.rektorat_summa")
        money("Stipendiya jami byudjet", "narx.stip_byudjet")

    st.subheader("To'lov shartlari")
    c1, c2 = st.columns(2)
    with c1:
        yn("Bo'lib to'lash", "narx.bolib_tolash")
        num("Bo'lib to'lash (necha oy)", "narx.bolib_oy")
        pct("Bo'lib to'lash ustama %", "narx.bolib_ustama")
        yn("Click.uz", "narx.click")
        yn("Payme", "narx.payme")
        yn("Uzum Bank", "narx.uzum")
    with c2:
        txt("Kredit hamkor bank", "narx.kredit_bank")
        pct("Kredit foiz stavka %", "narx.kredit_foiz")
        num("Kredit max muddat (oy)", "narx.kredit_muddat")
        pct("Kechikish jarima %", "narx.jarima")
        txt("Qaytarish siyosati", "narx.qaytarish")


elif sec_num == 4:
    st.header("📢 Marketing")

    st.subheader("Umumiy byudjet")
    c1, c2, c3 = st.columns(3)
    with c1:
        money("Jami byudjet (yillik)", "mkt.jami_byudjet")
        money("O'tgan yil byudjet", "mkt.otgan_byudjet")
    with c2:
        num("Marketing jamoa soni", "mkt.jamoa_soni")
        txt("Marketing rahbari", "mkt.rahbar")
    with c3:
        yn("Tashqi agentlik bor", "mkt.agentlik_bor")
        money("Agentlik byudjeti", "mkt.agentlik_byudjet")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📱 Digital", "📺 Traditional", "🎪 Tadbirlar", "🤝 Agentlar", "📝 Content"
    ])

    with tab1:
        for platform in ["Telegram", "Instagram", "Facebook", "YouTube", "TikTok", "Google Ads", "SEO", "SMS", "Email"]:
            key = platform.lower().replace(" ", "_")
            with st.expander(f"{platform}"):
                c1, c2, c3 = st.columns(3)
                with c1:
                    money("Byudjet", f"mkt.{key}.byudjet")
                    txt("Profil/Kanal nomi", f"mkt.{key}.nomi")
                with c2:
                    num("Obunchilar/Followers", f"mkt.{key}.followers")
                    num("O'rtacha reach", f"mkt.{key}.reach")
                with c3:
                    num("Konversiya % (arizagacha)", f"mkt.{key}.konversiya")
                    money("CPA (bir talaba narxi)", f"mkt.{key}.cpa")

    with tab2:
        for media in ["TV reklama", "Radio", "Gazeta/Jurnal", "Billboard", "Transport reklama", "Poligrafiya"]:
            key = media.lower().replace(" ", "_").replace("/", "_")
            with st.expander(f"{media}"):
                c1, c2 = st.columns(2)
                with c1:
                    money("Byudjet", f"mkt.{key}.byudjet")
                    tags("Kanallar/Joylar", f"mkt.{key}.kanallar")
                with c2:
                    num("Oyiga necha marta", f"mkt.{key}.oyiga")
                    num("Konversiya %", f"mkt.{key}.konversiya")

    with tab3:
        for event in ["Ochiq eshiklar kuni", "Maktablarga tashrif", "Festival", "Olimpiadalar", "Yarmarkalar"]:
            key = event.lower().replace(" ", "_")
            with st.expander(f"{event}"):
                c1, c2 = st.columns(2)
                with c1:
                    num("Yilda necha marta", f"mkt.{key}.yilda")
                    num("O'rtacha ishtirokchilar", f"mkt.{key}.ishtirokchi")
                with c2:
                    money("Xarajat (har biri)", f"mkt.{key}.xarajat")
                    num("Konversiya %", f"mkt.{key}.konversiya")

    with tab4:
        st.subheader("Agentlar (Referral) tizimi")
        c1, c2 = st.columns(2)
        with c1:
            num("Jami agentlar", "mkt.agent.jami")
            num("Faol agentlar", "mkt.agent.faol")
            pct("Komissiya %", "mkt.agent.komissiya_foiz")
            money("Komissiya (fixed)", "mkt.agent.komissiya_fixed")
        with c2:
            num("O'tgan yil keltirgan", "mkt.agent.otgan_yil")
            txt("Eng samarali turi", "mkt.agent.samarali_turi")
            yn("Agent CRM bor", "mkt.agent.crm")
            yn("Agent training bor", "mkt.agent.training")

        st.markdown("**Agent turlari bo'yicha taqsimot:**")
        c1, c2, c3 = st.columns(3)
        with c1:
            num("Maktab o'qituvchilari", "mkt.agent.turi.oqituvchi")
            num("Joriy talabalar", "mkt.agent.turi.talaba")
        with c2:
            num("Tashqi agentlar", "mkt.agent.turi.tashqi")
            num("Bitiruvchilar", "mkt.agent.turi.bitiruvchi")
        with c3:
            num("Ota-ona/tanish", "mkt.agent.turi.tanish")

    with tab5:
        c1, c2 = st.columns(2)
        with c1:
            num("Content jamoa soni", "mkt.content.jamoa")
            num("Oyiga video soni", "mkt.content.video")
            num("Oyiga post soni", "mkt.content.post")
        with c2:
            num("Success story soni", "mkt.content.success")
            yn("Virtual tur bor", "mkt.content.virtual_tur")
            yn("Podcast bor", "mkt.content.podcast")
        slider("NPS Score (-100 dan +100)", "mkt.nps", min_v=-100, max_v=100)


elif sec_num == 5:
    st.header("🎓 Abituriyent Profili")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Demografik", "Oila", "Qaror omillari", "Axborot manbalari", "O'tgan yil"
    ])

    with tab1:
        st.subheader("Hududiy taqsimot (% da, jami 100)")
        st.caption("Buxoro tumanlari:")
        cols = st.columns(4)
        tumans = ["Buxoro shahar", "Kogon", "Gijduvon", "Vobkent",
                  "Jondor", "Olot", "Peshku", "Qorakol",
                  "Romitan", "Shofirkon", "Buxoro tuman", "Qorovulbozor"]
        for i, t in enumerate(tumans):
            with cols[i % 4]:
                pct(t, f"abit.hudud.buxoro_{t.lower().replace(' ', '_')}")

        st.caption("Boshqa viloyatlar:")
        cols = st.columns(4)
        viloyatlar = ["Samarqand", "Navoiy", "Qashqadaryo", "Surxondaryo",
                      "Toshkent shahar", "Toshkent viloyat", "Xorazm", "Fargona",
                      "Andijon", "Namangan", "Jizzax", "Sirdaryo", "Qoraqalpogiston"]
        for i, v in enumerate(viloyatlar):
            with cols[i % 4]:
                pct(v, f"abit.hudud.{v.lower().replace(' ', '_')}")

        st.markdown("---")
        st.subheader("Jins taqsimot")
        c1, c2 = st.columns(2)
        with c1: pct("Erkak %", "abit.jins.erkak")
        with c2: pct("Ayol %", "abit.jins.ayol")

        st.subheader("Yosh taqsimot")
        cols = st.columns(4)
        for i, yosh in enumerate(["16", "17", "18", "19", "20", "21-23", "24-27", "28+"]):
            with cols[i % 4]:
                pct(f"{yosh} yosh %", f"abit.yosh.{yosh.replace('-','_').replace('+','_plus')}")

    with tab2:
        st.subheader("Oilaviy daromad (oylik)")
        for seg in ["Juda past (1.5M gacha)", "Past (1.5-3M)", "O'rtacha past (3-5M)",
                     "O'rtacha (5-8M)", "Yuqori o'rtacha (8-12M)", "Yuqori (12-20M)", "Boylar (20M+)"]:
            key = seg.split("(")[0].strip().lower().replace(" ", "_").replace("'", "")
            pct(f"{seg} %", f"abit.daromad.{key}")

        st.subheader("Ota-ona ta'limi")
        for item in ["Ikkalasi oliy", "Bittasi oliy", "O'rta maxsus", "Maktab"]:
            key = item.lower().replace(" ", "_").replace("'", "")
            pct(f"{item} %", f"abit.ota_talim.{key}")

        st.subheader("Ota-ona kasbi")
        for item in ["Davlat xizmatchisi", "Tadbirkor", "Ishchi", "Dehqon/Fermer",
                     "Pensioner", "Ishsiz", "Xorijda ishlaydi (migrant)"]:
            key = item.split("(")[0].strip().lower().replace(" ", "_").replace("/", "_")
            pct(f"{item} %", f"abit.ota_kasb.{key}")

    with tab3:
        st.subheader("Qaror omillari (1-10, qanchalik muhim)")
        omillar = [
            ("Kontrakt narxi", "narx"), ("Stipendiya/grant", "stipendiya"),
            ("Bo'lib to'lash", "bolib"), ("Yo'nalish sifati", "sifat"),
            ("Professor darajasi", "prof"), ("Kampus sharoiti", "kampus"),
            ("Yotoqxona", "yotoq"), ("Joylashuv/masofa", "masofa"),
            ("Ish bilan bandlik", "ish"), ("Xalqaro aloqalar", "xalqaro"),
            ("Brend nomi", "brend"), ("Do'stlar ta'siri", "dostlar"),
            ("Oila bosimi", "oila"), ("Ijtimoiy tarmoq", "social"),
            ("Chegirma/aksiya", "chegirma"), ("Agent tavsiyasi", "agent"),
            ("Maktab tavsiyasi", "maktab_tavs"),
            ("Harbiy xizmatdan qochish", "harbiy"),
            ("Zamonaviy bino", "bino"), ("Sport imkoniyatlari", "sport"),
        ]
        cols = st.columns(2)
        for i, (label, key) in enumerate(omillar):
            with cols[i % 2]:
                slider(label, f"abit.qaror.{key}")

    with tab4:
        st.subheader("Axborot manbalari (1-10)")
        manbalar = [
            "Telegram", "Instagram", "YouTube", "TikTok", "TV",
            "Radio", "Do'stlar", "Ota-ona", "Maktab o'qituvchisi",
            "Agent", "Google", "Billboard", "Ochiq eshiklar kuni",
            "WhatsApp guruh", "SMS", "Ta'lim portallari"
        ]
        cols = st.columns(3)
        for i, m in enumerate(manbalar):
            with cols[i % 3]:
                manba_key = m.lower().replace(" ", "_").replace("'", "")
                slider(m, f"abit.manba.{manba_key}")

    with tab5:
        st.subheader("O'tgan yilgi statistika (2025)")
        c1, c2 = st.columns(2)
        with c1:
            num("Jami ariza soni", "abit.2025.ariza")
            num("Qabul qilingan", "abit.2025.qabul")
            num("Hujjat topshirgan", "abit.2025.hujjat")
            num("To'lov qilgan", "abit.2025.tolov")
            num("Darsga kelgan", "abit.2025.kelgan")
        with c2:
            num("1-semestr ketgan", "abit.2025.ketgan")
            pct("Ariza→Qabul konversiya %", "abit.2025.konv_ariza")
            pct("Qabul→To'lov konversiya %", "abit.2025.konv_tolov")
            txt("Eng ko'p ariza oyi", "abit.2025.eng_kop_oy")
            pct("Buxorolik %", "abit.2025.buxorolik")

        st.subheader("Psixologik segmentlar")
        segmentlar = [
            ("Narx sezgir (eng arzon kerak)", "narx_sezgir"),
            ("Sifat izlovchi (eng yaxshi kerak)", "sifat_izlovchi"),
            ("Qulaylik izlovchi (uyga yaqin)", "qulaylik"),
            ("Status izlovchi (brend/nufuz)", "status"),
            ("Pragmatik (ish topish kerak)", "pragmatik"),
            ("Ota-ona boshqaruvchi", "ota_ona"),
            ("Guruh ergashuvchi (do'stlari bilan)", "guruh"),
            ("Tasodifiy (oxirgi daqiqada)", "tasodifiy"),
        ]
        for label, key in segmentlar:
            pct(label, f"abit.segment.{key}")


elif sec_num == 6:
    st.header("⚔️ Raqobatchilar")
    st.info("Kamida 5-8 ta raqobatchi kiriting.")

    raq_count = get_val("raq_count", 1)
    raq_count = st.number_input("Raqobatchilar soni", value=int(raq_count),
                                min_value=1, max_value=20, key="w_raq_count")
    set_val("raq_count", raq_count)

    for i in range(int(raq_count)):
        prefix = f"raq.{i}"
        raq_nomi = get_val(f"{prefix}.nomi", "Yangi raqobatchi")
        with st.expander(f"Raqobatchi #{i+1}: {raq_nomi}", expanded=(i==0)):
            c1, c2, c3 = st.columns(3)
            with c1:
                txt("Nomi", f"{prefix}.nomi")
                txt("Qisqa nomi", f"{prefix}.qisqa")
                txt("Turi", f"{prefix}.turi", "Davlat / Nodavlat / Filial")
                txt("Shahar", f"{prefix}.shahar")
                num("Tashkil etilgan yil", f"{prefix}.yil")
            with c2:
                num("Jami talabalar", f"{prefix}.talabalar")
                num("Yillik qabul", f"{prefix}.yillik_qabul")
                money("Eng arzon kontrakt", f"{prefix}.arzon")
                money("Eng qimmat kontrakt", f"{prefix}.qimmat")
                money("O'rtacha kontrakt", f"{prefix}.ortacha")
            with c3:
                num("Grant o'rinlar", f"{prefix}.grant")
                slider("Reyting (1-10)", f"{prefix}.reyting")
                slider("Marketing faolligi", f"{prefix}.mkt_faollik")
                slider("Kampus sifati", f"{prefix}.kampus")
                slider("BUI uchun xavf darajasi", f"{prefix}.xavf")

            c1, c2 = st.columns(2)
            with c1:
                num("Telegram obunchilar", f"{prefix}.telegram")
                num("Instagram followers", f"{prefix}.instagram")
                yn("TV reklama bor", f"{prefix}.tv_bor")
                yn("Agentlar bor", f"{prefix}.agent_bor")
            with c2:
                yn("Online qabul bor", f"{prefix}.online_bor")
                yn("Yotoqxona bor", f"{prefix}.yotoq_bor")
                yn("Ikki diplom bor", f"{prefix}.ikki_diplom")
                yn("Chegirma bor", f"{prefix}.chegirma_bor")

            tags("Kuchli tomonlari", f"{prefix}.kuchli")
            tags("Zaif tomonlari", f"{prefix}.zaif")
            tags("BUI bilan umumiy yo'nalishlar", f"{prefix}.umumiy_yon")
            txt("Narx strategiyasi", f"{prefix}.narx_strat", "arzon / premium / o'rtacha")


elif sec_num == 7:
    st.header("🏗️ Infratuzilma")

    tab1, tab2, tab3, tab4 = st.tabs(["Kampus", "Yotoqxona", "Sport/Madaniyat", "Xavfsizlik"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            num("Kampus maydoni (ga)", "infra.maydon")
            num("Binolar soni", "infra.binolar")
            num("Auditoriyalar", "infra.auditoriya")
            num("Smart auditoriyalar", "infra.smart_aud")
            num("Laboratoriyalar", "infra.lab")
            num("Kompyuter xonalar", "infra.komp_xona")
        with c2:
            num("Kompyuterlar soni", "infra.kompyuter")
            num("Internet tezligi (Mbps)", "infra.internet")
            yn("WiFi bor", "infra.wifi")
            pct("WiFi qoplami %", "infra.wifi_foiz")
            num("Kutubxona o'rinlari", "infra.kutubxona")
            num("Kitoblar soni", "infra.kitoblar")
        yn("Coworking space", "infra.coworking")
        yn("Oshxona bor", "infra.oshxona")
        money("O'rtacha tushlik narxi", "infra.tushlik")
        slider("Oshxona sifati", "infra.oshxona_sifat")

    with tab2:
        yn("Yotoqxona bor", "infra.yotoq_bor")
        c1, c2 = st.columns(2)
        with c1:
            num("O'rinlar soni", "infra.yotoq_orin")
            money("Narxi (oylik)", "infra.yotoq_narx")
            slider("Sifati", "infra.yotoq_sifat")
            num("Masofasi (km)", "infra.yotoq_masofa")
        with c2:
            num("Xonada necha kishi", "infra.yotoq_kishi")
            yn("WiFi bor", "infra.yotoq_wifi")
            yn("Kir yuvish", "infra.yotoq_kir")
            yn("Oshxona bor", "infra.yotoq_oshxona")

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            yn("Sport zal", "infra.sport_zal")
            yn("Stadion", "infra.stadion")
            yn("Suzish havzasi", "infra.suzish")
            yn("Futbol maydon", "infra.futbol")
        with c2:
            yn("Madaniyat markazi", "infra.madaniyat")
            num("Konferens-zal sig'imi", "infra.konferens")
            num("Talabalar klublari", "infra.klublar")
            tags("Klub nomlari", "infra.klub_nomlari")

    with tab4:
        c1, c2 = st.columns(2)
        with c1:
            yn("Kuzatuv kameralari", "infra.kamera")
            num("Kameralar soni", "infra.kamera_soni")
            yn("Qorovul", "infra.qorovul")
        with c2:
            yn("Kirish kartasi", "infra.kirish_karta")
            yn("Yong'in signalizatsiya", "infra.yongin")
            yn("Tibbiy punkt", "infra.tibbiy")


elif sec_num == 8:
    st.header("🌍 Xalqaro Hamkorlik")
    c1, c2 = st.columns(2)
    with c1:
        num("Xorijiy hamkor universitetlar", "xalq.hamkor_soni")
        num("Ikki diplom dasturlari", "xalq.ikki_diplom")
        yn("Almashinuv dasturi bor", "xalq.almashinuv")
        num("Yilda xorijga ketgan talaba", "xalq.ketgan")
        num("Yilda kelgan xorijiy talaba", "xalq.kelgan")
    with c2:
        num("Xorijiy professorlar", "xalq.xorijiy_prof")
        num("Ingliz tilida dasturlar", "xalq.ingliz_dastur")
        yn("Til tayyorlov kursi", "xalq.til_kurs")
        yn("Xorijiy amaliyot", "xalq.xorijiy_amaliyot")
        slider("Xalqaro brend ta'siri", "xalq.brend_tasiri")

    tags("Xalqaro grant dasturlari", "xalq.grantlar", "Erasmus+, KOICA, JICA")
    tags("Sertifikat markazlari", "xalq.sertifikatlar", "IELTS, TOEFL, Cisco")
    tags("Hamkor universitetlar", "xalq.hamkorlar")


elif sec_num == 9:
    st.header("📋 Qabul Jarayoni")
    st.subheader("Vaqt jadvali")
    c1, c2, c3 = st.columns(3)
    with c1:
        txt("Qabul boshlanishi", "qabul.boshlanish", "2026-03-01")
        txt("Qabul tugashi", "qabul.tugash", "2026-09-01")
        txt("Darslar boshlanishi", "qabul.darslar")
    with c2:
        txt("Early bird boshlanishi", "qabul.early_bosh")
        txt("Early bird tugashi", "qabul.early_tugash")
    with c3:
        txt("DTM imtihon sanasi", "qabul.dtm_sana")
        txt("Natijalar e'lon", "qabul.natija_sana")

    st.subheader("Bosqichlar")
    c1, c2 = st.columns(2)
    with c1:
        yn("Online ariza", "qabul.online")
        yn("DTM ball talab", "qabul.dtm_talab")
        yn("Ichki imtihon", "qabul.ichki_imtihon")
        yn("Suhbat bor", "qabul.suhbat")
    with c2:
        num("Ariza vaqti (daqiqa)", "qabul.ariza_vaqt")
        num("Javob vaqti (soat)", "qabul.javob_vaqt")
        num("Qabul xodimlari", "qabul.xodimlar")
        num("Hududiy vakilliklar", "qabul.vakilliklar")


elif sec_num == 10:
    st.header("💵 Moliya")
    st.subheader("Daromadlar (2025, so'mda)")
    c1, c2 = st.columns(2)
    with c1:
        money("Jami daromad", "moliya.jami_daromad")
        money("Kontrakt (bakalavr)", "moliya.kontrakt_bak")
        money("Kontrakt (magistr)", "moliya.kontrakt_mag")
        money("Kontrakt (sirtqi)", "moliya.kontrakt_sirtqi")
    with c2:
        money("Grant moliyalashtirish", "moliya.grant")
        money("Qo'shimcha kurslar", "moliya.kurslar")
        money("Boshqa daromadlar", "moliya.boshqa")

    st.subheader("Xarajatlar")
    c1, c2 = st.columns(2)
    with c1:
        money("Jami xarajat", "moliya.jami_xarajat")
        money("Ish haqi fondi", "moliya.ish_haqi")
        money("Marketing", "moliya.mkt_xarajat")
    with c2:
        money("Kommunal", "moliya.kommunal")
        money("Texnologiya", "moliya.texno")
        money("Boshqa", "moliya.boshqa_xarajat")

    st.subheader("2026 maqsadlar")
    c1, c2 = st.columns(2)
    with c1:
        num("Maqsad qabul soni", "moliya.maqsad_qabul")
        money("Maqsad daromad", "moliya.maqsad_daromad")
        money("Marketing byudjet", "moliya.mkt_byudjet_2026")
    with c2:
        money("Min kontrakt narx", "moliya.min_narx")
        num("Max talaba sig'imi", "moliya.max_sigim")
        pct("Min foyda margin %", "moliya.min_margin")


elif sec_num == 11:
    st.header("🗺️ Hududiy Bozor")
    st.subheader("Buxoro viloyati")
    c1, c2 = st.columns(2)
    with c1:
        num("Viloyat aholisi", "hudud.buxoro_aholi")
        num("17-18 yosh aholisi", "hudud.buxoro_17_18")
        num("Bitiruvchilar (2026)", "hudud.buxoro_bitir")
    with c2:
        num("Universitetlar soni", "hudud.buxoro_uni")
        money("O'rtacha daromad", "hudud.buxoro_daromad")
        pct("Ishsizlik %", "hudud.buxoro_ishsizlik")

    st.subheader("O'zbekiston bo'yicha")
    c1, c2 = st.columns(2)
    with c1:
        num("Jami aholi", "hudud.uzb_aholi")
        num("17-18 yosh", "hudud.uzb_17_18")
        num("Universitetlar soni", "hudud.uzb_uni")
    with c2:
        money("O'rtacha kontrakt narx", "hudud.uzb_kontrakt")
        money("O'rtacha maosh", "hudud.uzb_maosh")
        pct("Ta'lim inflyatsiyasi %", "hudud.uzb_inflyatsiya")

    st.subheader("Viloyatlar potentsiali")
    for v in ["Samarqand", "Navoiy", "Qashqadaryo", "Toshkent", "Xorazm", "Fargona"]:
        with st.expander(v):
            c1, c2 = st.columns(2)
            key = v.lower()
            with c1:
                num("17-18 yosh aholi", f"hudud.vil.{key}.yosh")
                num("Universitetlar", f"hudud.vil.{key}.uni")
            with c2:
                slider("Raqobat darajasi", f"hudud.vil.{key}.raqobat")
                slider("BUI tanilganligi", f"hudud.vil.{key}.tanilganlik")


elif sec_num == 12:
    st.header("📅 Mavsumiylik")
    st.subheader("Oylik ariza faolligi (0-100)")
    cols = st.columns(4)
    oylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
             "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
    for i, oy in enumerate(oylar):
        with cols[i % 4]:
            num(oy, f"mavsum.{oy.lower()}", max_val=100)

    st.subheader("Muhim sanalar")
    c1, c2 = st.columns(2)
    with c1:
        txt("DTM imtihon sanasi", "mavsum.dtm")
        txt("Maktab bitirish", "mavsum.maktab_bitir")
    with c2:
        txt("Ramadan boshlanishi", "mavsum.ramadan_bosh")
        txt("Armiya chaqiruv oyi", "mavsum.armiya")


elif sec_num == 13:
    st.header("💻 Texnologiya")
    c1, c2 = st.columns(2)
    with c1:
        yn("CRM tizimi bor", "texno.crm")
        txt("CRM nomi", "texno.crm_nomi")
        yn("Google Analytics", "texno.ga")
        yn("UTM tracking", "texno.utm")
        yn("A/B test", "texno.ab_test")
        yn("Chatbot", "texno.chatbot")
        yn("AI chatbot", "texno.ai_chatbot")
    with c2:
        yn("LMS bor", "texno.lms")
        txt("LMS nomi", "texno.lms_nomi")
        yn("Mobil ilova", "texno.mobil")
        yn("Marketing automation", "texno.automation")
        yn("Retargeting", "texno.retargeting")
        slider("Data-driven qaror qilish", "texno.data_driven")


elif sec_num == 14:
    st.header("🌐 Tashqi Omillar")
    st.subheader("Iqtisodiy")
    c1, c2 = st.columns(2)
    with c1:
        pct("Inflyatsiya %", "tashqi.inflyatsiya")
        num("Dollar kursi", "tashqi.dollar")
        pct("Ishsizlik %", "tashqi.ishsizlik")
    with c2:
        pct("Yoshlar ishsizlik %", "tashqi.yoshlar_ishsiz")
        money("O'rtacha maosh", "tashqi.maosh")
        pct("GDP o'sishi %", "tashqi.gdp")

    st.subheader("Trendlar")
    c1, c2 = st.columns(2)
    with c1:
        slider("AI ta'siri ta'limga", "tashqi.ai_tasiri")
        slider("Online ta'lim o'sishi", "tashqi.online")
        slider("Diploma qadrsizlanishi", "tashqi.diploma_qadrsiz")
    with c2:
        slider("Xorijga ketish trendi", "tashqi.emigratsiya")
        slider("Startup madaniyati", "tashqi.startup")
        slider("Siyosiy barqarorlik (10=barqaror)", "tashqi.barqarorlik")


elif sec_num == 15:
    st.header("👥 Kadrlar")
    c1, c2 = st.columns(2)
    with c1:
        num("Jami xodimlar", "kadr.jami")
        num("Professor-o'qituvchi", "kadr.professor")
        num("Ma'muriy xodim", "kadr.admin")
        pct("PhD li professor %", "kadr.phd_foiz")
        pct("Xorijiy tajriba %", "kadr.xorijiy")
    with c2:
        money("Professor min maosh", "kadr.prof_min_maosh")
        money("Professor max maosh", "kadr.prof_max_maosh")
        slider("Xodim qoniqishi", "kadr.qoniqish")
        pct("Xodim ketish %", "kadr.turnover")

    st.subheader("Qabul jamoasi")
    c1, c2 = st.columns(2)
    with c1:
        num("Jamoa soni", "kadr.qabul_soni")
        num("O'rtacha tajriba (yil)", "kadr.qabul_tajriba")
    with c2:
        yn("KPI tizimi bor", "kadr.kpi")
        yn("Bonus tizimi bor", "kadr.bonus")

    st.subheader("Marketing jamoasi")
    c1, c2 = st.columns(2)
    with c1:
        num("Jamoa soni", "kadr.mkt_soni")
        yn("SMM mutaxassis", "kadr.smm")
        yn("Dizayner", "kadr.dizayner")
    with c2:
        yn("Videograf", "kadr.videograf")
        yn("Copywriter", "kadr.copywriter")
        yn("Analitik", "kadr.analitik")


elif sec_num == 16:
    st.header("🎓 Alumni / Bitiruvchilar")
    c1, c2 = st.columns(2)
    with c1:
        num("Jami bitiruvchilar", "alumni.jami")
        pct("6 oy ichida ishga joylashgan %", "alumni.ish_6oy")
        pct("Mutaxassislik bo'yicha %", "alumni.mutaxassislik")
        money("O'rtacha maosh (1-yil)", "alumni.maosh_1yil")
        money("O'rtacha maosh (3-yil)", "alumni.maosh_3yil")
    with c2:
        yn("Alumni assotsiatsiya", "alumni.assotsiatsiya")
        num("Alumni guruh a'zolari", "alumni.guruh")
        pct("BUI ni tavsiya qiladi %", "alumni.tavsiya")
        num("Alumni agent sifatida", "alumni.agent")
        num("Ish beruvchi hamkorlar", "alumni.ish_beruvchi")


elif sec_num == 17:
    st.header("🎒 Talaba Hayoti")
    st.subheader("Qoniqish ko'rsatkichlari (1-10)")
    cols = st.columns(3)
    items = [("Umumiy", "umumiy"), ("Ta'lim sifati", "talim"),
             ("Infratuzilma", "infra"), ("Ovqatlanish", "ovqat"),
             ("Transport", "transport"), ("Internet", "internet"),
             ("O'qituvchilar", "oqituvchi"), ("Admin xizmat", "admin")]
    for i, (label, key) in enumerate(items):
        with cols[i % 3]:
            slider(label, f"hayot.qoniqish.{key}")

    tags("Eng ko'p shikoyatlar", "hayot.shikoyat")
    tags("Ketish sabablari", "hayot.ketish_sabab")
    pct("1-semestr ketish %", "hayot.ketish_1sem")
    yn("Startap inkubator", "hayot.startap")
    num("Hackathon yilda", "hayot.hackathon")


elif sec_num == 18:
    st.header("🏷️ Brend va Reputatsiya")
    c1, c2 = st.columns(2)
    with c1:
        pct("Tanilganlik Buxoroda %", "brend.tanilgan_bux")
        pct("Tanilganlik O'zbekistonda %", "brend.tanilgan_uzb")
        pct("Maqsadli auditoriyada %", "brend.tanilgan_maqsad")
        num("Google reyting", "brend.google_reyting", is_float=True)
        num("Google sharhlar", "brend.google_sharh")
    with c2:
        txt("Slogan", "brend.slogan")
        tags("Brend assosiatsiyalari", "brend.assosiatsiya")
        tags("Brend qadriyatlari", "brend.qadriyat")
        tags("Mukofotlar/yutuqlar", "brend.mukofot")
        yn("Brand book bor", "brend.brandbook")


elif sec_num == 19:
    st.header("🤝 Hamkorliklar")
    c1, c2 = st.columns(2)
    with c1:
        num("Sanoat hamkorlar", "hamkor.sanoat_soni")
        num("Stajировка joylari", "hamkor.staj_joy")
        num("Tadqiqot loyihalari", "hamkor.tadqiqot")
    with c2:
        num("Patent soni", "hamkor.patent")
        num("Scopus maqolalar (yilda)", "hamkor.scopus")
        yn("Texnopark bor", "hamkor.texnopark")
    tags("IT hamkorlar", "hamkor.it")
    tags("IT sertifikat markazlari", "hamkor.sertifikat")


elif sec_num == 20:
    st.header("⚖️ Qonunchilik")
    c1, c2 = st.columns(2)
    with c1:
        yn("Litsenziya amal qiladi", "qonun.litsenziya")
        txt("Litsenziya tugash sanasi", "qonun.litsenziya_tugash")
        txt("Akkreditatsiya tugashi", "qonun.akkred_tugash")
        yn("Soliq imtiyozi bor", "qonun.soliq_imtiyoz")
    with c2:
        yn("Akademik halollik siyosati", "qonun.halollik")
        yn("Anti-korrupsiya siyosati", "qonun.anti_korr")
        yn("Gender tenglik siyosati", "qonun.gender")
        txt("Sifat boshqaruv tizimi", "qonun.iso", "ISO 9001")


elif sec_num == 21:
    st.header("🔄 Qabul Funnel")
    st.subheader("Bosqichlar bo'yicha sonlar")
    items = [
        ("Xabardor bo'lgan", "xabardor"), ("Qiziqgan (saytga kirgan)", "qiziqish"),
        ("Ariza boshlagan", "ariza_bosh"), ("Ariza tugatgan", "ariza_tugat"),
        ("Qabul qilingan", "qabul"), ("Shartnoma imzolagan", "shartnoma"),
        ("To'lov qilgan", "tolov"), ("Darsga kelgan", "dars"),
    ]
    cols = st.columns(4)
    for i, (label, key) in enumerate(items):
        with cols[i % 4]:
            num(label, f"funnel.{key}")

    st.subheader("Konversiyalar (%)")
    cols = st.columns(4)
    konv = [("Xabardor→Qiziqish", "k1"), ("Qiziqish→Ariza", "k2"),
            ("Ariza→Qabul", "k3"), ("Qabul→To'lov", "k4"),
            ("To'lov→Dars", "k5")]
    for i, (label, key) in enumerate(konv):
        with cols[i % 4]:
            pct(label, f"funnel.konv.{key}")


elif sec_num == 22:
    st.header("🖥️ Raqamli Aktivlar")
    c1, c2 = st.columns(2)
    with c1:
        num("Sayt tezligi (sek)", "digital.sayt_tezlik", is_float=True)
        num("Oylik tashrif", "digital.sayt_tashrif")
        pct("Bounce rate %", "digital.bounce")
        yn("Mobil optimizatsiya", "digital.mobil")
    with c2:
        yn("Virtual tur bor", "digital.virtual_tur")
        yn("Blog bor", "digital.blog")
        num("Landing sahifalar soni", "digital.landing")
        pct("Landing konversiya %", "digital.landing_konv")


elif sec_num == 23:
    st.header("🌱 Ijtimoiy Ta'sir")
    c1, c2 = st.columns(2)
    with c1:
        num("Ijtimoiy loyihalar", "ijtimoiy.loyiha_soni")
        num("Bepul kurslar", "ijtimoiy.bepul_kurs")
        num("Bepul kurs ishtirokchilari", "ijtimoiy.bepul_ishtirok")
    with c2:
        yn("Maktab hamkorligi", "ijtimoiy.maktab")
        num("Hamkor maktablar soni", "ijtimoiy.maktab_soni")
        slider("Ijtimoiy reputatsiya", "ijtimoiy.reputatsiya")


elif sec_num == 24:
    st.header("🔮 Kelajak Rejalari")
    st.subheader("Qisqa muddatli (2026)")
    tags("Yangi yo'nalishlar", "kelajak.yangi_yon")
    txt("Yangi bino rejalari", "kelajak.bino")
    tags("Yangi hamkorliklar", "kelajak.hamkor")

    st.subheader("O'rta muddatli (3 yil)")
    num("Maqsad talaba soni", "kelajak.maqsad_3yil")
    yn("Kampus kengaytirish", "kelajak.kampus_keng")
    yn("Filial ochish", "kelajak.filial")
    txt("Filial shahri", "kelajak.filial_shahar")

    st.subheader("Uzoq muddatli (5-10 yil)")
    txtarea("Vizyon 2030", "kelajak.vizyon")
    txtarea("Missiya", "kelajak.missiya")
    num("Maqsad talaba (5 yil)", "kelajak.maqsad_5yil")


elif sec_num == 25:
    st.header("🎯 Simulyatsiya Maqsadlari")
    st.info("Og'irliklar jami 1.00 bo'lishi kerak!")

    maqsadlar = [
        ("Talabalar soni MAX", "son", 0.30),
        ("Daromad MAX", "daromad", 0.25),
        ("Marketing ROI MAX", "roi", 0.15),
        ("Sifatli talabalar", "sifat", 0.10),
        ("Hududiy diversifikatsiya", "hudud", 0.10),
        ("Brend tanilganligi", "brend", 0.05),
        ("Talaba retention", "retention", 0.05),
    ]

    for label, key, default in maqsadlar:
        c1, c2, c3 = st.columns([3, 1, 2])
        with c1:
            st.write(f"**{label}**")
        with c2:
            num("Og'irlik", f"maqsad.{key}.ogirlik", is_float=True)
        with c3:
            num("Maqsad qiymat", f"maqsad.{key}.qiymat")

    st.subheader("Qattiq cheklovlar")
    c1, c2 = st.columns(2)
    with c1:
        num("Max talaba sig'imi", "maqsad.cheklov.max_talaba")
        money("Min kontrakt narx", "maqsad.cheklov.min_narx")
        money("Max marketing byudjet", "maqsad.cheklov.max_mkt")
    with c2:
        pct("Max chegirma %", "maqsad.cheklov.max_chegirma")
        pct("Min foyda margin %", "maqsad.cheklov.min_foyda")
        num("Min DTM ball", "maqsad.cheklov.min_ball")


# ─── Avtomatik saqlash ───
save_data(st.session_state["data"])

# ─── Footer ───
st.markdown("---")
st.caption("BUI Qabul Simulyatori v2.0 | 25 bo'lim | 1000+ parametr")
