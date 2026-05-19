"""
BUI QABUL SIMULYATORI — MEGA MA'LUMOT SXEMASI (1000+ PARAMETR)
================================================================
25 bo'lim | 1000+ parametr | Hech narsa qolib ketmaydi

TO'LDIRISH TARTIBI:
1. Har bir 0 → haqiqiy raqam
2. Har bir "" → haqiqiy matn
3. Har bir [] → haqiqiy ro'yxat
4. Bilmasangiz → # TAXMIN yozing
5. Ro'yxatlarni (YONALISHLAR, RAQOBATCHILAR...) ko'paytiring
"""

# ══════════════════════════════════════════════════════════════════════
# 1-BO'LIM: UNIVERSITET PROFILI (45 parametr)
# ══════════════════════════════════════════════════════════════════════
UNIVERSITET = {
    # --- Asosiy ---
    "nomi": "Buxoro innovatsion universiteti",
    "qisqa_nomi": "BUI",
    "tashkil_etilgan_yil": 2024,
    "litsenziya_turi": "Nodavlat",          # Davlat / Nodavlat
    "litsenziya_raqami": "",
    "litsenziya_berilgan_sana": "",
    "akkreditatsiya": True,
    "akkreditatsiya_darajasi": "",           # "Milliy" / "Xalqaro" / "Ikkalasi"
    "akkreditatsiya_organi": "",
    "akkreditatsiya_muddati": "",            # "2030-01-01" gacha
    "rektor_fio": "",
    "rektor_ilmiy_darajasi": "",             # "PhD" / "DSc" / "Professor"
    "prorektor_soni": 0,
    "tashkiliy_tuzilma": "",                 # "Fakultet" / "Instituti" / "Aralash"

    # --- Joylashuv ---
    "shahar": "Buxoro",
    "viloyat": "Buxoro viloyati",
    "tuman": "",
    "manzil_toliq": "",
    "pochta_indeksi": "",
    "koordinatalar_lat": 39.7747,
    "koordinatalar_lng": 64.4286,
    "shahar_markazidan_km": 0,
    "aeroport_dan_km": 0,
    "temir_yol_dan_km": 0,
    "avtovokzal_dan_km": 0,

    # --- Veb va aloqa ---
    "veb_sayt": "https://bui.uz",
    "qabul_sayt": "https://qabul.bui.uz",
    "email": "",
    "telefon_asosiy": "",
    "telefon_qabul": "",
    "faks": "",
    "telegram_kanal": "",
    "instagram": "",
    "facebook": "",
    "youtube": "",
    "tiktok": "",
    "linkedin": "",

    # --- Reyting va nufuz (1-10) ---
    "mahalliy_reyting_bali": 0,
    "xalqaro_reyting_bali": 0,
    "ish_beruvchi_ishonchi": 0,
    "talabalar_qoniqishi": 0,
    "ota_ona_ishonchi": 0,
    "media_ko_rinishi": 0,               # OAVda qancha chiqadi
    "brend_tanilganligi_buxoro": 0,       # 1-10 Buxoroda
    "brend_tanilganligi_uzb": 0,          # 1-10 O'zbekiston bo'yicha
    "google_reyting": 0.0,                # Google Maps'da 1.0-5.0
    "google_sharh_soni": 0,

    # --- Umumiy raqamlar ---
    "joriy_talabalar_soni": 0,
    "bakalavr_talabalar": 0,
    "magistr_talabalar": 0,
    "phd_talabalar": 0,
    "sirtqi_talabalar": 0,
    "kechki_talabalar": 0,
    "xorijiy_talabalar": 0,
    "fakultetlar_soni": 0,
    "kafedralar_soni": 0,
    "professor_oqituvchilar_soni": 0,
    "xalqaro_professor_soni": 0,
    "phd_li_professor_foizi": 0,
    "dsc_li_professor_soni": 0,
    "talaba_oqituvchi_nisbati": 0,        # masalan 25
    "bitiruvchilar_jami_soni": 0,         # tashkil etilgandan beri
}

# ══════════════════════════════════════════════════════════════════════
# 2-BO'LIM: TA'LIM YO'NALISHLARI (55+ parametr x har bir yo'nalish)
# ══════════════════════════════════════════════════════════════════════
YONALISHLAR = [
    {
        # --- Identifikatsiya ---
        "kodi": "YON_001",
        "nomi": "",                          # "Kompyuter injiniringi"
        "nomi_inglizcha": "",
        "fakultet": "",
        "kafedra": "",
        "klassifikator_kodi": "",            # DTM klassifikatori

        # --- Ta'lim shakli ---
        "talim_turi": "Bakalavr",            # Bakalavr / Magistratura / PhD
        "talim_tili": "O'zbek",              # O'zbek / Rus / Ingliz / Aralash
        "talim_shakli": "Kunduzgi",          # Kunduzgi / Sirtqi / Kechki / Masofaviy
        "talim_muddati_yil": 4,
        "kreditlar_soni": 0,                 # ECTS kredit
        "semestrlar_soni": 8,
        "amaliyot_oylari": 0,                # ishlab chiqarish amaliyoti

        # --- Kvota va qabul ---
        "davlat_granti_bor": False,
        "grant_kvota": 0,
        "kontrakt_kvota": 0,
        "jami_kvota": 0,
        "transfer_kvota": 0,                 # boshqa uni'dan o'tish
        "xorijiy_kvota": 0,                  # xorijiy talabalar uchun

        # --- O'tgan yil statistikasi ---
        "otgan_yil_ariza_soni": 0,
        "otgan_yil_qabul_soni": 0,
        "otgan_yil_kelgan_soni": 0,          # hujjat topshirgan
        "otgan_yil_tolov_qilgan": 0,         # to'lov boshlagan
        "otgan_yil_1_semestr_ketgan": 0,     # birinchi semestrda ochirilgan
        "raqobat_darajasi": 0,               # 1 o'ringa nechta
        "konversiya_ariza_kelish": 0,        # ariza → kelish %
        "eng_yuqori_ball": 0,                # eng yuqori qabul bali
        "eng_past_ball": 0,                  # eng past qabul bali

        # --- Ball talablari ---
        "minimal_ball": 0,                   # DTM min
        "ortacha_qabul_bali": 0,
        "tavsiya_etilgan_ball": 0,           # "X dan yuqori bo'lsa yaxshi"
        "ielts_talab": 0.0,                  # 0 = talab yo'q
        "boshqa_sertifikat_talab": "",

        # --- Narx ---
        "kontrakt_narxi_yillik": 0,          # so'mda
        "kontrakt_narxi_semestr": 0,
        "kontrakt_narxi_dollarda": 0,        # referens uchun
        "otgan_yilgi_narx": 0,               # 2025 narxi
        "narx_osihi_foiz": 0,                # yillik % o'sish
        "sirtqi_narxi": 0,
        "kechki_narxi": 0,

        # --- Ish bilan bandlik ---
        "ish_bilan_bandlik_foizi": 0,        # 6 oy ichida %
        "ortacha_maosh_bitiruvchi": 0,       # so'mda, 1-yil
        "ortacha_maosh_3_yil": 0,            # so'mda, 3-yildan keyin
        "ish_beruvchi_hamkorlar_soni": 0,
        "top_ish_beruvchilar": [],            # ["kompaniya1", "kompaniya2"]
        "stajировка_imkoniyati": False,
        "stajировка_tolov": False,           # to'lovli amaliyotmi

        # --- O'quv dastur sifati ---
        "xalqaro_dastur_asosida": False,     # xorijiy uni dasturi
        "xalqaro_hamkor_uni": "",
        "zamonaviy_fanlar_soni": 0,          # AI, blockchain kabi
        "amaliy_fanlar_foizi": 0,            # % nazariy vs amaliy
        "loyiha_asosida_oqitish": False,     # PBL
        "mehmon_maruza_yilda": 0,            # yilda nechta
        "sanoat_hamkorlik_loyiha": 0,        # sanoat bilan loyihalar

        # --- Tavsif ---
        "kuchli_tomonlari": [],
        "zaif_tomonlari": [],
        "usp": "",                           # Unique Selling Point
        "maqsadli_auditoriya": "",           # "IT ga qiziquvchi yoshlar"
        "mashhurlik_darajasi": 0,            # 1-10, abituriyentlar orasida
    },
    # ... KAMIDA 10-20 ta yo'nalish kiritiladi
]

