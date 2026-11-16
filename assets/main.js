// 只處理本機介面互動，不會傳送資料。
const search = document.querySelector('#guide-search');
if (search) {
  const cards = [...document.querySelectorAll('.guide-card')];
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#no-results');
  function filterGuides() {
    const query = search.value.trim().toLocaleLowerCase();
    let shown = 0;
    cards.forEach(card => {
      const text = `${card.textContent} ${card.dataset.search || ''}`.toLocaleLowerCase();
      card.hidden = !text.includes(query);
      if (!card.hidden) shown++;
    });
    count.textContent = `顯示 ${shown} 篇指南`;
    empty.hidden = shown !== 0;
  }
  search.addEventListener('input', filterGuides);
  document.querySelector('#clear-search').addEventListener('click', () => {
    search.value = ''; filterGuides(); search.focus();
  });
  filterGuides();
}
const checks = [...document.querySelectorAll('.check-list input')];
if (checks.length) {
  const update = () => document.querySelector('#check-status').textContent =
    `已確認 ${checks.filter(c => c.checked).length} / ${checks.length} 項（重新整理後重設）`;
  checks.forEach(c => c.addEventListener('change', update));
  update();
}
