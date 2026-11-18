# Site content in three languages. Edit text here, then run:  python3 _src/build.py
# Facts come from "Karina CV 2026 (SMLE).pdf" (confirmed by the family 18.11.2026).

PHONE_DISPLAY = "+7 961 668-94-81"
PHONE_TEL = "+79616689481"
WHATSAPP = "https://wa.me/79616689481"
EMAIL = "karinar888@mail.ru"
CV_FILE = "Karina-Rauashde-CV.pdf"
SITE = "https://karina.rauashde.com/"

LANGS = ["en", "ar", "ru"]
PATHS = {"en": "", "ar": "ar/", "ru": "ru/"}
SWITCH_LABEL = {"en": "EN", "ar": "عربي", "ru": "RU"}
SWITCH_NAME = {"en": "English", "ar": "العربية", "ru": "Русский"}

T = {}

# ───────────────────────────── ENGLISH ─────────────────────────────
T["en"] = dict(
    dir="ltr",
    og_locale="en_US",
    title="Dr. Karina Rauashde — Dermatologist · Laser & Aesthetic Medicine",
    description="Dr. Karina Rauashde — dermatologist in Moscow with 5+ years of medical practice: "
                "skin, hair and nail disorders, minor surgery, Botox, fillers, lasers and IPL. "
                "Passed the Saudi Medical Licensure Examination (SMLE), 2026.",
    skip="Skip to content",
    brand="Dr. Karina Rauashde",
    nav=[("about", "About"), ("experience", "Experience"), ("procedures", "Procedures"),
         ("education", "Education"), ("contact", "Contact")],
    eyebrow="Dermatology · Trichology · Cosmetology",
    name_html='<span class="dr">Dr.</span> Karina<br>Rauashde',
    role="Dermatologist specializing in laser &amp; aesthetic medicine",
    lead="More than five years of medical practice treating disorders of the skin, hair and nails — "
         "from clinical dermatology and minor surgery to injectables and lasers.",
    cta_contact="Get in touch",
    cta_cv="Download CV",
    cv_note="PDF · English",
    meta=["Moscow, Russia", "SMLE passed · 2026", "Arabic · Russian · English"],
    img_alt="Dr. Karina Rauashde in a white blazer, putting on black medical gloves",

    about_label="About",
    about_title="Skin, hair and nails — treated with precision and care",
    about_p=[
        "I am a dermatologist with more than five years of experience as a doctor, focused on disorders of "
        "the skin, hair and nails. I diagnose and treat acute and chronic skin conditions — acne, rosacea, "
        "psoriasis, eczema and more — perform minor surgical procedures such as biopsies and excisions, and "
        "offer a full range of laser, injectable and aesthetic treatments.",
        "Every treatment plan is built around the patient’s skin type and skin tone. I studied General "
        "Medicine at Volgograd State Medical University, completed my dermatology residency and trichology "
        "training at RUDN University, and trained in cosmetology at the First Professional Institute of "
        "Aesthetics in Moscow.",
        "Arabic is my native language, and I also work in Russian and English. In November 2026 I passed "
        "the Saudi Medical Licensure Examination (SMLE).",
    ],
    stats=[("5+", "years of medical practice"), ("15+", "aesthetic &amp; laser procedures"),
           ("3", "working languages"), ("SMLE", "passed · November 2026")],

    exp_label="Experience",
    exp_title="Clinical experience",
    exp=[
        dict(period="2023 — present", role="Dermatologist",
             org="Elabuzhskaya Central Regional Hospital", place="Tatarstan, Russia",
             desc="Dermatology department of a regional hospital — diagnosis and treatment of acute and "
                  "chronic skin disorders.",
             bullets=[
                 "Diagnosis and treatment of acne, psoriasis, rosacea, warts, seborrheic dermatitis and eczema",
                 "Laser techniques to improve the appearance of the skin and treat skin conditions",
                 "Minor surgical procedures — biopsies and excisions",
                 "Skin-care counselling, including the correct use of topical medications",
                 "Anti-aging and anti-acne treatment plans for patients of all ages",
                 "Personalized treatment for every skin type and skin tone",
             ], chips=[]),
        dict(period="2023 — present", role="Dermatologist · aesthetic medicine",
             org="Beauty Medicine Private Clinic", place="Kazan, Russia",
             desc="Private dermatology clinic — aesthetic procedures and treatment of skin conditions. "
                  "More than fifteen procedures, from Botox and fillers to CO₂ lasers and IPL.",
             bullets=[],
             chips=["Botox &amp; fillers", "CO₂ &amp; erbium lasers", "IPL", "Biorevitalization",
                    "PRP", "PDO threads", "Peels &amp; Hydrafacial"]),
        dict(period="2023 — 2024", role="Trainee, Dermatology Department",
             org="Al Hadith Hospital", place="Aqaba, Jordan", desc="", bullets=[], chips=[]),
    ],

    proc_label="Procedures",
    proc_title="Treatments &amp; procedures",
    proc_intro="From medical dermatology to injectables and lasers — the procedures I perform.",
    proc=[
        ("syringe", "Injectables", [
            ("Botulinum toxin (Botox)", "Full face and neck"),
            ("Hyperhidrosis treatment", "Botox for underarms, hands and feet"),
            ("Dermal fillers", "Lips, jawline and chin, temples, cheeks, under-eye area, nasolabial folds"),
            ("Biorevitalization", "Skin boosters and biostimulators — face and body"),
            ("Mesotherapy", "Face and body"),
            ("PRP therapy", "Face, body and hair"),
            ("PDO mono threads", ""),
        ]),
        ("light", "Lasers &amp; devices", [
            ("CO₂ fractional laser resurfacing", ""),
            ("Non-ablative laser resurfacing", "1540 nm erbium-glass laser"),
            ("Laser treatment of telangiectasia", "Removal of small visible blood vessels"),
            ("IPL procedures", "Advanced certified specialist — Candela and DEKA"),
            ("Radio-wave electrosurgery", "Removal of skin tags and warts"),
        ]),
        ("drop", "Skin renewal", [
            ("Microdermabrasion", "Hydrafacial"),
            ("Chemical peels", ""),
            ("Anti-aging programs", "Personalized plans for every age, skin type and skin tone"),
        ]),
        ("stetho", "Medical dermatology", [
            ("Inflammatory skin disease", "Acne, rosacea, psoriasis, eczema, seborrheic dermatitis"),
            ("Hair, scalp and nails", "Trichology"),
            ("Minor surgery", "Biopsies and excisions; warts and skin tags"),
            ("Topical-therapy guidance", "Correct use of prescribed creams and medications"),
        ]),
    ],

    edu_label="Education",
    edu_title="Education &amp; licensing",
    edu=[
        ("2014 — 2021", "Volgograd State Medical University (VolgSMU)", "General Medicine", "Volgograd, Russia"),
        ("2021 — 2023", "RUDN University", "Residency in Dermatology", "Moscow, Russia"),
        ("2021 — 2022", "RUDN University", "Trichology", "Moscow, Russia"),
        ("2022 — 2023", "First Professional Institute of Aesthetics", "Cosmetology", "Moscow, Russia"),
    ],
    lic_label="Licenses &amp; exams",
    lic_status="Passed",
    lic_date="November 2026",
    lic_name="Saudi Medical Licensure Examination (SMLE)",
    lic_issuer="Saudi Commission for Health Specialties (SCFHS) · Prometric",
    langs_label="Languages",
    langs=[("Arabic", "native"), ("Russian", ""), ("English", "")],

    contact_label="Contact",
    contact_title="Let’s talk",
    contact_lead="For job opportunities, collaboration or consultations — in Arabic, Russian or English.",
    c_phone="Phone", c_whatsapp="WhatsApp", c_whatsapp_v="Send a message",
    c_email="Email", c_location="Based in", c_location_v="Moscow, Russia",
    c_cv="Download CV (PDF)",
    footer="© 2026 Dr. Karina Rauashde · Dermatologist",
)

