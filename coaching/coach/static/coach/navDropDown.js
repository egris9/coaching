const navDropDownBtn = document.querySelector("[data-nav-dropDown-btn]");
console.log('🚀 ~ hello ~', );
function toggleNavDropDown() {
	const dropDown = document.querySelector(
		`[data-nav-dropDown-list]`
	);
	dropDown.classList.toggle("invisible");
	dropDown.classList.toggle("opacity-0");
}


navDropDownBtn.addEventListener("click", (e) => {
		toggleNavDropDown();
console.log('🚀 ~ hello ~', );

});

const navDropDownItems = document.querySelectorAll("[data-nav-dropDown-item]");



navDropDownItems.forEach((el) => {
	el.addEventListener("click", (e) => {
		toggleNavDropDown()
	});
});
