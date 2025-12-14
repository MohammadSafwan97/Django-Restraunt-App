document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".menu-item");
  const searchInput = document.getElementById("searchInput");
  const vegFilter = document.getElementById("vegFilter");
  const categoryBtns = document.querySelectorAll(".category-btn");

  const modal = document.getElementById("modal");
  const modalName = document.getElementById("modalName");
  const modalPrice = document.getElementById("modalPrice");
  const qtyEl = document.getElementById("qty");

  const plusQty = document.getElementById("plusQty");
  const minusQty = document.getElementById("minusQty");
  const closeModal = document.getElementById("closeModal");

  let activeCategory = "all";
  let quantity = 1;
  let price = 0;

  function filterItems() {
    if (!searchInput) return;

    const q = searchInput.value.toLowerCase();
    const vegOnly = vegFilter?.checked;

    items.forEach(item => {
      const matchSearch = item.dataset.name.toLowerCase().includes(q);
      const matchCat = activeCategory === "all" || item.dataset.category === activeCategory;
      const matchVeg = !vegOnly || item.dataset.vegetarian === "true";

      item.style.display = matchSearch && matchCat && matchVeg ? "block" : "none";
    });
  }

  searchInput?.addEventListener("input", filterItems);
  vegFilter?.addEventListener("change", filterItems);

  categoryBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      activeCategory = btn.dataset.category;

      categoryBtns.forEach(b =>
        b.classList.remove("bg-orange-600", "text-white")
      );

      btn.classList.add("bg-orange-600", "text-white");
      filterItems();
    });
  });

  items.forEach(item => {
    item.addEventListener("click", () => {
      if (!modal) return;

      modal.classList.remove("hidden");
      modal.classList.add("flex");

      quantity = 1;
      qtyEl.textContent = quantity;

      price = parseFloat(item.dataset.price);
      modalName.textContent = item.dataset.name;
      modalPrice.textContent = "$" + price.toFixed(2);
    });
  });

  plusQty?.addEventListener("click", () => {
    quantity++;
    qtyEl.textContent = quantity;
    modalPrice.textContent = "$" + (price * quantity).toFixed(2);
  });

  minusQty?.addEventListener("click", () => {
    if (quantity > 1) quantity--;
    qtyEl.textContent = quantity;
    modalPrice.textContent = "$" + (price * quantity).toFixed(2);
  });

  closeModal?.addEventListener("click", () => {
    modal.classList.add("hidden");
    modal.classList.remove("flex");
  });
});
