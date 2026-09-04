/* agents/shared/signals.js  【何权】写；科研助手读。不要写入 MM.ENTRIES。 */
window.MM = window.MM || {};

MM.submitSignal = function (row) {
  var key = MM.storageKeys.signals;
  var list = [];
  try { list = JSON.parse(localStorage.getItem(key) || "[]"); } catch (e) { list = []; }
  row.id = row.id || ("s" + Date.now());
  list.unshift(row);
  localStorage.setItem(key, JSON.stringify(list));
  return row.id;
};

MM.summarizeSignals = function (ethnicity, topic) {
  var list = [];
  try { list = JSON.parse(localStorage.getItem(MM.storageKeys.signals) || "[]"); } catch (e) { list = []; }
  var n = list.filter(function (s) {
    return (!ethnicity || s.ethnicity === ethnicity) && (!topic || String(s.topic).indexOf(topic) !== -1);
  }).length;
  var lit = (MM.searchLiterature && MM.searchLiterature({ ethnicity: ethnicity, topic: topic })) || [];
  return { n: n, lit: lit.length };
};
