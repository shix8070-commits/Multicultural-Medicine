/* literature/js/search.js  【张璨】 */
window.MM = window.MM || {};

MM.listShelves = function () {
  return (MM.SHELVES || []).map(function (s) {
    return { id: s[0], name: s[2] };
  });
};

MM.getLiterature = function (id) {
  return (MM.ENTRIES || []).filter(function (e) { return e.id === id; })[0] || null;
};

MM.searchLiterature = function (q) {
  q = q || {};
  return (MM.ENTRIES || []).filter(function (e) {
    if (q.shelf && e.shelf !== q.shelf) return false;
    if (q.ethnicity && e.ethnicity !== q.ethnicity && e.ethnicity !== "多民族") return false;
    if (q.topic && String(e.topic).indexOf(q.topic) === -1) return false;
    if (q.q) {
      var blob = [e.ethnicity, e.topic, e.conclusion, e.recTitle, e.source].join(" ");
      if (blob.indexOf(q.q) === -1) return false;
    }
    return true;
  });
};
