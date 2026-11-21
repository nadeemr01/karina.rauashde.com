# Site content in three languages. Edit text here, then run:  python3 _src/build.py
# Facts come from "Karina CV 2026.pdf" (updated 19.11.2026: Ashab Clinics, Riyadh; SCFHS Registrar).
# Do not add the SMLE back — the family asked for it to be removed; the SCFHS classification replaces it.

PHONE_DISPLAY = "+7 961 668-94-81"
PHONE_TEL = "+79616689481"
WHATSAPP = "https://wa.me/79616689481"
EMAIL = "karinar888@mail.ru"
CV_FILE = "Karina-Rauashde-CV.pdf"
SITE = "https://karina.rauashde.com/"

LANGS = ["en", "ar", "ru"]
LANG_PREFIX = {"en": "", "ar": "ar/", "ru": "ru/"}
SWITCH_LABEL = {"en": "EN", "ar": "عربي", "ru": "RU"}
SWITCH_NAME = {"en": "English", "ar": "العربية", "ru": "Русский"}

# Pages, in menu order. "" is the home page.
PAGES = ["home", "about", "experience", "treatments", "education", "contact"]
SLUG = {"home": "", "about": "about/", "experience": "experience/", "treatments": "treatments/",
        "education": "education/", "contact": "contact/"}
NEXT = {"about": "experience", "experience": "treatments", "treatments": "education", "education": "contact"}

T = {}

