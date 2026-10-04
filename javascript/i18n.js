/* ==========================================================================
   i18n Engine for Multi-Language Support (EN, FR, AR, DE)
   Features:
   - Dynamic locale loading with fallback & localStorage caching
   - Full data-i18n, data-i18n-attr attribute translation
   - RTL/LTR dynamic switching on <html> and <body>
   - Integration with Typed.js for animated tagline
   - Dynamic render for Projects and Timeline sections
   - Preservation of existing intersection observers & animations
   ========================================================================== */

import { typeAnimation } from './typeAnimation.js';

export const SUPPORTED_LOCALES = ['en', 'fr', 'ar', 'de'];
export const DEFAULT_LOCALE = 'en';

const LOCALE_LABELS = {
  en: { label: 'EN', full: 'English', flag: '🇬🇧' },
  fr: { label: 'FR', full: 'Français', flag: '🇫🇷' },
  ar: { label: 'العربية', full: 'العربية', flag: '🇹🇳' },
  de: { label: 'DE', full: 'Deutsch', flag: '🇩🇪' }
};

let currentLocale = DEFAULT_LOCALE;
let dictionaries = {};
let typedInstance = null;

/**
 * Fetch and cache locale dictionary
 */
async function loadDictionary(lang) {
  if (dictionaries[lang]) return dictionaries[lang];
  try {
    const response = await fetch(`./locales/${lang}.json?v=${Date.now()}`);
    if (!response.ok) throw new Error(`Could not load ${lang}.json`);
    const data = await response.json();
    dictionaries[lang] = data;
    return data;
  } catch (error) {
    console.error(`Failed to load dictionary for [${lang}]:`, error);
    if (lang !== DEFAULT_LOCALE) {
      return loadDictionary(DEFAULT_LOCALE);
    }
    return {};
  }
}

/**
 * Deep key lookup: e.g. "hero.greeting"
 */
export function t(key, dict = dictionaries[currentLocale]) {
  if (!dict) return key;
  const keys = key.split('.');
  let result = dict;
  for (const k of keys) {
    if (result && typeof result === 'object' && k in result) {
      result = result[k];
    } else {
      return key;
    }
  }
  return result;
}

/**
 * Update static text, placeholders, and attributes
 */
function translateDOM(dict) {
  // Elements with data-i18n (replaces innerHTML or textContent)
  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const key = el.getAttribute('data-i18n');
    const val = t(key, dict);
    if (val && typeof val === 'string') {
      el.innerHTML = val;
    }
  });

  // Elements with data-i18n-attr="placeholder:contact.form.namePlaceholder"
  document.querySelectorAll('[data-i18n-attr]').forEach((el) => {
    const attrDefs = el.getAttribute('data-i18n-attr').split(';');
    attrDefs.forEach((def) => {
      const [attr, key] = def.split(':').map((s) => s.trim());
      if (attr && key) {
        const val = t(key, dict);
        if (val && typeof val === 'string') {
          el.setAttribute(attr, val);
        }
      }
    });
  });
}

/**
 * Render Project Cards dynamically with localized content
 */
