(function () {
  function createFloatingMenu(options = {}) {
    const menuItems = options.items || [];
    const icon = options.icon || "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg";
    const position = options.position || "bottom-right";

    const container = document.createElement("div");
    container.style.position = "fixed";
    container.style.zIndex = "10000";
    container.style.width = "60px";
    container.style.height = "60px";

    if (position === "bottom-right") {
      container.style.bottom = "20px";
      container.style.right = "40px";
    } else if (position === "bottom-left") {
      container.style.bottom = "20px";
      container.style.left = "40px";
    }

    const menu = document.createElement("div");
    menu.style.position = "absolute";
    menu.style.bottom = "70px"; // separarlo del botón
    menu.style.right = "-14px";
    menu.style.display = "none";
    menu.style.flexDirection = "column";
    menu.style.backgroundColor = "#0069ff";
    menu.style.borderRadius = "6px";
    menu.style.overflow = "hidden";
    menu.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.3)";

    menuItems.forEach(item => {
      const btn = document.createElement("button");
      btn.innerText = item.text;
      btn.className = "optionChat";
      btn.style.padding = "10px 20px";
      btn.style.border = "none";
      btn.style.background = "inherit";
      btn.style.color = "#fff";
      btn.style.textAlign = "left";
      btn.style.cursor = "pointer";
      btn.style.fontSize = "14px";
      btn.style.borderBottom = "1px solid rgba(255,255,255,0.2)";

      btn.addEventListener("click", () => {
        if (item.url) window.open(item.url, "_blank");
      });

      btn.addEventListener("mouseenter", () => {
        btn.style.borderBottomColor = "white";
      });

      btn.addEventListener("mouseleave", () => {
        btn.style.borderBottomColor = "transparent";
      });


      menu.appendChild(btn);
    });

    const fab = document.createElement("div");
    fab.style.width = "60px";
    fab.style.height = "60px";
    fab.style.borderRadius = "50%";
    fab.style.backgroundColor = "#25D366";
    fab.style.display = "flex";
    fab.style.alignItems = "center";
    fab.style.justifyContent = "center";
    fab.style.cursor = "pointer";
    fab.style.boxShadow = "0 2px 10px rgba(0,0,0,0.2)";
    fab.innerHTML = `<img src="${icon}" width="30" height="30" alt="icon" />`;

    fab.addEventListener("click", () => {
      menu.style.display = menu.style.display === "none" ? "flex" : "none";
    });

    container.appendChild(menu);
    container.appendChild(fab);
    document.body.appendChild(container);
  }

  window.FloatingMenuPlugin = {
    init: createFloatingMenu,
  };
})();
