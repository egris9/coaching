import universalCookie from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";
const cookies = new universalCookie(null, { path: "/" });

const deleteBtns = document.querySelectorAll("[data-delete-product-btn]");
const cartTotal = document.querySelector("#cart-total")

async function deleteItem(id){
	const csrfToken = cookies.get("csrftoken");
	const url = "http://127.0.0.1:8000/cart/delete_cart_item";
	const method = "POST";
	const headers = {
		"Content-Type": "application/json",
		"X-CSRFToken": csrfToken,
	};

	const res = await fetch(url, {
		method,
		headers,
		body: JSON.stringify({id}),
	}).then((promise) => promise.json());

	return res;
	
}

deleteBtns.forEach((btn) => {

	btn.addEventListener("click", async (e) => {
		const itemId = btn.getAttribute("data-item-id");

		const productContainer = document.querySelector(`[data-product-container="${itemId}"]`);

		productContainer.remove();
		const res = await deleteItem(itemId)

		if (res.ok) {
			if (res.action === "redirect") {
				window.location.href = `http://127.0.0.1:8000${res.url}`;
				return;
			}
			cartTotal.setAttribute('data-total', res.data.cart_total)
			cartTotal.innerText = `total: ${res.data.cart_total} $`
		}
	})
})