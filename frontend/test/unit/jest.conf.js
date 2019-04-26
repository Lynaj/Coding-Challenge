const path = require('path')
//
process.env.VUE_CLI_BABEL_TARGET_NODE = true;
process.env.VUE_CLI_BABEL_TRANSPILE_MODULES = true;
//
module.exports = {
  rootDir: path.resolve(__dirname, '../../'),
  moduleFileExtensions: [
    'js',
    'json',
    'vue'
  ],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  transform: {
    '^.+\\.js$': '<rootDir>/node_modules/babel-jest',
    '.*\\.(vue)$': '<rootDir>/node_modules/vue-jest',
    "^.+\\.(js|jsx)?$": "<rootDir>/node_modules/babel-jest"
  },
  testPathIgnorePatterns: [
    '<rootDir>/test/e2e'
  ],
  transformIgnorePatterns: [
      "<rootDir>/node_modules/(?!(babel-jest|jest-vue-preprocessor)/)",
      "<rootDir>/node_modules/",
      "/node_modules/.*",
      "node_modules/(?!(babel-jest|jest-vue-preprocessor)/)"
  ],
  snapshotSerializers: ['<rootDir>/node_modules/jest-serializer-vue'],
  setupFiles: ['<rootDir>/test/unit/setup'],
  coverageDirectory: '<rootDir>/test/unit/coverage',
  collectCoverage: true,
  coverageReporters: ["html", "text-summary"],
  collectCoverageFrom: [
    'src/**/*.{js,vue}',
    '!src/main.js',
    '!src/router/index.js',
    '!**/node_modules/**'
  ]
}
//
// module.exports = {
//   rootDir: path.resolve(__dirname, '../../'),
//   moduleFileExtensions: ['js', 'jsx', 'json', 'vue'],
//   transform: {
//     '^.+\\.vue$': 'vue-jest',
//     // '.+\\.(css|styl|less|sass|scss|png|jpg|ttf|woff|woff2)$':
//     //   'jest-transform-stub',
//     '^.+\\.(js|jsx)?$': 'babel-jest'
//   },
//   moduleNameMapper: {
//     '^@/(.*)$': '<rootDir>/src/$1'
//   },
//   snapshotSerializers: ['jest-serializer-vue'],
//   testMatch: [
//     '<rootDir>/(test/unit/**/*.spec.(js|jsx|ts|tsx)|**/__test__/*.(js|jsx|ts|tsx))'
//   ],
//   transformIgnorePatterns: ['<rootDir>/node_modules/']
// };
