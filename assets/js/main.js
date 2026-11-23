// ==========================================================================
// LaBiOmicS · Blog & Radar Científico - Scripts
// ==========================================================================

document.addEventListener("DOMContentLoaded", () => {
  // 1. Barra de progresso de leitura
  const progressBar = document.getElementById("progress-bar");
  if (progressBar) {
    const updateProgress = () => {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const progress = docHeight > 0 ? scrollTop / docHeight : 0;
      progressBar.style.transform = `scaleX(${Math.min(Math.max(progress, 0), 1)})`;
    };
    window.addEventListener("scroll", updateProgress, { passive: true });
    updateProgress();
  }

  // 2. Alternador de tema claro / escuro sincronizado com labiomics.github.io
  const themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", () => {
      const currentTheme = document.documentElement.getAttribute("data-theme");
      const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      
      let newTheme = "light";
      if (!currentTheme) {
        newTheme = prefersDark ? "light" : "dark";
      } else if (currentTheme === "dark") {
        newTheme = "light";
      } else {
        newTheme = "dark";
      }

      document.documentElement.setAttribute("data-theme", newTheme);
      try {
        localStorage.setItem("labiomics-theme", newTheme);
      } catch (e) {
        console.warn("Não foi possível salvar preferência de tema no localStorage", e);
      }
    });
  }

  // 3. Filtro dinâmico de categorias na página inicial
  const filterBtns = document.querySelectorAll(".filter-btn");
  const postCards = document.querySelectorAll(".post-card");

  if (filterBtns.length > 0 && postCards.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        // Atualiza estado ativo do botão
        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        const selectedCategory = btn.getAttribute("data-filter");

        postCards.forEach(card => {
          const cardCategories = (card.getAttribute("data-categories") || "").toLowerCase();
          const cardTags = (card.getAttribute("data-tags") || "").toLowerCase();
          
          if (selectedCategory === "all" || cardCategories.includes(selectedCategory.toLowerCase()) || cardTags.includes(selectedCategory.toLowerCase())) {
            card.style.display = "flex";
          } else {
            card.style.display = "none";
          }
        });
      });
    });
  }
});
