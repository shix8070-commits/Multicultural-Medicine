/* forum/js/store.js  【张鸣】 */
window.MM = window.MM || {};

MM.listPosts = function () {
  var list = [];
  try { list = JSON.parse(localStorage.getItem(MM.storageKeys.posts) || "[]"); } catch (e) { list = []; }
  if (!list.length) list = (MM.SEED_POSTS || []).slice();
  return list;
};

MM.createPost = function (row) {
  var list = MM.listPosts();
  row.id = row.id || ("p" + Date.now());
  row.time = row.time || "刚刚";
  list.unshift(row);
  localStorage.setItem(MM.storageKeys.posts, JSON.stringify(list));
  return row.id;
};
