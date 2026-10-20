/**
 * Presentation Engine - Bab 6 Diferensiasi Numerik
 * Minimalist White Interactive PPT with KaTeX & 3D Transitions
 */

class PresentationController {
  constructor() {
    this.slides = Array.from(document.querySelectorAll('.slide'));
    this.totalSlides = this.slides.length;
    this.currentIndex = 0;
    this.isTransitioning = false;
    
    // Ordered sequence of transitions for "auto" mode
    this.transitionSequence = [
      'center-fold',         // 1 -> 2: Kertas dibalik tengah
      'bottom-right-curl',   // 2 -> 3: Dari kanan bawah
      'curtain-roll',        // 3 -> 4: Tirai yang digulung
      'cube',                // 4 -> 5: Kubus 3D
      'doors',               // 5 -> 6: Pintu terbuka 3D
      'diagonal',            // 6 -> 7: Sapu diagonal
      'center-fold',         // 7 -> 8: Kertas dibalik tengah
      'bottom-right-curl',   // 8 -> 9: Dari kanan bawah
      'curtain-roll',        // 9 -> 10: Tirai yang digulung
      'cube',                // 10 -> 11: Kubus 3D
      'center-fold',         // 11 -> 12: Kertas dibalik tengah
      'bottom-right-curl',   // 12 -> 13: Dari kanan bawah
      'curtain-roll',        // 13 -> 14: Tirai yang digulung
      'doors',               // 14 -> 15: Pintu terbuka 3D
      'center-fold',         // 15 -> 16: Kertas dibalik tengah
      'bottom-right-curl',   // 16 -> 17: Dari kanan bawah
      'curtain-roll',        // 17 -> 18: Tirai yang digulung
      'diagonal',            // 18 -> 19: Sapu diagonal
      'cube',                // 19 -> 20: Kubus 3D
      'curtain-roll'         // 20 -> 21: Tirai yang digulung
    ];

    this.selectedTransition = 'auto'; // 'auto' or specific transition key

    // UI elements
    this.btnPrev = document.getElementById('btnPrev');
    this.btnNext = document.getElementById('btnNext');
    this.counterBadge = document.getElementById('slideCounterBadge');
    this.progressLine = document.getElementById('progressLine');
    this.transitionSelect = document.getElementById('transitionSelect');
    this.notesDrawer = document.getElementById('notesDrawer');
    this.notesContent = document.getElementById('notesContent');
    this.btnToggleNotes = document.getElementById('btnToggleNotes');
    this.btnCloseNotes = document.getElementById('btnCloseNotes');
    this.overviewModal = document.getElementById('overviewModal');
    this.overviewGrid = document.getElementById('overviewGrid');
    this.btnToggleOverview = document.getElementById('btnToggleOverview');
    this.btnCloseOverview = document.getElementById('btnCloseOverview');
    this.btnFullscreen = document.getElementById('btnFullscreen');
    this.btnReplayTransition = document.getElementById('btnReplayTransition');

    this.init();
  }

  init() {
    this.renderKaTeX();
    this.buildOverviewGrid();
    this.attachEventListeners();
    this.goToSlide(0, false);
    this.initTouchSupport();
  }

