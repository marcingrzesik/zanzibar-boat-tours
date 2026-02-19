// 1) Replace with your friend's real WhatsApp number (international format, no +, no spaces)
const WHATSAPP_NUMBER = "+255622702571"; // e.g. 2557XXXXXXXX

function makeWhatsAppLink(message) {
  const base = "https://wa.me/";
  const text = encodeURIComponent(message);
  return `${base}${WHATSAPP_NUMBER}?text=${text}`;
}

function setWhatsAppLinks() {
  const defaultMsg =
    "Hi! I’d like to book a tour in Zanzibar. Date: __/__/__. Hotel: ____. People: __. Which tours are available today? Thanks!";

  const top = document.getElementById("whatsappTop");
  const bottom = document.getElementById("whatsappBottom");
  const sticky = document.getElementById("stickyWA");

  [top, bottom, sticky].forEach((el) => {
    if (!el) return;
    el.href = makeWhatsAppLink(defaultMsg);
  });

  document.querySelectorAll(".wa").forEach((btn) => {
    const tour = btn.getAttribute("data-tour") || "a tour";
    const msg =
      `Hi! I’d like to book: ${tour}. ` +
      "Date: __/__/__. Hotel: ____. People: __. Private or group? Price please. Thanks!";
    btn.href = makeWhatsAppLink(msg);
  });
}

function setYear() {
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
}

function setupCopyTemplate() {
  const btn = document.getElementById("copyBtn");
  const text = document.getElementById("templateText");
  if (!btn || !text) return;

  btn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(text.textContent.trim());
      btn.textContent = "Copied ✅";
      setTimeout(() => (btn.textContent = "Copy"), 1400);
    } catch {
      btn.textContent = "Copy manually";
      setTimeout(() => (btn.textContent = "Copy"), 1400);
    }
  });
}

function setupMobileMenu() {
  const burger = document.getElementById("burger");
  const menu = document.getElementById("mobileMenu");
  if (!burger || !menu) return;

  burger.addEventListener("click", () => {
    menu.classList.toggle("show");
  });

  menu.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => menu.classList.remove("show"))
  );
}

setWhatsAppLinks();
setYear();
setupCopyTemplate();
setupMobileMenu();
