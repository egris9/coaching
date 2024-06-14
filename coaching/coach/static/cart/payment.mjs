import universalCookie from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";
const cookies = new universalCookie(null, { path: "/" });

const form = document.querySelector("#payment-form");

const isValidName = (name) => {
	return name.trim().length >= 3 && name.trim().length <= 225;
};

const isValidAddress = (address) => {
	return address.trim().length > 0;
};

const isValidEmail = (email) => {
	/*
	This Javascript regex will match 99% of valid email addresses and will not pass validation for email addresses that have, for instance:

	Dots in the beginning
	Multiple dots at the end
	But at the same time it will allow part after @ to be IP address.
	
	*/
	const regex =
		/^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

	return regex.test(email);
};

const isValidCartName = (cartName) => {
	return cartName.trim().length > 0;
};

const isValidExp = (date) => {
	const regex =
		/^[1-9][0-9][0-9]{2}-([0][1-9]|[1][0-2])-([1-2][0-9]|[0][1-9]|[3][0-1])?$/;
	return regex.test(date);
};

const isValidCVV = (code) => {
	if (!isNaN(Number(code)) && (code.length === 4 || code.length === 3))
		return true;
	return false;
};

const validateField = (selector, validator, value, text) => {
	const field = document.querySelector(selector);
	if (validator(value) === false) {
		field.innerText = text;
		return false;
	} else {
		field.innerText = "";
		return true;
	}
};

async function addOrder(data) {
	const csrfToken = cookies.get("csrftoken");
	const url = "http://127.0.0.1:8000/cart/add_order";
	const method = "POST";
	const headers = {
		"Content-Type": "application/json",
		"X-CSRFToken": csrfToken,
	};

	const res = await fetch(url, {
		method,
		headers,
		body: JSON.stringify({ data }),
	}).then((promise) => promise.json());

	return res;
}

function validateForm() {
	const formData = new FormData(form);

	const data = Object.fromEntries(formData.entries());

	const validFirstName = validateField(
		"#first_name_msg",
		isValidName,
		data.first_name,
		"Name must be between 3 and 225 characters"
	);
	const validLastName = validateField(
		"#last_name_msg",
		isValidName,
		data.last_name,
		"Name must be between 3 and 225 characters"
	);
	const validEmail = validateField(
		"#email_msg",
		isValidEmail,
		data.email,
		"write a valid email, example: apostel@email.com"
	);
	const validAddress = validateField(
		"#address_msg",
		isValidAddress,
		data.address,
		"address is required"
	);
	const validCartName = validateField(
		"#cartName_msg",
		isValidCartName,
		data.cart_name,
		"cart name is required"
	);
	const validExp = validateField(
		"#exp_msg",
		isValidExp,
		data.exp,
		"please write a valid date example: 2028-12-30"
	);
	const validCVV = validateField(
		"#cvv_msg",
		isValidCVV,
		data.cvv,
		"please write a valid CVV code example: 0000"
	);

	if (
		validFirstName &&
		validLastName &&
		validEmail &&
		validAddress &&
		validCartName &&
		validExp &&
		validCVV
	) {
		return data;
	}
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
		stopOnFocus: true,
	}).showToast();



form.addEventListener("submit", async (e) => {
	e.preventDefault();
	const data = validateForm();
	if (data) {
		const cartItemId = document
			.querySelector("[data-table-row]")
			.getAttribute("data-product-container");

		data.cart_item_id = cartItemId;
		const res = await addOrder(data);
		if (res.ok) {
			if (res.action === "redirect") {
				window.location.href = `http://127.0.0.1:8000${res.url}`;
				return;
			}
			successToast("your order is confirmed");
			setTimeout(() => {
				window.location.href = "http://127.0.0.1:8000/shop";
			}, 2000)
		} 
	}
});
