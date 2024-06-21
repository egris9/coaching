import Cookies from 'https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm'
      
const cookies = new Cookies (null, { path: "/" });

const btns = document.querySelectorAll("[data-add-to-cart-btn]");

function getData(btn) {
	let quantity = 1;

	const productId = Number(btn.getAttribute("data-product-id"));
	const product_type = btn.getAttribute("data-product-type");
	if (product_type == "accessory"){
		quantity = Number(document.querySelector("#quantity-value").value);
	}

	const price = Number(
		document.getElementById("product-price").getAttribute("data-price")
	);

	if (isNaN(quantity) === true || quantity < 1) quantity = 1;

	if (productId <= 0 || isNaN(productId)) {
		console.log("please set product id", productId);
		return;
	}
	return {
		productId,
		quantity,
		price,
		product_type,
	};
}

async function addToCart(data) {
	const csrfToken = cookies.get("csrftoken");
	const url = "http://127.0.0.1:8000/cart/add_to_cart";
	const method = "POST";
	const headers = {
		"Content-Type": "application/json",
		"X-CSRFToken": csrfToken,
	};

	const res = await fetch(url, {
		method,
		headers,
		body: JSON.stringify(data),
	}).then((promise) => promise.json());

	return res;
}

const successToast = (text) =>
	Toastify({
		text,
		avatar:
			"https://api.iconify.design/material-symbols:done.svg?color=%234ade80",

		className:
			"bg-gradient-to-l from-neutral-800 to-neutral-800 text-sm w-full px-4 py-4 border-2 border-green-700 rounded-md max-w-fit capitalize flex items-center justify-between text-body text-neutral-300",
		close: true,
		gravity: "top", // `top` or `bottom`
		position: "right", // `left`, `center` or `right`
		stopOnFocus: true, // Prevents dismissing of toast on hover
	}).showToast();

const errorToast = (text) =>
	Toastify({
		text,
		avatar:
			"https://api.iconify.design/jam:triangle-danger-f.svg?color=%23fb7185",

		className:
			"bg-gradient-to-l from-neutral-800 to-neutral-800 text-sm w-full px-4 py-4 border-2 border-red-700 rounded-md max-w-fit capitalize flex items-center justify-between text-body text-neutral-300",
		close: true,
		gravity: "top", // `top` or `bottom`
		position: "right", // `left`, `center` or `right`
		stopOnFocus: true, // Prevents dismissing of toast on hover
	}).showToast();

btns.forEach((btn) => {
	btn.addEventListener("click", async () => {
		const data = getData(btn);

		const res = await addToCart(data);

		if (res.ok) {
			// see what type of action happened in the backend
			if (res.action === "nothing") {
				successToast("your product just got added");
				return;
			}

			if (res.action === "create") {
				successToast("product was added successfully");
				return;
			}

			if (res.action === "update") {
				successToast("your cart was updated successfully");
				return;
			}
			if (res.action === "redirect") {
				window.location.href = `http://127.0.0.1:8000${res.url}`;
				return;
			}
		} else {
			errorToast("an error has occured, try again later.");
			return;
		}
	});
});
