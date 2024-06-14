import universalCookie from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";

const cookies = new universalCookie(null, { path: "/" });

const addQuantityBtn = document.querySelectorAll("[data-add-quantity]")
const minusQuantityBtn = document.querySelectorAll("[data-minus-quantity]")
const quantityInputs = document.querySelectorAll("[data-quantity-value]")
const cartTotal = document.querySelector("#cart-total")

async function updateQuantity(id,quantity, cartTotal){
	const csrfToken = cookies.get("csrftoken");
	const url = "http://127.0.0.1:8000/cart/update_item_quantity";
	const method = "POST";
	const headers = {
		"Content-Type": "application/json",
		"X-CSRFToken": csrfToken,
	};

	const res = await fetch(url, {
		method,
		headers,
		body: JSON.stringify({id, quantity, cartTotal}),
	}).then((promise) => promise.json());

	return res;
	
}

function setCartTotal(total, prevQuantity, quantity, productPrice) {
	if (prevQuantity > quantity) {
		const difference = prevQuantity - quantity
		const reducedTotal = total - (difference * productPrice)
		cartTotal.setAttribute('data-total', reducedTotal)
		cartTotal.innerText = `total: ${reducedTotal} DH`
		return reducedTotal
	} else if (prevQuantity < quantity) {
		const difference = quantity - prevQuantity
		const newTotal = total + (difference * productPrice)
		cartTotal.setAttribute('data-total', newTotal)
		cartTotal.innerText = `total: ${newTotal} DH`
		return newTotal
	}
}

function keepNumbersOnly(inputString) {
    // Use regular expression to match only numeric characters
    const numericString = inputString.replace(/\D/g, '');

    return Number(numericString);
}


addQuantityBtn.forEach((btn) => {
	btn.addEventListener("click", async () => {
		const id = btn.getAttribute("data-item-id");
		const quantityInput = document.querySelector(`[data-quantity-value][data-item-id="${id}"]`);
		const prevQuantity = keepNumbersOnly(quantityInput.getAttribute('data-prev-quantity'))
		let quantity = keepNumbersOnly(quantityInput.value)
		quantity = quantity + 1 
		quantityInput.value = quantity
		
		const total = Number(cartTotal.getAttribute('data-total'))
		const productPrice = Number(btn.getAttribute('data-item-price'))

		const newTotal = setCartTotal(total, prevQuantity, quantity, productPrice)
		quantityInput.setAttribute('data-prev-quantity',quantity)
		const res = await updateQuantity(id,quantity, newTotal)
		if (res.ok && res.action === "redirect") {
			window.location.href = `http://127.0.0.1:8000${res.url}`;
			return;
		}

	})
})


minusQuantityBtn.forEach((btn) => {
	btn.addEventListener("click", async () => {
		const id = btn.getAttribute("data-item-id");
		const quantityInput = document.querySelector(`[data-quantity-value][data-item-id="${id}"]`);
		const prevQuantity = keepNumbersOnly(quantityInput.getAttribute('data-prev-quantity'))
		let quantity = keepNumbersOnly(quantityInput.value)
		if(quantity > 1){
		quantity = quantity - 1
		quantityInput.value = quantity
		}

		const total = Number(cartTotal.getAttribute('data-total'))
		const productPrice = Number(btn.getAttribute('data-item-price'))

		const newTotal = setCartTotal(total, prevQuantity, quantity, productPrice)
		quantityInput.setAttribute('data-prev-quantity',quantity)
		await updateQuantity(id,quantity, newTotal)

	})
})

quantityInputs.forEach((input) => {
	input.addEventListener("change", async () => {
		const quantity = keepNumbersOnly(input.value)
		const prevQuantity = Number(input.getAttribute('data-prev-quantity'))
		const id = input.getAttribute("data-item-id")
		const newTotal = setCartTotal(total, prevQuantity, quantity, productPrice)
		input.setAttribute('data-prev-quantity',quantity)
		if(newTotal) {
			await updateQuantity(id,quantity, newTotal)
		}
	})
})

