/* agents/clinic/agent.js  【何权】 */
window.MM = window.MM || {};
MM.answerClinic = function (text) {
  if (MM.refuseForumCite(text)) return { html: MM.refuseHtml("forum"), citeIds: [] };
  if (MM.refuseClinic(text)) return { html: MM.refuseHtml("clinic"), citeIds: [] };
  var ask = MM.parseAsk(text);
  var rows = MM.searchLiterature({ ethnicity: ask.ethnicity, topic: ask.topic }) || [];
  var ids = rows.slice(0, 3).map(function (e) { return e.id; });
  var html = rows.length
    ? "<p>现有入库 " + rows.length + " 条。只作对照，不是医嘱。</p>"
    : "<p>现有公开材料不足，不能当成诊疗结论。</p>";
  return { html: html, citeIds: ids };
};