# ══════════════════════════════════════════════════════════════════════
# 3-BO'LIM: NARXLASH STRATEGIYASI (65 parametr)
# ══════════════════════════════════════════════════════════════════════
NARXLASH = {
    # --- Joriy narx diapazoni ---
    "eng_arzon_kontrakt": 0,
    "eng_qimmat_kontrakt": 0,
    "ortacha_kontrakt": 0,
    "mediana_kontrakt": 0,
    "sirtqi_narx_koeffitsient": 0.6,
    "kechki_narx_koeffitsient": 0.7,
    "masofaviy_narx_koeffitsient": 0.5,

    # --- Narx tarixiy o'zgarishi ---
    "narx_2023": 0,
    "narx_2024": 0,
    "narx_2025": 0,
    "narx_2026_rejali": 0,
    "yillik_osish_foiz_ortacha": 0,

    # --- Chegirmalar ---
    "early_bird_chegirma_foiz": 0,
    "early_bird_deadline": "",
    "early_bird_otgan_yil_foydalangan": 0,  # nechta talaba ishlatgan
    "bir_yillik_tolash_chegirma": 0,
    "aka_uka_chegirma": 0,
    "aka_uka_otgan_yil_foydalangan": 0,
    "oltin_medal_chegirma": 0,
    "kumush_medal_chegirma": 0,
    "sport_chegirma": 0,
    "sport_chegirma_talablar": "",           # "viloyat chempioni" kabi
    "ijtimoiy_chegirma": 0,
    "ijtimoiy_kategoriyalar": [],            # ["yetim", "nogironlik", "kam ta'min"]
    "hamkor_maktab_chegirma": 0,
    "hamkor_maktablar_soni": 0,
    "hamkor_maktablar_royxati": [],
    "xodim_farzandi_chegirma": 0,
    "talaba_tavsiya_chegirma": 0,            # referral bonus
    "olimpiada_gold_chegirma": 0,
    "olimpiada_silver_chegirma": 0,
    "olimpiada_bronze_chegirma": 0,
    "qayta_qabul_chegirma": 0,              # ikkinchi marta kelganlar
    "guruh_chegirma": 0,                     # 3+ kishi birga kelsa
    "guruh_min_talaba": 3,
    "maxsus_aksiya_chegirma": 0,             # vaqtinchalik aksiyalar
    "maxsus_aksiya_muddati": "",
    "max_chegirma_cheklovi_foiz": 0,         # bir talabaga max chegirma

    # --- Stipendiyalar ---
    "toliq_grant_soni": 0,
    "toliq_grant_shartlari": "",
    "yarim_grant_soni": 0,
    "yarim_grant_shartlari": "",
    "chorak_grant_soni": 0,                  # 25% chegirma
    "rektorat_stipendiya_soni": 0,
    "rektorat_stipendiya_summasi": 0,        # oylik so'mda
    "akademik_stipendiya_soni": 0,
    "akademik_stipendiya_min_gpa": 0.0,      # min GPA talab
    "sport_stipendiya_soni": 0,
    "ijtimoiy_stipendiya_soni": 0,
    "xorijiy_donor_stipendiya": 0,           # xalqaro fondlardan
    "sanoat_hamkor_stipendiya": 0,           # kompaniyalardan
    "stipendiya_jami_byudjet": 0,            # so'mda, yillik

    # --- To'lov shartlari ---
    "bolib_tolash_bor": True,
    "bolib_tolash_oylar": 0,
    "bolib_tolash_ustama": 0,
    "click_uz_bor": True,
    "payme_bor": False,
    "uzum_bank_bor": False,
    "naqd_qabul_qilish": True,
    "plastik_karta_qabul": True,
    "xalqaro_karta_qabul": False,            # Visa/Mastercard
    "kredit_hamkorlik_bank": "",
    "kredit_foiz_stavka": 0,
    "kredit_max_muddat_oy": 0,
    "kredit_boshlangich_tolov": 0,           # % dan
    "kechikish_jarima_foiz": 0,              # oylik kechikish jarima
    "qaytarish_siyosati": "",                # "1 oy ichida 80% qaytariladi"

    # --- Simulyatsiya chegaralari ---
    "narx_oshirish_max_foiz": 20,
    "narx_kamaytirish_max_foiz": 30,
    "chegirma_byudjet_max": 0,               # so'mda, max chegirmalarga sarflash
}

# ══════════════════════════════════════════════════════════════════════
# 4-BO'LIM: MARKETING KANALLARI VA BYUDJET (160+ parametr)
# ══════════════════════════════════════════════════════════════════════
MARKETING = {
    "jami_byudjet_yillik": 0,
    "otgan_yil_byudjet": 0,
    "byudjet_osish_foiz": 0,
    "marketing_jamoa_soni": 0,               # nechta kishi
    "marketing_rahbar": "",                   # ismi
    "tashqi_agentlik_bor": False,
    "tashqi_agentlik_nomi": "",
    "tashqi_agentlik_byudjet": 0,

    # === DIGITAL KANALLAR ===
    "telegram": {
        "byudjet": 0,
        "kanal_nomi": "",
        "obunchilar_soni": 0,
        "oylik_osish": 0,                    # har oyda yangi obunchi
        "postlar_oyiga": 0,                  # oyiga nechta post
        "ortacha_reach": 0,
        "ortacha_engagement": 0,             # like+comment+share
        "eng_yaxshi_post_reach": 0,
        "guruh_bor": False,
        "guruh_azolar": 0,
        "bot_bor": False,
        "bot_foydalanuvchilar": 0,
        "reklama_byudjet": 0,               # paid promotion
        "boshqa_kanallarda_reklama": 0,      # boshqa kanallarda reklama byudjeti
        "konversiya_korinish_ariza": 0,      # ko'rishdan arizagacha %
        "konversiya_ariza_tolov": 0,         # arizadan to'lovgacha %
        "cpa": 0,                            # cost per acquisition
    },
    "instagram": {
        "byudjet": 0,
        "profil_nomi": "",
        "followers": 0,
        "oylik_osish": 0,
        "postlar_oyiga": 0,
        "reels_oyiga": 0,
        "stories_oyiga": 0,
        "ortacha_reach": 0,
        "ortacha_engagement_rate": 0,        # %
        "reklama_byudjet": 0,
        "konversiya_foiz": 0,
        "cpa": 0,
        "eng_samarali_content_turi": "",     # "reels" / "post" / "stories"
    },
    "facebook": {
        "byudjet": 0,
        "sahifa_nomi": "",
        "followers": 0,
        "ads_byudjet": 0,
        "konversiya_foiz": 0,
        "cpa": 0,
        "maqsadli_auditoriya_hajmi": 0,
    },
    "youtube": {
        "byudjet": 0,
        "kanal_nomi": "",
        "subscribers": 0,
        "videolar_soni": 0,
        "ortacha_views": 0,
        "oyiga_yangi_video": 0,
        "reklama_byudjet": 0,
        "konversiya_foiz": 0,
        "cpa": 0,
        "eng_mashhur_video_views": 0,
        "shorts_foydalanish": False,
    },
    "tiktok": {
        "byudjet": 0,
        "profil_nomi": "",
        "followers": 0,
        "ortacha_views": 0,
        "videolar_soni": 0,
        "oyiga_yangi_video": 0,
        "konversiya_foiz": 0,
        "cpa": 0,
        "viral_video_bor": False,
        "viral_video_max_views": 0,
    },
    "google_ads": {
        "byudjet": 0,
        "oylik_clicks": 0,
        "cpc_ortacha": 0,
        "ctr": 0,                            # click-through rate %
        "konversiya_foiz": 0,
        "cpa": 0,
        "kalit_sozlar": [],                  # ["buxoro universitet", "kontrakt arzon"]
        "display_ads_bor": False,
        "remarketing_bor": False,
    },
    "yandex_ads": {
        "byudjet": 0,
        "konversiya_foiz": 0,
        "cpa": 0,
    },
    "seo": {
        "byudjet": 0,
        "google_pozitsiya_asosiy": 0,        # "buxoro universitet" so'rovi uchun
        "organik_traffic_oylik": 0,
        "sahifalar_soni_indexed": 0,
        "backlinks_soni": 0,
        "blog_bor": False,
        "blog_maqolalar_oyiga": 0,
    },
    "sms_marketing": {
        "byudjet": 0,
        "baza_hajmi": 0,
        "yuborish_soni_yilda": 0,
        "ochilish_foizi": 0,                 # open rate %
        "konversiya_foiz": 0,
        "cpa": 0,
        "provayder": "",                     # "Playmobile" / "Eskiz"
    },
    "email_marketing": {
        "byudjet": 0,
        "baza_hajmi": 0,
        "yuborish_soni_yilda": 0,
        "ochilish_foizi": 0,
        "click_foizi": 0,
        "konversiya_foiz": 0,
    },
    "messenger_marketing": {
        "whatsapp_bor": False,
        "whatsapp_baza": 0,
        "whatsapp_konversiya": 0,
        "viber_bor": False,
    },

    # === TRADITIONAL MEDIA ===
    "tv_reklama": {
        "byudjet": 0,
        "kanallar": [],                      # [{"nomi": "O'zbekiston", "byudjet": 0, "vaqt": "prime-time"}]
        "oyiga_necha_marta": 0,
        "rolik_davomiyligi_sek": 0,
        "taxminiy_auditoriya": 0,
        "konversiya_foiz": 0,
        "cpa": 0,
        "mavsumiy_bor": False,               # faqat qabul davrida
    },
    "radio": {
        "byudjet": 0,
        "stansiyalar": [],
        "oyiga_necha_marta": 0,
        "konversiya_foiz": 0,
        "cpa": 0,
    },
    "gazeta_jurnal": {
        "byudjet": 0,
        "nashrlar": [],
        "yilda_necha_marta": 0,
        "konversiya_foiz": 0,
    },
    "billboard_banner": {
        "byudjet": 0,
        "joylashuv_soni": 0,
        "shaharlar": [],
        "joylashuvlar": [],                  # [{"shahar": "Buxoro", "manzil": "...", "hajm": "3x6"}]
        "oylik_ijara": 0,
        "dizayn_xarajat": 0,
        "konversiya_foiz": 0,
    },
    "transport_reklama": {
        "byudjet": 0,
        "avtobus_soni": 0,
        "taksi_soni": 0,
        "marshrut": [],
        "konversiya_foiz": 0,
    },
    "poligrafiya": {
        "byudjet": 0,
        "buklet_soni": 0,
        "plakat_soni": 0,
        "flayer_soni": 0,
        "katalog_soni": 0,
        "souvenir_soni": 0,                  # ruchka, bloknot kabi
    },

    # === OFFLINE TADBIRLAR ===
    "ochiq_eshiklar_kuni": {
        "yilda_necha_marta": 0,
        "ortacha_keluvchilar": 0,
        "konversiya_foiz": 0,
        "xarajat_har_biri": 0,
        "dastur": [],                        # ["prezentatsiya", "lab tur", "talabalar bilan suhbat"]
        "transport_taminlanadi": False,
        "ovqat_taminlanadi": False,
        "sovga_beriladi": False,
    },
    "maktablarga_tashrif": {
        "yilda_necha_maktab": 0,
        "viloyatlar": [],
        "ortacha_tinglovchilar": 0,
        "konversiya_foiz": 0,
        "xarajat_bir_safari": 0,
        "jamoa_soni_har_safari": 0,
        "material_tarqatiladi": True,
        "talabalar_ishtirok_etadi": False,   # joriy talabalar boradimi
        "maktab_tanlov_mezonlari": "",       # "500+ o'quvchi, shahar maktablari"
    },
    "talabalar_festival": {
        "yilda_necha_marta": 0,
        "xarajat_har_biri": 0,
        "taxminiy_auditoriya": 0,
        "konversiya_foiz": 0,
        "tadbir_nomlari": [],
    },
    "olimpiadalar": {
        "yilda_necha_marta": 0,
        "fanlar": [],                        # ["matematika", "fizika", "IT"]
        "ishtirokchilar_soni": 0,
        "konversiya_foiz": 0,
        "xarajat_har_biri": 0,
        "mukofotlar": [],                    # ["to'liq grant", "50% chegirma", "laptop"]
    },
    "konferensiya_seminar": {
        "yilda_necha_marta": 0,
        "xarajat": 0,
        "ishtirokchilar": 0,
    },
    "yarmarkalar": {
        "talim_yarmarkasi_ishtirok": 0,      # yilda nechta
        "xalqaro_yarmarkalar": 0,
        "xarajat": 0,
    },

    # === AGENTLAR (REFERRAL) TIZIMI ===
    "agentlar": {
        "jami_agentlar_soni": 0,
        "faol_agentlar_soni": 0,             # aslida ishlaydigan
        "agent_turi_taqsimot": {
            "maktab_oqituvchi": 0,           # nechta
            "universitet_talaba": 0,
            "tashqi_agent": 0,
            "bitiruvchi": 0,
            "ota_ona_tanish": 0,
        },
        "agent_komissiya_foiz": 0,
        "agent_komissiya_fixed": 0,
        "agent_bonus_5_talaba": 0,           # 5+ keltirsa qo'shimcha
        "agent_bonus_10_talaba": 0,          # 10+ keltirsa qo'shimcha
        "otgan_yil_agent_keltirilgan": 0,
        "eng_samarali_agent_turi": "",
        "agent_crm_bor": False,
        "agent_training_bor": False,
        "agent_material_beriladi": False,
        "agent_viloyat_taqsimot": {},        # {"Buxoro": 10, "Samarqand": 5}
    },

    # === SO'Z MARKETING ===
    "soz_marketing": {
        "nps_score": 0,                      # -100 dan +100
        "joriy_talaba_tavsiya_foiz": 0,
        "bitiruvchi_tavsiya_foiz": 0,
        "ota_ona_tavsiya_foiz": 0,
        "online_sharh_bali": 0,              # 1-5
        "salbiy_sharh_foiz": 0,              # % salbiy
        "viral_koeffitsient": 0.0,           # 1 talaba nechta yangi keltiradi
    },

    # === INFLUENCER MARKETING ===
    "influencer": {
        "byudjet": 0,
        "hamkorlar_soni": 0,
        "hamkorlar": [],                     # [{"nomi": "", "platforma": "", "followers": 0, "narx": 0}]
        "talaba_ambassador_soni": 0,
        "ambassador_oylik_tolov": 0,
    },

    # === CONTENT STRATEGIYA ===
    "content": {
        "content_jamoa_soni": 0,
        "oyiga_video_soni": 0,
        "oyiga_post_soni": 0,
        "oyiga_blog_maqola": 0,
        "success_story_soni": 0,             # bitiruvchi muvaffaqiyat hikoyalari
        "virtual_tur_bor": False,
        "podcast_bor": False,
        "webinar_oyiga": 0,
    },
}