  renderKaTeX() {
    if (window.renderMathInElement) {
      renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  }

  attachEventListeners() {
    // Buttons
    if (this.btnPrev) this.btnPrev.addEventListener('click', () => this.prevSlide());
    if (this.btnNext) this.btnNext.addEventListener('click', () => this.nextSlide());
    if (this.btnReplayTransition) this.btnReplayTransition.addEventListener('click', () => this.replayCurrentSlide());

    if (this.transitionSelect) {
      this.transitionSelect.addEventListener('change', (e) => {
        this.selectedTransition = e.target.value;
      });
    }

    if (this.btnToggleNotes) {
      this.btnToggleNotes.addEventListener('click', () => this.toggleNotes());
    }
    if (this.btnCloseNotes) {
      this.btnCloseNotes.addEventListener('click', () => this.closeNotes());
    }

    if (this.btnToggleOverview) {
      this.btnToggleOverview.addEventListener('click', () => this.toggleOverview());
    }
    if (this.btnCloseOverview) {
      this.btnCloseOverview.addEventListener('click', () => this.closeOverview());
    }

    if (this.btnFullscreen) {
      this.btnFullscreen.addEventListener('click', () => this.toggleFullscreen());
    }

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
      // Ignore if focus is in a select or input
      if (['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

      switch (e.key) {
        case 'ArrowRight':
        case 'PageDown':
        case ' ': // Space
        case 'Enter':
          e.preventDefault();
          this.nextSlide();
          break;
        case 'ArrowLeft':
        case 'PageUp':
        case 'Backspace':
          e.preventDefault();
          this.prevSlide();
          break;
        case 'Home':
          e.preventDefault();
          this.goToSlide(0);
          break;
        case 'End':
          e.preventDefault();
          this.goToSlide(this.totalSlides - 1);
          break;
        case 's':
        case 'S':
          this.toggleNotes();
          break;
        case 'o':
        case 'O':
          this.toggleOverview();
          break;
        case 'f':
        case 'F':
          this.toggleFullscreen();
          break;
        case 'Escape':
          this.closeNotes();
          this.closeOverview();
          break;
      }
    });
  }

  getActiveTransition(targetIndex) {
    if (this.selectedTransition !== 'auto') {
      return this.selectedTransition;
    }
    // Auto sequence based on target slide index
    const seqIdx = Math.max(0, targetIndex - 1) % this.transitionSequence.length;
    return this.transitionSequence[seqIdx];
  }

  getTransitionClasses(transitionName) {
    switch (transitionName) {
      case 'center-fold':
        return {
          out: 'transition-center-fold-out',
          in: 'transition-center-fold-in',
          duration: 800
        };
      case 'bottom-right-curl':
        return {
          out: 'transition-bottom-right-curl-out',
          in: 'transition-bottom-right-curl-in',
          duration: 850
        };
      case 'curtain-roll':
        return {
          out: 'transition-curtain-roll-out',
          in: 'transition-curtain-roll-in',
          duration: 850
        };
      case 'cube':
        return {
          out: 'transition-cube-out',
          in: 'transition-cube-in',
          duration: 750
        };
      case 'doors':
        return {
          out: 'transition-doors-out',
          in: 'transition-doors-in',
          duration: 750
        };
      case 'diagonal':
        return {
          out: 'transition-diagonal-out',
          in: 'transition-diagonal-in',
          duration: 650
        };
      default:
        return {
          out: 'transition-fade-out',
          in: 'transition-fade-in',
          duration: 400
        };
    }
  }

  goToSlide(newIndex, animate = true) {
    if (newIndex < 0 || newIndex >= this.totalSlides) return;
    if (this.isTransitioning && animate) return;

    const oldIndex = this.currentIndex;
    const oldSlide = this.slides[oldIndex];
    const newSlide = this.slides[newIndex];

    if (!animate || oldIndex === newIndex) {
      this.slides.forEach((s, idx) => {
        s.className = 'slide' + (idx === newIndex ? ' active' : '');
      });
      this.currentIndex = newIndex;
      this.updateUI();
      return;
    }

    this.isTransitioning = true;
    const transitionName = this.getActiveTransition(newIndex);
    const trans = this.getTransitionClasses(transitionName);

    // Make new slide visible underneath or ready to animate in
    newSlide.classList.add('active');
    oldSlide.classList.add(trans.out);
    newSlide.classList.add(trans.in);

    setTimeout(() => {
      oldSlide.className = 'slide';
      newSlide.className = 'slide active';
      this.currentIndex = newIndex;
      this.isTransitioning = false;
      this.updateUI();
    }, trans.duration);
  }

  replayCurrentSlide() {
    if (this.isTransitioning) return;
    const currentSlide = this.slides[this.currentIndex];
    const transitionName = this.getActiveTransition(this.currentIndex);
    const trans = this.getTransitionClasses(transitionName);

    this.isTransitioning = true;
    currentSlide.classList.remove('active');
    void currentSlide.offsetWidth; // Trigger reflow
    currentSlide.classList.add('active', trans.in);

    setTimeout(() => {
      currentSlide.className = 'slide active';
      this.isTransitioning = false;
    }, trans.duration);
  }

  nextSlide() {
    if (this.currentIndex < this.totalSlides - 1) {
      this.goToSlide(this.currentIndex + 1, true);
    }
  }

  prevSlide() {
    if (this.currentIndex > 0) {
      this.goToSlide(this.currentIndex - 1, true);
    }
  }

  updateUI() {
    const slideNumber = this.currentIndex + 1;
    
    // Update counter
    if (this.counterBadge) {
      this.counterBadge.textContent = `${slideNumber} / ${this.totalSlides}`;
    }

    // Update progress bar
    if (this.progressLine) {
      const pct = (slideNumber / this.totalSlides) * 100;
      this.progressLine.style.width = `${pct}%`;
    }

    // Update nav buttons disabled state
    if (this.btnPrev) this.btnPrev.disabled = this.currentIndex === 0;
    if (this.btnNext) this.btnNext.disabled = this.currentIndex === this.totalSlides - 1;

    // Update speaker notes
    this.updateSpeakerNotes();

    // Update overview grid current card
    const cards = this.overviewGrid.querySelectorAll('.overview-card');
    cards.forEach((card, idx) => {
      if (idx === this.currentIndex) {
        card.classList.add('current');
      } else {
        card.classList.remove('current');
      }
    });

    // Notify current transition effect indicator in top bar if present
    const currentTrans = this.getActiveTransition(this.currentIndex);
    if (this.transitionSelect && this.selectedTransition === 'auto') {
      const opt = this.transitionSelect.querySelector(`option[value="${currentTrans}"]`);
      if (opt) {
        // Optional subtle badge or tooltip update
      }
    }
  }

  updateSpeakerNotes() {
    if (!this.notesContent) return;
    const currentSlide = this.slides[this.currentIndex];
    const notesElem = currentSlide.querySelector('.speaker-notes-data');
    if (notesElem) {
      this.notesContent.innerHTML = notesElem.innerHTML;
    } else {
      this.notesContent.innerHTML = '<p><em>Tidak ada catatan khusus untuk slide ini.</em></p>';
    }
  }

  toggleNotes() {
    if (!this.notesDrawer) return;
    this.notesDrawer.classList.toggle('open');
    if (this.btnToggleNotes) {
      this.btnToggleNotes.classList.toggle('active', this.notesDrawer.classList.contains('open'));
    }
  }

  closeNotes() {
    if (!this.notesDrawer) return;
    this.notesDrawer.classList.remove('open');
    if (this.btnToggleNotes) this.btnToggleNotes.classList.remove('active');
  }

  buildOverviewGrid() {
    if (!this.overviewGrid) return;
    this.overviewGrid.innerHTML = '';

    this.slides.forEach((slide, idx) => {
      const card = document.createElement('div');
      card.className = 'overview-card' + (idx === this.currentIndex ? ' current' : '');

      const titleElem = slide.querySelector('.slide-title') || slide.querySelector('.title-main-heading');
      const titleText = titleElem ? titleElem.textContent.trim() : `Slide ${idx + 1}`;
      const catElem = slide.querySelector('.slide-category');
      const catText = catElem ? catElem.textContent.trim() : `Bab 6`;

      card.innerHTML = `
        <div class="overview-card-num">${catText} · ${idx + 1}</div>
        <div class="overview-card-title">${titleText}</div>
        <div style="font-size: 11px; color: var(--text-light); text-align: right;">${idx + 1} dari ${this.totalSlides}</div>
      `;

      card.addEventListener('click', () => {
        this.goToSlide(idx, true);
        this.closeOverview();
      });

      this.overviewGrid.appendChild(card);
    });
  }

  toggleOverview() {
    if (!this.overviewModal) return;
    this.overviewModal.classList.toggle('open');
    if (this.btnToggleOverview) {
      this.btnToggleOverview.classList.toggle('active', this.overviewModal.classList.contains('open'));
    }
  }

  closeOverview() {
    if (!this.overviewModal) return;
    this.overviewModal.classList.remove('open');
    if (this.btnToggleOverview) this.btnToggleOverview.classList.remove('active');
  }

  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {
        console.warn(`Error attempting to enable fullscreen: ${err.message}`);
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  initTouchSupport() {
    let touchStartX = 0;
    let touchEndX = 0;

    const stage = document.querySelector('.stage-viewport');
    if (!stage) return;

    stage.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    stage.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      this.handleSwipe(touchStartX, touchEndX);
    }, { passive: true });
  }

  handleSwipe(start, end) {
    const diff = end - start;
    if (Math.abs(diff) > 50) {
      if (diff < 0) {
        this.nextSlide();
      } else {
        this.prevSlide();
      }
    }
  }
}

// Global initialization on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.presentation = new PresentationController();
});
