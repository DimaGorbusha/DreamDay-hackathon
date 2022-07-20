/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        main: "#3A82F1"
      },
      fontFamily: {
        'gilroy-bold': ['Gilroy-Bold'],
        'gilroy-medium': ['Gilroy-Medium'],
      }
    },
  },
  plugins: [],
}
