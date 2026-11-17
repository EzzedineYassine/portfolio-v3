import os
import subprocess
import shutil
import pypdf

OUTPUT_DIR = r"c:\Users\yassi\portfolio-website\Portfolio\assets"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

CSS_BASE = """
@page {
    size: A4;
    margin: 8mm 12mm 8mm 12mm;
}
* {
    box-sizing: border-box;
}
body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #111827;
    margin: 0;
    padding: 0;
    font-size: 8.2pt;
    line-height: 1.25;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
.header {
    text-align: center;
    margin-bottom: 5px;
}
.name {
    font-size: 19pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    margin: 0 0 1px 0;
    color: #0b192c;
}
.title {
    font-size: 9.8pt;
    font-weight: 600;
    color: #1f2937;
    margin-bottom: 2px;
    letter-spacing: 0.3px;
}
.contact-line {
    font-size: 8pt;
    color: #374151;
    line-height: 1.35;
}
.contact-line a {
    color: #183a5a;
    text-decoration: none;
}
.section-header {
    font-size: 9.2pt;
    font-weight: 700;
    color: #183a5a;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    border-bottom: 0.8px solid #183a5a;
    padding-bottom: 1px;
    margin-top: 5px;
    margin-bottom: 3px;
}
.entry-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.2pt;
    margin-top: 2.5px;
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
    font-size: 7.8pt;
}
.entry-sub {
    font-style: italic;
    color: #4b5563;
    font-size: 7.8pt;
    margin-bottom: 1px;
}
ul.bullets {
    margin: 1px 0 2px 0;
    padding-left: 13px;
    list-style-type: square;
}
ul.bullets li {
    margin-bottom: 1px;
    font-size: 8pt;
    line-height: 1.22;
    color: #1f2937;
}
.skills-line {
    margin: 1.5px 0;
    font-size: 8pt;
    line-height: 1.24;
}
.skills-line strong {
    font-weight: 700;
    color: #111827;
}
.cert-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5px 10px;
    margin-top: 1px;
    font-size: 7.9pt;
}
.cert-item strong {
    font-weight: 700;
}
.languages-row {
    margin-top: 1.5px;
    font-size: 8pt;
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
    font-size: 7.8pt;
    margin-bottom: 1px;
}
ul.bullets {
    padding-left: 0;
    padding-right: 16px;
    list-style-type: square;
    text-align: right;
}
ul.bullets li {
    text-align: right;
    margin-bottom: 1px;
    line-height: 1.25;
}
.skills-row {
    display: flex;
    align-items: baseline;
    margin: 1.5px 0;
    font-size: 8pt;
    line-height: 1.24;
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
.cert-grid-rtl {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5px 10px;
    margin-top: 1px;
    font-size: 7.9pt;
    direction: ltr;
    text-align: left;
}
.languages-row-rtl {
    display: flex;
    justify-content: flex-start;
    gap: 20px;
    margin-top: 1.5px;
    font-size: 8pt;
    text-align: right;
}
"""

EN_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Yassine Ezzedine — CV</title>
<style>
{CSS_BASE}
</style>
</head>
<body>

<div class="header">
    <div class="name">Yassine EZZEDINE</div>
    <div class="title">Full-Stack Software Engineer &amp; Data / AI Specialist</div>
    <div class="contact-line">
        Nabeul, Tunisia &nbsp;|&nbsp; +216 20 208 038 &nbsp;|&nbsp; <a href="mailto:yassineezzediney2g@gmail.com">yassineezzediney2g@gmail.com</a>
    </div>
    <div class="contact-line">
        <a href="https://linkedin.com/in/yassin-ezzedine/">linkedin.com/in/yassin-ezzedine/</a> &nbsp;|&nbsp;
        <a href="https://github.com/EzzedineYassine">github.com/EzzedineYassine</a> &nbsp;|&nbsp;
        <a href="https://yassineezzedine.dev">yassineezzedine.dev</a>
    </div>
</div>

<div class="section-header">Profile</div>
<div style="font-size: 8pt; line-height: 1.25; margin: 1.5px 0 3px 0;">
Third-year Business Computing student specializing in Business Intelligence (FSEG Nabeul), seeking a PFE internship in Data Science, Artificial Intelligence, or Full-Stack Engineering. Experienced in building production web applications and data platforms with React, Next.js, FastAPI, Python, SQL, and Supabase, supported by an engineering internship at Tunisie Telecom developing an HR management system, and commercial platforms including D.TN Audio Architecture.
</div>

