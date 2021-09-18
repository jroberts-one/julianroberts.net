gsap.from(".navbar > .container > .navbar-brand > .logo", 0.8, {
  delay: 0.2,
  opacity: 0,
  x: -20,
  ease: Expo.easeInOut
});

gsap.from(".logo > a", 0.9, {
  delay: 0.2,
  opacity: 0,
  x: -20,
  ease: Expo.easeInOut
});


gsap.from(".nav-item > a", 1.2, {
  delay: 0.4,
  opacity: 0,
  stagger: 0.2,
  x: -20,
  ease: Expo.easeInOut
});

gsap.from("img", 2.2, {
  delay: 0.6,
  opacity: 0,
  y: 80,
  ease: Power4.easeInOut
});

gsap.from(".social-media-container > div > a", 1, {
  delay: 1.2,
  opacity: 0,
  stagger: 0.2,
  x: -20,
  ease: Expo.easeInOut
});

gsap.from(".portfolio-text-container > *", 1.6, {
  delay: .2,
  opacity: 0,
  stagger: 0.2,
  y: 80,
  ease: Power4.easeInOut
});