# ───────────────────────────── ARABIC ─────────────────────────────
T["ar"] = dict(
    dir="rtl",
    og_locale="ar_SA",
    title="د. كارينا الرواشدة — أخصائية الأمراض الجلدية والليزر والتجميل",
    description="د. كارينا الرواشدة — طبيبة أمراض جلدية في موسكو بخبرة تزيد على 5 سنوات: أمراض الجلد والشعر "
                "والأظافر، الجراحة الصغرى، البوتوكس والفيلر والليزر. اجتازت اختبار الترخيص الطبي السعودي (SMLE) عام 2026.",
    skip="انتقل إلى المحتوى",
    brand="د. كارينا الرواشدة",
    nav=[("about", "نبذة"), ("experience", "الخبرة"), ("procedures", "الإجراءات"),
         ("education", "التعليم"), ("contact", "التواصل")],
    eyebrow="الأمراض الجلدية · طب الشعر · التجميل",
    name_html='<span class="dr">د.</span> كارينا<br>الرواشدة',
    role="أخصائية الأمراض الجلدية والليزر والتجميل",
    lead="أكثر من خمس سنوات من الممارسة الطبية في علاج أمراض الجلد والشعر والأظافر — "
         "من الأمراض الجلدية والجراحة الصغرى إلى الحقن التجميلية والليزر.",
    cta_contact="تواصل معي",
    cta_cv="تحميل السيرة الذاتية",
    cv_note="PDF · بالإنجليزية",
    meta=["موسكو، روسيا", "اجتياز SMLE · 2026", "العربية · الروسية · الإنجليزية"],
    img_alt="د. كارينا الرواشدة بسترة بيضاء ترتدي قفازات طبية سوداء",

    about_label="نبذة",
    about_title="عناية دقيقة بالبشرة والشعر والأظافر",
    about_p=[
        "طبيبة أمراض جلدية بخبرة تزيد على خمس سنوات في الممارسة الطبية، أركّز على أمراض الجلد والشعر والأظافر. "
        "أشخّص الأمراض الجلدية الحادة والمزمنة وأعالجها — كحب الشباب والوردية والصدفية والإكزيما وغيرها — "
        "وأُجري العمليات الجراحية الصغرى كأخذ الخزعات والاستئصال، إلى جانب مجموعة متكاملة من علاجات الليزر "
        "والحقن والإجراءات التجميلية.",
        "أصمّم كل خطة علاجية وفق نوع بشرة المريض ولونها. درست الطب العام في جامعة فولغوغراد الطبية الحكومية، "
        "وأتممت الإقامة في الأمراض الجلدية والتدريب في طب الشعر في جامعة الصداقة بين الشعوب الروسية (RUDN)، "
        "ودرست التجميل الطبي في المعهد المهني الأول للتجميل في موسكو.",
        "العربية لغتي الأم، وأعمل كذلك بالروسية والإنجليزية. اجتزت اختبار الترخيص الطبي السعودي (SMLE) "
        "في نوفمبر 2026.",
    ],
    stats=[("5+", "سنوات من الممارسة الطبية"), ("15+", "إجراءً تجميليًا وليزريًا"),
           ("3", "لغات عمل"), ("SMLE", "اجتياز · نوفمبر 2026")],

    exp_label="الخبرة",
    exp_title="الخبرة العملية",
    exp=[
        dict(period="2023 — حتى الآن", role="طبيبة أمراض جلدية",
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
        dict(period="2023 — حتى الآن", role="طبيبة جلدية وتجميل",
             org="عيادة خاصة للطب التجميلي", place="قازان، روسيا",
             desc="عيادة خاصة للأمراض الجلدية — إجراءات تجميلية وعلاج الأمراض الجلدية. أكثر من خمسة عشر إجراءً، "
                  "من البوتوكس والفيلر إلى ليزر CO₂ والضوء النبضي المكثف.",
             bullets=[],
             chips=["البوتوكس والفيلر", "ليزر CO₂ والإربيوم", "IPL", "إعادة إحياء البشرة",
                    "PRP", "خيوط PDO", "التقشير والهيدرافيشال"]),
        dict(period="2023 — 2024", role="متدربة في قسم الأمراض الجلدية",
             org="مستشفى الحديث", place="العقبة، الأردن", desc="", bullets=[], chips=[]),
    ],

    proc_label="الإجراءات",
    proc_title="العلاجات والإجراءات",
    proc_intro="من الأمراض الجلدية إلى الحقن التجميلية والليزر — الإجراءات التي أُجريها.",
    proc=[
        ("syringe", "الحقن التجميلية", [
            ("البوتوكس", "الوجه كاملًا والرقبة"),
            ("علاج فرط التعرّق", "بالبوتوكس للإبطين واليدين والقدمين"),
            ("الفيلر", "الشفاه، خط الفك والذقن، الصدغان، الوجنتان، منطقة تحت العين، الطيات الأنفية الشفوية"),
            ("إعادة إحياء البشرة", "معززات البشرة والمحفزات الحيوية — للوجه والجسم"),
            ("الميزوثيرابي", "للوجه والجسم"),
            ("البلازما الغنية بالصفائح الدموية (PRP)", "للوجه والجسم والشعر"),
            ("خيوط PDO الأحادية", ""),
        ]),
        ("light", "الليزر والأجهزة", [
            ("ليزر ثاني أكسيد الكربون الجزئي (CO₂ Fractional)", "لتجديد سطح البشرة"),
            ("تجديد البشرة بالليزر غير التقشيري", "ليزر الإربيوم جلاس بطول موجي 1540 نانومتر"),
            ("علاج توسّع الشعيرات الدموية بالليزر", "إزالة الأوعية الدموية الدقيقة الظاهرة"),
            ("الضوء النبضي المكثّف (IPL)", "أخصائية معتمدة بمستوى متقدم — Candela وDEKA"),
            ("الجراحة الكهربائية بالترددات الراديوية", "إزالة الزوائد الجلدية والثآليل"),
        ]),
        ("drop", "تجديد البشرة", [
            ("التقشير الدقيق للبشرة", "هيدرافيشال"),
            ("التقشير الكيميائي", ""),
            ("برامج مكافحة الشيخوخة", "خطط مخصصة لكل عمر ونوع بشرة ولونها"),
        ]),
        ("stetho", "الأمراض الجلدية", [
            ("الأمراض الجلدية الالتهابية", "حب الشباب، الوردية، الصدفية، الإكزيما، التهاب الجلد الدهني"),
            ("الشعر وفروة الرأس والأظافر", "طب الشعر (الترايكولوجي)"),
            ("الجراحة الصغرى", "الخزعات والاستئصال، الثآليل والزوائد الجلدية"),
            ("الإرشاد في العلاجات الموضعية", "الاستخدام الصحيح للكريمات والأدوية الموصوفة"),
        ]),
    ],

    edu_label="التعليم",
    edu_title="التعليم والترخيص",
    edu=[
        ("2014 — 2021", "جامعة فولغوغراد الطبية الحكومية", "الطب العام", "فولغوغراد، روسيا"),
        ("2021 — 2023", "جامعة الصداقة بين الشعوب الروسية (RUDN)", "الإقامة في الأمراض الجلدية", "موسكو، روسيا"),
        ("2021 — 2022", "جامعة الصداقة بين الشعوب الروسية (RUDN)", "طب الشعر وفروة الرأس (الترايكولوجي)", "موسكو، روسيا"),
        ("2022 — 2023", "المعهد المهني الأول للتجميل", "التجميل الطبي (الكوزمتولوجي)", "موسكو، روسيا"),
    ],
    lic_label="التراخيص والاختبارات",
    lic_status="ناجحة",
    lic_date="نوفمبر 2026",
    lic_name="اختبار الترخيص الطبي السعودي (SMLE)",
    lic_issuer="الهيئة السعودية للتخصصات الصحية (SCFHS) · بروميترك",
    langs_label="اللغات",
    langs=[("العربية", "اللغة الأم"), ("الروسية", ""), ("الإنجليزية", "")],

    contact_label="التواصل",
    contact_title="لنتواصل",
    contact_lead="لفرص العمل أو التعاون أو الاستشارات — بالعربية أو الروسية أو الإنجليزية.",
    c_phone="الهاتف", c_whatsapp="واتساب", c_whatsapp_v="مراسلة عبر واتساب",
    c_email="البريد الإلكتروني", c_location="مقيمة في", c_location_v="موسكو، روسيا",
    c_cv="تحميل السيرة الذاتية (PDF)",
    footer="© 2026 د. كارينا الرواشدة · أخصائية الأمراض الجلدية",
)

# ───────────────────────────── RUSSIAN ─────────────────────────────
T["ru"] = dict(
    dir="ltr",
    og_locale="ru_RU",
    title="Рауашде Карина Раедовна — врач-дерматовенеролог, косметолог",
    description="Карина Рауашде — врач-дерматовенеролог и косметолог в Москве, более 5 лет врачебной практики: "
                "заболевания кожи, волос и ногтей, малая хирургия, ботулинотерапия, филлеры, лазеры и IPL. "
                "Сдан Саудовский медицинский лицензионный экзамен (SMLE), 2026.",
    skip="Перейти к содержанию",
    brand="Карина Рауашде",
    nav=[("about", "Обо мне"), ("experience", "Опыт"), ("procedures", "Процедуры"),
         ("education", "Образование"), ("contact", "Контакты")],
    eyebrow="Дерматология · Трихология · Косметология",
    name_html='Карина<br>Рауашде',
    role="Врач-дерматовенеролог, специалист по лазерной и эстетической медицине",
    lead="Более пяти лет врачебной практики: заболевания кожи, волос и ногтей — "
         "от клинической дерматологии и малой хирургии до инъекционных методик и лазеров.",
    cta_contact="Связаться",
    cta_cv="Скачать резюме",
    cv_note="PDF · на английском",
    meta=["Москва", "SMLE сдан · 2026", "Русский · арабский · английский"],
    img_alt="Карина Рауашде в белом жакете надевает чёрные медицинские перчатки",

    about_label="Обо мне",
    about_title="Кожа, волосы и ногти — точность и забота",
    about_p=[
        "Врач-дерматовенеролог с опытом врачебной практики более пяти лет: заболевания кожи, волос и ногтей. "
        "Диагностирую и лечу острые и хронические дерматозы — акне, розацеа, псориаз, экзему и другие, "
        "выполняю малые хирургические вмешательства (биопсия, иссечение образований), провожу лазерные, "
        "инъекционные и эстетические процедуры.",
        "Схему лечения подбираю индивидуально — с учётом типа и тона кожи. Окончила Волгоградский "
        "государственный медицинский университет по специальности «Лечебное дело», ординатуру по "
        "дерматовенерологии и курс трихологии в РУДН, а также обучение косметологии в Первом "
        "профессиональном институте эстетики (Москва).",
        "Арабский — мой родной язык, также работаю на русском и английском. В ноябре 2026 года сдала "
        "Саудовский медицинский лицензионный экзамен (SMLE).",
    ],
    stats=[("5+", "лет врачебной практики"), ("15+", "эстетических и лазерных процедур"),
           ("3", "языка общения"), ("SMLE", "сдан · ноябрь 2026")],

    exp_label="Опыт",
    exp_title="Опыт работы",
    exp=[
        dict(period="2023 — наст. время", role="Врач-дерматовенеролог",
             org="Елабужская центральная районная больница", place="Республика Татарстан",
             desc="Дерматологическое отделение районной больницы — диагностика и лечение острых и "
                  "хронических заболеваний кожи.",
             bullets=[
                 "Диагностика и лечение акне, псориаза, розацеа, бородавок, себорейного дерматита и экземы",
                 "Лазерные методики для улучшения состояния кожи и лечения дерматозов",
                 "Малые хирургические вмешательства: биопсия, иссечение",
                 "Рекомендации по уходу за кожей и правильному применению наружных средств",
                 "Антивозрастные программы и схемы лечения акне для пациентов любого возраста",
                 "Индивидуальное лечение с учётом типа и тона кожи",
             ], chips=[]),
        dict(period="2023 — наст. время", role="Дерматолог-косметолог",
             org="Частная клиника эстетической медицины", place="Казань",
             desc="Частная дерматологическая клиника — эстетические процедуры и лечение заболеваний кожи. "
                  "Более пятнадцати методик: от ботулинотерапии и филлеров до CO₂-лазера и IPL.",
             bullets=[],
             chips=["Ботулинотерапия и филлеры", "CO₂- и эрбиевый лазер", "IPL", "Биоревитализация",
                    "PRP", "Нити PDO", "Пилинги и Hydrafacial"]),
        dict(period="2023 — 2024", role="Стажёр дерматологического отделения",
             org="Больница Al Hadith", place="Акаба, Иордания", desc="", bullets=[], chips=[]),
    ],

    proc_label="Процедуры",
    proc_title="Методики и процедуры",
    proc_intro="От клинической дерматологии до инъекций и лазеров — процедуры, которые я провожу.",
    proc=[
        ("syringe", "Инъекционная косметология", [
            ("Ботулинотерапия", "Всё лицо и шея"),
            ("Лечение гипергидроза", "Ботулотоксин: подмышечные впадины, ладони, стопы"),
            ("Контурная пластика филлерами", "Губы, линия челюсти и подбородок, виски, скулы, "
                                             "подглазничная область, носогубные складки"),
            ("Биоревитализация", "Скинбустеры и биостимуляторы — лицо и тело"),
            ("Мезотерапия", "Лицо и тело"),
            ("PRP-терапия", "Лицо, тело, волосы"),
            ("Мононити PDO", ""),
        ]),
        ("light", "Лазеры и аппаратные методики", [
            ("Фракционная CO₂-лазерная шлифовка", ""),
            ("Неаблятивное лазерное омоложение", "Эрбиевое стекло, 1540 нм"),
            ("Лазерное лечение телеангиэктазий", "Удаление сосудистых звёздочек"),
            ("IPL-процедуры", "Сертифицированный специалист продвинутого уровня — Candela и DEKA"),
            ("Радиоволновая электрохирургия", "Удаление папиллом и бородавок"),
        ]),
        ("drop", "Обновление кожи", [
            ("Микродермабразия", "Hydrafacial"),
            ("Химические пилинги", ""),
            ("Антивозрастные программы", "Индивидуальные схемы с учётом возраста, типа и тона кожи"),
        ]),
        ("stetho", "Клиническая дерматология", [
            ("Воспалительные заболевания кожи", "Акне, розацеа, псориаз, экзема, себорейный дерматит"),
            ("Волосы, кожа головы и ногти", "Трихология"),
            ("Малая хирургия", "Биопсия и иссечение, удаление бородавок и папиллом"),
            ("Наружная терапия", "Подбор средств и обучение правильному применению"),
        ]),
    ],

    edu_label="Образование",
    edu_title="Образование и лицензирование",
    edu=[
        ("2014 — 2021", "Волгоградский государственный медицинский университет (ВолгГМУ)", "Лечебное дело", "Волгоград"),
        ("2021 — 2023", "Российский университет дружбы народов (РУДН)", "Ординатура по дерматовенерологии", "Москва"),
        ("2021 — 2022", "Российский университет дружбы народов (РУДН)", "Трихология", "Москва"),
        ("2022 — 2023", "Первый профессиональный институт эстетики", "Косметология", "Москва"),
    ],
    lic_label="Лицензии и экзамены",
    lic_status="Сдан",
    lic_date="Ноябрь 2026",
    lic_name="Саудовский медицинский лицензионный экзамен (SMLE)",
    lic_issuer="Саудовская комиссия по специальностям здравоохранения (SCFHS) · Prometric",
    langs_label="Языки",
    langs=[("Арабский", "родной"), ("Русский", ""), ("Английский", "")],

    contact_label="Контакты",
    contact_title="Связаться со мной",
    contact_lead="Предложения о работе, сотрудничество или консультации — на русском, арабском или английском.",
    c_phone="Телефон", c_whatsapp="WhatsApp", c_whatsapp_v="Написать сообщение",
    c_email="Эл. почта", c_location="Город", c_location_v="Москва, Россия",
    c_cv="Скачать резюме (PDF)",
    footer="© 2026 Рауашде Карина Раедовна · врач-дерматовенеролог",
)