<div class="section-header">Education</div>
<div class="entry-header">
    <span class="entry-title">Licence in Business Computing – Business Intelligence</span>
    <span class="entry-date">2024 – 2027</span>
</div>
<div class="entry-sub">FSEG Nabeul, Tunisia</div>

<div class="entry-header">
    <span class="entry-title">Baccalaureate in Computer Science – Honors: Assez Bien</span>
    <span class="entry-date">2024</span>
</div>
<div class="entry-sub">Nabeul, Tunisia</div>

<div class="section-header">Professional Experience</div>
<div class="entry-header">
    <span class="entry-title">Tunisie Telecom – Software Engineering Intern</span>
    <span class="entry-date">July 2026</span>
</div>
<div class="entry-sub">Nabeul, Tunisia</div>
<ul class="bullets">
    <li><strong>HR Management System:</strong> Designed and implemented an end-to-end human resources and leave management platform with 11 operational modules (employee dossier, leave balance tracking, request lifecycle, approval audit trails, printable reports) using Python, SQLite, and interactive frontend.</li>
    <li>Developed internal task and workflow automation applications with Python, Java, and the MERN stack with MongoDB in local staging environments.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Commercial Client Projects</span>
    <span class="entry-date">2026</span>
</div>
<ul class="bullets">
    <li><strong>D.TN Audio Architecture:</strong> Commercial digital music marketplace &amp; beat licensing platform built with Next.js (App Router), TypeScript, Supabase PostgreSQL (Row Level Security), Web Audio API waveform scrubbing, tamper-proof checkout, and trilingual RTL engine.</li>
    <li><strong>Phantom Stickers:</strong> Full-stack e-commerce application with MERN stack, Supabase, role-based admin dashboard, catalog CRUD, and Vercel deployment.</li>
    <li><strong>Moto Parts Stock Manager:</strong> Inventory management application delivered for a motorcycle parts retailer (Mobile &amp; PC) using Flutter, SQLite, and Supabase.</li>
</ul>

<div class="section-header">Technical Projects</div>
<div class="entry-header">
    <span class="entry-title">Attritex – Customer Retention &amp; ARR Risk Intelligence</span>
    <span class="entry-date">FastAPI, React 19, TypeScript, Scikit-learn</span>
</div>
<ul class="bullets">
    <li>Engineered an ML classification platform quantifying ARR risk and feature importance with automated retention playbooks; tested with 44 Pytest cases.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">AWS Retail Data Lake &amp; Infrastructure Pipeline</span>
    <span class="entry-date">Terraform (IaC), AWS S3, Lambda, Glue, Athena</span>
</div>
<ul class="bullets">
    <li>Built an event-driven serverless POS data lake with Terraform IaC, S3 data quality quarantine gates, Glue Data Catalog partitions, and Athena SQL queries.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Customer Segmentation &amp; Market Basket Analysis</span>
    <span class="entry-date">Python, Scikit-learn, PyQt5</span>
</div>
<ul class="bullets">
    <li>Executed RFM analysis, K-Means clustering, and Apriori association rule mining on retail transaction data with a desktop PyQt5 analytical GUI.</li>
</ul>

<div class="section-header">Technical Skills</div>
<div class="skills-line"><strong>Data Science / AI / ML:</strong> Python, Pandas, NumPy, Scikit-learn, Statistics, Data Cleaning, EDA, Machine Learning, RFM, K-Means, Apriori</div>
<div class="skills-line"><strong>Web / Full-Stack:</strong> React, Next.js, TypeScript, JavaScript, Node.js, Express.js, FastAPI, REST APIs, HTML5, CSS3, Tailwind CSS, Flutter</div>
<div class="skills-line"><strong>Cloud / Databases / Tools:</strong> AWS (S3, Lambda, Glue, Athena), Terraform, Supabase, PostgreSQL, MongoDB, SQLite, MySQL, Git, GitHub, Linux, Vercel</div>

<div class="section-header">Certifications</div>
<div class="cert-grid">
    <div class="cert-item"><strong>Microsoft AI &amp; ML Engineering</strong> – Microsoft</div>
    <div class="cert-item"><strong>IBM Data Engineering</strong> – IBM</div>
    <div class="cert-item"><strong>Google Cybersecurity</strong> – Google</div>
    <div class="cert-item"><strong>AWS Cloud Solutions Architect</strong> – AWS</div>
    <div class="cert-item"><strong>Google Advanced Data Analytics</strong> – Google</div>
    <div class="cert-item"><strong>Google AI Essentials</strong> – Google</div>
