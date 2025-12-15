console.log("menu.js loaded");

document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".menu-item");

  const modal = document.getElementById("modal");
  const modalName = document.getElementById("modalName");
  const modalDescription = document.getElementById("modalDescription");
  const modalPrice = document.getElementById("modalPrice");
  const qtyEl = document.getElementById("qty");

  const plusQty = document.getElementById("plusQty");
  const minusQty = document.getElementById("minusQty");
  const closeModal = document.getElementById("closeModal");
  const addToCartBtn = document.getElementById("addToCartBtn");

  let quantity = 1;
  let price = 0;
  let currentItem = null;

  items.forEach(item => {
    item.addEventListener("click", () => {
      quantity = 1;
      price = parseFloat(item.dataset.price);

      currentItem = {
        id: item.dataset.id,
        name: item.dataset.name,
        price: price,
      };

      modalName.textContent = item.dataset.name;
      modalDescription.textContent = item.dataset.description || "";
      modalPrice.textContent = "$" + price.toFixed(2);
      qtyEl.textContent = quantity;

      modal.classList.remove("hidden");
      modal.classList.add("flex");
    });
  });

  plusQty.onclick = () => {
    quantity++;
    qtyEl.textContent = quantity;
    modalPrice.textContent = "$" + (price * quantity).toFixed(2);
  };

  minusQty.onclick = () => {
    if (quantity > 1) quantity--;
    qtyEl.textContent = quantity;
    modalPrice.textContent = "$" + (price * quantity).toFixed(2);
  };

  addToCartBtn.onclick = () => {
    if (!currentItem) return;

    addToCart({
      ...currentItem,
      quantity: quantity,
    });

    modal.classList.add("hidden");
    modal.classList.remove("flex");
  };

  closeModal.onclick = () => {
    modal.classList.add("hidden");
    modal.classList.remove("flex");
  };
});
