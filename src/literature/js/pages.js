/* literature/js/pages.js  【张璨】
 * 在这里画速查页、详情页。约定：MM.renderSearchPage / MM.renderLitDetail
 * 外壳 app.js 会在 page === "lit" | "litDetail" 时调用。
 */

window.MM = window.MM || {};
MM.renderSearchPage = MM.renderSearchPage || function () {
  return "<div class='pad'><p class='note'>张璨：在 literature/js/pages.js 实现速查页。</p></div>";
};
MM.renderLitDetail = MM.renderLitDetail || function () {
  return "<div class='pad'><p class='note'>张璨：在 literature/js/pages.js 实现详情页。</p></div>";
};