</div>

<div class="section-header">Languages</div>
<div class="languages-row">
    <strong>Arabic:</strong> Native &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>French:</strong> Fluent / Advanced &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>English:</strong> Fluent &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>German:</strong> Beginner (A1)
</div>

</body>
</html>
"""

FR_HTML = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Yassine Ezzedine — CV</title>
<style>
{CSS_BASE}
</style>
</head>
<body>

<div class="header">
    <div class="name">Yassine EZZEDINE</div>
    <div class="title">Ingénieur Logiciel Full-Stack &amp; Spécialiste Data / IA</div>
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
<div style="font-size: 8pt; line-height: 1.25; margin: 1.5px 0 3px 0;">
Étudiant en 3<sup>ème</sup> année de Licence en Informatique de Gestion (Business Intelligence, FSEG Nabeul), à la recherche d'un stage PFE en Data Science, Intelligence Artificielle ou Ingénierie Full-Stack. Expérience concrète dans la conception d'applications web de production et de plateformes de données avec React, Next.js, FastAPI, Python, SQL et Supabase, renforcée par un stage chez Tunisie Telecom (système de gestion RH) et plusieurs plateformes commerciales dont D.TN Audio Architecture.
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

<div class="section-header">Expérience Professionnelle</div>
<div class="entry-header">
    <span class="entry-title">Tunisie Telecom – Stagiaire Développeur Logiciel</span>
    <span class="entry-date">Juillet 2026</span>
</div>
<div class="entry-sub">Nabeul, Tunisie</div>
<ul class="bullets">
    <li><strong>Système de Gestion RH :</strong> Conception et développement complet d'une application de gestion des ressources humaines et des congés avec 11 modules opérationnels (dossier agent, gestion des soldes, cycle des demandes, audit d'approbation à 2 niveaux, édition de rapports) en Python, SQLite et interface interactive.</li>
    <li>Développement d'outils internes de gestion des flux de travail et de suivi des tâches en Python, Java et MERN stack avec MongoDB.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Projets Clients Commerciaux</span>
    <span class="entry-date">2026</span>
</div>
<ul class="bullets">
    <li><strong>D.TN Audio Architecture :</strong> Marketplace audio numérique et licensing d'instrumentales conçue avec Next.js (App Router), TypeScript, Supabase PostgreSQL (RLS), Web Audio API, paiement sécurisé et support trilingue RTL.</li>
    <li><strong>Phantom Stickers :</strong> Plateforme e-commerce MERN stack et Supabase avec tableau de bord administrateur et déploiement Vercel.</li>
    <li><strong>Moto Parts Stock Manager :</strong> Application de gestion de stock et caisse (Mobile &amp; PC) développée avec Flutter, SQLite et Supabase.</li>
</ul>

<div class="section-header">Projets Techniques</div>
<div class="entry-header">
    <span class="entry-title">Attritex – Prédiction du Risque de Churn &amp; Revenu ARR</span>
    <span class="entry-date">FastAPI, React 19, TypeScript, Scikit-learn</span>
</div>
<ul class="bullets">
    <li>Plateforme ML de classification évaluant le risque financier ARR et les leviers de rétention client (44 tests unitaires Pytest).</li>
</ul>

<div class="entry-header">
    <span class="entry-title">AWS Retail Data Lake &amp; Pipeline Serverless</span>
    <span class="entry-date">Terraform (IaC), AWS S3, Lambda, Glue, Athena</span>
</div>
<ul class="bullets">
    <li>Data lake retail événementiel avec Terraform IaC, validation des données S3, catalogue AWS Glue et requêtes SQL Athena.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Segmentation Clientèle &amp; Analyse du Panier</span>
    <span class="entry-date">Python, Scikit-learn, PyQt5</span>
</div>
<ul class="bullets">
    <li>Analyse RFM, clustering K-Means et extraction de règles Apriori sur données transactionnelles avec dashboard analytique PyQt5.</li>
</ul>

<div class="section-header">Compétences Techniques</div>
<div class="skills-line"><strong>Data Science / IA / ML :</strong> Python, Pandas, NumPy, Scikit-learn, Statistiques, Nettoyage, EDA, Machine Learning, RFM, K-Means, Apriori</div>
<div class="skills-line"><strong>Web &amp; Full-Stack :</strong> React, Next.js, TypeScript, JavaScript, Node.js, Express.js, FastAPI, REST APIs, HTML5, CSS3, Tailwind CSS, Flutter</div>
<div class="skills-line"><strong>Cloud, BDD &amp; Outils :</strong> AWS (S3, Lambda, Glue, Athena), Terraform, Supabase, PostgreSQL, MongoDB, SQLite, MySQL, Git, GitHub, Linux, Vercel</div>

<div class="section-header">Certifications</div>
<div class="cert-grid">
    <div class="cert-item"><strong>Microsoft AI &amp; ML Engineering</strong> – Microsoft</div>
    <div class="cert-item"><strong>IBM Data Engineering</strong> – IBM</div>
    <div class="cert-item"><strong>Google Cybersecurity</strong> – Google</div>
    <div class="cert-item"><strong>AWS Cloud Solutions Architect</strong> – AWS</div>
    <div class="cert-item"><strong>Google Advanced Data Analytics</strong> – Google</div>
    <div class="cert-item"><strong>Google AI Essentials</strong> – Google</div>
</div>

<div class="section-header">Langues</div>
<div class="languages-row">
    <strong>Arabe :</strong> Langue maternelle &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>Français :</strong> Courant / Avancé &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>Anglais :</strong> Courant &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>Allemand :</strong> Débutant (A1)
</div>

</body>
</html>
"""