function renderProjects(dict) {
  const container = document.getElementById('dynamic-projects-list');
  if (!container) return;

  const projects = dict.projects?.items || [];
  const btnLabels = dict.projects?.buttons || { demo: 'Demo', code: 'Code' };

  const projectsHtml = projects
    .map((project, index) => {
      const isReverse = index % 2 === 1 ? 'projects__project--reverse fromLeft' : 'fromRight';
      const techTags = (project.tags || [])
        .map(
          (tag) => `
          <section class="all-skills__container">
            <span class="timeline__tag">${tag}</span>
          </section>`
        )
        .join('');

      let previewContent = '';
      if (project.video && project.video.endsWith('.webm')) {
        previewContent = `
          <video disableRemotePlayback muted autoplay loop playsinline>
            <source
              src="${project.video}"
              type='video/webm;codecs="vp9"'
              onerror="fallback(parentNode);
              function fallback(video) {
                while (video.hasChildNodes()) {
                  if (video.firstChild instanceof HTMLSourceElement) video.removeChild(video.firstChild);
                  else video.parentNode.insertBefore(video.firstChild, video);
                }
                video.parentNode.removeChild(video);
              }"
            />
            <img src="${project.fallbackImg || './assets/videos/yourpj-ios.png'}" alt="${project.title}" loading="lazy" />
          </video>
        `;
      } else if (project.video) {
        previewContent = `
          <div class="project-card__mockup-browser">
            <div class="project-card__browser-header">
              <div class="project-card__browser-dots">
                <span class="project-card__dot project-card__dot--red"></span>
                <span class="project-card__dot project-card__dot--yellow"></span>
                <span class="project-card__dot project-card__dot--green"></span>
              </div>
              <div class="project-card__browser-url">${project.title} - Live Demo</div>
            </div>
            <div class="project-card__image-wrap">
              <video class="project-card__img" autoplay loop muted playsinline preload="metadata" disableRemotePlayback>
                <source src="${project.video}" type="video/mp4" />
                Your browser does not support the video tag.
              </video>
            </div>
          </div>
        `;
      } else if (project.image) {
        previewContent = `
          <div class="project-card__mockup-browser">
            <div class="project-card__browser-header">
              <div class="project-card__browser-dots">
                <span class="project-card__dot project-card__dot--red"></span>
                <span class="project-card__dot project-card__dot--yellow"></span>
                <span class="project-card__dot project-card__dot--green"></span>
              </div>
              <div class="project-card__browser-url">${project.demoUrl.replace(/^https?:\/\//, '')}</div>
            </div>
            <div class="project-card__image-wrap">
              <img class="project-card__img" src="${project.image}" alt="${project.title}" loading="lazy" />
            </div>
          </div>
        `;
      } else {
        previewContent = `
          <div class="project-card__preview">
            <div class="project-card__badge">${project.category || 'Featured'}</div>
            <div class="project-card__title-glance">${project.title}</div>
          </div>
        `;
      }

      return `
      <article class="projects__project ${isReverse} hidden" id="project-${project.id}">
        <article class="projects__laptop-mockup">
          ${previewContent}
        </article>
        <section class="projects__info">
          <h3 class="projects__title">${project.title}</h3>
          <p class="projects__paragraph">${project.description}</p>
          <div class="projects__tech-tags">${techTags}</div>
          <section class="projects__buttons">
            <a href="${project.demoUrl}" target="_blank" rel="noopener noreferrer">
              <button class="button">${btnLabels.demo}</button>
            </a>
            <a href="${project.codeUrl}" target="_blank" rel="noopener noreferrer">
              <button class="button button--secondary">${btnLabels.code}</button>
            </a>
          </section>
        </section>
      </article>
    `;
    })
    .join('');

  const yp = dict.projects?.yourProject || {
    title: 'YOUR PROJECT',
    desc: 'Are you looking for a dedicated and skilled professional to join your team or help with your next project? Look no further!',
    btn: 'Contact Me'
  };

  const yourProjectHtml = `
    <article class="projects__project project__your-project projects__your-project hidden fromLeft" id="project-your-project">
      <article class="projects__laptop-mockup">
        <video disableRemotePlayback muted autoplay playsinline loop>
          <source
            src="./assets/videos/yourproj.webm"
            type="video/webm"
            onerror="fallback(parentNode);
            function fallback(video) {
              while (video.hasChildNodes()) {
                if (video.firstChild instanceof HTMLSourceElement) video.removeChild(video.firstChild);
                else video.parentNode.insertBefore(video.firstChild, video);
              }
              video.parentNode.removeChild(video);
            }"
          />
          <img src="./assets/videos/yourpj-ios.png" alt="your project" loading="lazy" />
        </video>
      </article>

      <section class="projects__info projects__info--project">
        <h3 class="projects__title">${yp.title}</h3>
        <p class="projects__paragraph">${yp.desc}</p>
        <a href="#contact"><button class="button">${yp.btn}</button></a>
      </section>
    </article>
  `;

  container.innerHTML = projectsHtml + yourProjectHtml;
}

/**
 * Render Timeline (Experience & Education)
 */