# ══════════════════════════════════════════════════════════════════════
# 5-BO'LIM: ABITURIYENT PROFILI VA XULQ MODELI (130+ parametr)
# ══════════════════════════════════════════════════════════════════════
ABITURIYENT_PROFILI = {
    # --- Hududiy taqsimot (% da, jami=100) ---
    "hududiy_taqsimot": {
        "Buxoro_shahar": 0,
        "Buxoro_Kogon": 0,
        "Buxoro_Gijduvon": 0,
        "Buxoro_Vobkent": 0,
        "Buxoro_Jondor": 0,
        "Buxoro_Olot": 0,
        "Buxoro_Peshku": 0,
        "Buxoro_Qorakol": 0,
        "Buxoro_Romitan": 0,
        "Buxoro_Shofirkon": 0,
        "Buxoro_Buxoro_tuman": 0,
        "Buxoro_Qorovulbozor": 0,
        "Samarqand_viloyat": 0,
        "Navoiy_viloyat": 0,
        "Qashqadaryo_viloyat": 0,
        "Surxondaryo_viloyat": 0,
        "Toshkent_shahar": 0,
        "Toshkent_viloyat": 0,
        "Xorazm_viloyat": 0,
        "Fargona_viloyat": 0,
        "Andijon_viloyat": 0,
        "Namangan_viloyat": 0,
        "Jizzax_viloyat": 0,
        "Sirdaryo_viloyat": 0,
        "Qoraqalpogiston": 0,
    },

    # --- Jins ---
    "jins_taqsimot": {
        "erkak_foiz": 0,
        "ayol_foiz": 0,
    },

    # --- Yosh ---
    "yosh_taqsimot": {
        "16_yosh": 0,
        "17_yosh": 0,
        "18_yosh": 0,
        "19_yosh": 0,
        "20_yosh": 0,
        "21_23_yosh": 0,
        "24_27_yosh": 0,
        "28_plus": 0,
    },

    # --- Oilaviy daromad (oylik, so'mda) ---
    "daromad_segmentlari": {
        "juda_past_1_5mln_gacha": 0,
        "past_1_5_3mln": 0,
        "ortacha_past_3_5mln": 0,
        "ortacha_5_8mln": 0,
        "yuqori_ortacha_8_12mln": 0,
        "yuqori_12_20mln": 0,
        "boylar_20mln_plus": 0,
    },

    # --- Ota-ona ta'limi ---
    "ota_ona_talimi": {
        "ikkalasi_oliy": 0,                  # %
        "bittasi_oliy": 0,
        "ortacha_maxsus": 0,
        "maktab": 0,
        "tugallanmagan": 0,
    },

    # --- Ota-ona kasbi ---
    "ota_ona_kasbi": {
        "davlat_xizmatchisi": 0,             # %
        "tadbirkor": 0,
        "ishchi": 0,
        "dehqon_fermer": 0,
        "oquvchi_talaba": 0,
        "pensioner": 0,
        "ishsiz": 0,
        "xorijda_ishlaydi": 0,              # migrant
    },

    # --- Maktab turi ---
    "maktab_turi": {
        "oddiy_maktab": 0,                  # %
        "ixtisoslashgan_maktab": 0,
        "prezident_maktab": 0,
        "xususiy_maktab": 0,
        "litsey": 0,
        "kollej": 0,
        "texnikum": 0,
        "boshqa_uni_transfer": 0,            # boshqa uni'dan o'tuvchi
    },

    # --- Abituriyent akademik profili ---
    "akademik_profil": {
        "ortacha_dtm_ball": 0,
        "median_dtm_ball": 0,
        "yuqori_ball_foiz": 0,              # 170+ ball %
        "ortacha_ball_foiz": 0,              # 120-170 ball %
        "past_ball_foiz": 0,                 # 120- ball %
        "ortacha_maktab_bali": 0,            # 5-ballik tizimda
        "ingliz_tili_bilish": 0,             # % biladiganlar
        "ielts_bor_foiz": 0,                # % IELTS sertifikati bor
        "kompyuter_savodxonlik": 0,          # % yaxshi biladi
    },

    # --- Qaror qabul qilish omillari (1-10 ahamiyat) ---
    "qaror_omillari": {
        "kontrakt_narxi": 0,
        "stipendiya_grant": 0,
        "bolib_tolash": 0,
        "yonalish_sifati": 0,
        "professor_darajasi": 0,
        "kampus_sharoit": 0,
        "yotoqxona": 0,
        "ovqatlanish": 0,
        "joylashuv_masofa": 0,
        "transport_qulaylik": 0,
        "ish_bilan_bandlik": 0,
        "stajировка_imkoniyat": 0,
        "xalqaro_aloqalar": 0,
        "ikki_diplom": 0,
        "xorijga_chiqish_imkoniyati": 0,
        "brend_nomi": 0,
        "reyting": 0,
        "dostlar_tasiri": 0,
        "oila_bosimi": 0,
        "ota_ona_tanlovi": 0,
        "ijtimoiy_tarmoq_tasiri": 0,
        "influencer_tasiri": 0,
        "chegirma_aksiya": 0,
        "maktab_tavsiyasi": 0,
        "oqituvchi_tavsiyasi": 0,
        "agent_tavsiyasi": 0,
        "bitiruvchi_tavsiyasi": 0,
        "joriy_talaba_fikri": 0,
        "online_sharh_tasiri": 0,
        "ochiq_eshiklar_kuni_tasiri": 0,
        "veb_sayt_tasiri": 0,
        "harbiy_xizmatdan_qochish": 0,       # yigitlar uchun
        "farzand_yaqin_bolishi": 0,           # ota-ona uchun
        "zamonaviy_bino": 0,
        "laboratoriya_jihozlari": 0,
        "kutubxona_sifati": 0,
        "sport_imkoniyatlari": 0,
        "madaniy_hayot": 0,
        "wifi_internet": 0,
    },

    # --- Axborot manbalari (1-10, qayerdan eshitadi) ---
    "axborot_manbalari": {
        "telegram": 0,
        "instagram": 0,
        "youtube": 0,
        "tiktok": 0,
        "facebook": 0,
        "televizor": 0,
        "radio": 0,
        "gazeta": 0,
        "dostlar_sinfdoshlar": 0,
        "ota_ona": 0,
        "aka_uka_opa_singil": 0,
        "maktab_oqituvchisi": 0,
        "repetitor": 0,
        "agent_vositachi": 0,
        "veb_sayt_qidiruv": 0,
        "google_reklama": 0,
        "ochiq_eshiklar_kuni": 0,
        "billboard": 0,
        "buklet_flayer": 0,
        "yarmarkalar": 0,
        "whatsapp_guruh": 0,
        "sms": 0,
        "email": 0,
        "talim_portallari": 0,              # uzbattest.uz kabi
    },

    # --- Qaror qabul qilish jarayoni ---
    "qaror_jarayoni": {
        "qidiruv_boshlash_oyi": "",          # "yanvar" / "mart" / "may"
        "ortacha_qidiruv_davomiyligi_oy": 0, # necha oy izlaydi
        "nechta_uni_ko_radi": 0,             # nechta universitetni taqqoslaydi
        "nechta_uni_ariza_beradi": 0,        # nechtaga ariza beradi
        "oxirgi_qaror_oyi": "",              # "iyul" / "avgust"
        "kim_qaror_qiladi": "",              # "o'zi" / "ota-onasi" / "birgalikda"
        "ota_ona_qaror_foiz": 0,             # ota-ona qaror qiladigan %
        "narx_sezgirligi_elastiklik": 0.0,   # 0-2, narx o'zgarganda qancha ta'sir
    },

    # --- O'tgan yilgi statistika ---
    "otgan_yil": {
        "jami_ariza_soni": 0,
        "jami_qabul_qilingan": 0,
        "jami_hujjat_topshirgan": 0,
        "jami_tolov_qilgan": 0,
        "jami_darsga_kelgan": 0,
        "birinchi_semestr_ketgan": 0,
        "konversiya_ariza_qabul": 0,         # %
        "konversiya_qabul_hujjat": 0,        # %
        "konversiya_hujjat_tolov": 0,        # %
        "konversiya_tolov_davom": 0,          # %
        "ortacha_ariza_sanasi": "",           # "2025-06-15"
        "eng_ko_p_ariza_oyi": "",
        "eng_kam_ariza_oyi": "",
        "erkak_foiz": 0,
        "ayol_foiz": 0,
        "buxorolik_foiz": 0,                 # Buxoro viloyatidan %
        "boshqa_viloyat_foiz": 0,
    },

    # --- Psixologik segmentlar ---
    "psixologik_segmentlar": {
        "narx_sezgir": 0,                   # % — eng arzon kerak
        "sifat_izlovchi": 0,                 # % — eng yaxshisi kerak
        "qulaylik_izlovchi": 0,              # % — uyga yaqin, oson
        "status_izlovchi": 0,                # % — brend, nufuz kerak
        "pragmatik": 0,                      # % — ish topish kerak
        "ota_ona_boshqaruvchi": 0,           # % — ota-ona tanlaydi
        "guruh_ergashuvchi": 0,              # % — do'stlari qayerga ketsa
        "tasodifiy": 0,                      # % — oxirgi daqiqada qaror
    },
}

