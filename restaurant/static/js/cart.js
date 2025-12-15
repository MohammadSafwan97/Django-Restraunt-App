const DELIVERY_FEE = 4.99;
const FREE_DELIVERY_THRESHOLD = 30;

let cart = [];

function openCart() {
  document.getElementById("cart-sidebar").classList.remove("translate-x-full");
  document.getElementById("cart-backdrop").classList.remove("hidden");
  renderCart();
}

function closeCart() {
  document.getElementById("cart-sidebar").classList.add("translate-x-full");
  document.getElementById("cart-backdrop").classList.add("hidden");
}

function addToCart(item) {
  const existing = cart.find(c => c.id === item.id);

  if (existing) {
    existing.quantity += item.quantity;
  } else {
    cart.push({ ...item });
  }

  updateCartCount();
  openCart();
}

function updateQuantity(id, qty) {
  if (qty < 1) return;

  cart = cart.map(item =>
    item.id === id ? { ...item, quantity: qty } : item
  );

  updateCartCount();
  renderCart();
}

function removeFromCart(id) {
  cart = cart.filter(item => item.id !== id);
  updateCartCount();
  renderCart();
}

function renderCart() {
  const container = document.getElementById("cart-items");
  const footer = document.getElementById("cart-footer");

  if (!container || !footer) return;

  if (cart.length === 0) {
    container.innerHTML = `
      <div class="text-center py-12 text-neutral-500">
        Your cart is empty
      </div>
    `;
    footer.classList.add("hidden");
    return;
  }

  footer.classList.remove("hidden");

  let subtotal = 0;

  container.innerHTML = cart.map(item => {
    subtotal += item.price * item.quantity;

    return `
      <div class="bg-neutral-50 rounded-lg p-4 mb-4 space-y-3">
        <div class="flex justify-between">
          <div>
            <h3 class="font-medium">${item.name}</h3>
            <p class="text-orange-600">$${item.price.toFixed(2)}</p>
          </div>
          <button onclick="removeFromCart('${item.id}')">🗑</button>
        </div>

        <div class="flex justify-between items-center">
          <div class="flex gap-2">
            <button onclick="updateQuantity('${item.id}', ${item.quantity - 1})">−</button>
            <span>${item.quantity}</span>
            <button onclick="updateQuantity('${item.id}', ${item.quantity + 1})">+</button>
          </div>
          <span>$${(item.price * item.quantity).toFixed(2)}</span>
        </div>
      </div>
    `;
  }).join("");

  const delivery = subtotal >= FREE_DELIVERY_THRESHOLD ? 0 : DELIVERY_FEE;
  const total = subtotal + delivery;

  document.getElementById("cart-subtotal").innerText = `$${subtotal.toFixed(2)}`;
  document.getElementById("cart-delivery").innerText =
    delivery === 0 ? "FREE" : `$${DELIVERY_FEE}`;
  document.getElementById("cart-total").innerText = `$${total.toFixed(2)}`;
}

function updateCartCount() {
  const countEl = document.getElementById("cart-count");
  if (!countEl) return;

  const totalItems = cart.reduce((sum, i) => sum + i.quantity, 0);
  countEl.textContent = totalItems;
  countEl.classList.toggle("hidden", totalItems === 0);
}
