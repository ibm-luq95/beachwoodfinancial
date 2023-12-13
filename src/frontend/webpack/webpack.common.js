const glob = require("glob");
const { VueLoaderPlugin } = require("vue-loader");
const Webpack = require("webpack");
const Path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const WebpackAssetsManifest = require("webpack-assets-manifest");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const getEntryObject = () => {
  const entries = {};
  glob.sync(Path.join(__dirname, "../src/application/*.js")).forEach((path) => {
    const name = Path.basename(path, ".js");
    entries[name] = path;
  });
  return entries;
};

module.exports = {
  entry: getEntryObject(),
  output: {
    path: Path.join(__dirname, "../build"),
    filename: "js/[name].js",
    publicPath: "/static/",
    assetModuleFilename: "[path][name][ext]",
  },

  plugins: [
    new Webpack.ProgressPlugin(),
    new Webpack.EnvironmentPlugin({
      FETCHURLNAMEURL: "/core/api/fetch_url",
    }),

    /* new Webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
    }), */
    new CleanWebpackPlugin(),
    new CopyWebpackPlugin({
      patterns: [{ from: Path.resolve(__dirname, "../vendors"), to: "vendors" }],
    }),
    new WebpackAssetsManifest({
      entrypoints: true,
      output: "manifest.json",
      writeToDisk: true,
      publicPath: true,
    }),
    new VueLoaderPlugin(),
  ],
  resolve: {
    alias: {
      "~": Path.resolve(__dirname, "../src"),
      // jQuery: Path.resolve(__dirname, "../node_modules/jquery"),
    },
  },
  module: {
    rules: [
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: "javascript/auto",
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
        type: "asset",
      },
      {
        test: /\.vue$/,
        loader: "vue-loader",
      },
    ],
  },
};