function renderTimeline(dict) {
  const track = document.getElementById('timeline-track');
  const languagesGrid = document.getElementById('timeline-languages-grid');
  if (!track) return;

  const items = dict.timeline?.items || [];

  track.innerHTML = items
    .map((item, idx) => {
      const side = idx % 2 === 0 ? 'timeline__item--left fromLeft' : 'timeline__item--right fromRight';
      const icon = item.type === 'education' ? 'fa-graduation-cap' : 'fa-briefcase';
      const tags = (item.tags || []).map((t) => `<span class="timeline__tag">${t}</span>`).join('');

      return `
      <div class="timeline__item ${side} hidden" data-type="${item.type}">
        <div class="timeline__marker">
          <i class="fa-solid ${icon}"></i>
        </div>
        <div class="timeline__content">
          <div class="timeline__header">
            <div class="timeline__title-group">
              <h4 class="timeline__role">${item.role}</h4>
              <div class="timeline__org"><i class="fa-solid fa-building-columns"></i> ${item.organization}</div>
            </div>
            <div class="timeline__badge-group">
              <span class="timeline__badge timeline__badge--period">${item.period}</span>
              <span class="timeline__badge timeline__badge--type">${item.type}</span>
            </div>
          </div>
          <p class="timeline__description">${item.description}</p>
          <div class="timeline__tags">${tags}</div>
        </div>
      </div>
    `;
    })
    .join('');

  // Render spoken languages
  if (languagesGrid) {
    const spoken = dict.timeline?.spokenLanguages || [];
    languagesGrid.innerHTML = spoken
      .map(
        (lang) => `
      <div class="timeline__language-card">
        <span class="timeline__language-name">${lang.name}</span>
        <span class="timeline__language-level">${lang.level}</span>
      </div>
    `
      )
      .join('');
  }

  // Setup tab filter listeners
  setupTimelineFilter();
}

/**
 * Filter timeline items by All / Experience / Education
 */
function setupTimelineFilter() {
  const tabs = document.querySelectorAll('.timeline__tab');
  tabs.forEach((tab) => {
    tab.onclick = () => {
      tabs.forEach((t) => t.classList.remove('active'));
      tab.classList.add('active');
      const filter = tab.getAttribute('data-filter');
      const items = document.querySelectorAll('.timeline__item');
      items.forEach((item) => {
        if (filter === 'all' || item.getAttribute('data-type') === filter) {
          item.classList.remove('hidden-tab');
        } else {
          item.classList.add('hidden-tab');
        }
      });
    };
  });
}

/**
 * Re-run scroll animations observer on newly rendered DOM elements
 */
function reobserveAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.hidden').forEach((el) => observer.observe(el));
}

/**
 * Update Typed.js instance with strings for current locale
 */
function updateTypedStrings(dict) {
  const typedStrings = dict.hero?.typed || [
    'A <span class="hero__fullstack">Full-Stack</span> Developer',
    'A <span class="hero__frontend">Data Science</span> Aspirant',
    'An <span class="hero__backend">AI</span> Aspirant',
    'Your <span class="hero__next">Next</span> Colleague'
  ];

  const typedContainer = document.getElementById('typed-strings');
  if (typedContainer) {
    typedContainer.innerHTML = typedStrings.map((str) => `<p>${str}</p>`).join('');
  }

  // Recreate typed animation instance
  if (window.Typed) {
    const typedEl = document.querySelector('#typed');
    if (typedEl) {
      typedEl.innerHTML = '';
      if (typedInstance) {
        try {
          typedInstance.destroy();
        } catch (e) {}
      }
      typedInstance = new window.Typed('#typed', {
        stringsElement: '#typed-strings',
        smartBackspace: true,
        typeSpeed: 30,
        backSpeed: 30,
        loop: true
      });
    }
  }
}

/**
 * Apply directional & lang attributes
 */
function applyDirection(lang) {
  const isRtl = lang === 'ar';
  const html = document.documentElement;
  const body = document.body;

  if (isRtl) {
    html.setAttribute('dir', 'rtl');
    html.setAttribute('lang', 'ar');
    body.classList.add('rtl');
  } else {
    html.setAttribute('dir', 'ltr');
    html.setAttribute('lang', lang);
    body.classList.remove('rtl');
  }
}

/**
 * Render Language Switcher UI (Desktop & Mobile)
 */
