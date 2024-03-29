/** @type {import('tailwindcss').Config} */
export default {
    content: ["index.html", "src/**/*.{js,jsx}"],
    theme: {
        extend: {},
        colors: {
            fontPrimary: "#444444",
            secondaryColor: "#F4F4F4",
            yellow: "#FFD43B",
        },
    },
    plugins: [require("daisyui")],
}
