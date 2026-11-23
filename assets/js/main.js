// ==========================================================================
// LaBiOmicS · Blog & Radar Científico - Scripts & Motor de Busca
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

  // 3. Motor de Busca de Artigos e Filtros (Padrão Oficial do LaBiOmicS)
  const searchInput = document.getElementById("q");
  const postsContainer = document.getElementById("posts-container");
  const paginationNav = document.getElementById("pagination-nav");
  const searchMsg = document.getElementById("search-msg");
  const filterBtns = document.querySelectorAll(".filter-btn");

  let allPostsIndex = null;
  let defaultPostsHTML = postsContainer ? postsContainer.innerHTML : "";

  // Atalho de teclado '/' para focar a busca e 'Esc' para limpar
  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && document.activeElement !== searchInput && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) {
      e.preventDefault();
      if (searchInput) {
        searchInput.focus();
      }
    } else if (e.key === "Escape" && document.activeElement === searchInput) {
      searchInput.value = "";
      restoreDefaultView();
    }
  });

  // Carrega o índice search.json sob demanda
  const loadSearchIndex = async () => {
    if (allPostsIndex) return allPostsIndex;
    try {
      const baseUrl = (document.querySelector('meta[name="baseurl"]') || {}).content || "";
      const res = await fetch(`${baseUrl}/search.json`);
      if (res.ok) {
        allPostsIndex = await res.json();
      }
    } catch (err) {
      console.warn("Falha ao carregar índice de busca:", err);
    }
    return allPostsIndex || [];
  };

  const renderSearchResults = (results, query) => {
    if (!postsContainer) return;

    if (results.length === 0) {
      postsContainer.innerHTML = `
        <div class="empty-state" style="grid-column: 1 / -1; padding: 48px 0; text-align: center;">
          <p style="font-size: 1.1rem; color: var(--muted); margin-bottom: 12px;">Nenhum artigo encontrado para "<strong>${escapeHtml(query)}</strong>".</p>
        </div>
      `;
    } else {
      postsContainer.innerHTML = results.map(post => `
        <article class="post-card" data-categories="${(post.categories || []).join(' ')}" data-tags="${(post.tags || []).join(' ')}">
          <div class="post-card-top">
            <div class="post-badges">
              ${post.journal ? `<span class="badge badge-journal">${escapeHtml(post.journal)}</span>` : ""}
              ${(post.categories || []).map(cat => `<span class="badge badge-category">${escapeHtml(cat)}</span>`).join("")}
            </div>
            <h2 class="post-card-title">
              <a href="${post.url}">${escapeHtml(post.title)}</a>
            </h2>
            <p class="post-card-excerpt">${escapeHtml(post.excerpt)}</p>
          </div>
          <div class="post-card-meta">
            <div class="post-date-read">
              <span>📅 ${post.date}</span>
            </div>
            <a class="post-card-link" href="${post.url}">Ler síntese <span>→</span></a>
          </div>
        </article>
      `).join("");
    }

    if (searchMsg) {
      searchMsg.hidden = false;
      searchMsg.innerHTML = `
        <span><strong>${results.length}</strong> ${results.length === 1 ? 'artigo encontrado' : 'artigos encontrados'} para "<strong>${escapeHtml(query)}</strong>"</span>
        <button type="button" class="search-msg-clear" id="search-msg-clear">✕ Limpar busca</button>
      `;

      const clearBtn = document.getElementById("search-msg-clear");
      if (clearBtn) clearBtn.addEventListener("click", () => {
        if (searchInput) searchInput.value = "";
        restoreDefaultView();
      });
    }

    if (paginationNav) {
      paginationNav.style.display = "none";
    }
  };

  const restoreDefaultView = () => {
    if (postsContainer) postsContainer.innerHTML = defaultPostsHTML;
    if (paginationNav) paginationNav.style.display = "flex";
    if (searchMsg) searchMsg.hidden = true;
    attachFilterListeners();
  };

  const escapeHtml = (str) => {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  };

  if (searchInput) {
    searchInput.addEventListener("focus", () => { loadSearchIndex(); });

    searchInput.addEventListener("input", async (e) => {
      const q = e.target.value.trim().toLowerCase();
      if (!q) {
        restoreDefaultView();
        return;
      }

      const posts = await loadSearchIndex();
      const filtered = posts.filter(p => {
        const titleMatch = (p.title || "").toLowerCase().includes(q);
        const excerptMatch = (p.excerpt || "").toLowerCase().includes(q);
        const journalMatch = (p.journal || "").toLowerCase().includes(q);
        const authorMatch = (p.authors || "").toLowerCase().includes(q);
        const doiMatch = (p.doi || "").toLowerCase().includes(q);
        const tagMatch = (p.tags || []).some(t => t.toLowerCase().includes(q));
        const catMatch = (p.categories || []).some(c => c.toLowerCase().includes(q));

        return titleMatch || excerptMatch || journalMatch || authorMatch || doiMatch || tagMatch || catMatch;
      });

      renderSearchResults(filtered, e.target.value.trim());
    });
  }

  // 4. Filtro por Linhas de Pesquisa
  const attachFilterListeners = () => {
    const cards = document.querySelectorAll(".post-card");
    filterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        if (searchInput) searchInput.value = "";
        if (searchMsg) searchMsg.hidden = true;
        if (paginationNav) paginationNav.style.display = "flex";

        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        const selected = btn.getAttribute("data-filter");
        cards.forEach(card => {
          const cats = (card.getAttribute("data-categories") || "").toLowerCase();
          const tags = (card.getAttribute("data-tags") || "").toLowerCase();
          if (selected === "all" || cats.includes(selected.toLowerCase()) || tags.includes(selected.toLowerCase())) {
            card.style.display = "flex";
          } else {
            card.style.display = "none";
          }
        });
      });
    });
  };

  attachFilterListeners();
});
