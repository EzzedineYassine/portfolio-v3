import { showSidebar } from './hamburgerMenu.js';
import { intersectionObserver } from './intersectionObserver.js';
import { parallaxHero } from './parallaxHero.js';
import { cursor } from './cursor.js';
import { initI18n } from './i18n.js';
import './sendEmail.js';
import './animations.js';
import { load } from "./load.js";

async function main() {
  cursor();
  showSidebar();
  intersectionObserver();
  parallaxHero();
  try {
    if (window.emailjs) {
      emailjs.init();
    }
  } catch (e) {}
  await initI18n();
  await load();
}

main();