# ───────────────────────────── ENGLISH ─────────────────────────────
T["en"] = dict(
    dir="ltr",
    og_locale="en_US",
    brand="Dr. Karina Rauashde",
    skip="Skip to content",
    menu="Menu",
    close="Close",
    nav={"home": "Home", "about": "About", "experience": "Experience", "treatments": "Treatments",
         "education": "Education", "contact": "Contact"},
    meta={
        "home": ("Dr. Karina Rauashde — Dermatologist in Riyadh",
                 "Dr. Karina Rauashde — dermatologist at Ashab Clinics, Riyadh, with 5+ years of medical practice: "
                 "skin, hair and nails, minor surgery, Botox, fillers, lasers and IPL. SCFHS Registrar, Dermatology."),
        "about": ("About — Dr. Karina Rauashde",
                  "Dermatologist trained in Russia, now practicing in Riyadh. Arabic, Russian and English."),
        "experience": ("Experience — Dr. Karina Rauashde",
                       "Ashab Clinics, Riyadh; Elabuzhskaya Central Regional Hospital; Beauty Medicine clinic; "
                       "Al Hadith Hospital, Aqaba; residency at the State Research Center of Dermatovenereology "
                       "and Cosmetology, Moscow."),
        "treatments": ("Treatments — Dr. Karina Rauashde",
                       "Botox, fillers, skin boosters, PRP, PDO threads, CO₂ and erbium lasers, IPL, peels and "
                       "medical dermatology."),
        "education": ("Education & licensing — Dr. Karina Rauashde",
                      "VolgSMU, RUDN University, First Professional Institute of Aesthetics. "
                      "SCFHS Professional Classification: Registrar, Dermatology (2026)."),
        "contact": ("Contact — Dr. Karina Rauashde",
                    "Phone, WhatsApp and email. Consultations in Arabic, Russian and English."),
    },
    more="Learn more",
    next="Next",
    cta_contact="Get in touch",
    cta_cv="Download CV",
    cv_meta="PDF · 2 pages · English",

    # ── home
    hero_eyebrow="Dermatologist · Riyadh",
    hero_title="Dr. Karina Rauashde",
    hero_sub="Skin, hair and nails — treated with precision and care.",
    hero_alt="Dr. Karina Rauashde in a white blazer, putting on black medical gloves",
    glance_label="At a glance",
    glance_title="Where clinical dermatology meets aesthetic medicine.",
    stats=[("5+", "years of medical practice"),
           ("15+", "aesthetic and laser procedures"),
           ("3", "languages — Arabic, Russian and English"),
           ("SCFHS", "classified Registrar, Dermatology · 2026")],
    tiles={
        "about": ("About Karina.", "Trained in Russia. Now practicing in Riyadh."),
        "experience": ("Experience.", "From residency in Moscow to Ashab Clinics in Riyadh."),
        "treatments": ("Treatments.", "Injectables, lasers, skin renewal and medical dermatology."),
        "education": ("Education &amp; licensing.", "VolgSMU, RUDN University and an SCFHS classification."),
        "contact": ("Let’s talk.", "In Arabic, Russian or English."),
    },
    lic_tile_rank="Registrar",
    lic_tile_field="Dermatology",

    # ── about
    about_title="About Karina.",
    about_lead="Care for skin, hair and nails — personal to every patient.",
    about_alt="Dr. Karina Rauashde in a white coat over black scrubs",
    about_intro="I’m a dermatologist with more than five years of experience as a doctor, "
                "now practicing at Ashab Clinics in Riyadh.",
    about_p=[
        "I diagnose and treat acute and chronic conditions of the skin, hair and nails — acne, rosacea, psoriasis, "
        "eczema, seborrheic dermatitis and more. I perform minor surgical procedures such as biopsies and "
        "excisions, and offer a full range of laser, injectable and aesthetic treatments.",
        "Every treatment plan is built around the patient’s skin type and skin tone. I studied General Medicine "
        "at Volgograd State Medical University and completed my dermatology residency in Moscow — at RUDN "
        "University and the State Research Center of Dermatovenereology and Cosmetology. I also trained in "
        "trichology at RUDN and in cosmetology at the First Professional Institute of Aesthetics.",
        "In November 2026 the Saudi Commission for Health Specialties (SCFHS) classified me as Registrar in "
        "Dermatology. Arabic is my native language, and I also work in Russian and English.",
    ],
    approach_label="Approach",
    approach_title="Medicine first. Beauty that follows.",
    approach=[
        ("person", "Personal plans", "Treatment matched to each patient’s skin type and skin tone — for patients of all ages."),
        ("stetho", "Medical and aesthetic", "Clinical dermatology and minor surgery alongside injectables, lasers and IPL."),
        ("globe", "Three languages", "Consultations in Arabic, Russian and English."),
    ],
    langs_label="Languages",
    langs=[("العربية", "Arabic · native", "ar"), ("Русский", "Russian", "ru"), ("English", "English", "en")],

    # ── experience
    exp_title="Experience.",
    exp_lead="More than five years of medical practice in Saudi Arabia, Russia and Jordan.",
    exp_alt="Dr. Karina Rauashde in a surgical gown and mask during a procedure",
    now="Now",
    exp=[
        dict(period="Jul 2026 — present", current=True, role="Dermatologist",
             org="Ashab Clinics", place="Riyadh, Saudi Arabia",
             desc="Private clinic in Riyadh — diagnosing and treating skin, hair and nail disorders and providing "
                  "aesthetic dermatology procedures.",
             bullets=[], chips=[]),
        dict(period="2023 — 2026", role="Dermatologist",
             org="Elabuzhskaya Central Regional Hospital", place="Tatarstan, Russia",
             desc="Dermatology department of a regional hospital — diagnosis and treatment of acute and chronic "
                  "skin disorders.",
             bullets=[
                 "Diagnosis and treatment of acne, psoriasis, rosacea, warts, seborrheic dermatitis and eczema",
                 "Laser techniques to improve the appearance of the skin and treat skin conditions",
                 "Minor surgical procedures — biopsies and excisions",
                 "Skin-care counselling, including the correct use of topical medications",
                 "Anti-aging and anti-acne treatment plans for patients of all ages",
                 "Personalized treatment for every skin type and skin tone",
             ], chips=[]),
        dict(period="2023 — 2026", role="Dermatologist · aesthetic medicine",
             org="Beauty Medicine Private Clinic", place="Kazan, Russia",
             desc="Private dermatology clinic — aesthetic procedures and treatment of skin conditions. "
                  "More than fifteen procedures, from Botox and fillers to CO₂ lasers and IPL.",
             bullets=[],
             chips=["Botox &amp; fillers", "CO₂ &amp; erbium lasers", "IPL", "Biorevitalization",
                    "PRP", "PDO threads", "Peels &amp; Hydrafacial"]),
        dict(period="2023 — 2024", role="Trainee, Dermatology Department",
             org="Al Hadith Hospital", place="Aqaba, Jordan", desc="", bullets=[], chips=[]),
        dict(period="2021 — 2023", role="Dermatology Resident",
             org="State Research Center of Dermatovenereology and Cosmetology", place="Moscow, Russia",
             desc="Two-year residency in dermatology, venereology and cosmetology, managing outpatient and "
                  "specialist cases.",
             bullets=[], chips=[]),
    ],
    exp_see_all="See all treatments",

    # ── treatments
    tr_title="Treatments.",
    tr_lead="More than fifteen procedures — from clinical dermatology to injectables and lasers.",
    tr_alt="Dr. Karina Rauashde in black scrubs beside a laser device",
    tr_jump="Jump to",
    proc=[
        ("injectables", "syringe", "Injectables", "Botulinum toxin, fillers and skin boosters for the face, neck and body.", [
            ("Botulinum toxin (Botox)", "Full face and neck"),
            ("Hyperhidrosis treatment", "Botox for underarms, hands and feet"),
            ("Dermal fillers", "Lips, jawline and chin, temples, cheeks, under-eye area, nasolabial folds"),
            ("Biorevitalization", "Skin boosters and biostimulators — face and body"),
            ("Mesotherapy", "Face and body"),
            ("PRP therapy", "Face, body and hair"),
            ("PDO mono threads", ""),
        ]),
        ("lasers", "light", "Lasers &amp; devices", "Ablative and non-ablative lasers, IPL and radio-wave surgery.", [
            ("CO₂ fractional laser resurfacing", ""),
            ("Non-ablative laser resurfacing", "1540 nm erbium-glass laser"),
            ("Laser treatment of telangiectasia", "Removal of small visible blood vessels"),
            ("IPL procedures", "Advanced certified specialist — Candela and DEKA"),
            ("Radio-wave electrosurgery", "Removal of skin tags and warts"),
        ]),
        ("renewal", "drop", "Skin renewal", "Peels, microdermabrasion and anti-aging programs.", [
            ("Microdermabrasion", "Hydrafacial"),
            ("Chemical peels", ""),
            ("Anti-aging programs", "Personalized plans for every age, skin type and skin tone"),
        ]),
        ("medical", "stetho", "Medical dermatology", "Diagnosis and treatment of skin, hair and nail conditions.", [
            ("Inflammatory skin disease", "Acne, rosacea, psoriasis, eczema, seborrheic dermatitis"),
            ("Hair, scalp and nails", "Trichology"),
            ("Minor surgery", "Biopsies and excisions; warts and skin tags"),
            ("Topical-therapy guidance", "Correct use of prescribed creams and medications"),
        ]),
    ],
    ipl_badge="Advanced certified IPL specialist",
    ipl_note="Candela and DEKA systems",

    # ── education
    edu_title="Education &amp; licensing.",
    edu_lead="A medical degree from Volgograd, residency and specialist training in Moscow, "
             "and a Saudi professional classification.",
    lic_label="License",
    lic_issuer="Saudi Commission for Health Specialties",
    lic_name="Professional Classification",
    lic_rank="Registrar, Dermatology",
    lic_date="November 2026",
    edu_label="Education",
    edu=[
        ("2014 — 2021", "Volgograd State Medical University (VolgSMU)", "General Medicine", "Volgograd, Russia"),
        ("2021 — 2023", "RUDN University", "Residency in Dermatology", "Moscow, Russia"),
        ("2021 — 2022", "RUDN University", "Trichology", "Moscow, Russia"),
        ("2022 — 2023", "First Professional Institute of Aesthetics", "Cosmetology", "Moscow, Russia"),
    ],

    # ── contact
    c_title="Let’s talk.",
    c_lead="For job opportunities, collaboration or consultations — in Arabic, Russian or English.",
    c_phone="Phone", c_whatsapp="WhatsApp", c_whatsapp_v="Send a message",
    c_email="Email", c_location="Based in", c_location_v="Riyadh, Saudi Arabia",
    c_cv_title="The full CV.",
    c_cv_text="Experience, procedures, education and licensing on two pages.",

    # ── footer
    foot_tagline="Dr. Karina Rauashde — Dermatologist · Riyadh, Saudi Arabia",
    foot_pages="Pages",
    foot_contact="Contact",
    foot_lang="Language",
    copyright="© 2026 Dr. Karina Rauashde. All rights reserved.",
)