# ══════════════════════════════════════════════════════════════════════
# 6-BO'LIM: RAQOBATCHILAR (55+ parametr x har biri)
# ══════════════════════════════════════════════════════════════════════
RAQOBATCHILAR = [
    {
        # --- Identifikatsiya ---
        "nomi": "",
        "qisqa_nomi": "",
        "turi": "Davlat",                    # Davlat / Nodavlat / Filial / Xorijiy
        "shahar": "Buxoro",
        "tashkil_etilgan_yil": 0,
        "veb_sayt": "",

        # --- Hajm ---
        "jami_talabalar": 0,
        "yillik_qabul_soni": 0,
        "fakultetlar_soni": 0,
        "professor_soni": 0,

        # --- Narxlash ---
        "eng_arzon_kontrakt": 0,
        "eng_qimmat_kontrakt": 0,
        "ortacha_kontrakt": 0,
        "grant_orinlar_soni": 0,
        "narx_farqi_foiz": 0,               # BUI ga nisbatan +/- %
        "chegirma_bor": False,
        "chegirma_turi": "",
        "bolib_tolash_bor": False,

        # --- Sifat ---
        "reyting_bali": 0,                  # 1-10
        "ish_bilan_bandlik": 0,              # %
        "xalqaro_hamkorliklar": 0,
        "ikki_diplom_bor": False,
        "yotoqxona_bor": False,
        "kampus_sifati": 0,                  # 1-10
        "talaba_qoniqishi": 0,               # 1-10

        # --- Marketing ---
        "marketing_faolligi": 0,             # 1-10
        "marketing_byudjeti_taxmin": 0,
        "telegram_obunchilar": 0,
        "instagram_followers": 0,
        "youtube_subscribers": 0,
        "tiktok_followers": 0,
        "tv_reklama_bor": False,
        "billboard_bor": False,
        "agentlar_bor": False,
        "ochiq_eshiklar_bor": False,
        "online_qabul_bor": False,
        "influencer_hamkorlik": False,

        # --- SWOT ---
        "kuchli_tomonlari": [],
        "zaif_tomonlari": [],
        "imkoniyatlari": [],
        "xavflari": [],

        # --- BUI bilan umumiy ---
        "umumiy_yonalishlar": [],            # BUI bilan raqobat yo'nalishlari
        "talaba_oqimasi": "",                # "BUI dan ketadi" / "BUI ga keladi"
        "talaba_oqimasi_soni": 0,            # taxminan
        "narx_strategiyasi": "",             # "arzon" / "premium" / "o'rtacha"

        # --- Kelajak ---
        "kengayish_rejalari": "",            # "yangi bino" / "yangi yo'nalish"
        "xavf_darajasi_bui_uchun": 0,        # 1-10
    },
    # ... KAMIDA 8-15 ta raqobatchi kiritiladi
]

# ══════════════════════════════════════════════════════════════════════
# 7-BO'LIM: INFRATUZILMA VA SHAROITLAR (75 parametr)
# ══════════════════════════════════════════════════════════════════════
INFRATUZILMA = {
    # --- Kampus ---
    "kampus_maydoni_ga": 0,
    "kampus_yoshi_yil": 0,
    "binolar_soni": 0,
    "yangi_bino_bor": False,
    "remont_qilingan": False,
    "remont_yili": 0,
    "arxitektura_sifati": 0,             # 1-10, zamonaviy ko'rinish

    # --- O'quv ---
    "auditoriyalar_soni": 0,
    "katta_auditoriya_100_plus": 0,
    "smart_auditoriya_soni": 0,          # projektor, smart board
    "laboratoriyalar_soni": 0,
    "kompyuter_xonalar_soni": 0,
    "kompyuterlar_soni": 0,
    "kompyuter_yoshi_ortacha": 0,        # yilda
    "maxsus_laboratoriya": [],            # ["fizika", "kimyo", "robototexnika"]
    "coworking_space_bor": False,
    "coworking_orinlar": 0,

    # --- Internet ---
    "internet_tezligi_mbps": 0,
    "wifi_bor": True,
    "wifi_qoplami_foiz": 0,              # kampusning nechtasida wifi bor
    "wifi_tezligi_mbps": 0,

    # --- Kutubxona ---
    "kutubxona_bor": True,
    "kutubxona_orinlar": 0,
    "kitoblar_soni": 0,
    "elektron_kutubxona_bor": False,
    "elektron_kitoblar_soni": 0,
    "24_soat_ochiq": False,
    "o_quv_zallar_soni": 0,

    # --- Yotoqxona ---
    "yotoqxona_bor": False,
    "yotoqxona_binolar_soni": 0,
    "yotoqxona_orinlar_soni": 0,
    "yotoqxona_narxi_oylik": 0,
    "yotoqxona_sifati": 0,               # 1-10
    "yotoqxona_masofasi_km": 0,
    "yotoqxona_xonada_necha_kishi": 0,
    "yotoqxona_wifi": False,
    "yotoqxona_kir_yuvish": False,
    "yotoqxona_oshxona": False,
    "yotoqxona_qorovul": False,
    "yotoqxona_talablar": "",             # "faqat viloyatdan kelganlar"

    # --- Ovqatlanish ---
    "oshxona_bor": True,
    "oshxona_orinlar": 0,
    "oshxona_sifati": 0,
    "ortacha_tushlik_narxi": 0,
    "kafe_bor": False,
    "avtomat_ichimlik_bor": False,
    "halol_taom_kafolati": True,

    # --- Transport ---
    "universitet_avtobusi": False,
    "avtobus_marshrut_soni": 0,
    "metro_yaqin": False,
    "eng_yaqin_avtobus_bekat_m": 0,
    "eng_yaqin_metro_bekat_m": 0,
    "parking_bor": True,
    "parking_orinlar": 0,
    "velosiped_parking": False,

    # --- Sport ---
    "sport_zal_bor": False,
    "sport_zal_maydoni": 0,
    "stadion_bor": False,
    "suzish_havza_bor": False,
    "tennis_kort_bor": False,
    "futbol_maydon_bor": False,
    "basketbol_maydon_bor": False,
    "sport_seksiyalar": [],               # ["futbol", "kurash", "suzish"]
    "sport_yutuqlari": [],

    # --- Madaniyat va ijtimoiy ---
    "madaniyat_markazi_bor": False,
    "konferens_zal_bor": False,
    "konferens_zal_sigimi": 0,
    "talabalar_klublari_soni": 0,
    "talabalar_klublari": [],             # ["IT club", "English club", "Debat"]
    "masjid_yaqin": False,
    "masjid_masofasi_m": 0,

    # --- Tibbiy ---
    "tibbiy_punkt_bor": False,
    "psixolog_bor": False,
    "apteka_yaqin": False,

    # --- Xavfsizlik ---
    "kuzatuv_kameralar": True,
    "kameralar_soni": 0,
    "qorovul_bor": True,
    "qorovul_soni": 0,
    "kirish_kartasi_bor": False,
    "yong_in_signalizatsiya": True,

    # --- Atrof muhit ---
    "yashil_hudud_bor": True,
    "yashil_hudud_foiz": 0,              # kampusning nechtasi
    "dokon_yaqin": True,
    "bank_yaqin": True,
    "pochta_yaqin": False,
}

# ══════════════════════════════════════════════════════════════════════
# 8-BO'LIM: XALQARO HAMKORLIK (40 parametr)
# ══════════════════════════════════════════════════════════════════════
XALQARO = {
    "xorijiy_hamkor_soni": 0,
    "hamkor_universitetlar": [
        # {
        #     "nomi": "",
        #     "davlat": "",
        #     "shahar": "",
        #     "reyting_pozitsiya": 0,          # QS/THE reytingida
        #     "hamkorlik_turi": "",             # "ikki diplom" / "almashinuv" / "tadqiqot"
        #     "hamkorlik_boshlanish": "",
        #     "yilda_yuborilgan_talaba": 0,
        #     "yilda_kelgan_talaba": 0,
        #     "faol": True,
        # }
    ],

    # --- Dasturlar ---
    "ikki_diplom_dasturlari_soni": 0,
    "ikki_diplom_yonalishlar": [],
    "almashinuv_dasturi_bor": False,
    "almashinuv_yilda_talaba": 0,
    "almashinuv_davomiyligi": "",            # "1 semestr" / "1 yil"
    "yozgi_maktab_bor": False,
    "yozgi_maktab_qaerda": [],
    "online_hamkorlik_bor": False,           # onlayn birgalikdagi kurslar

    # --- Xorijiy talabalar ---
    "xorijiy_talabalar_soni": 0,
    "xorijiy_talaba_davlatlar": [],
    "xorijiy_talaba_kvota": 0,
    "xorijiy_talaba_narxi": 0,              # $ da

    # --- Xorijiy professor ---
    "xorijiy_professor_soni": 0,
    "xorijiy_professor_davlatlar": [],
    "visiting_professor_yilda": 0,

    # --- Grantlar ---
    "xorijiy_grant_dasturlari": [],          # ["Erasmus+", "KOICA", "JICA"]
    "xorijiy_grant_yilda_summa": 0,          # $ da
    "xorijiy_grant_talabalar": 0,

    # --- Sertifikatlar ---
    "xalqaro_sertifikat_markazlari": [],     # ["IELTS", "TOEFL", "Cisco", "Huawei"]
    "xorijiy_amaliyot_imkoniyati": False,
    "xorijiy_amaliyot_davlatlar": [],
    "xorijiy_konferensiya_yilda": 0,

    # --- Til ---
    "ingliz_tilida_dasturlar": 0,
    "rus_tilida_dasturlar": 0,
    "til_tayyorlov_kursi_bor": False,
    "til_kursi_narxi": 0,
    "bepul_til_kursi_bor": False,

    # --- Marketing qiymati ---
    "xalqaro_brend_tasiri": 0,              # 1-10, abituriyent uchun
    "ikki_diplom_tasiri": 0,                # 1-10, qaror omili sifatida
}

