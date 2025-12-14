let authMode = "login";

function openAuthModal(mode) {
  authMode = mode;
  const modal = document.getElementById("authModal");
  modal.classList.remove("hidden");
  modal.classList.add("flex");
  updateAuthUI();
}

function closeAuthModal() {
  document.getElementById("authModal").classList.add("hidden");
}

function switchAuthMode() {
  authMode = authMode === "login" ? "signup" : "login";
  updateAuthUI();
}

function updateAuthUI() {
  const isLogin = authMode === "login";

  document.getElementById("authTitle").innerText =
    isLogin ? "Welcome Back" : "Create Account";

  document.getElementById("nameField").classList.toggle("hidden", isLogin);

  document.querySelector("button[type='submit']").innerText =
    isLogin ? "Sign In" : "Create Account";

  document.getElementById("switchText").innerText =
    isLogin ? "Don't have an account?" : "Already have an account?";
}

function submitAuth(e) {
  e.preventDefault();
  alert("Auth submitted (demo)");
  closeAuthModal();
}