# ───────────────────────────── ARABIC ─────────────────────────────
T["ar"] = dict(
    dir="rtl",
    og_locale="ar_SA",
    brand="د. كارينا الرواشدة",
    skip="انتقل إلى المحتوى",
    menu="القائمة",
    close="إغلاق",
    nav={"home": "الرئيسية", "about": "نبذة", "experience": "الخبرة", "treatments": "العلاجات",
         "education": "التعليم", "contact": "التواصل"},
    meta={
        "home": ("د. كارينا الرواشدة — طبيبة أمراض جلدية في الرياض",
                 "د. كارينا الرواشدة — طبيبة أمراض جلدية في عيادات أسهب بالرياض، بخبرة تزيد على 5 سنوات: أمراض الجلد "
                 "والشعر والأظافر، الجراحة الصغرى، البوتوكس والفيلر والليزر. مصنّفة «أخصائي» في الأمراض الجلدية من الهيئة "
                 "السعودية للتخصصات الصحية."),
        "about": ("نبذة — د. كارينا الرواشدة",
                  "طبيبة أمراض جلدية درست في روسيا وتمارس الطب اليوم في الرياض. العربية والروسية والإنجليزية."),
        "experience": ("الخبرة — د. كارينا الرواشدة",
                       "عيادات أسهب في الرياض، مستشفى يلابوغا المركزي، عيادة بيوتي ميديسن، مستشفى الحديث في العقبة، "
                       "والإقامة في المركز الحكومي للأبحاث في الأمراض الجلدية والتجميل بموسكو."),
        "treatments": ("العلاجات — د. كارينا الرواشدة",
                       "البوتوكس، الفيلر، معززات البشرة، PRP، خيوط PDO، ليزر CO₂ والإربيوم، الضوء النبضي المكثّف، "
                       "التقشير والأمراض الجلدية."),
        "education": ("التعليم والترخيص — د. كارينا الرواشدة",
                      "جامعة فولغوغراد الطبية، جامعة RUDN، المعهد المهني الأول للتجميل. التصنيف المهني من الهيئة "
                      "السعودية للتخصصات الصحية: أخصائي — الأمراض الجلدية (2026)."),
        "contact": ("التواصل — د. كارينا الرواشدة",
                    "الهاتف وواتساب والبريد الإلكتروني. استشارات بالعربية والروسية والإنجليزية."),
    },
    more="اعرف المزيد",
    next="التالي",
    cta_contact="تواصل معي",
    cta_cv="تحميل السيرة الذاتية",
    cv_meta="PDF · صفحتان · بالإنجليزية",

    hero_eyebrow="طبيبة أمراض جلدية · الرياض",
    hero_title="د. كارينا الرواشدة",
    hero_sub="عناية بالبشرة والشعر والأظافر، بدقة واهتمام.",
    hero_alt="د. كارينا الرواشدة بسترة بيضاء ترتدي قفازات طبية سوداء",
    glance_label="لمحة سريعة",
    glance_title="حيث تلتقي الأمراض الجلدية بالطب التجميلي.",
    stats=[("5+", "سنوات من الممارسة الطبية"),
           ("15+", "إجراءً تجميليًا وليزريًا"),
           ("3", "لغات: العربية والروسية والإنجليزية"),
           ("SCFHS", "تصنيف «أخصائي» في الأمراض الجلدية · 2026")],
    tiles={
        "about": ("تعرّف على كارينا.", "درست الطب في روسيا، وتمارسه اليوم في الرياض."),
        "experience": ("الخبرة.", "من الإقامة الطبية في موسكو إلى عيادات أسهب في الرياض."),
        "treatments": ("العلاجات.", "الحقن التجميلية والليزر وتجديد البشرة والأمراض الجلدية."),
        "education": ("التعليم والترخيص.", "جامعة فولغوغراد الطبية وجامعة RUDN وتصنيف مهني سعودي."),
        "contact": ("لنتواصل.", "بالعربية أو الروسية أو الإنجليزية."),
    },
    lic_tile_rank="أخصائي",
    lic_tile_field="الأمراض الجلدية",

    about_title="تعرّف على كارينا.",
    about_lead="عناية بالبشرة والشعر والأظافر، مصمّمة لكل مريض.",
    about_alt="د. كارينا الرواشدة بمعطف طبي أبيض فوق زي طبي أسود",
    about_intro="طبيبة أمراض جلدية بخبرة تزيد على خمس سنوات في الممارسة الطبية، أعمل حاليًا في عيادات أسهب بالرياض.",
    about_p=[
        "أشخّص الأمراض الحادة والمزمنة للجلد والشعر والأظافر وأعالجها — كحب الشباب والوردية والصدفية والإكزيما "
        "والتهاب الجلد الدهني وغيرها — وأُجري العمليات الجراحية الصغرى كأخذ الخزعات والاستئصال، إلى جانب مجموعة "
        "متكاملة من علاجات الليزر والحقن والإجراءات التجميلية.",
        "أصمّم كل خطة علاجية وفق نوع بشرة المريض ولونها. درست الطب العام في جامعة فولغوغراد الطبية الحكومية، "
        "وأتممت الإقامة في الأمراض الجلدية في موسكو — في جامعة الصداقة بين الشعوب الروسية (RUDN) والمركز الحكومي "
        "للأبحاث في الأمراض الجلدية والتناسلية والتجميل — كما درست طب الشعر في RUDN والتجميل الطبي في المعهد المهني "
        "الأول للتجميل.",
        "في نوفمبر 2026 صنّفتني الهيئة السعودية للتخصصات الصحية بدرجة «أخصائي» في الأمراض الجلدية. العربية لغتي الأم، "
        "وأعمل كذلك بالروسية والإنجليزية.",
    ],
    approach_label="النهج",
    approach_title="الطب أولًا، والجمال يأتي بعده.",
    approach=[
        ("person", "خطط علاجية شخصية", "علاج يناسب نوع بشرة كل مريض ولونها، ولجميع الأعمار."),
        ("stetho", "طب وتجميل", "الأمراض الجلدية والجراحة الصغرى جنبًا إلى جنب مع الحقن والليزر والضوء النبضي المكثّف."),
        ("globe", "ثلاث لغات", "استشارات بالعربية والروسية والإنجليزية."),
    ],
    langs_label="اللغات",
    langs=[("العربية", "اللغة الأم", "ar"), ("Русский", "الروسية", "ru"), ("English", "الإنجليزية", "en")],

    exp_title="الخبرة.",
    exp_lead="أكثر من خمس سنوات من الممارسة الطبية في السعودية وروسيا والأردن.",
    exp_alt="د. كارينا الرواشدة بثوب جراحي وكمامة أثناء إجراء طبي",
    now="حاليًا",
    exp=[
        dict(period="يوليو 2026 — حتى الآن", current=True, role="طبيبة أمراض جلدية",
             org="عيادات أسهب", place="الرياض، السعودية",
             desc="عيادة خاصة في الرياض — تشخيص أمراض الجلد والشعر والأظافر وعلاجها، وتقديم إجراءات التجميل الجلدي.",
             bullets=[], chips=[]),
        dict(period="2023 — 2026", role="طبيبة أمراض جلدية",
             org="مستشفى يلابوغا المركزي الإقليمي", place="تتارستان، روسيا",
             desc="قسم الأمراض الجلدية في مستشفى إقليمي — تشخيص الأمراض الجلدية الحادة والمزمنة وعلاجها.",
             bullets=[
                 "تشخيص وعلاج حب الشباب والصدفية والوردية والثآليل والتهاب الجلد الدهني والإكزيما",
                 "استخدام تقنيات الليزر لتحسين مظهر البشرة وعلاج الأمراض الجلدية",
                 "إجراء العمليات الجراحية الصغرى كأخذ الخزعات والاستئصال",
                 "تقديم إرشادات العناية بالبشرة، ومنها الاستخدام الصحيح للأدوية الموضعية",
                 "وضع خطط علاجية لمكافحة الشيخوخة وحب الشباب للمرضى من جميع الأعمار",
                 "علاج مخصص لكل نوع بشرة ولونها",
             ], chips=[]),
        dict(period="2023 — 2026", role="طبيبة جلدية وتجميل",
             org="عيادة بيوتي ميديسن الخاصة", place="قازان، روسيا",
             desc="عيادة خاصة للأمراض الجلدية — إجراءات تجميلية وعلاج الأمراض الجلدية. أكثر من خمسة عشر إجراءً، "
                  "من البوتوكس والفيلر إلى ليزر CO₂ والضوء النبضي المكثّف.",
             bullets=[],
             chips=["البوتوكس والفيلر", "ليزر CO₂ والإربيوم", "IPL", "إعادة إحياء البشرة",
                    "PRP", "خيوط PDO", "التقشير والهيدرافيشال"]),
        dict(period="2023 — 2024", role="متدربة في قسم الأمراض الجلدية",
             org="مستشفى الحديث", place="العقبة، الأردن", desc="", bullets=[], chips=[]),
        dict(period="2021 — 2023", role="طبيبة مقيمة في الأمراض الجلدية",
             org="المركز الحكومي للأبحاث في الأمراض الجلدية والتناسلية والتجميل", place="موسكو، روسيا",
             desc="إقامة لمدة عامين في الأمراض الجلدية والتناسلية والتجميل، مع متابعة حالات العيادات الخارجية "
                  "والحالات التخصصية.",
             bullets=[], chips=[]),
    ],
    exp_see_all="جميع العلاجات",

    tr_title="العلاجات.",
    tr_lead="أكثر من خمسة عشر إجراءً — من الأمراض الجلدية إلى الحقن التجميلية والليزر.",
    tr_alt="د. كارينا الرواشدة بزي طبي أسود بجوار جهاز ليزر",
    tr_jump="انتقل إلى",
    proc=[
        ("injectables", "syringe", "الحقن التجميلية", "البوتوكس والفيلر ومعززات البشرة للوجه والرقبة والجسم.", [
            ("البوتوكس", "الوجه كاملًا والرقبة"),
            ("علاج فرط التعرّق", "بالبوتوكس للإبطين واليدين والقدمين"),
            ("الفيلر", "الشفاه، خط الفك والذقن، الصدغان، الوجنتان، منطقة تحت العين، الطيات الأنفية الشفوية"),
            ("إعادة إحياء البشرة", "معززات البشرة والمحفزات الحيوية — للوجه والجسم"),
            ("الميزوثيرابي", "للوجه والجسم"),
            ("البلازما الغنية بالصفائح الدموية (PRP)", "للوجه والجسم والشعر"),
            ("خيوط PDO الأحادية", ""),
        ]),
        ("lasers", "light", "الليزر والأجهزة", "الليزر التقشيري وغير التقشيري، والضوء النبضي المكثّف، والجراحة بالترددات الراديوية.", [
            ("ليزر ثاني أكسيد الكربون الجزئي (CO₂ Fractional)", "لتجديد سطح البشرة"),
            ("تجديد البشرة بالليزر غير التقشيري", "ليزر الإربيوم جلاس بطول موجي 1540 نانومتر"),
            ("علاج توسّع الشعيرات الدموية بالليزر", "إزالة الأوعية الدموية الدقيقة الظاهرة"),
            ("الضوء النبضي المكثّف (IPL)", "أخصائية معتمدة بمستوى متقدم — Candela وDEKA"),
            ("الجراحة الكهربائية بالترددات الراديوية", "إزالة الزوائد الجلدية والثآليل"),
        ]),
        ("renewal", "drop", "تجديد البشرة", "التقشير الكيميائي والتقشير الدقيق وبرامج مكافحة الشيخوخة.", [
            ("التقشير الدقيق للبشرة", "هيدرافيشال"),
            ("التقشير الكيميائي", ""),
            ("برامج مكافحة الشيخوخة", "خطط مخصصة لكل عمر ونوع بشرة ولونها"),
        ]),
        ("medical", "stetho", "الأمراض الجلدية", "تشخيص أمراض الجلد والشعر والأظافر وعلاجها.", [
            ("الأمراض الجلدية الالتهابية", "حب الشباب، الوردية، الصدفية، الإكزيما، التهاب الجلد الدهني"),
            ("الشعر وفروة الرأس والأظافر", "طب الشعر (الترايكولوجي)"),
            ("الجراحة الصغرى", "الخزعات والاستئصال، الثآليل والزوائد الجلدية"),
            ("الإرشاد في العلاجات الموضعية", "الاستخدام الصحيح للكريمات والأدوية الموصوفة"),
        ]),
    ],
    ipl_badge="أخصائية IPL معتمدة بمستوى متقدم",
    ipl_note="أجهزة Candela وDEKA",

    edu_title="التعليم والترخيص.",
    edu_lead="شهادة الطب من فولغوغراد، والإقامة والتدريب التخصصي في موسكو، وتصنيف مهني سعودي.",
    lic_label="الترخيص",
    lic_issuer="الهيئة السعودية للتخصصات الصحية",
    lic_name="التصنيف المهني",
    lic_rank="أخصائي — الأمراض الجلدية",
    lic_date="نوفمبر 2026",
    edu_label="التعليم",
    edu=[
        ("2014 — 2021", "جامعة فولغوغراد الطبية الحكومية", "الطب العام", "فولغوغراد، روسيا"),
        ("2021 — 2023", "جامعة الصداقة بين الشعوب الروسية (RUDN)", "الإقامة في الأمراض الجلدية", "موسكو، روسيا"),
        ("2021 — 2022", "جامعة الصداقة بين الشعوب الروسية (RUDN)", "طب الشعر وفروة الرأس (الترايكولوجي)", "موسكو، روسيا"),
        ("2022 — 2023", "المعهد المهني الأول للتجميل", "التجميل الطبي (الكوزمتولوجي)", "موسكو، روسيا"),
    ],

    c_title="لنتواصل.",
    c_lead="لفرص العمل أو التعاون أو الاستشارات — بالعربية أو الروسية أو الإنجليزية.",
    c_phone="الهاتف", c_whatsapp="واتساب", c_whatsapp_v="مراسلة عبر واتساب",
    c_email="البريد الإلكتروني", c_location="مقيمة في", c_location_v="الرياض، المملكة العربية السعودية",
    c_cv_title="السيرة الذاتية كاملة.",
    c_cv_text="الخبرة والإجراءات والتعليم والترخيص في صفحتين.",

    foot_tagline="د. كارينا الرواشدة — طبيبة أمراض جلدية · الرياض، المملكة العربية السعودية",
    foot_pages="الصفحات",
    foot_contact="التواصل",
    foot_lang="اللغة",
    copyright="© 2026 د. كارينا الرواشدة. جميع الحقوق محفوظة.",
)

