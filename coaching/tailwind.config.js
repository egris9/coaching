/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./coach/templates/**/*.html",
		"./coach/static/**/*.css",
	
		"./coach/static/**/*.js",
		"./coach/static/**/*.mjs",
		'node_modules/preline/dist/*.js',
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
			backgroundImage: {
				'light-arrow': 'url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAyNCAyNCc+PHBhdGggZmlsbD0nIzBmMTcyYScgZD0nTTEyIDE2Yy0uMyAwLS41LS4xLS43LS4zbC02LTZjLS40LS40LS40LTEgMC0xLjRzMS0uNCAxLjQgMGw1LjMgNS4zIDUuMy01LjNjLjQtLjQgMS0uNCAxLjQgMHMuNCAxIDAgMS40bC02IDZjLS4yLjItLjQuMy0uNy4zeicvPjwvc3ZnPg==")',
				'dark-arrow': 'url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAyNCAyNCc+PHBhdGggZmlsbD0nI2ZmZicgZD0nTTEyIDE2Yy0uMyAwLS41LS4xLS43LS4zbC02LTZjLS40LS40LS40LTEgMC0xLjRzMS0uNCAxLjQgMGw1LjMgNS4zIDUuMy01LjNjLjQtLjQgMS0uNCAxLjQgMHMuNCAxIDAgMS40bC02IDZjLS4yLjItLjQuMy0uNy4zeicvPjwvc3ZnPg==")',
				'light-mode': 'linear-gradient(145deg, rgb(6 182 212 / 4%) 12%, rgb(6 182 212 / 10%) 42%, rgb(6 182 212 / 5%) 60%, rgb(6 182 212 / 18%) 85%)',
				'dark-mode': 'linear-gradient(145deg, rgb(6 182 212 / 0%) 12%, rgb(6 182 212 / 3%) 42%, rgb(6 182 212 / 10%) 60%, rgb(6 182 212 / 4%) 85%)',
			},
	},
	
	plugins: [require("@tailwindcss/forms"),
	require('preline/plugin')
	],
	
}};
