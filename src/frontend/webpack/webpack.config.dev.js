const Path = require("path");
const Webpack = require("webpack");
const WebpackNotifierPlugin = require("webpack-notifier");
const { merge } = require("webpack-merge");
const StylelintPlugin = require("stylelint-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const ESLintPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const common = require("./webpack.common.js");

module.exports = merge(common, {
  stats: {
    errorDetails: true,
  },
  // cache: false,
  target: "web",
  mode: "development",
  devtool: "inline-source-map",
  output: {
    chunkFilename: "js/[name].chunk.js",
    publicPath: "http://localhost:9091/",
    clean: true,
  },
  devServer: {
    hot: true,
    host: "0.0.0.0",
    port: 9091,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    devMiddleware: {
      writeToDisk: true,
    },
  },
  // node: {
  //   global: true,
  // },
  plugins: [
    new WebpackNotifierPlugin({ emoji: true }),
    new HtmlWebpackPlugin({
      title: "TinyMCE Webpack Demo",
      meta: { viewport: "width=device-width, initial-scale=1" },
    }),
    new Webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("development"),
    }),
    new StylelintPlugin({
      files: Path.resolve(__dirname, "../src/**/*.s?(a|c)ss"),
    }),
    new ESLintPlugin({
      extensions: "js",
      emitWarning: true,
      files: Path.resolve(__dirname, "../src"),
    }),
    new MiniCssExtractPlugin({
      filename: "css/[name].css",
      chunkFilename: "css/[id].css",
    }),
  ],
  module: {
    rules: [
      {
        test: /\.html$/i,
        loader: "html-loader",
      },
      /* {
        test: /\.js$/,
        include: Path.resolve(__dirname, "../src"),
        loader: "babel-loader",
      }, */
      {
        test: /\.js$/,
        include: Path.resolve(__dirname, "../src"),
        loader: "esbuild-loader", // replace loader for the js files
        options: {
          // we can pass options as we like
          target: ["es2017"],
        },
      },
      {
        test: /\.s?css$/i,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: "css-loader",
            options: {
              sourceMap: true,
            },
          },
          "postcss-loader",
          "sass-loader",
        ],
      },
    ],
  },
});