# ───────────────────────────── RUSSIAN ─────────────────────────────
T["ru"] = dict(
    dir="ltr",
    og_locale="ru_RU",
    brand="Карина Рауашде",
    skip="Перейти к содержанию",
    menu="Меню",
    close="Закрыть",
    nav={"home": "Главная", "about": "Обо мне", "experience": "Опыт", "treatments": "Процедуры",
         "education": "Образование", "contact": "Контакты"},
    meta={
        "home": ("Рауашде Карина Раедовна — врач-дерматовенеролог, косметолог",
                 "Карина Рауашде — врач-дерматовенеролог в Ashab Clinics (Эр-Рияд), более 5 лет врачебной практики: "
                 "заболевания кожи, волос и ногтей, малая хирургия, ботулинотерапия, филлеры, лазеры и IPL. "
                 "Профессиональная классификация SCFHS: Registrar, дерматология."),
        "about": ("Обо мне — Карина Рауашде",
                  "Врач-дерматовенеролог: образование в России, практика в Эр-Рияде. Арабский, русский, английский."),
        "experience": ("Опыт работы — Карина Рауашде",
                       "Ashab Clinics (Эр-Рияд), Елабужская ЦРБ, клиника Beauty Medicine (Казань), больница Al Hadith "
                       "(Акаба), ординатура в ГНЦДК (Москва)."),
        "treatments": ("Процедуры — Карина Рауашде",
                       "Ботулинотерапия, филлеры, биоревитализация, PRP, нити PDO, CO₂- и эрбиевый лазер, IPL, "
                       "пилинги и клиническая дерматология."),
        "education": ("Образование и лицензии — Карина Рауашде",
                      "ВолгГМУ, РУДН, Первый профессиональный институт эстетики. Профессиональная классификация "
                      "SCFHS: Registrar, дерматология (2026)."),
        "contact": ("Контакты — Карина Рауашде",
                    "Телефон, WhatsApp и электронная почта. Консультации на русском, арабском и английском."),
    },
    more="Подробнее",
    next="Далее",
    cta_contact="Связаться",
    cta_cv="Скачать резюме",
    cv_meta="PDF · 2 страницы · на английском",

    hero_eyebrow="Врач-дерматовенеролог · Эр-Рияд",
    hero_title="Карина Рауашде",
    hero_sub="Кожа, волосы и ногти — с точностью и заботой.",
    hero_alt="Карина Рауашде в белом жакете надевает чёрные медицинские перчатки",
    glance_label="Коротко",
    glance_title="Клиническая дерматология и эстетическая медицина.",
    stats=[("5+", "лет врачебной практики"),
           ("15+", "эстетических и лазерных процедур"),
           ("3", "языка: арабский, русский, английский"),
           ("SCFHS", "классификация Registrar, дерматология · 2026")],
    tiles={
        "about": ("Обо мне.", "Образование — в России. Практика — в Эр-Рияде."),
        "experience": ("Опыт.", "От ординатуры в Москве до Ashab Clinics в Эр-Рияде."),
        "treatments": ("Процедуры.", "Инъекции, лазеры, обновление кожи и клиническая дерматология."),
        "education": ("Образование и лицензии.", "ВолгГМУ, РУДН и профессиональная классификация SCFHS."),
        "contact": ("Связаться.", "На русском, арабском или английском."),
    },
    lic_tile_rank="Registrar",
    lic_tile_field="Дерматология",

    about_title="Обо мне.",
    about_lead="Кожа, волосы и ногти — индивидуальный подход к каждому пациенту.",
    about_alt="Карина Рауашде в белом халате поверх чёрного медицинского костюма",
    about_intro="Врач-дерматовенеролог с опытом врачебной практики более пяти лет. "
                "Сейчас работаю в Ashab Clinics в Эр-Рияде.",
    about_p=[
        "Диагностирую и лечу острые и хронические заболевания кожи, волос и ногтей — акне, розацеа, псориаз, экзему, "
        "себорейный дерматит и другие. Выполняю малые хирургические вмешательства (биопсия, иссечение образований), "
        "провожу лазерные, инъекционные и эстетические процедуры.",
        "Схему лечения подбираю индивидуально — с учётом типа и тона кожи. Окончила Волгоградский государственный "
        "медицинский университет по специальности «Лечебное дело» и ординатуру по дерматовенерологии в Москве — "
        "в РУДН и Государственном научном центре дерматовенерологии и косметологии. Также прошла курс трихологии "
        "в РУДН и обучение косметологии в Первом профессиональном институте эстетики.",
        "В ноябре 2026 года Саудовская комиссия по специальностям здравоохранения (SCFHS) присвоила мне "
        "профессиональную классификацию Registrar по дерматологии. Арабский — мой родной язык, также работаю "
        "на русском и английском.",
    ],
    approach_label="Подход",
    approach_title="Сначала медицина. Красота — следом.",
    approach=[
        ("person", "Индивидуальные схемы", "Лечение с учётом типа и тона кожи — для пациентов любого возраста."),
        ("stetho", "Медицина и эстетика", "Клиническая дерматология и малая хирургия, инъекции, лазеры и IPL."),
        ("globe", "Три языка", "Консультации на русском, арабском и английском."),
    ],
    langs_label="Языки",
    langs=[("العربية", "Арабский · родной", "ar"), ("Русский", "Русский", "ru"), ("English", "Английский", "en")],

    exp_title="Опыт работы.",
    exp_lead="Более пяти лет врачебной практики в Саудовской Аравии, России и Иордании.",
    exp_alt="Карина Рауашде в хирургическом халате и маске во время процедуры",
    now="Сейчас",
    exp=[
        dict(period="Июль 2026 — наст. время", current=True, role="Врач-дерматолог",
             org="Ashab Clinics", place="Эр-Рияд, Саудовская Аравия",
             desc="Частная клиника в Эр-Рияде — диагностика и лечение заболеваний кожи, волос и ногтей, "
                  "эстетические дерматологические процедуры.",
             bullets=[], chips=[]),
        dict(period="2023 — 2026", role="Врач-дерматовенеролог",
             org="Елабужская центральная районная больница", place="Республика Татарстан",
             desc="Дерматологическое отделение районной больницы — диагностика и лечение острых и хронических "
                  "заболеваний кожи.",
             bullets=[
                 "Диагностика и лечение акне, псориаза, розацеа, бородавок, себорейного дерматита и экземы",
                 "Лазерные методики для улучшения состояния кожи и лечения дерматозов",
                 "Малые хирургические вмешательства: биопсия, иссечение",
                 "Рекомендации по уходу за кожей и правильному применению наружных средств",
                 "Антивозрастные программы и схемы лечения акне для пациентов любого возраста",
                 "Индивидуальное лечение с учётом типа и тона кожи",
             ], chips=[]),
        dict(period="2023 — 2026", role="Дерматолог-косметолог",
             org="Частная клиника Beauty Medicine", place="Казань",
             desc="Частная дерматологическая клиника — эстетические процедуры и лечение заболеваний кожи. "
                  "Более пятнадцати методик: от ботулинотерапии и филлеров до CO₂-лазера и IPL.",
             bullets=[],
             chips=["Ботулинотерапия и филлеры", "CO₂- и эрбиевый лазер", "IPL", "Биоревитализация",
                    "PRP", "Нити PDO", "Пилинги и Hydrafacial"]),
        dict(period="2023 — 2024", role="Стажёр дерматологического отделения",
             org="Больница Al Hadith", place="Акаба, Иордания", desc="", bullets=[], chips=[]),
        dict(period="2021 — 2023", role="Ординатор-дерматовенеролог",
             org="Государственный научный центр дерматовенерологии и косметологии", place="Москва",
             desc="Двухлетняя ординатура по дерматовенерологии и косметологии: ведение амбулаторных "
                  "и специализированных пациентов.",
             bullets=[], chips=[]),
    ],
    exp_see_all="Все процедуры",

    tr_title="Процедуры.",
    tr_lead="Более пятнадцати методик — от клинической дерматологии до инъекций и лазеров.",
    tr_alt="Карина Рауашде в чёрном медицинском костюме рядом с лазерным аппаратом",
    tr_jump="Перейти к разделу",
    proc=[
        ("injectables", "syringe", "Инъекционная косметология", "Ботулинотерапия, филлеры и скинбустеры для лица, шеи и тела.", [
            ("Ботулинотерапия", "Всё лицо и шея"),
            ("Лечение гипергидроза", "Ботулотоксин: подмышечные впадины, ладони, стопы"),
            ("Контурная пластика филлерами", "Губы, линия челюсти и подбородок, виски, скулы, "
                                             "подглазничная область, носогубные складки"),
            ("Биоревитализация", "Скинбустеры и биостимуляторы — лицо и тело"),
            ("Мезотерапия", "Лицо и тело"),
            ("PRP-терапия", "Лицо, тело, волосы"),
            ("Мононити PDO", ""),
        ]),
        ("lasers", "light", "Лазеры и аппараты", "Аблятивные и неаблятивные лазеры, IPL и радиоволновая хирургия.", [
            ("Фракционная CO₂-лазерная шлифовка", ""),
            ("Неаблятивное лазерное омоложение", "Эрбиевое стекло, 1540 нм"),
            ("Лазерное лечение телеангиэктазий", "Удаление сосудистых звёздочек"),
            ("IPL-процедуры", "Сертифицированный специалист продвинутого уровня — Candela и DEKA"),
            ("Радиоволновая электрохирургия", "Удаление папиллом и бородавок"),
        ]),
        ("renewal", "drop", "Обновление кожи", "Пилинги, микродермабразия и антивозрастные программы.", [
            ("Микродермабразия", "Hydrafacial"),
            ("Химические пилинги", ""),
            ("Антивозрастные программы", "Индивидуальные схемы с учётом возраста, типа и тона кожи"),
        ]),
        ("medical", "stetho", "Клиническая дерматология", "Диагностика и лечение заболеваний кожи, волос и ногтей.", [
            ("Воспалительные заболевания кожи", "Акне, розацеа, псориаз, экзема, себорейный дерматит"),
            ("Волосы, кожа головы и ногти", "Трихология"),
            ("Малая хирургия", "Биопсия и иссечение, удаление бородавок и папиллом"),
            ("Наружная терапия", "Подбор средств и обучение правильному применению"),
        ]),
    ],
    ipl_badge="Сертифицированный IPL-специалист продвинутого уровня",
    ipl_note="Аппараты Candela и DEKA",

    edu_title="Образование и лицензии.",
    edu_lead="Медицинское образование в Волгограде, ординатура и специализация в Москве, "
             "профессиональная классификация в Саудовской Аравии.",
    lic_label="Лицензия",
    lic_issuer="Саудовская комиссия по специальностям здравоохранения (SCFHS)",
    lic_name="Профессиональная классификация",
    lic_rank="Registrar, дерматология",
    lic_date="Ноябрь 2026",
    edu_label="Образование",
    edu=[
        ("2014 — 2021", "Волгоградский государственный медицинский университет (ВолгГМУ)", "Лечебное дело", "Волгоград"),
        ("2021 — 2023", "Российский университет дружбы народов (РУДН)", "Ординатура по дерматовенерологии", "Москва"),
        ("2021 — 2022", "Российский университет дружбы народов (РУДН)", "Трихология", "Москва"),
        ("2022 — 2023", "Первый профессиональный институт эстетики", "Косметология", "Москва"),
    ],

    c_title="Связаться со мной.",
    c_lead="Предложения о работе, сотрудничество или консультации — на русском, арабском или английском.",
    c_phone="Телефон", c_whatsapp="WhatsApp", c_whatsapp_v="Написать сообщение",
    c_email="Эл. почта", c_location="Город", c_location_v="Эр-Рияд, Саудовская Аравия",
    c_cv_title="Полное резюме.",
    c_cv_text="Опыт, процедуры, образование и лицензии на двух страницах.",

    foot_tagline="Карина Рауашде — врач-дерматовенеролог · Эр-Рияд, Саудовская Аравия",
    foot_pages="Разделы",
    foot_contact="Контакты",
    foot_lang="Язык",
    copyright="© 2026 Карина Рауашде. Все права защищены.",
)
