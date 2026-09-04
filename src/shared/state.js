/* shared/state.js  【张鸣】页面级状态。外壳读写，各人页面只读当前端。 */
window.MM = window.MM || {};
MM.state = MM.state || {
  tab: "clinic",   /* clinic | research | forum | lit */
  page: "home"
};