DE_HTML = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>Yassine Ezzedine — Lebenslauf</title>
<style>
{CSS_BASE}
</style>
</head>
<body>

<div class="header">
    <div class="name">Yassine EZZEDINE</div>
    <div class="title">Full-Stack Software Engineer &amp; Data / KI-Spezialist</div>
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
<div style="font-size: 8pt; line-height: 1.25; margin: 1.5px 0 3px 0;">
Student im 3. Jahr der Wirtschaftsinformatik mit Schwerpunkt Business Intelligence (FSEG Nabeul), auf der Suche nach einem PFE-Abschlusspraktikum in Data Science, Künstlicher Intelligenz oder Full-Stack Engineering. Fundierte praktische Erfahrung in der Entwicklung moderner Webanwendungen und Datenplattformen mit React, Next.js, FastAPI, Python, SQL und Supabase, belegt durch ein Praktikum bei Tunisie Telecom (Entwicklung eines HR-Managementsystems) und kommerzielle Plattformen wie D.TN Audio Architecture.
</div>

<div class="section-header">Ausbildung</div>
<div class="entry-header">
    <span class="entry-title">Bachelor in Wirtschaftsinformatik – Business Intelligence</span>
    <span class="entry-date">2024 – 2027</span>
</div>
<div class="entry-sub">FSEG Nabeul, Tunesien</div>

<div class="entry-header">
    <span class="entry-title">Abitur in Informatik – Prädikat: Assez Bien</span>
    <span class="entry-date">2024</span>
</div>
<div class="entry-sub">Nabeul, Tunesien</div>

<div class="section-header">Berufserfahrung</div>
<div class="entry-header">
    <span class="entry-title">Tunisie Telecom – Software-Engineering-Praktikant</span>
    <span class="entry-date">Juli 2026</span>
</div>
<div class="entry-sub">Nabeul, Tunesien</div>
<ul class="bullets">
    <li><strong>HR-Managementsystem:</strong> Konzeption und Entwicklung eines vollständigen HR- und Urlaubsverwaltungssystems mit 11 Betriebsmodulen (Mitarbeiterakte, Urlaubskontoführung, Genehmigungsworkflow, Berichterstellung) mit Python, SQLite und interaktivem Frontend.</li>
    <li>Entwicklung interner Workflow- und Aufgabenverwaltungsanwendungen mit Python, Java und dem MERN-Stack mit MongoDB.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Kommerzielle Kundenprojekte</span>
    <span class="entry-date">2026</span>
