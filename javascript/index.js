import { showSidebar } from './hamburgerMenu.js';
import { intersectionObserver } from './intersectionObserver.js';
import { parallaxHero } from './parallaxHero.js';
import { cursor } from './cursor.js';
import { initI18n } from './i18n.js';
import { setupMobileVideoAutoplay } from './videoAutoplay.js';
import './sendEmail.js';
import './animations.js';
import { load } from "./load.js";

async function main() {
  // 1. Safe desktop-only cursor
  try {
    if (window.matchMedia && window.matchMedia('(pointer: fine)').matches) {
      cursor();
    }
  } catch (e) {}

  // 2. Navigation & UI listeners
  try {
    showSidebar();
    intersectionObserver();
    parallaxHero();
  } catch (e) {
    console.warn('Navigation observer error:', e);
  }

  // 3. EmailJS init
  try {
    if (window.emailjs) {
      emailjs.init();
    }
  } catch (e) {}

  // 4. Initialize i18n & Render
  try {
    await initI18n();
  } catch (e) {
    console.error('i18n initialization error:', e);
  } finally {
    // 5. Dismiss loader unconditionally - page is GUARANTEED to display
    await load();
    try {
      setupMobileVideoAutoplay();
    } catch (e) {
      console.warn('Autoplay setup error:', e);
    }
  }
}

// Execute immediately when DOM is ready or current
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', main);
} else {
  main();
}
