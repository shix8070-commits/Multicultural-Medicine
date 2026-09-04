/* forum/js/pages.js  【张鸣】 */
window.MM = window.MM || {};
MM.renderForum = MM.renderForum || function () {
  var posts = (MM.listPosts && MM.listPosts()) || [];
  var cards = posts.map(function (p) {
    return "<article class='forum-card'><b>" + p.author + "</b><p>" + p.body + "</p></article>";
  }).join("");
  return "<div class='forum-body'><p class='note'>讨论不是证据。助手不会引用这里的帖子。</p>" + cards + "</div>";
};
