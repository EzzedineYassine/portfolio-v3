import os
import subprocess
import shutil

OUTPUT_DIR = r"c:\Users\yassi\portfolio-website\Portfolio\assets"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
ORIGINAL_PDF = r"C:\Users\yassi\.gemini\antigravity\brain\7616c9ea-6e6a-4a5c-b64b-6b6e8f2d0932\.user_uploaded\media_1791133246974.pdf"

# 1. Ensure English CV is the exact original uploaded PDF
shutil.copyfile(ORIGINAL_PDF, os.path.join(OUTPUT_DIR, "cv-en.pdf"))
shutil.copyfile(ORIGINAL_PDF, os.path.join(OUTPUT_DIR, "cv.pdf"))
print("Copied original uploaded PDF to cv-en.pdf and cv.pdf")

CSS_BASE = """
@page {
    size: A4;
    margin: 10mm 14mm 10mm 14mm;
}
* {
    box-sizing: border-box;
}
body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #111827;
    margin: 0;
    padding: 0;
    font-size: 8.8pt;
    line-height: 1.32;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
.header {
    text-align: center;
    margin-bottom: 8px;
}
.name {
    font-size: 21pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    margin: 0 0 2px 0;
    color: #0b192c;
    text-transform: none;
}
.title {
    font-size: 10.5pt;
    font-weight: 600;
    color: #1f2937;
    margin-bottom: 3px;
    letter-spacing: 0.3px;
}
.contact-line {
    font-size: 8.5pt;
    color: #374151;
    line-height: 1.4;
}
.contact-line a {
    color: #183a5a;
    text-decoration: none;
}
.section-header {
    font-size: 9.8pt;
    font-weight: 700;
    color: #183a5a;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    border-bottom: 0.8px solid #183a5a;
    padding-bottom: 1.5px;
    margin-top: 7px;
    margin-bottom: 4px;
}
.entry-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.8pt;
    margin-top: 3.5px;
    margin-bottom: 1px;
}
.entry-title {
    font-weight: 700;
    color: #111827;
}
.entry-date {
    font-style: italic;
    color: #374151;
    white-space: nowrap;
    font-size: 8.5pt;
}
.entry-sub {
    font-style: italic;
    color: #4b5563;
    font-size: 8.4pt;
    margin-bottom: 2px;
}
ul.bullets {
    margin: 1.5px 0 3px 0;
    padding-left: 14px;
    list-style-type: square;
}
ul.bullets li {
    margin-bottom: 1.5px;
    font-size: 8.6pt;
    line-height: 1.28;
    color: #1f2937;
}
.skills-line {
    margin: 2px 0;
    font-size: 8.6pt;
    line-height: 1.32;
}
.skills-line strong {
    font-weight: 700;
    color: #111827;
}
.cert-item {
    margin: 2px 0;
    font-size: 8.6pt;
}
.cert-item strong {
    font-weight: 700;
}
.languages-row {
    margin-top: 2px;
    font-size: 8.8pt;
}
.languages-row strong {
    font-weight: 700;
}
"""

CSS_RTL = """
body {
    direction: rtl;
    text-align: right;
    font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
}
.header {
    text-align: center;
}
.contact-line {
    text-align: center;
}
.entry-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.entry-sub {
    font-style: italic;
    color: #4b5563;
    font-size: 8.4pt;
    margin-bottom: 2px;
}
ul.bullets {
    padding-left: 0;
    padding-right: 18px;
    list-style-type: square;
    text-align: right;
}
ul.bullets li {
    text-align: right;
    margin-bottom: 2px;
    line-height: 1.34;
}
.skills-row {
    display: flex;
    align-items: baseline;
    margin: 2.5px 0;
    font-size: 8.6pt;
    line-height: 1.32;
}
.skills-cat {
    font-weight: 700;
    color: #111827;
    white-space: nowrap;
    margin-left: 8px;
    flex-shrink: 0;
}
.skills-items {
    direction: ltr;
    text-align: left;
    flex-grow: 1;
}
.cert-row {
    direction: ltr;
    text-align: right;
    margin: 2.5px 0;
    font-size: 8.6pt;
}
.cert-row strong {
    font-weight: 700;
}
.languages-row {
    display: flex;
    justify-content: flex-start;
    gap: 24px;
    margin-top: 2px;
    font-size: 8.8pt;
    text-align: right;
}
"""

