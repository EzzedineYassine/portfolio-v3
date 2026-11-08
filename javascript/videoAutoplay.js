/**
 * Lightweight, Mobile-Optimized Video Autoplay Engine
 * - Zero layout thrashing: Uses IntersectionObserver exclusively
 * - Low-power & battery-saver safe: Only plays the currently visible video
 * - User-interaction unblocker runs ONCE, preventing CPU/GPU overloading
 */

let observerInstance = null;
let isUnlocked = false;

export function setupMobileVideoAutoplay() {
  const videoWraps = document.querySelectorAll('.project-card__image-wrap');
  if (!videoWraps.length) return;

  videoWraps.forEach((wrap) => {
    const video = wrap.querySelector('video');
    if (!video) return;

    // 1. Strict mobile inline attributes and DOM properties (iOS Safari & Android Chrome)
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

    if (!video._hasAutoplayListeners) {
      video._hasAutoplayListeners = true;

      video.addEventListener('play', markPlaying, { passive: true });
      video.addEventListener('playing', markPlaying, { passive: true });
      video.addEventListener('pause', markPaused, { passive: true });
      video.addEventListener('ended', () => {
        video.currentTime = 0;
        safePlay(video);
      }, { passive: true });

      // Tap / Click anywhere on the card to toggle play/pause
      wrap.addEventListener('click', (e) => {
        e.stopPropagation();
        if (video.paused) {
          video.muted = true;
          safePlay(video);
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

  // 2. Off-main-thread IntersectionObserver for silky smooth viewport playback
  if ('IntersectionObserver' in window) {
    if (observerInstance) {
      observerInstance.disconnect();
    }

    observerInstance = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const video = entry.target;
          if (entry.isIntersecting) {
            safePlay(video);
          } else {
            if (!video.paused) {
              video.pause();
            }
          }
        });
      },
      {
        root: null,
        rootMargin: '60px 0px 60px 0px',
        threshold: 0.2
      }
    );

    document.querySelectorAll('.project-card__image-wrap video').forEach((vid) => {
      observerInstance.observe(vid);
    });
  }

  // 3. User Gesture Fallback - Runs ONCE on first interaction, NEVER floods the main thread
  if (!isUnlocked) {
    const unlockOnFirstTouch = () => {
      if (isUnlocked) return;
      isUnlocked = true;

      // Unblock only intersecting videos
      document.querySelectorAll('.project-card__image-wrap video').forEach((vid) => {
        const rect = vid.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0 && vid.paused) {
          safePlay(vid);
        }
      });

      window.removeEventListener('touchstart', unlockOnFirstTouch);
      window.removeEventListener('touchend', unlockOnFirstTouch);
      window.removeEventListener('pointerdown', unlockOnFirstTouch);
    };

    window.addEventListener('touchstart', unlockOnFirstTouch, { passive: true, once: true });
    window.addEventListener('touchend', unlockOnFirstTouch, { passive: true, once: true });
    window.addEventListener('pointerdown', unlockOnFirstTouch, { passive: true, once: true });
  }
}

function safePlay(video) {
  if (!video) return;
  video.muted = true;
  if (!video.paused) return; // Already playing

  const playPromise = video.play();
  if (playPromise !== undefined) {
    playPromise.catch(() => {
      // Autoplay silently deferred until user interacts; handled by UI play badge
    });
  }
}
