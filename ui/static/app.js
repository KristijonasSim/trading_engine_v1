const message = document.querySelector("#message");
let dashboard = null;
const storageKeys = {
  searchSource: "trading-engine.search-source",
  searchMarket: "trading-engine.search-market",
  searchLimit: "trading-engine.search-limit",
  sourceFilter: "trading-engine.source-filter",
  marketFilter: "trading-engine.market-filter",
};

function restoreSelect(id, key) {
  const value = localStorage.getItem(key);
  const select = document.querySelector(id);
  if (value && [...select.options].some((option) => option.value === value)) {
    select.value = value;
  }
}

restoreSelect("#source", storageKeys.searchSource);
restoreSelect("#search-market", storageKeys.searchMarket);
restoreSelect("#limit", storageKeys.searchLimit);
restoreSelect("#source-filter", storageKeys.sourceFilter);
restoreSelect("#market-filter", storageKeys.marketFilter);

function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text) node.textContent = text;
  return node;
}

function render(data) {
  dashboard = data;
  document.querySelector("#source-total").textContent = `${data.research.unique_sources} source ideas`;
  document.querySelector("#card-total").textContent = `${data.adapter.drafts} adapter drafts`;
  document.querySelector("#test-total").textContent = `${data.testing.reports} test runs`;
  document.querySelector("#testing-copy").textContent = data.testing.reports
    ? `${data.testing.reports} saved reports. Testing engine is not built yet.`
    : "Not built yet. It cannot run strategies.";

  const sourceCounts = document.querySelector("#source-counts");
  sourceCounts.replaceChildren();
  const counts = Object.entries(data.research.source_counts);
  if (!counts.length) sourceCounts.append(element("p", "small", "No saved sources yet. Run a search above."));
  for (const [source, count] of counts) {
    sourceCounts.append(element("span", "count", `${source}: ${count}`));
  }

  const records = document.querySelector("#records");
  records.replaceChildren();
  const filter = document.querySelector("#source-filter").value;
  const market = document.querySelector("#market-filter").value;
  const visibleRecords = data.research.records.filter((record) =>
    (filter === "all" || record.source === filter) &&
    (market === "all" || record.market === market)
  );
  document.querySelector("#filter-status").textContent = `Showing ${visibleRecords.length} newest ${market === "all" ? "" : `${market} `}${filter === "all" ? "sources" : `${filter} sources`}.`;
  if (!visibleRecords.length) records.append(element("p", "empty", "No saved source ideas match this filter."));
  for (const record of visibleRecords) {
    const row = element("article", "record");
    const title = document.createElement("a");
    title.href = record.url;
    title.target = "_blank";
    title.rel = "noreferrer";
    title.textContent = record.short_title || record.title || record.id;
    title.title = record.title || record.id;
    row.append(element("span", "source", record.source));
    row.append(element("span", `market ${record.market || "other"}`, record.market || "other"));
    row.append(title);
    row.append(element("p", "summary", record.summary || "No summary returned. Read the source."));
    const date = (record.harvested_at || "").slice(0, 10) || "Unknown date";
    const details = element("p", "small", `Harvested: ${date}`);
    row.append(details);
    const deleteButton = element("button", "danger", "Delete source");
    deleteButton.addEventListener("click", () => deleteSource(record.source, record.id));
    row.append(deleteButton);
    const target = document.createElement("select");
    target.innerHTML = '<option value="crypto-spot">Crypto spot</option><option value="crypto-futures">Crypto futures</option>';
    row.append(target);
    const adaptButton = element("button", "secondary", "Add to adapter queue");
    adaptButton.addEventListener("click", () => queueAdapter(record.source, record.id, record.short_title, target.value));
    row.append(adaptButton);
    records.append(row);
  }
  const adapters = document.querySelector("#adapters"); adapters.replaceChildren();
  if (!data.adapters.length) adapters.append(element("p", "empty", "No adapter drafts yet."));
  for (const adapter of data.adapters) {
    const card = element("article", "card"); card.append(element("h3", "", adapter.title)); card.append(element("p", "small", `Target: ${adapter.target} · Status: ${adapter.status}`)); card.append(element("p", "small", adapter.file)); adapters.append(card);
  }
}

async function loadDashboard() {
  const response = await fetch("/api/dashboard");
  render(await response.json());
}

async function deleteSource(source, id) {
  if (!window.confirm("Delete this source from your saved list?")) return;
  message.textContent = "Deleting source...";
  const response = await fetch("/api/delete-source", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ source, id }),
  });
  const result = await response.json();
  if (!response.ok) {
    message.textContent = result.error || "Delete failed.";
    return;
  }
  message.textContent = "Source deleted. It will stay hidden in future searches.";
  render(result.dashboard);
}

async function createAdapter(source, id, target) {
  const response = await fetch("/api/create-adapter", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({source, id, target})});
  const result = await response.json();
  if (!response.ok) { message.textContent = result.error; return; }
  message.textContent = `Created ${result.created}`; render(result.dashboard);
}
async function queueAdapter(source, id, title, target) {
  const response = await fetch("/api/queue-adapter", {method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({source,id,title,target})});
  const result=await response.json(); if(!response.ok){message.textContent=result.error;return;} message.textContent="Added to Adapter queue."; render(result.dashboard);
}

document.querySelector("#search-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const button = event.currentTarget.querySelector("button");
  button.disabled = true;
  message.textContent = "Searching public sources...";
  try {
    const response = await fetch("/api/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: document.querySelector("#query").value,
        source: document.querySelector("#source").value,
        market: document.querySelector("#search-market").value,
        limit: document.querySelector("#limit").value,
      }),
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Search failed.");
    const selectedMarket = document.querySelector("#search-market").value;
    document.querySelector("#market-filter").value = selectedMarket;
    localStorage.setItem(storageKeys.marketFilter, selectedMarket);
    message.textContent = result.search_query === document.querySelector("#query").value
      ? `Saved results to ${result.saved}`
      : `Searched as “${result.search_query}” and saved results.`;
    render(result.dashboard);
  } catch (error) {
    message.textContent = error.message;
  } finally {
    button.disabled = false;
  }
});

document.querySelector("#source-filter").addEventListener("change", () => {
  localStorage.setItem(storageKeys.sourceFilter, document.querySelector("#source-filter").value);
  if (dashboard) render(dashboard);
});

document.querySelector("#market-filter").addEventListener("change", () => {
  localStorage.setItem(storageKeys.marketFilter, document.querySelector("#market-filter").value);
  if (dashboard) render(dashboard);
});

document.querySelector("#source").addEventListener("change", (event) => {
  localStorage.setItem(storageKeys.searchSource, event.target.value);
});

document.querySelector("#search-market").addEventListener("change", (event) => {
  localStorage.setItem(storageKeys.searchMarket, event.target.value);
});

document.querySelector("#limit").addEventListener("change", (event) => {
  localStorage.setItem(storageKeys.searchLimit, event.target.value);
});

loadDashboard().catch((error) => { message.textContent = error.message; });