</div>
<ul class="bullets">
    <li><strong>D.TN Audio Architecture:</strong> Digitale Musik-Marketplace- und Beat-Lizenzierungsplattform mit Next.js (App Router), TypeScript, Supabase PostgreSQL (RLS), Web Audio API, manipulationssicherem Checkout und dreisprachiger RTL-Engine.</li>
    <li><strong>Phantom Stickers:</strong> Full-Stack E-Commerce-Plattform mit MERN-Stack, Supabase, rollenbasiertem Admin-Dashboard und Vercel-Deployment.</li>
    <li><strong>Moto Parts Stock Manager:</strong> Inventar- und Kassenverwaltungsanwendung (Mobile &amp; PC) entwickelt mit Flutter, SQLite und Supabase.</li>
</ul>

<div class="section-header">Technische Projekte</div>
<div class="entry-header">
    <span class="entry-title">Attritex – Kundenbindung &amp; ARR-Risikointelligenz</span>
    <span class="entry-date">FastAPI, React 19, TypeScript, Scikit-learn</span>
</div>
<ul class="bullets">
    <li>End-to-End-ML-Klassifikationsplattform zur Quantifizierung des gefährdeten ARR-Umsatzes mit 44 Pytest-Unittests.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">AWS Retail Data Lake &amp; Serverless Pipeline</span>
    <span class="entry-date">Terraform (IaC), AWS S3, Lambda, Glue, Athena</span>
</div>
<ul class="bullets">
    <li>Ereignisgesteuerter Serverless-Data-Lake mit Terraform IaC, S3-Qualitätsprüfung, Glue Data Catalog und Athena SQL.</li>
</ul>

<div class="entry-header">
    <span class="entry-title">Kundensegmentierung &amp; Warenkorbanalyse</span>
    <span class="entry-date">Python, Scikit-learn, PyQt5</span>
</div>
<ul class="bullets">
    <li>RFM-Analyse, K-Means-Clustering und Apriori-Assoziationsregeln für Einzelhandelsdaten mit interaktiver PyQt5-GUI.</li>
</ul>

<div class="section-header">Technische Fähigkeiten</div>
<div class="skills-line"><strong>Data Science / KI / ML:</strong> Python, Pandas, NumPy, Scikit-learn, Statistik, Datenbereinigung, EDA, Machine Learning, RFM, K-Means, Apriori</div>
<div class="skills-line"><strong>Web &amp; Full-Stack:</strong> React, Next.js, TypeScript, JavaScript, Node.js, Express.js, FastAPI, REST APIs, HTML5, CSS3, Tailwind CSS, Flutter</div>
<div class="skills-line"><strong>Cloud, Datenbanken &amp; Tools:</strong> AWS (S3, Lambda, Glue, Athena), Terraform, Supabase, PostgreSQL, MongoDB, SQLite, MySQL, Git, GitHub, Linux, Vercel</div>

<div class="section-header">Zertifizierungen</div>
<div class="cert-grid">
    <div class="cert-item"><strong>Microsoft AI &amp; ML Engineering</strong> – Microsoft</div>
    <div class="cert-item"><strong>IBM Data Engineering</strong> – IBM</div>
    <div class="cert-item"><strong>Google Cybersecurity</strong> – Google</div>
    <div class="cert-item"><strong>AWS Cloud Solutions Architect</strong> – AWS</div>
    <div class="cert-item"><strong>Google Advanced Data Analytics</strong> – Google</div>
    <div class="cert-item"><strong>Google AI Essentials</strong> – Google</div>
</div>

<div class="section-header">Sprachen</div>
<div class="languages-row">
    <strong>Arabisch:</strong> Muttersprache &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>Französisch:</strong> Verhandlungssicher &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>Englisch:</strong> Fließend &nbsp;&nbsp;|&nbsp;&nbsp;
    <strong>Deutsch:</strong> Grundkenntnisse (A1)
</div>