# ══════════════════════════════════════════════════════════════════════
# 9-BO'LIM: QABUL JARAYONI (60 parametr)
# ══════════════════════════════════════════════════════════════════════
QABUL_JARAYONI = {
    # --- Vaqt jadvali ---
    "qabul_boshlanish": "",
    "qabul_tugash": "",
    "early_bird_boshlanish": "",
    "early_bird_tugash": "",
    "asosiy_qabul_boshlanish": "",
    "asosiy_qabul_tugash": "",
    "kech_qabul_boshlanish": "",
    "kech_qabul_tugash": "",
    "darslar_boshlanishi": "",
    "orientatsiya_hafta_bor": False,
    "orientatsiya_davomiyligi_kun": 0,

    # --- Bosqichlar ---
    "online_ariza_bor": True,
    "dtm_ball_talab": True,
    "ichki_imtihon_bor": False,
    "ichki_imtihon_turi": "",                # "test" / "suhbat" / "portfolio"
    "suhbat_bor": False,
    "suhbat_turi": "",                       # "individual" / "guruhli"
    "portfolio_talab": False,
    "motivatsion_xat_talab": False,
    "tavsiyatoma_talab": False,

    # --- Hujjatlar ---
    "hujjatlar_royxati": [],
    "hujjat_nusxa_kerak": False,
    "apostil_kerak": False,
    "tarjima_kerak": False,
    "tibbiy_malumotnoma_kerak": True,
    "foto_kerak": True,
    "foto_talablar": "",                     # "3x4, 4 dona"

    # --- Qulaylik ---
    "ariza_topshirish_vaqti_daqiqa": 0,
    "javob_berish_vaqti_soat": 0,
    "javob_berish_vaqti_kun": 0,
    "avtomatik_qabul_xabarnoma": False,      # SMS/email
    "qabul_natija_online": True,
    "hujjat_yuklab_olish_mumkin": True,
    "onlayn_tolov_mumkin": True,

    # --- Hujjat topshirish usullari ---
    "online_topshirish": True,
    "shaxsan_topshirish": True,
    "pochta_topshirish": False,
    "mobil_ilova_topshirish": False,
    "telegram_bot_topshirish": False,

    # --- Call center va qo'llab-quvvatlash ---
    "call_center_bor": True,
    "call_center_xodimlar": 0,
    "call_center_ish_vaqti": "",
    "call_center_tillar": [],                # ["o'zbek", "rus", "ingliz"]
    "whatsapp_qollab_quvvatlash": False,
    "telegram_qollab_quvvatlash": False,
    "chatbot_bor": False,
    "ai_chatbot_bor": False,
    "ortacha_javob_vaqti_min": 0,            # daqiqada

    # --- Qabul markazi ---
    "qabul_markazi_bor": True,
    "qabul_markazi_maydoni": 0,              # m2
    "qabul_markazi_sifati": 0,               # 1-10
    "kutish_zonasi_bor": False,
    "bolalar_xonasi_bor": False,
    "sovuq_suv_choy_bor": False,

    # --- Hududiy vakilliklar ---
    "hududiy_vakilliklar_soni": 0,
    "hududiy_vakilliklar": [],               # [{"shahar": "", "manzil": "", "xodimlar": 0}]

    # --- Admin jamoa ---
    "qabul_xodimlari_jami": 0,
    "qabul_boshligi": "",
    "qabul_xodim_tajribasi_ortacha_yil": 0,
    "qabul_xodim_tili": [],

    # --- Funnel tracking ---
    "crm_tizimi_bor": False,
    "crm_nomi": "",
    "lead_scoring_bor": False,
    "avtomatik_follow_up_bor": False,
    "follow_up_necha_marta": 0,
    "follow_up_kanallari": [],               # ["sms", "telefon", "email"]
    "abandoned_ariza_qaytarish": False,       # tashlab ketgan arizalarni qaytarish
}

# ══════════════════════════════════════════════════════════════════════
# 10-BO'LIM: MOLIYAVIY MA'LUMOTLAR (55 parametr)
# ══════════════════════════════════════════════════════════════════════
MOLIYA = {
    # --- Daromadlar (o'tgan yil, so'mda) ---
    "otgan_yil_jami_daromad": 0,
    "kontrakt_daromadi_bakalavr": 0,
    "kontrakt_daromadi_magistr": 0,
    "kontrakt_daromadi_sirtqi": 0,
    "grant_moliyalashtirish": 0,
    "qoshimcha_kurslar_daromad": 0,
    "ijara_daromad": 0,
    "xizmatlar_daromad": 0,                  # laboratoriya, sertifikat
    "donor_homiylar_daromad": 0,
    "boshqa_daromadlar": 0,

    # --- Xarajatlar ---
    "jami_xarajat": 0,
    "ish_haqi_fondi": 0,
    "professor_ortacha_maosh": 0,
    "marketing_xarajat": 0,
    "kommunal_xarajat": 0,
    "ijara_xarajat": 0,
    "infra_ta_mirlash": 0,
    "texnologiya_xarajat": 0,
    "kutubxona_xarajat": 0,
    "sport_madaniyat_xarajat": 0,
    "xavfsizlik_xarajat": 0,
    "boshqa_xarajat": 0,

    # --- Unit economics ---
    "bir_talaba_ortacha_daromad": 0,         # yillik
    "bir_talaba_ortacha_xarajat": 0,
    "bir_talaba_foyda": 0,
    "cac_ortacha": 0,                        # customer acquisition cost
    "cac_kanal_boyicha": {},                 # {"telegram": 0, "agent": 0, "tv": 0}
    "ltv_ortacha": 0,                        # lifetime value (4 yil)
    "ltv_cac_nisbati": 0.0,

    # --- Qarzdorlik ---
    "debitor_qarzdorlik": 0,                 # to'lamagan talabalar
    "debitor_foiz": 0,                       # % to'lamaydigan
    "yig_ib_olingan_foiz": 0,               # undirish %
    "ochirilgan_qarzdorlik": 0,

    # --- Maqsadlar 2026 ---
    "maqsad_jami_qabul": 0,
    "maqsad_daromad": 0,
    "maqsad_foyda": 0,
    "marketing_byudjet_2026": 0,
    "chegirma_byudjet_2026": 0,
    "stipendiya_byudjet_2026": 0,
    "infra_investitsiya_2026": 0,
    "yangi_xodim_byudjet_2026": 0,

    # --- Cheklovlar ---
    "min_kontrakt_narx": 0,                  # bundan arzon bo'lmaydi
    "max_talaba_sigim": 0,                   # infra ko'taradi
    "maqsad_foyda_margin_foiz": 0,
    "max_marketing_byudjet": 0,
    "max_chegirma_foiz": 0,
    "max_stipendiya_foiz_daromad": 0,        # daromadning max % stipendiyaga

    # --- Investorlar / ta'sischilar ---
    "tasischi_turi": "",                     # "xususiy" / "fond" / "davlat"
    "tasischi_kutishi": "",                  # "foyda" / "ijtimoiy" / "aralash"
    "investor_bor": False,
    "investor_kutgan_roi": 0,                # %
}

# ══════════════════════════════════════════════════════════════════════
# 11-BO'LIM: HUDUDIY BOZOR (55 parametr)
# ══════════════════════════════════════════════════════════════════════
HUDUDIY_BOZOR = {
    # --- Buxoro viloyati ---
    "buxoro_aholisi": 0,
    "buxoro_17_18_yosh": 0,
    "buxoro_bitiruvchilar_2026": 0,
    "buxoro_universitetlar_soni": 0,
    "buxoro_uni_jami_orinlar": 0,
    "buxoro_ortacha_daromad": 0,
    "buxoro_ishsizlik_foiz": 0,
    "buxoro_oliy_talim_foiz": 0,             # aholining oliy ta'limli %
    "buxoro_asosiy_sanoat": [],
    "buxoro_asosiy_ish_beruvchilar": [],
    "buxoro_talim_tashkil_soni": 0,          # barcha ta'lim muassasalari

    # --- O'zbekiston ---
    "uzb_jami_aholi": 0,
    "uzb_17_18_yosh": 0,
    "uzb_bitiruvchilar_2026": 0,
    "uzb_universitetlar_soni": 0,
    "uzb_jami_talaba_orinlar": 0,
    "uzb_oliy_talim_qamrovi_foiz": 0,        # % yoshlar oliy ta'limda
    "uzb_ortacha_kontrakt_narx": 0,
    "uzb_talim_inflyatsiya_foiz": 0,
    "uzb_ortacha_maosh": 0,
    "uzb_minimum_ish_haqi": 0,

    # --- Viloyatlar bo'yicha potentsial ---
    "viloyat_potentsial": {
        "Buxoro": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Samarqand": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Navoiy": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Qashqadaryo": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Surxondaryo": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Toshkent_shahar": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Toshkent_viloyat": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Xorazm": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Fargona": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Andijon": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Namangan": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Jizzax": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Sirdaryo": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
        "Qoraqalpogiston": {"aholi_17_18": 0, "universitetlar": 0, "raqobat": 0, "transport": 0, "BUI_tanilganlik": 0},
    },

    # --- Bozor trendlari ---
    "trend_online_talim_osish": 0,           # % yillik
    "trend_xorijga_ketish_osish": 0,         # %
    "trend_nodavlat_uni_osish": 0,           # %
    "trend_it_yonalish_talabi": 0,           # 1-10
    "trend_biznes_yonalish_talabi": 0,       # 1-10
    "trend_tibbiyot_talabi": 0,              # 1-10
    "trend_pedagogika_talabi": 0,            # 1-10
    "trend_qishloq_xojalik_talabi": 0,       # 1-10
    "trend_turizm_talabi": 0,                # 1-10
}

