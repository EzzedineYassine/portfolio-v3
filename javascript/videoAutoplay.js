/**
 * Video Autoplay & Touch-Unblock Engine for Mobile & Desktop
 * Ensures videos autoplay inline without requiring explicit manual play buttons,
 * handles iOS Low Power Mode, battery savers, and dynamically created DOM nodes.
 */

let observerInstance = null;

export function setupMobileVideoAutoplay() {
  const videoWraps = document.querySelectorAll('.project-card__image-wrap');

  videoWraps.forEach((wrap) => {
    const video = wrap.querySelector('video');
    if (!video) return;

    // 1. Strict mobile inline attributes and DOM properties (iOS WebKit & Android Chrome)
    video.muted = true;
    video.defaultMuted = true;
    video.playsInline = true;
    video.setAttribute('muted', '');
    video.setAttribute('playsinline', '');
    video.setAttribute('webkit-playsinline', '');
    video.setAttribute('disableRemotePlayback', '');

    const markPlaying = () => {
      wrap.classList.remove('is-paused');
      wrap.classList.add('is-playing');
    };

    const markPaused = () => {
      wrap.classList.remove('is-playing');
      wrap.classList.add('is-paused');
    };

    // Attach status listeners if not already bound
    if (!video._hasAutoplayListeners) {
      video._hasAutoplayListeners = true;
      video.addEventListener('play', markPlaying);
      video.addEventListener('playing', markPlaying);
      video.addEventListener('pause', markPaused);
      video.addEventListener('ended', () => {
        video.currentTime = 0;
        video.play().catch(() => {});
      });

      // Tap / Click anywhere on card to toggle play/pause effortlessly
      wrap.addEventListener('click', () => {
        if (video.paused) {
          video.muted = true;
          video.play().catch(() => {});
        } else {
          video.pause();
        }
      });
    }

    if (video.paused) {
      markPaused();
    } else {
      markPlaying();
    }
  });

  // 2. IntersectionObserver: Autoplay when scrolled into viewport, pause when offscreen
  if ('IntersectionObserver' in window) {
    if (observerInstance) {
      observerInstance.disconnect();
    }

    observerInstance = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const video = entry.target;
          if (entry.isIntersecting) {
            video.muted = true;
            const playPromise = video.play();
            if (playPromise !== undefined) {
              playPromise.catch(() => {
                // Autoplay may be deferred until first user touch
              });
            }
          } else {
            video.pause();
          }
        });
      },
      {
        root: null,
        rootMargin: '120px 0px 120px 0px', // Pre-trigger slightly before entering viewport
        threshold: 0.1
      }
    );

    document.querySelectorAll('.project-card__image-wrap video').forEach((vid) => {
      observerInstance.observe(vid);
    });
  }

  // 3. User Gesture Fallback (iOS Low Power Mode / Android Data Saver)
  // The first time the user touches or scrolls on mobile, immediately start visible videos
  const unlockVideos = () => {
    document.querySelectorAll('.project-card__image-wrap video').forEach((vid) => {
      const rect = vid.getBoundingClientRect();
      const inView = rect.top < window.innerHeight + 150 && rect.bottom > -150;
      if (inView && vid.paused) {
        vid.muted = true;
        vid.play().catch(() => {});
      }
    });
  };

  ['touchstart', 'touchend', 'pointerdown', 'scroll'].forEach((event) => {
    window.addEventListener(event, unlockVideos, { passive: true });
  });
}
