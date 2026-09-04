/* shared/contracts.js
 * 负责人：张鸣（形状） / 张璨实现 search* / 何权实现 answer* 与 signal / 张鸣实现 forum
 * 实际实现分放在各自目录，这里只规定名字，避免对不上。
 */

window.MM = window.MM || {};

/** @typedef {{ id:number, ethnicity:string, topic:string, shelf:string, conclusion:string, boundary:string, source:string, rec?:string, recTitle?:string }} Literature */

MM.contracts = {
  // —— 张璨实现（literature/js/search.js）——
  // searchLiterature({ ethnicity, topic, shelf, q }) -> Literature[]
  // getLiterature(id) -> Literature | null
  // listShelves() -> [{ id, name }]

  // —— 何权实现（agents/）——
  // parseAsk(text) -> { ethnicity, topic, phen }
  // answerClinic(text) -> { html, citeIds }          citeIds 只能是文献 id
  // answerResearch(text) -> { html, citeIds, rank }   rank: 跟 | 不跟 | 再等等
  // 本期不做 submitSignal / 脱敏观察上传；现场只进论坛

  // —— 张鸣实现（forum/）——
  // createPost({ author, body }) -> id     不得写入 ENTRIES
  // listPosts() -> Post[]
};