function renderLanguageSwitcher() {
  // Desktop switcher
  const desktopContainer = document.getElementById('lang-switcher-desktop');
  if (desktopContainer) {
    const curr = LOCALE_LABELS[currentLocale] || LOCALE_LABELS.en;
    desktopContainer.innerHTML = `
      <div class="lang-switcher" id="desktop-lang-dropdown-wrapper">
        <button class="lang-btn" id="lang-btn-trigger" aria-label="Select Language">
          <i class="fa-solid fa-globe"></i>
          <span>${curr.label}</span>
          <i class="fa-solid fa-chevron-down lang-caret"></i>
        </button>
        <ul class="lang-dropdown" id="lang-dropdown-menu">
          ${SUPPORTED_LOCALES.map(
            (code) => `
            <li>
              <button class="lang-option ${code === currentLocale ? 'active' : ''}" data-locale="${code}">
                <span>${LOCALE_LABELS[code].flag} ${LOCALE_LABELS[code].full}</span>
                ${code === currentLocale ? '<i class="fa-solid fa-check"></i>' : ''}
              </button>
            </li>
          `
          ).join('')}
        </ul>
      </div>
    `;

    const trigger = document.getElementById('lang-btn-trigger');
    const wrapper = document.getElementById('desktop-lang-dropdown-wrapper');
    if (trigger && wrapper) {
      const toggleDropdown = (e) => {
        e.preventDefault();
        e.stopPropagation();
        wrapper.classList.toggle('open');
      };
      trigger.addEventListener('click', toggleDropdown);
      trigger.addEventListener('touchstart', toggleDropdown, { passive: false });
    }

    desktopContainer.querySelectorAll('.lang-option').forEach((btn) => {
      const selectLang = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const loc = btn.getAttribute('data-locale');
        setLanguage(loc);
        if (wrapper) wrapper.classList.remove('open');
      };
      btn.addEventListener('click', selectLang);
      btn.addEventListener('touchstart', selectLang, { passive: false });
    });
  }

  // Mobile pills inside sidebar
  const mobileContainer = document.getElementById('lang-switcher-mobile');
  if (mobileContainer) {
    mobileContainer.innerHTML = `
      <div class="lang-switcher-mobile">
        <span class="lang-switcher-mobile__title" data-i18n="nav.language">Language / Langue</span>
        <div class="lang-pills-mobile">
          ${SUPPORTED_LOCALES.map(
            (code) => `
            <button class="lang-pill ${code === currentLocale ? 'active' : ''}" data-locale="${code}">
              ${LOCALE_LABELS[code].flag} ${LOCALE_LABELS[code].label}
            </button>
          `
          ).join('')}
        </div>
      </div>
    `;

    mobileContainer.querySelectorAll('.lang-pill').forEach((btn) => {
      const selectLang = (e) => {
        e.preventDefault();
        const loc = btn.getAttribute('data-locale');
        setLanguage(loc);
      };
      btn.addEventListener('click', selectLang);
      btn.addEventListener('touchstart', selectLang, { passive: false });
    });
  }

  // Close dropdown on outside click
  document.removeEventListener('click', closeDropdownOutside);
  document.addEventListener('click', closeDropdownOutside);
}

function closeDropdownOutside(e) {
  const wrapper = document.getElementById('desktop-lang-dropdown-wrapper');
  if (wrapper && !wrapper.contains(e.target)) {
    wrapper.classList.remove('open');
  }
}

/**
 * Update resume links to point to the language-specific CV
 */
function updateResumeLinks(lang) {
  const cvPath = `./assets/cv-${lang}.pdf`;
  const fallbackPath = `./assets/cv.pdf`;
  const finalPath = ['en', 'fr', 'de', 'ar'].includes(lang) ? cvPath : fallbackPath;

  const desktopResume = document.getElementById('resume-link');
  if (desktopResume) {
    desktopResume.setAttribute('href', finalPath);
    desktopResume.setAttribute('title', `Resume (${lang.toUpperCase()})`);
  }

  const mobileResume = document.getElementById('sidebar-resume-link');
  if (mobileResume) {
    mobileResume.setAttribute('href', finalPath);
    mobileResume.setAttribute('title', `Resume (${lang.toUpperCase()})`);
  }
}

/**
 * Set active language and re-render
 */
export async function setLanguage(lang) {
  if (!SUPPORTED_LOCALES.includes(lang)) lang = DEFAULT_LOCALE;
  currentLocale = lang;
  try {
    localStorage.setItem('portfolio_language', lang);
  } catch (e) {}

  const dict = await loadDictionary(lang);
  applyDirection(lang);
  translateDOM(dict);
  updateResumeLinks(lang);
  renderProjects(dict);
  renderTimeline(dict);
  updateTypedStrings(dict);
  renderLanguageSwitcher();
  reobserveAnimations();
}

/**
 * Initialize i18n system
 */
export async function initI18n() {
  let savedLocale = DEFAULT_LOCALE;
  try {
    savedLocale = localStorage.getItem('portfolio_language') || DEFAULT_LOCALE;
  } catch (e) {}

  if (!SUPPORTED_LOCALES.includes(savedLocale)) {
    savedLocale = DEFAULT_LOCALE;
  }

  await setLanguage(savedLocale);
}
