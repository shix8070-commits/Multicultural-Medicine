/* agents/research/agent.js  【何权】只对照文献，不读论坛、不汇总上传观察。 */
window.MM = window.MM || {};
MM.answerResearch = function (text) {
  if (MM.refuseForumCite(text)) return { html: MM.refuseHtml("forum"), citeIds: [], rank: "再等等" };
  var ask = MM.parseAsk(text);
  var rows = MM.searchLiterature({ ethnicity: ask.ethnicity, topic: ask.topic }) || [];
  var lit = rows.length;
  var rank = "再等等";
  if (lit === 0) rank = "跟";
  else if (lit > 2) rank = "不跟";
  var html = "<p>入库文献 " + lit + " 条。参考：" + rank + "。现场情况请到论坛查看，帖子不是证据。不替代立项审批。</p>";
  return { html: html, citeIds: rows.slice(0, 3).map(function (e) { return e.id; }), rank: rank };
};