# ══════════════════════════════════════════════════════════════════════
# 12-BO'LIM: MAVSUMIYLIK VA VAQT (35 parametr)
# ══════════════════════════════════════════════════════════════════════
MAVSUMIYLIK = {
    # --- Oylik ariza faolligi (0-100) ---
    "oylik_ariza_faolligi": {
        "yanvar": 0, "fevral": 0, "mart": 0,
        "aprel": 0, "may": 0, "iyun": 0,
        "iyul": 0, "avgust": 0, "sentyabr": 0,
        "oktyabr": 0, "noyabr": 0, "dekabr": 0,
    },

    # --- Haftalik pattern ---
    "haftalik_faollik": {
        "dushanba": 0, "seshanba": 0, "chorshanba": 0,
        "payshanba": 0, "juma": 0, "shanba": 0, "yakshanba": 0,
    },

    # --- Soatlik pattern ---
    "eng_faol_soat_boshlanish": 0,           # masalan 10
    "eng_faol_soat_tugash": 0,               # masalan 16

    # --- Muhim sanalar ---
    "dtm_imtihon_sanasi": "",
    "dtm_natija_sanasi": "",
    "maktab_bitirish_sanasi": "",
    "maktab_ohirgi_qongiroq": "",
    "attestat_berilish_sanasi": "",
    "bayramlar": [],                         # [{"nomi": "Navro'z", "sana": "03-21", "tasiri": "past"}]
    "ramadan_boshlanish": "",
    "ramadan_tugash": "",
    "qurbon_hayit": "",

    # --- Mavsumiy ta'sir omillari ---
    "yozgi_kanikul_tasiri": 0,               # 1-10
    "armiya_chaqiruv_oyi": "",
    "armiya_chaqiruv_tasiri": 0,             # 1-10
    "mehnat_migratsiya_oyi": [],             # yoshlar xorijga ketish oylari
    "ob_havo_tasiri": 0,                     # 1-10, issiq yozda kelish kamayadi
}

# ══════════════════════════════════════════════════════════════════════
# 13-BO'LIM: TEXNOLOGIK IMKONIYATLAR (40 parametr)
# ══════════════════════════════════════════════════════════════════════
TEXNOLOGIYA = {
    # --- Qabul tizimi ---
    "crm_bor": False,
    "crm_nomi": "",
    "crm_narxi_oylik": 0,
    "online_ariza_tizimi": "",
    "ariza_tizimi_custom": False,            # o'zimiz yozganmiz
    "avtomatik_javob_sms": False,
    "avtomatik_javob_email": False,
    "avtomatik_javob_telegram": False,
    "lead_nurturing_bor": False,
    "a_b_test_landing": False,
    "heatmap_analytics_bor": False,

    # --- Analitika ---
    "google_analytics_bor": False,
    "yandex_metrika_bor": False,
    "facebook_pixel_bor": False,
    "tiktok_pixel_bor": False,
    "utm_tracking_bor": False,
    "konversiya_tracking_bor": False,
    "dashboard_bor": False,
    "dashboard_nomi": "",
    "data_driven_qaror_qilish": 0,           # 1-10

    # --- LMS ---
    "lms_bor": False,
    "lms_nomi": "",
    "lms_talabalar": 0,
    "online_darslar_bor": False,
    "video_darslar_soni": 0,
    "zoom_teams_bor": False,

    # --- Mobil ---
    "mobil_ilova_bor": False,
    "mobil_ilova_nomi": "",
    "mobil_ilova_downloads": 0,
    "mobil_ilova_reyting": 0.0,

    # --- Chatbot ---
    "chatbot_bor": False,
    "ai_chatbot_bor": False,
    "chatbot_platforma": "",                 # "Telegram" / "Web" / "WhatsApp"
    "chatbot_oylik_suhbatlar": 0,
    "chatbot_javob_aniqlik": 0,              # %

    # --- Avtomatlashtirish ---
    "marketing_automation_bor": False,
    "email_automation_bor": False,
    "sms_automation_bor": False,
    "retargeting_bor": False,
    "personalizatsiya_bor": False,
}

# ══════════════════════════════════════════════════════════════════════
# 14-BO'LIM: TASHQI OMILLAR (35 parametr)
# ══════════════════════════════════════════════════════════════════════
TASHQI_OMILLAR = {
    # --- Iqtisodiy ---
    "inflyatsiya_foiz": 0,
    "dollar_kursi": 0,
    "dollar_kursi_otgan_yil": 0,
    "dollar_trend": "",                      # "o'sish" / "tushish" / "barqaror"
    "ishsizlik_foiz": 0,
    "yoshlar_ishsizlik_foiz": 0,
    "ortacha_maosh_uzb": 0,
    "ortacha_maosh_buxoro": 0,
    "iqtisodiy_osish_foiz": 0,               # GDP growth
    "kredit_stavka_ortacha": 0,              # bank kredit %

    # --- Siyosiy va qonunchilik ---
    "yangi_talim_qonunlari": [],
    "grant_siyosati_ozgarishi": "",
    "litsenziya_talablari": "",
    "soliq_imtiyozlari_bor": False,
    "nodavlat_uni_qollab_quvvatlash": "",    # davlat pozitsiyasi
    "xorijiy_uni_filiallar_siyosati": "",

    # --- Demografik ---
    "tug_ilish_trendi": "",
    "yoshlar_emigratsiya": "",
    "xorijda_oqish_trendi": "",
    "xorijda_oqish_foizi": 0,               # % abituriyentlardan
    "mashhur_xorijiy_mamlakatlar": [],       # ["Rossiya", "Turkiya", "Koreya"]
    "qaytish_trendi": "",                    # xorijdan qaytib kelish

    # --- Texnologik trendlar ---
    "ai_tasiri_talimga": 0,                  # 1-10
    "online_talim_osishi": 0,                # % yillik
    "digital_savodxonlik_osishi": 0,         # 1-10
    "yangi_kasblar_paydo_bolishi": [],       # ["AI engineer", "Data analyst"]

    # --- Ijtimoiy ---
    "oliy_talim_qadri_osishi": 0,            # 1-10
    "diploma_qadrsizlanishi": 0,             # 1-10, "diplom kerak emas" trendi
    "skill_based_yollash_trendi": 0,         # 1-10
    "startup_madaniyati_osishi": 0,          # 1-10

    # --- Force majeure ---
    "pandemiya_xavfi": 0,                    # 1-10
    "tabiiy_ofat_xavfi": 0,                  # 1-10
    "siyosiy_barqarorlik": 0,                # 1-10 (10=barqaror)
}

# ══════════════════════════════════════════════════════════════════════
# 15-BO'LIM: KADRLAR VA JAMOA (50 parametr)
# ══════════════════════════════════════════════════════════════════════
KADRLAR = {
    # --- Umumiy ---
    "jami_xodimlar": 0,
    "professor_oqituvchi": 0,
    "ma_muriy_xodim": 0,
    "texnik_xodim": 0,
    "xavfsizlik_xodim": 0,

    # --- Professor sifati ---
    "professor_phd_foiz": 0,
    "professor_dsc_foiz": 0,
    "professor_xorijiy_tajriba": 0,          # % xorijda o'qigan/ishlagan
    "professor_sanoat_tajriba": 0,           # % sanoatda ishlagan
    "professor_yoshlar_foiz": 0,             # 35 yoshgacha %
    "professor_ortacha_yoshi": 0,
    "professor_ilmiy_maqolalar_ortacha": 0,
    "professor_scopus_bor_foiz": 0,          # % Scopus'da maqolasi bor

    # --- Maosh ---
    "professor_min_maosh": 0,
    "professor_max_maosh": 0,
    "professor_ortacha_maosh": 0,
    "admin_ortacha_maosh": 0,
    "xodim_qoniqishi": 0,                   # 1-10
    "xodim_ketish_foiz": 0,                  # % yillik turnover

    # --- Qabul jamoasi ---
    "qabul_jamoa_soni": 0,
    "qabul_jamoa_tajriba_yil": 0,
    "qabul_jamoa_tillar": [],
    "qabul_boshligi_tajriba": 0,
    "qabul_jamoa_motivatsiya": 0,            # 1-10
    "qabul_jamoa_kpi_bor": False,
    "qabul_jamoa_bonus_tizimi": False,

    # --- Marketing jamoasi ---
    "marketing_jamoa_soni": 0,
    "marketing_boshligi_tajriba": 0,
    "smm_mutaxassis_bor": False,
    "dizayner_bor": False,
    "videograf_bor": False,
    "copywriter_bor": False,
    "analitik_bor": False,
    "seo_mutaxassis_bor": False,

    # --- IT jamoasi ---
    "it_jamoa_soni": 0,
    "veb_dasturchi_bor": False,
    "tizim_admin_bor": False,

    # --- Talabalar bilan ishlash ---
    "kurator_soni": 0,
    "kurator_talaba_nisbati": 0,
    "psixolog_bor": False,
    "kariyer_markazi_bor": False,
    "kariyer_xodimlar": 0,
    "talaba_dekani_bor": False,

    # --- Trening ---
    "xodim_malaka_oshirish_bor": False,
    "yillik_trening_soat": 0,
    "xorijiy_trening_bor": False,
}

