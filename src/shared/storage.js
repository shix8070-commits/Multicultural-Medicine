/* shared/storage.js  负责人：张鸣。键名全组共用，不要自己另起一套。 */

window.MM = window.MM || {};
MM.storageKeys = {
  signals: "mm-signals-v1",      // 本期不用：现场走论坛，助手不汇总上传
  cases: "mm-cases-v1",          // 何权
  judges: "mm-judges-v1",        // 何权
  favs: "mm-favs-v1",            // 张璨收藏，张鸣知识库入口去读
  posts: "mm-posts-v1",          // 张鸣论坛；Agent 禁止读这个键
};