</body>
</html>
"""

AR_HTML = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>ياسين عزالدين — السيرة الذاتية</title>
<style>
{CSS_BASE}
{CSS_RTL}
</style>
</head>
<body>

<div class="header">
    <div class="name">ياسين عزالدين</div>
    <div class="title">مهندس برمجيات وتطوير شامل (Full-Stack) ومتخصص في علوم البيانات والذكاء الاصطناعي</div>
    <div class="contact-line">
        نابل، تونس &nbsp;|&nbsp; 208 208 20 216+ &nbsp;|&nbsp; <a href="mailto:yassineezzediney2g@gmail.com">yassineezzediney2g@gmail.com</a>
    </div>
    <div class="contact-line" dir="ltr">
        <a href="https://linkedin.com/in/yassin-ezzedine/">linkedin.com/in/yassin-ezzedine/</a> &nbsp;|&nbsp;
        <a href="https://github.com/EzzedineYassine">github.com/EzzedineYassine</a> &nbsp;|&nbsp;
        <a href="https://yassineezzedine.dev">yassineezzedine.dev</a>
    </div>
</div>

<div class="section-header">الملف المهني</div>
<div style="font-size: 8pt; line-height: 1.25; margin: 1.5px 0 3px 0;">
طالب بالسنة الثالثة إجازة في إعلامية التصرف – اختصاص ذكاء الأعمال (FSEG نابل)، أبحث عن تدريب مشروع تخرج (PFE) في علوم البيانات، الذكاء الاصطناعي، أو هندسة البرمجيات الشاملة. أمتلك خبرة عملية في بناء تطبيقات ويب ومنصات بيانات احترافية باستخدام React وNext.js وFastAPI وPython وSQL وSupabase، مدعومة بتدريب هندسي في اتصالات تونس لتطوير نظام إدارة الموارد البشرية، ومشاريع تجارية ناجحة من بينها D.TN Audio Architecture.
</div>

<div class="section-header">التعليم والتكوين الأكاديمي</div>
<div class="entry-header">
    <span class="entry-title">إجازة في إعلامية التصرف – ذكاء الأعمال (Business Intelligence)</span>
    <span class="entry-date" dir="ltr">2024 – 2027</span>
</div>
<div class="entry-sub">كلية العلوم الاقتصادية والتصرف بنابل، تونس</div>

<div class="entry-header">
    <span class="entry-title">بكالوريا في علوم الإعلامية – الملاحظة: قريب من الحسن</span>
    <span class="entry-date" dir="ltr">2024</span>
</div>
<div class="entry-sub">المعهد الثانوي بنابل، تونس</div>

<div class="section-header">الخبرة المهنية</div>
<div class="entry-header">
    <span class="entry-title">اتصالات تونس (Tunisie Telecom) – متدرب في هندسة البرمجيات</span>
    <span class="entry-date" dir="ltr">جويلية 2026</span>
</div>
<div class="entry-sub">نابل، تونس</div>
<ul class="bullets">
    <li>&rlm;<strong>نظام إدارة الموارد البشرية (HR Management System):</strong> تصميم وتطوير منصة شاملة لإدارة شؤون الموظفين والإجازات تضم 11 وحدة تشغيلية (ملف الموظف، أرصدة العطل، دورة حياة الطلبات، مسار المصادقة الثنائي، طباعة التقارير) باستخدام Python وSQLite وواجهة تفاعلية.</li>
    <li>&rlm;تطوير تطبيقات داخلية لأتمتة سير العمل وإدارة المهام باستخدام Python وJava وMERN Stack مع MongoDB.&rlm;</li>
</ul>

<div class="entry-header">
    <span class="entry-title">مشاريع العملاء والعمل الحر</span>
    <span class="entry-date" dir="ltr">2026</span>
</div>
<ul class="bullets">
    <li>&rlm;<strong>D.TN Audio Architecture:</strong> منصة تجارة إلكترونية صوتية وترخيص إيقاعات موسيقية مبنية بـ Next.js وTypeScript وSupabase PostgreSQL مع Web Audio API ودفع آمن ودعم ثلاثي اللغات مع محاذاة RTL كاملة.&rlm;</li>
    <li>&rlm;<strong>Phantom Stickers:</strong> تطبيق تجارة إلكترونية كامل بـ MERN Stack وSupabase ولوحة تحكم للمشرف ونشر على Vercel.&rlm;</li>
    <li>&rlm;<strong>Moto Parts Stock Manager:</strong> تطبيق إدارة مخزون وبيع قطع الدراجات (هاتف وحاسوب) بـ Flutter وSQLite وSupabase.&rlm;</li>
</ul>

<div class="section-header">المشاريع التقنية المميزة</div>
<div class="entry-header">
    <span class="entry-title">Attritex – التنبؤ بمخاطر خسارة العملاء والإيرادات</span>
    <span class="entry-date" dir="ltr">FastAPI, React 19, TypeScript, Scikit-learn</span>
</div>
<ul class="bullets">
    <li>&rlm;منصة ذكاء أعمال وتعلّم آلي لتقدير الإيرادات المعرضة للخطر مع خطط استباقية للاحتفاظ بالعملاء (44 اختبار وحدات بـ Pytest).&rlm;</li>
</ul>

<div class="entry-header">
    <span class="entry-title">AWS Retail Data Lake &amp; Pipeline</span>
    <span class="entry-date" dir="ltr">Terraform (IaC), AWS S3, Lambda, Glue, Athena</span>
</div>
<ul class="bullets">
    <li>&rlm;بحيرة بيانات سحابية متوافقة مع ممارسات IaC بـ Terraform، عزل البيانات المعيبة، وفهرسة Glue واستعلام Athena SQL.&rlm;</li>
</ul>

<div class="entry-header">
    <span class="entry-title">تقسيم العملاء وتحليل سلة المشتريات</span>
    <span class="entry-date" dir="ltr">Python, Scikit-learn, PyQt5</span>
</div>
<ul class="bullets">
    <li>&rlm;تنظيف البيانات، تطبيق تحليل RFM وخوارزمية K-Means للتجزئة وقواعد Apriori مع واجهة مكتبية تفاعلية بـ PyQt5.&rlm;</li>
</ul>

<div class="section-header">المهارات التقنية</div>
<div class="skills-row">
    <span class="skills-cat">علوم البيانات والذكاء الاصطناعي :</span>
    <span class="skills-items">Python, Pandas, NumPy, Scikit-learn, Statistics, Data Cleaning, EDA, Machine Learning, RFM, K-Means, Apriori</span>
</div>
<div class="skills-row">
    <span class="skills-cat">الويب والتطوير الشامل :</span>
    <span class="skills-items">React, Next.js, TypeScript, JavaScript, Node.js, Express.js, FastAPI, REST APIs, HTML5, CSS3, Tailwind CSS, Flutter</span>
</div>
<div class="skills-row">
    <span class="skills-cat">السحابة وقواعد البيانات والأدوات :</span>
    <span class="skills-items">AWS (S3, Lambda, Glue, Athena), Terraform, Supabase, PostgreSQL, MongoDB, SQLite, MySQL, Git, GitHub, Linux, Vercel</span>
</div>

<div class="section-header">الشهادات المعتمدة</div>
<div class="cert-grid-rtl">
    <div><strong>Microsoft AI &amp; ML Engineering</strong> – Microsoft</div>
    <div><strong>IBM Data Engineering</strong> – IBM</div>
    <div><strong>Google Cybersecurity</strong> – Google</div>
    <div><strong>AWS Cloud Solutions Architect</strong> – AWS</div>
    <div><strong>Google Advanced Data Analytics</strong> – Google</div>
    <div><strong>Google AI Essentials</strong> – Google</div>
</div>

<div class="section-header">اللغات</div>
<div class="languages-row-rtl">
    <div><strong>العربية :</strong> اللغة الأم</div>
    <div><strong>الفرنسية :</strong> متقدم / طليق</div>
    <div><strong>الإنجليزية :</strong> طليق</div>
    <div><strong>الألمانية :</strong> مبتدئ (A1)</div>
</div>

</body>
</html>
"""