FR_HTML = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<style>
{CSS_BASE}
</style>
</head>
<body>

<div class="header">
    <div class="name">Yassine EZZEDINE</div>
    <div class="title">Candidat PFE en Data Science / IA</div>
    <div class="contact-line">
        Nabeul, Tunisie &nbsp;|&nbsp; +216 20 208 038 &nbsp;|&nbsp; <a href="mailto:yassineezzediney2g@gmail.com">yassineezzediney2g@gmail.com</a>
    </div>
    <div class="contact-line">
        <a href="https://linkedin.com/in/yassin-ezzedine/">linkedin.com/in/yassin-ezzedine/</a> &nbsp;|&nbsp;
        <a href="https://github.com/EzzedineYassine">github.com/EzzedineYassine</a> &nbsp;|&nbsp;
        <a href="https://yassineezzedine.dev">yassineezzedine.dev</a>
    </div>
</div>

<div class="section-header">Profil</div>
<div style="font-size: 8.6pt; line-height: 1.34; margin: 2px 0 4px 0;">
Étudiant en 3<sup>ème</sup> année de Licence en Informatique de Gestion (spécialité Business Intelligence / Décisionnel), à la recherche d'un stage de fin d'études (PFE) en Data Science ou Intelligence Artificielle. Solides compétences pratiques en Python, Pandas, NumPy, SQL, statistiques, nettoyage de données et Machine Learning, renforcées par un stage chez Tunisie Telecom et plusieurs projets clients rémunérés menés en 2026.
</div>

<div class="section-header">Formation</div>
<div class="entry-header">
    <span class="entry-title">Licence en Informatique de Gestion – Business Intelligence</span>
    <span class="entry-date">2024 – 2027</span>
</div>
<div class="entry-sub">FSEG Nabeul, Tunisie</div>

<div class="entry-header">
    <span class="entry-title">Baccalauréat en Sciences de l'Informatique – Mention : Assez Bien</span>
    <span class="entry-date">2024</span>
</div>
<div class="entry-sub">Nabeul, Tunisie</div>

<div class="section-header">Expérience</div>
<div class="entry-header">
    <span class="entry-title">Tunisie Telecom – Stagiaire en Développement d'Applications</span>
    <span class="entry-date">Juillet 2026</span>
</div>
<div class="entry-sub">Nabeul, Tunisie</div>
<ul class="bullets">
    <li>Conception et développement d'une application de gestion des tâches et d'une application de gestion de workflow avec la stack MERN et MongoDB.</li>
    <li>Intervention sur l'ensemble de l'architecture applicative et des bases de données en environnement de développement local, en autonomie et en collaboration d'équipe.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Projets Clients Rémunérés</span>
    <span class="entry-date">2026</span>
</div>
<ul class="bullets">
    <li><strong>Phantom Stickers</strong> | MERN, Supabase : Plateforme e-commerce complète avec authentification administrateur, tableau de bord de gestion, CRUD produits et déploiement Vercel. Démo en ligne.</li>
    <li><strong>Moto Parts Stock Manager</strong> | Flutter, SQLite, Supabase : Co-développement et livraison d'une application de gestion d'inventaire pour un commerce de pièces moto (Mobile et PC), gestion des stocks, alertes, stockage SQLite local et synchronisation cloud Supabase.</li>
    <li><strong>Cafément</strong> | Web : Menu numérique accessible par QR Code avec accès direct aux avis Google ; conçu et déployé en conditions réelles pour le client.</li>
    <li><strong>Hôtel Amira</strong> | Frontend Web : Développement de l'interface frontend d'un site hôtelier professionnel conformément au cahier des charges client.</li>
</ul>

<div class="section-header">Projets Personnels</div>
<div class="entry-header">
    <span class="entry-title">Segmentation Client et Analyse du Panier d'Achat</span>
    <span class="entry-date">2025</span>
