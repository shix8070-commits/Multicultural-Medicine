/* src/app/js/app.js  【张鸣】外壳路由。调用各人挂在 MM 上的 render 函数。 */
(function () {
  var page = "clinic";

  function header() {
    return '<div class="status" style="padding:8px 18px 0;font-size:12px;font-weight:650"><span>9:41</span><span>100%</span></div>'
      + '<div class="wx-bar"><div></div><div class="seg">'
      + '<button data-go="clinic" class="' + (page === "clinic" ? "on" : "") + '">临床助手</button>'
      + '<button data-go="research" class="' + (page === "research" ? "on" : "") + '">科研助手</button>'
      + '<button data-go="forum" class="' + (page === "forum" ? "on" : "") + '">我的论坛</button>'
      + '</div><div class="capsule"><span>···</span><span>○</span></div></div>';
  }

  function body() {
    if (page === "forum") return (MM.renderForum && MM.renderForum()) || "";
    if (page === "research") return (MM.renderResearchHome && MM.renderResearchHome()) || "";
    if (page === "lit") return (MM.renderSearchPage && MM.renderSearchPage()) || "";
    return (MM.renderClinicHome && MM.renderClinicHome()) || "";
  }

  function render() {
    document.getElementById("app").innerHTML = header() + '<div class="pad" style="flex:1;overflow:auto">' + body() + "</div>";
    document.querySelectorAll("[data-go]").forEach(function (b) {
      b.onclick = function () { page = b.getAttribute("data-go"); render(); };
    });
  }

  render();
})();
