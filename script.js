'use strict';
const number = '255622702571';
let language = 'en';
const whatsapp = message => `https://wa.me/${number}?text=${encodeURIComponent(message)}`;
function setLanguage(lang) {
  language = lang === 'pl' ? 'pl' : 'en';
  document.documentElement.lang = language;
  document.querySelectorAll('[data-en][data-pl]').forEach(el => {el.textContent = el.dataset[language];});
  document.querySelectorAll('[data-lang]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.lang === language)));
  document.title = language === 'pl' ? 'Captain Busara | Atrakcje Zanzibaru · Kendwa Beach' : 'Captain Busara | Zanzibar Experiences · Kendwa Beach';
  document.querySelectorAll('.tour-link').forEach(link => {
    link.href = whatsapp(language === 'pl' ? `Cześć Busara! Interesuje mnie: ${link.dataset.tour}. Proszę o dostępność, zakres i cenę. Data: __. Osoby: __. Hotel: __.` : `Hi Busara! I am interested in: ${link.dataset.tour}. Please confirm availability, inclusions and price. Date: __. People: __. Hotel: __.`);
  });
  try { localStorage.setItem('busara-language', language); } catch {}
}
document.querySelectorAll('[data-lang]').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.lang)));
let initialLanguage = 'en';
try { initialLanguage = localStorage.getItem('busara-language') || 'en'; } catch {}
setLanguage(initialLanguage);
document.getElementById('year').textContent = new Date().getFullYear();
const menu = document.getElementById('menu');
const mobileNav = document.getElementById('mobile-nav');
function closeMenu(){mobileNav.hidden = true;menu.setAttribute('aria-expanded','false');}
menu.addEventListener('click', () => {const open = menu.getAttribute('aria-expanded') !== 'true';menu.setAttribute('aria-expanded',String(open));mobileNav.hidden = !open;});
mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click',closeMenu));
document.addEventListener('keydown',event=>{if(event.key==='Escape'){closeMenu();menu.focus();}});
const form = document.getElementById('booking-form');
const date = form.elements.date;
const today = new Date();
const localDate = new Date(today.getTime()-today.getTimezoneOffset()*60000).toISOString().slice(0,10);
date.min = localDate;
form.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const data = new FormData(form);
  const message = language === 'pl'
    ? `Cześć Busara! Chcę zapytać o wycieczkę.\nAtrakcja: ${data.get('experience')}\nData: ${data.get('date')}\nLiczba osób: ${data.get('people')}\nHotel / okolica: ${data.get('hotel')}\nDodatkowe informacje: ${data.get('notes') || '—'}\nProszę o potwierdzenie dostępności, pełnej ceny, zakresu i zasad rezerwacji.`
    : `Hi Busara! I would like to enquire about a trip.\nExperience: ${data.get('experience')}\nDate: ${data.get('date')}\nPeople: ${data.get('people')}\nHotel / area: ${data.get('hotel')}\nNotes: ${data.get('notes') || '—'}\nPlease confirm availability, total price, inclusions and booking terms.`;
  window.location.assign(whatsapp(message));
});