</div>
<div class="entry-sub">Python, Pandas, NumPy, Scikit-learn, MLxtend, PyQt5</div>
<ul class="bullets">
    <li>Nettoyage des données transactionnelles, analyse RFM, application du clustering K-Means pour la segmentation client et algorithme Apriori pour l'extraction de règles d'association.</li>
    <li>Conception d'une interface graphique interactive PyQt5 pour la restitution des résultats analytiques.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Système de Recommandation de Films</span>
    <span class="entry-date"></span>
</div>
<div class="entry-sub">Python, Pandas, Scikit-learn, Streamlit</div>
<ul class="bullets">
    <li>Développement d'une application interactive de recommandation avec Pandas et Scikit-learn, exploitant CountVectorizer et la similarité cosinus pour des recommandations basées sur le contenu textuel.</li>
</ul>

<div class="section-header">Compétences Techniques</div>
<div class="skills-line"><strong>Data Science / ML :</strong> Python, Pandas, NumPy, Scikit-learn, Statistiques, Nettoyage de données, EDA, Machine Learning, Analyse RFM, K-Means, Apriori</div>
<div class="skills-line"><strong>Programmation :</strong> Python, Java, PHP, JavaScript, C, SQL, PL/SQL</div>
<div class="skills-line"><strong>Web / Applications :</strong> React, Node.js, Express.js, MERN, REST APIs, HTML/CSS, Flutter</div>
<div class="skills-line"><strong>Bases de données / Outils :</strong> MongoDB, Supabase, SQLite, Git, GitHub, Linux, Jupyter, Streamlit, PyQt5, Vercel</div>

<div class="section-header">Certifications</div>
<div class="cert-item"><strong>Google Advanced Data Analytics</strong> – Google</div>
<div class="cert-item"><strong>Google AI Essentials</strong> – Google</div>
<div class="cert-item"><strong>AWS Cloud Solutions Architect Professional</strong> – AWS</div>