# ══════════════════════════════════════════════════════════════════════
# 16-BO'LIM: BITIRUVCHILAR VA ALUMNI (30 parametr)
# ══════════════════════════════════════════════════════════════════════
ALUMNI = {
    "jami_bitiruvchilar": 0,
    "alumni_assotsiatsiya_bor": False,
    "alumni_telegram_guruh": "",
    "alumni_guruh_azolari": 0,

    # --- Ish bilan bandlik ---
    "6_oy_ichida_ishga_joylashgan": 0,       # %
    "1_yil_ichida_ishga_joylashgan": 0,      # %
    "mutaxassislik_boyicha_ishlayotgan": 0,  # %
    "xorijda_ishlayotgan": 0,                # %
    "tadbirkorlik_qilayotgan": 0,            # %
    "ortacha_maosh_1_yil": 0,
    "ortacha_maosh_3_yil": 0,
    "ortacha_maosh_5_yil": 0,
    "eng_yuqori_maosh": 0,

    # --- Mashhur bitiruvchilar ---
    "mashhur_bitiruvchilar": [],              # [{"ismi": "", "lavozimi": "", "kompaniya": ""}]
    "success_story_soni": 0,
    "media_da_chiqqan_bitiruvchi": 0,

    # --- Alumni ta'siri qabulga ---
    "alumni_tavsiya_foiz": 0,                # nechtasi BUI'ni tavsiya qiladi
    "alumni_agent_sifatida": 0,              # nechta alumni agent ishlaydi
    "alumni_homiylik": 0,                    # so'mda, yillik
    "alumni_mentorlik_bor": False,
    "alumni_stajировка_bor": False,          # alumni kompaniyasida amaliyot

    # --- Ish beruvchi aloqalar ---
    "ish_beruvchi_hamkorlar_soni": 0,
    "memorandum_soni": 0,
    "ish_yarmarkasi_yilda": 0,
    "to_gridan_yollash_bor": False,          # kompaniya to'g'ridan-to'g'ri oladi
    "ish_beruvchi_qoniqishi": 0,             # 1-10
}

# ══════════════════════════════════════════════════════════════════════
# 17-BO'LIM: TALABA HAYOTI VA TAJRIBASI (40 parametr)
# ══════════════════════════════════════════════════════════════════════
TALABA_HAYOTI = {
    # --- Akademik ---
    "dars_jadvali_qulayligi": 0,             # 1-10
    "dars_soatlari_kuniga": 0,
    "mustaqil_ish_soatlari": 0,
    "kurs_ishi_loyiha_soni": 0,              # semestrda
    "imtihon_turi": "",                      # "test" / "og'zaki" / "aralash"
    "akademik_qollab_quvvatlash": 0,         # 1-10
    "tutorlik_bor": False,
    "qo_shimcha_darslar_bor": False,

    # --- Ijtimoiy ---
    "talaba_klublari_faolligi": 0,           # 1-10
    "sport_musobaqalar_yilda": 0,
    "madaniy_tadbirlar_yilda": 0,
    "volontorlik_imkoniyati": False,
    "talaba_parlamenti_bor": False,
    "talaba_gazeta_bor": False,
    "startap_inkubator_bor": False,
    "hackathon_yilda": 0,

    # --- Amaliy tajriba ---
    "stajировка_majburiy": False,
    "stajировка_semestr": 0,                # qaysi semestrda
    "stajировка_kompaniyalar": [],
    "loyiha_asosida_oqitish": False,
    "real_buyurtmachi_loyiha": False,
    "laboratoriya_ishlar_foiz": 0,           # % darslarning

    # --- Qo'llab-quvvatlash ---
    "stipendiya_oluvchilar_foiz": 0,
    "ish_topish_yordami": 0,                 # 1-10
    "kariyer_konsultatsiya": False,
    "cv_yozish_yordami": False,
    "intervyu_tayyorgarlik": False,

    # --- Qoniqish ko'rsatkichlari ---
    "umumiy_qoniqish": 0,                   # 1-10
    "talim_sifati_qoniqish": 0,
    "infra_qoniqish": 0,
    "ovqat_qoniqish": 0,
    "transport_qoniqish": 0,
    "xavfsizlik_qoniqish": 0,
    "admin_xizmat_qoniqish": 0,
    "internet_qoniqish": 0,
    "oqituvchi_qoniqish": 0,

    # --- Muammolar ---
    "eng_kop_shikoyat": [],                  # ["internet sekin", "oshxona yomon"]
    "talaba_ketish_sabablari": [],            # ["moliyaviy", "sifat past", "ko'chirish"]
    "birinchi_semestr_ketish_foiz": 0,       # %
    "ikkinchi_yil_ketish_foiz": 0,
}

# ══════════════════════════════════════════════════════════════════════
# 18-BO'LIM: BREND VA REPUTATSIYA (35 parametr)
# ══════════════════════════════════════════════════════════════════════
BREND = {
    # --- Brend bilish darajasi ---
    "tanilganlik_buxoro": 0,                 # % Buxoroliklar biladi
    "tanilganlik_uzb": 0,                    # % O'zbekistonda biladi
    "tanilganlik_maqsadli": 0,               # % abituriyentlar biladi
    "brend_assosiatsiya": [],                # ["zamonaviy", "arzon", "yangi"]
    "raqobatchilardan_farqi": "",            # USP
    "slogan": "",
    "brend_rangi": "",
    "brend_qadriyatlari": [],                # ["innovatsiya", "sifat", "qulay narx"]

    # --- Online reputatsiya ---
    "google_reyting": 0.0,
    "google_sharhlar_soni": 0,
    "google_salbiy_foiz": 0,
    "yandex_reyting": 0.0,
    "2gis_reyting": 0.0,
    "talim_portal_reyting": 0.0,             # uzbattest, qabul.uz kabi
    "shikoyat_saytlari_bor": False,          # salbiy kontentlar
    "salbiy_yangiliklar": [],

    # --- Media ---
    "media_eslatish_oyiga": 0,               # OAVda necha marta
    "media_kanallari": [],                   # ["Kun.uz", "Gazeta.uz"]
    "press_reliz_yilda": 0,
    "media_byudjeti": 0,

    # --- Ijtimoiy isbotlar ---
    "video_testimonial_soni": 0,
    "yozma_testimonial_soni": 0,
    "case_study_soni": 0,
    "mukofotlar_yutuqlar": [],
    "davlat_mukofotlari": [],
    "xalqaro_mukofotlar": [],

    # --- Krizis boshqaruvi ---
    "krizis_boshqaruv_rejasi_bor": False,
    "salbiy_pr_tajribasi": [],
    "salbiy_pr_ta_siri": 0,                 # 1-10
    "reputatsiya_monitoring_bor": False,
    "brand_book_bor": False,
}

# ══════════════════════════════════════════════════════════════════════
# 19-BO'LIM: HAMKORLIKLAR VA SANOAT ALOQALARI (30 parametr)
# ══════════════════════════════════════════════════════════════════════
HAMKORLIKLAR = {
    "sanoat_hamkorlar_soni": 0,
    "sanoat_hamkorlar": [
        # {
        #     "nomi": "",
        #     "sohasi": "",
        #     "hamkorlik_turi": "",            # "stajировка" / "loyiha" / "grant" / "ish"
        #     "yilda_talaba_oladi": 0,
        #     "moliyaviy_yordam": 0,
        # }
    ],
    "davlat_tashkilotlar_hamkor": [],
    "nkm_hamkorlar": [],                     # nodavlat notijorat
    "xalqaro_tashkilot_hamkor": [],          # UN, USAID kabi

    # --- Amaliyot ---
    "stajировка_hamkorlar_soni": 0,
    "stajировка_joylari_soni": 0,            # jami nechta o'rin
    "tolovli_stajировка_foiz": 0,            # % to'lovli

    # --- Tadqiqot ---
    "tadqiqot_laboratoriya_soni": 0,
    "tadqiqot_loyiha_soni": 0,
    "tadqiqot_byudjeti": 0,
    "patent_soni": 0,
    "ilmiy_maqola_yilda": 0,
    "scopus_maqola_yilda": 0,

    # --- Texnopark ---
    "texnopark_bor": False,
    "biznes_inkubator_bor": False,
    "startap_loyiha_soni": 0,
    "startap_muvaffaqiyat_soni": 0,

    # --- IT kompaniyalar ---
    "it_hamkorlar": [],
    "it_sertifikat_markazlari": [],          # Cisco, Huawei, Microsoft
    "it_bootcamp_bor": False,

    # --- Mehmonlar ---
    "mehmon_maruza_yilda": 0,
    "masterclass_yilda": 0,
    "sanoat_konferensiya_yilda": 0,
}

# ══════════════════════════════════════════════════════════════════════
# 20-BO'LIM: QONUNCHILIK VA MUVOFIQLIK (20 parametr)
# ══════════════════════════════════════════════════════════════════════
QONUNCHILIK = {
    "litsenziya_amal_qiladi": True,
    "litsenziya_tugash_sanasi": "",
    "akkreditatsiya_tugash": "",
    "yangi_akkreditatsiya_rejalangan": "",
    "soliq_rejimi": "",                      # qanday soliq to'laydi
    "soliq_imtiyoz_bor": False,
    "davlat_tekshiruv_soni_yilda": 0,
    "jarima_olgan": False,
    "jarima_sababi": "",
    "malumot_himoyasi_bor": False,           # GDPR analog
    "talaba_shartnoma_standarti_bor": True,
    "ichki_tartib_qoidalari_bor": True,
    "akademik_halollik_siyosati": False,
    "anti_korrupsiya_siyosati": False,
    "gender_tenglik_siyosati": False,
    "nogironlar_qulayligi": False,
    "ekologik_siyosat_bor": False,
    "sifat_boshqaruv_tizimi": "",            # "ISO 9001" kabi
    "ichki_audit_bor": False,
    "tashqi_audit_bor": False,
}