cv_files = [
    ("cv-en.html", EN_HTML, "cv-en.pdf"),
    ("cv-fr.html", FR_HTML, "cv-fr.pdf"),
    ("cv-de.html", DE_HTML, "cv-de.pdf"),
    ("cv-ar.html", AR_HTML, "cv-ar.pdf")
]

for html_name, html_content, pdf_name in cv_files:
    html_path = os.path.join(OUTPUT_DIR, html_name)
    pdf_path = os.path.join(OUTPUT_DIR, pdf_name)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    cmd = f'cmd.exe /c ""{EDGE_EXE}" --headless --no-pdf-header-footer --print-to-pdf="{pdf_path}" "{html_path}""'
    subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    reader = pypdf.PdfReader(pdf_path)
    print(f"{pdf_name}: {len(reader.pages)} page(s), size: {os.path.getsize(pdf_path)} bytes")

# Copy cv-en.pdf -> cv.pdf and cv-en.html -> cv.html
shutil.copyfile(os.path.join(OUTPUT_DIR, "cv-en.pdf"), os.path.join(OUTPUT_DIR, "cv.pdf"))
shutil.copyfile(os.path.join(OUTPUT_DIR, "cv-en.html"), os.path.join(OUTPUT_DIR, "cv.html"))
print("Copied cv-en.pdf -> cv.pdf and cv-en.html -> cv.html")