<div class="section-header">Langues</div>
<div class="languages-row">
    <strong>Arabe :</strong> Langue maternelle &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>Français :</strong> Avancé &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>Anglais :</strong> Courant &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>Allemand :</strong> Débutant (en cours d'apprentissage)
</div>

</body>
</html>
"""

DE_HTML = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<style>
{CSS_BASE}
</style>
</head>
<body>

<div class="header">
    <div class="name">Yassine EZZEDINE</div>
    <div class="title">Data Science / KI Abschlussarbeitskandidat (PFE)</div>
    <div class="contact-line">
        Nabeul, Tunesien &nbsp;|&nbsp; +216 20 208 038 &nbsp;|&nbsp; <a href="mailto:yassineezzediney2g@gmail.com">yassineezzediney2g@gmail.com</a>
    </div>
    <div class="contact-line">
        <a href="https://linkedin.com/in/yassin-ezzedine/">linkedin.com/in/yassin-ezzedine/</a> &nbsp;|&nbsp;
        <a href="https://github.com/EzzedineYassine">github.com/EzzedineYassine</a> &nbsp;|&nbsp;
        <a href="https://yassineezzedine.dev">yassineezzedine.dev</a>
    </div>
</div>

<div class="section-header">Profil</div>
<div style="font-size: 8.6pt; line-height: 1.34; margin: 2px 0 4px 0;">
Wirtschaftsinformatik-Student im 3. Studienjahr (Schwerpunkt Business Intelligence), auf der Suche nach einem Abschlussarbeitspraktikum (PFE) im Bereich Data Science oder Künstliche Intelligenz. Fundierte praktische Erfahrung mit Python, Pandas, NumPy, SQL, Statistik, Datenbereinigung und maschinellem Lernen, untermauert durch ein Praktikum bei Tunisie Telecom und bezahlte Kundenprojekte im Jahr 2026.
</div>

<div class="section-header">Ausbildung</div>
<div class="entry-header">
    <span class="entry-title">Bachelor in Wirtschaftsinformatik – Business Intelligence</span>
    <span class="entry-date">2024 – 2027</span>
</div>
<div class="entry-sub">FSEG Nabeul, Tunesien</div>

<div class="entry-header">
    <span class="entry-title">Abitur mit Schwerpunkt Informatik – Prädikat: Gut (Assez Bien)</span>
    <span class="entry-date">2024</span>
</div>
<div class="entry-sub">Nabeul, Tunesien</div>

<div class="section-header">Berufserfahrung</div>
<div class="entry-header">
    <span class="entry-title">Tunisie Telecom – Praktikant Anwendungsentwicklung</span>
    <span class="entry-date">Juli 2026</span>
</div>
<div class="entry-sub">Nabeul, Tunesien</div>
<ul class="bullets">
    <li>Entwicklung einer Aufgaben- und einer Workflow-Management-Anwendung mit dem MERN-Stack und MongoDB.</li>
    <li>Arbeiten an Anwendungs- und Datenbankkomponenten in lokaler Entwicklungsumgebung, sowohl selbstständig als auch im Team.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Bezahlte Kundenprojekte</span>
    <span class="entry-date">2026</span>
</div>
<ul class="bullets">
    <li><strong>Phantom Stickers</strong> | MERN, Supabase: Full-Stack E-Commerce-Plattform mit Admin-Authentifizierung, Dashboard, Produkt-CRUD und Vercel-Deployment. Live-Demo.</li>
    <li><strong>Moto Parts Stock Manager</strong> | Flutter, SQLite, Supabase: Co-Entwicklung und Auslieferung einer Bestandsverwaltungs-App für einen Motorradteilehändler (Mobile & PC), Bestandsmanagement, Benachrichtigungen, lokale SQLite-Datenbank und Supabase-Backup.</li>
    <li><strong>Cafément</strong> | Web: QR-Code-basierte digitale Speisekarte mit direktem Google-Bewertungszugang; für den Kundenbetrieb bereitgestellt.</li>
    <li><strong>Hotel Amira</strong> | Frontend Web: Entwicklung des Frontends einer Hotel-Website gemäß den Kundenanforderungen.</li>
</ul>

<div class="section-header">Persönliche Projekte</div>
<div class="entry-header">
    <span class="entry-title">Kundensegmentierung und Warenkorbanalyse</span>
    <span class="entry-date">2025</span>
</div>
<div class="entry-sub">Python, Pandas, NumPy, Scikit-learn, MLxtend, PyQt5</div>
<ul class="bullets">
    <li>Bereinigung von Transaktionsdaten, RFM-Analyse, K-Means-Clustering zur Kundensegmentierung und Apriori-Algorithmus für Assoziationsregeln.</li>
    <li>Entwicklung einer PyQt5-Benutzeroberfläche zur Präsentation der Analyseergebnisse.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Film-Empfehlungssystem</span>
    <span class="entry-date"></span>
</div>
<div class="entry-sub">Python, Pandas, Scikit-learn, Streamlit</div>
<ul class="bullets">
    <li>Erstellung einer interaktiven Empfehlungsanwendung mit Pandas und Scikit-learn unter Verwendung von CountVectorizer und Kosinus-Ähnlichkeit für textbasierte Empfehlungen.</li>
</ul>

<div class="section-header">Technische Fähigkeiten</div>
<div class="skills-line"><strong>Data Science / ML:</strong> Python, Pandas, NumPy, Scikit-learn, Statistik, Datenbereinigung, Explorative Datenanalyse, Machine Learning, RFM-Analyse, K-Means, Apriori</div>
<div class="skills-line"><strong>Programmierung:</strong> Python, Java, PHP, JavaScript, C, SQL, PL/SQL</div>
<div class="skills-line"><strong>Web / Anwendungen:</strong> React, Node.js, Express.js, MERN, REST APIs, HTML/CSS, Flutter</div>
<div class="skills-line"><strong>Datenbanken / Tools:</strong> MongoDB, Supabase, SQLite, Git, GitHub, Linux, Jupyter, Streamlit, PyQt5, Vercel</div>

<div class="section-header">Zertifizierungen</div>
<div class="cert-item"><strong>Google Advanced Data Analytics</strong> – Google</div>
<div class="cert-item"><strong>Google AI Essentials</strong> – Google</div>
<div class="cert-item"><strong>AWS Cloud Solutions Architect Professional</strong> – AWS</div>

<div class="section-header">Sprachen</div>
<div class="languages-row">
    <strong>Arabisch:</strong> Muttersprache &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>Französisch:</strong> Verhandlungssicher &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>Englisch:</strong> Fließend &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>Deutsch:</strong> Grundkenntnisse (im Lernprozess)
</div>

</body>
</html>
"""

AR_HTML = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<style>
{CSS_BASE}
{CSS_RTL}
</style>
</head>
<body>

<div class="header">
    <div class="name">يسين عزالدين</div>
    <div class="title">مرشح لمشروع تخرج (PFE) في علوم البيانات والذكاء الاصطناعي</div>
    <div class="contact-line">
        نابل، تونس &nbsp;|&nbsp; <span dir="ltr">+216 20 208 038</span> &nbsp;|&nbsp; <a href="mailto:yassineezzediney2g@gmail.com">yassineezzediney2g@gmail.com</a>
    </div>
    <div class="contact-line" dir="ltr">
        <a href="https://linkedin.com/in/yassin-ezzedine/">linkedin.com/in/yassin-ezzedine/</a> &nbsp;|&nbsp;
        <a href="https://github.com/EzzedineYassine">github.com/EzzedineYassine</a> &nbsp;|&nbsp;
        <a href="https://yassineezzedine.dev">yassineezzedine.dev</a>
    </div>
</div>

<div class="section-header">الملف التعريفي</div>
<div style="font-size: 8.6pt; line-height: 1.36; margin: 2px 0 4px 0;">
طالب في السنة الثالثة إجازة في الإعلامية الموجهة للتصرف (Business Computing) تخصص ذكاء الأعمال (Business Intelligence)، أبحث عن تدريب مشروع تخرج (PFE) في مجال علوم البيانات أو الذكاء الاصطناعي. خبرة عملية متينة في Python وPandas وNumPy وSQL والإحصاء وتنظيف البيانات والتعلم الآلي، مدعومة بتدريب ميداني في شركة اتصالات تونس (Tunisie Telecom) ومشاريع تجارية ناجحة للعملاء في عام 2026.
</div>

<div class="section-header">التعليم</div>
<div class="entry-header">
    <span class="entry-title">الإجازة في إعلامية التصرف – ذكاء الأعمال (Business Intelligence)</span>
    <span class="entry-date" dir="ltr">2024 – 2027</span>
</div>
<div class="entry-sub">كلية العلوم الاقتصادية والتصرف بنابل (FSEG Nabeul)، تونس</div>

<div class="entry-header">
    <span class="entry-title">بكالوريا في علوم الإعلامية – التقدير: قريب من الحسن</span>
    <span class="entry-date" dir="ltr">2024</span>
</div>
<div class="entry-sub">نابل، تونس</div>

<div class="section-header">الخبرة المهنية</div>
<div class="entry-header">
    <span class="entry-title">اتصالات تونس (Tunisie Telecom) – متدرب في تطوير التطبيقات</span>
    <span class="entry-date">جويلية 2026</span>
</div>
<div class="entry-sub">نابل، تونس</div>
<ul class="bullets">
    <li>&rlm;تطوير تطبيق لإدارة المهام وتطبيق لإدارة مسارات العمل (Workflow Management) باستخدام حزمة MERN وقاعدة بيانات MongoDB.</li>
    <li>&rlm;العمل على مكونات التطبيق وقواعد البيانات في بيئة تطوير محلية، بشكل مستقل وضمن فريق العمل.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">مشاريع تجارية للعملاء (Paid Client Projects)</span>
    <span class="entry-date" dir="ltr">2026</span>
</div>
<ul class="bullets">
    <li>&rlm;<strong>Phantom Stickers</strong> | MERN, Supabase : منصة تجارة إلكترونية متكاملة مع مصادقة المشرف، لوحة تحكم، إدارة كاملة للمنتجات ونشر مباشر على Vercel.&rlm;</li>
    <li>&rlm;<strong>Moto Parts Stock Manager</strong> | Flutter, SQLite, Supabase : تطوير وتسليم تطبيق لإدارة مخزون ومبيعات قطع غيار الدراجات النارية، يدعم الهاتف والكمبيوتر، تنبيهات المخزون، تخزين محلي بـ SQLite ومزامنة عبر Supabase.&rlm;</li>
    <li>&rlm;<strong>Cafément</strong> | Web : قائمة طعام رقمية عبر رمز الاستجابة السريعة (QR Code) مع وصول مباشر لتقييمات Google؛ طُورت وخُصصت بالكامل للعميل.</li>
    <li>&rlm;<strong>Hotel Amira</strong> | Frontend Web : تطوير الواجهة الأمامية لموقع فندقي احترافي وفقاً لمتطلبات وتصميم العميل.</li>
</ul>

<div class="section-header">المشاريع الشخصية</div>
<div class="entry-header">
    <span class="entry-title">تقسيم العملاء وتحليل سلة المشتريات (Customer Segmentation & Market Basket Analysis)</span>
    <span class="entry-date" dir="ltr">2025</span>
</div>
<div class="entry-sub" dir="ltr" style="text-align: right;">Python, Pandas, NumPy, Scikit-learn, MLxtend, PyQt5</div>
<ul class="bullets">
    <li>&rlm;تنظيف البيانات المعاملاتية، إجراء تحليل RFM، تطبيق خوارزمية K-Means لتقسيم العملاء، واستخدام خوارزمية Apriori لاستخراج قواعد الارتباط الأكثر تكراراً.</li>
    <li>&rlm;بناء واجهة رسومية تفاعلية باستخدام PyQt5 لعرض النتائج والتحليلات البيانية.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">نظام توصية الأفلام (Movie Recommender System)</span>
    <span class="entry-date"></span>
</div>
<div class="entry-sub" dir="ltr" style="text-align: right;">Python, Pandas, Scikit-learn, Streamlit</div>
<ul class="bullets">
    <li>&rlm;بناء تطبيق تفاعلي لنظام التوصيات باستخدام Pandas وScikit-learn مع CountVectorizer وCosine Similarity للتوصية المبنية على محتوى النصوص.</li>
</ul>

<div class="section-header">المهارات التقنية</div>
<div class="skills-row">
    <span class="skills-cat">علوم البيانات والذكاء الاصطناعي :</span>
    <span class="skills-items">Python, Pandas, NumPy, Scikit-learn, Statistics, Data Cleaning, EDA, Machine Learning, RFM Analysis, K-Means, Apriori</span>
</div>
<div class="skills-row">
    <span class="skills-cat">لغات البرمجة :</span>
    <span class="skills-items">Python, Java, PHP, JavaScript, C, SQL, PL/SQL</span>
</div>
<div class="skills-row">
    <span class="skills-cat">تطوير الويب والتطبيقات :</span>
    <span class="skills-items">React, Node.js, Express.js, MERN Stack, REST APIs, HTML/CSS, Flutter</span>
</div>
<div class="skills-row">
    <span class="skills-cat">قواعد البيانات والأدوات :</span>
    <span class="skills-items">MongoDB, Supabase, SQLite, Git, GitHub, Linux, Jupyter, Streamlit, PyQt5, Vercel</span>
</div>

<div class="section-header">الشهادات</div>
<div class="cert-row"><strong>Google Advanced Data Analytics</strong> – Google</div>
<div class="cert-row"><strong>Google AI Essentials</strong> – Google</div>
<div class="cert-row"><strong>AWS Cloud Solutions Architect Professional</strong> – AWS</div>

<div class="section-header">اللغات</div>
<div class="languages-row">
    <strong>العربية :</strong> اللغة الأم &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>الفرنسية :</strong> متقدم &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>الإنجليزية :</strong> طليق &nbsp;&nbsp;&nbsp;&nbsp;
    <strong>الألمانية :</strong> مبتدئ (قيد التعلّم)
</div>

</body>
</html>
"""

# Write HTML files
files = [
    ("cv-fr.html", FR_HTML, "cv-fr.pdf"),
    ("cv-de.html", DE_HTML, "cv-de.pdf"),
    ("cv-ar.html", AR_HTML, "cv-ar.pdf")
]

for html_file, html_content, pdf_file in files:
    html_path = os.path.join(OUTPUT_DIR, html_file)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Wrote {html_path}")
