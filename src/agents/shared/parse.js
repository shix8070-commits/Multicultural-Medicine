/* agents/shared/parse.js  【何权】 */
window.MM = window.MM || {};
MM.parseAsk = function (text) {
  text = text || "";
  var eth = "";
  var topic = "";
  ["维吾尔族", "傣族", "哈萨克族", "藏族", "蒙古族", "回族", "白族", "哈尼族", "汉族"].forEach(function (e) {
    if (text.indexOf(e) !== -1) eth = e;
  });
  ["华法林", "出血", "氯吡格雷", "心血管", "糖尿病", "高血压"].forEach(function (t) {
    if (text.indexOf(t) !== -1) topic = topic || t;
  });
  return { ethnicity: eth, topic: topic, phen: text };
};
