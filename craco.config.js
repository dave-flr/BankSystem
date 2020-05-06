module.exports = {
  style: {
    postcss: {
      plugins: [
        require('tailwindcss'),
        require("autoprefixer"),
        require("precss"),
        require("postcss-nested"),
        require("postcss-preset-env"),
        require('postcss-import'),
      ],
    }
  }
};
