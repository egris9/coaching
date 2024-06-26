// The `debounce` function is function that takes two parameters:
// `func` (the function to be debounced) and `wait` (the time interval in milliseconds).
// it will wait the timeout has ended before calling the function that was given as an argument
//
// if the debounce function keeps getting called before the timeout has ended then the timeout is reset
function debounce(func, wait) {
	let timeout;
	return function (...args) {
		const context = this;
		clearTimeout(timeout);
		timeout = setTimeout(() => func.apply(context, args), wait);
	};
}

class FilterUrl {
	url = new URL(window.location.href);

	constructor() {
		this.url.searchParams.set("allow_filter", true);
	}
	setUrlParam(key, value) {
		this.url.searchParams.set(key, value);
	}

	getUrl() {
		return this.url.href;
	}
}

const filterUrl = new FilterUrl();

function reloadPageWithSearchParams() {
	window.location.href = filterUrl.getUrl();
}

function handleFilterChange(radioBtnSelector, name) {
	const filter = document.querySelector(`${radioBtnSelector}:checked`).value;
	filterUrl.setUrlParam(name, filter);
	const debouncedFunc = debounce(reloadPageWithSearchParams, 1000);
	debouncedFunc();
}

const filters = [
	{
		nodeList: document.querySelectorAll(".filter-price-radio"),
		radioBtnSelector: ".filter-price-radio",
		name: "price_range",
	},
	{
		nodeList: document.querySelectorAll(".filter-sort-radio"),
		radioBtnSelector: ".filter-sort-radio",
		name: "sort_by",
	},
	{
		nodeList: document.querySelectorAll(".filter-categorie-radio"),
		radioBtnSelector: ".filter-categorie-radio",
		name: "category",
	},
	{
		nodeList: document.querySelectorAll(".filter-type-radio"),
		radioBtnSelector: ".filter-type-radio",
		name: "session_type",
	},
];

for (let i = 0; i < filters.length; i++) {
	const filter = filters[i];
	filter.nodeList.forEach((f) => {
		f.addEventListener("change", () =>
			handleFilterChange(filter.radioBtnSelector, filter.name)
		);
	});
}