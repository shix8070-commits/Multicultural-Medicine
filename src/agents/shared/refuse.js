/* agents/shared/refuse.js  【何权】 */
window.MM = window.MM || {};

MM.refuseClinic = function (text) {
  return /怎么治|开什么药|改剂量|是否确诊|处方|医嘱/.test(text || "");
};

MM.refuseForumCite = function (text) {
  return /论坛|帖子|按帖|楼里说/.test(text || "");
};

MM.refuseHtml = function (kind) {
  if (kind === "forum") {
    return "<p>助手只依据入库文献回答，论坛讨论有真有假，不能当作出处。</p>";
  }
  return "<p>本助手只做证据对照，不替代诊疗。请说明民族和病/药，不要询问怎么治或开什么药。</p>";
};
