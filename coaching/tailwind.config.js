/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./coach/templates/**/*.html",
		"./coach/static/**/*.css",
	
		"./coach/static/**/*.js",
		"./coach/static/**/*.mjs",
	],
	theme: {
		extend: {

			fontFamily: {
				body: "Inter",
				header: "Bebas Neue",
			},
			backgroundImage: {
				"left-triangle": "linear-gradient(45deg, #F87171 6%, #0a0a0a 6%)",
				"right-triangle": "linear-gradient(45deg, #0a0a0a 94%, #F472B6 0%)",
			},


		colors: {
			foreground: {
				DEFAULT: "rgb(0 0 0)",
				subtle: "rgb(55 65 81)",
				disabled: "rgb(107 114 128)",
			},
			background: {
				DEFAULT: "rgb(229 231 235)",
				subtle: "rgb(249 250 251)",
				strong: "rgb(156 163 175)",
			},
			primary: {
				DEFAULT: "rgb(74 222 128)",
				hover: "rgb(34 197 94)",
				strong: "rgb(21 128 61)",
				subtle: "rgb(134 239 172)",
			},
			secondary: "#f472b6",
			danger: "#ef4444",
			success: "#a3e635",
			},
	},
	plugins: [require("@tailwindcss/forms")],
}};