# ══════════════════════════════════════════════════════════════════════
# 21-BO'LIM: QABUL FUNNEL METRIKALARI (30 parametr)
# ══════════════════════════════════════════════════════════════════════
FUNNEL = {
    # --- Bosqichlar ---
    "xabardorlik_soni": 0,                   # BUI haqida eshitgan
    "qiziqish_soni": 0,                      # saytga kirgan
    "ariza_boshlagan_soni": 0,               # ariza boshlagan
    "ariza_tugatgan_soni": 0,                # ariza tugatgan
    "qabul_qilingan_soni": 0,               # qabul qilingan
    "shartnoma_imzolagan_soni": 0,
    "tolov_qilgan_soni": 0,
    "darsga_kelgan_soni": 0,
    "1_semestr_tugatgan_soni": 0,
    "2_yil_davom_soni": 0,
    "bitirgan_soni": 0,

    # --- Konversiyalar (%) ---
    "xabardorlik_qiziqish": 0,
    "qiziqish_ariza": 0,
    "ariza_boshlash_tugatish": 0,
    "ariza_qabul": 0,
    "qabul_shartnoma": 0,
    "shartnoma_tolov": 0,
    "tolov_dars": 0,
    "dars_1semestr": 0,
    "semestr_2yil": 0,
    "yil2_bitirish": 0,

    # --- Tashlab ketish sabablari (har bosqichda) ---
    "ariza_tashlab_ketish_sabab": [],        # ["murakkab", "sekin", "hujjat ko'p"]
    "qabul_tashlab_ketish_sabab": [],        # ["narx qimmat", "boshqa uni tanladi"]
    "tolov_tashlab_ketish_sabab": [],        # ["pul yo'q", "qaror o'zgardi"]
    "dars_tashlab_ketish_sabab": [],         # ["kutgandek emas", "moliyaviy"]

    # --- Vaqt metrikalari ---
    "ortacha_ariza_vaqti_daqiqa": 0,
    "ortacha_qaror_vaqti_kun": 0,            # arizadan to'lovgacha
    "eng_tez_qaror_kun": 0,
    "eng_sekin_qaror_kun": 0,
}

# ══════════════════════════════════════════════════════════════════════
# 22-BO'LIM: RAQAMLI AKTIVLAR VA LANDING SAHIFALAR (25 parametr)
# ══════════════════════════════════════════════════════════════════════
RAQAMLI_AKTIVLAR = {
    # --- Veb-sayt ---
    "sayt_tezligi_sek": 0,                  # yuklanish vaqti
    "sayt_mobil_optimizatsiya": False,
    "sayt_oylik_tashrif": 0,
    "sayt_bounce_rate": 0,                   # %
    "sayt_ortacha_vaqt_min": 0,
    "sayt_sahifalar_soni": 0,
    "sayt_blog_bor": False,
    "sayt_virtual_tur_bor": False,
    "sayt_chatbot_bor": False,
    "sayt_tillar": [],                       # ["uz", "ru", "en"]

    # --- Landing sahifalar ---
    "landing_sahifalar_soni": 0,
    "landing_konversiya_ortacha": 0,         # %
    "landing_a_b_test_bor": False,
    "landing_personalizatsiya": False,

    # --- Qabul portali ---
    "qabul_portal_ux_bali": 0,              # 1-10
    "qabul_portal_mobil_bor": False,
    "qabul_portal_auto_save": False,
    "qabul_portal_progress_bar": False,
    "qabul_portal_tillar": [],

    # --- Media kontent ---
    "video_soni_jami": 0,
    "foto_galeriya_bor": False,
    "360_tur_bor": False,
    "infografika_soni": 0,
    "pdf_buklet_online": False,
    "student_vlog_bor": False,
}

# ══════════════════════════════════════════════════════════════════════
# 23-BO'LIM: IJTIMOIY TA'SIR VA CSR (20 parametr)
# ══════════════════════════════════════════════════════════════════════
IJTIMOIY = {
    "ijtimoiy_loyihalar_soni": 0,
    "ijtimoiy_loyihalar": [],
    "bepul_kurslar_soni": 0,
    "bepul_kurslar_ishtirokchilar": 0,
    "volontorlik_talabalar_foiz": 0,
    "ekologik_loyihalar": [],
    "jamiyat_uchun_ochiq_tadbirlar": 0,
    "mahalla_hamkorligi_bor": False,
    "maktab_hamkorligi_bor": False,
    "maktab_hamkorlik_soni": 0,
    "yetim_bolalar_dasturi_bor": False,
    "nogironlar_dasturi_bor": False,
    "ayollar_empowerment_bor": False,
    "qishloq_talim_dasturi_bor": False,
    "media_savodxonlik_kursi": False,
    "ijtimoiy_reputatsiya_bali": 0,          # 1-10
    "homiylik_keltirilgan": 0,               # so'mda
    "homiylar_soni": 0,
    "homiy_tashkilotlar": [],
    "csr_byudjeti": 0,
}

# ══════════════════════════════════════════════════════════════════════
# 24-BO'LIM: KELAJAK REJALARI (25 parametr)
# ══════════════════════════════════════════════════════════════════════
KELAJAK = {
    # --- Qisqa muddatli (1 yil) ---
    "yangi_yonalishlar_2026": [],
    "yangi_bino_rejalari": "",
    "yangi_laboratoriya": [],
    "yangi_hamkorlik": [],
    "marketing_yangiliklar": [],
    "texnologiya_yangiliklar": [],
    "xodim_kengaytirish": 0,

    # --- O'rta muddatli (3 yil) ---
    "maqsad_talaba_3yil": 0,
    "maqsad_yonalish_3yil": 0,
    "maqsad_xalqaro_hamkor_3yil": 0,
    "kampus_kengaytirish_bor": False,
    "yangi_kampus_bor": False,
    "filial_ochish_bor": False,
    "filial_shahar": "",
    "akkreditatsiya_maqsad": "",

    # --- Uzoq muddatli (5-10 yil) ---
    "vizyon_2030": "",
    "missiya": "",
    "strategik_maqsadlar": [],
    "maqsad_reyting": 0,
    "maqsad_talaba_5yil": 0,
    "maqsad_xorijiy_talaba_foiz": 0,
    "maqsad_tadqiqot_uni": False,
    "maqsad_regional_lider": False,
    "investitsiya_rejalangan": 0,
    "yangi_tashabbuslar": [],
}

# ══════════════════════════════════════════════════════════════════════
# 25-BO'LIM: SIMULYATSIYA MAQSADLARI VA CHEKLOVLAR (35 parametr)
# ══════════════════════════════════════════════════════════════════════
SIMULYATSIYA_MAQSADLAR = {
    # --- Asosiy maqsadlar ---
    "maqsad_1": {
        "nomi": "Talabalar sonini maksimallashtirish",
        "og_irligi": 0.30,
        "min_qiymat": 0,
        "maqsad_qiymat": 0,
        "ideal_qiymat": 0,
    },
    "maqsad_2": {
        "nomi": "Daromadni maksimallashtirish",
        "og_irligi": 0.25,
        "min_qiymat": 0,
        "maqsad_qiymat": 0,
        "ideal_qiymat": 0,
    },
    "maqsad_3": {
        "nomi": "Marketing ROI ni maksimallashtirish",
        "og_irligi": 0.15,
        "min_qiymat": 0,
        "maqsad_qiymat": 0,
    },
    "maqsad_4": {
        "nomi": "Sifatli talabalar ulushini oshirish",
        "og_irligi": 0.10,
        "min_qiymat": 0,
        "maqsad_qiymat": 0,
    },
    "maqsad_5": {
        "nomi": "Hududiy diversifikatsiya",
        "og_irligi": 0.10,
        "min_buxorodan_tashqari_foiz": 0,
        "maqsad_foiz": 0,
    },
    "maqsad_6": {
        "nomi": "Brend tanilganligini oshirish",
        "og_irligi": 0.05,
        "joriy_tanilganlik": 0,
        "maqsad_tanilganlik": 0,
    },
    "maqsad_7": {
        "nomi": "Talaba ushlab qolish (retention)",
        "og_irligi": 0.05,
        "joriy_retention": 0,
        "maqsad_retention": 0,
    },

    # --- Qattiq cheklovlar ---
    "cheklovlar": {
        "max_talaba_sigim": 0,
        "min_kontrakt_narx": 0,
        "max_kontrakt_narx": 0,
        "max_marketing_byudjet": 0,
        "max_chegirma_foiz_bir_talaba": 0,
        "max_chegirma_jami_byudjet": 0,
        "min_foyda_margin_foiz": 0,
        "min_sifat_ball_dtm": 0,
        "max_xodim_soni": 0,
        "max_agent_komissiya": 0,
        "min_professor_phd_foiz": 0,
        "max_talaba_oqituvchi_nisbat": 0,
    },

    # --- Stsenariylar ---
    "stsenariy_optimistik": {
        "iqtisodiy_osish": True,
        "raqobat_kamayishi": True,
        "brend_osishi": True,
    },
    "stsenariy_pessimistik": {
        "iqtisodiy_inqiroz": True,
        "yangi_raqobatchi": True,
        "narx_urushi": True,
    },
    "stsenariy_bazaviy": {
        "hozirgi_trend_davom": True,
    },
}


# ══════════════════════════════════════════════════════════════════════
# META: BARCHA BO'LIMLAR RO'YXATI
# ══════════════════════════════════════════════════════════════════════
BARCHA_BOLIMLAR = {
    "01_UNIVERSITET": UNIVERSITET,
    "02_YONALISHLAR": YONALISHLAR,
    "03_NARXLASH": NARXLASH,
    "04_MARKETING": MARKETING,
    "05_ABITURIYENT": ABITURIYENT_PROFILI,
    "06_RAQOBATCHILAR": RAQOBATCHILAR,
    "07_INFRATUZILMA": INFRATUZILMA,
    "08_XALQARO": XALQARO,
    "09_QABUL_JARAYONI": QABUL_JARAYONI,
    "10_MOLIYA": MOLIYA,
    "11_HUDUDIY_BOZOR": HUDUDIY_BOZOR,
    "12_MAVSUMIYLIK": MAVSUMIYLIK,
    "13_TEXNOLOGIYA": TEXNOLOGIYA,
    "14_TASHQI_OMILLAR": TASHQI_OMILLAR,
    "15_KADRLAR": KADRLAR,
    "16_ALUMNI": ALUMNI,
    "17_TALABA_HAYOTI": TALABA_HAYOTI,
    "18_BREND": BREND,
    "19_HAMKORLIKLAR": HAMKORLIKLAR,
    "20_QONUNCHILIK": QONUNCHILIK,
    "21_FUNNEL": FUNNEL,
    "22_RAQAMLI_AKTIVLAR": RAQAMLI_AKTIVLAR,
    "23_IJTIMOIY": IJTIMOIY,
    "24_KELAJAK": KELAJAK,
    "25_SIMULYATSIYA_MAQSADLAR": SIMULYATSIYA_MAQSADLAR,
}
