let sortBy = "score";
function number(value, descending = true) { const parsed = Number.parseFloat(String(value || "").replace("%", "")); return Number.isFinite(parsed) ? (descending ? -parsed : parsed) : Number.POSITIVE_INFINITY; }
function cell(row, value) { const td = document.createElement("td"); td.textContent = value || "—"; row.append(td); }

async function startTest(strategy) {
  const response = await fetch("/api/start-test", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({strategy})});
  if (!response.ok) { alert((await response.json()).error || "Could not start test."); }
  loadTesting();
}

async function loadTesting() {
  const data = await (await fetch("/api/dashboard")).json(); const policy = data.testing.policy;
  document.querySelector("#policy-title").textContent = `${policy.pair} · ${policy.timerange.slice(0, 4)}–${policy.timerange.slice(9, 13)}`;
  document.querySelector("#policy-copy").textContent = `Scalping: ${policy.scalping_timeframes.join(", ")}. Day trading: ${policy.day_trading_timeframes.join(", ")}. Metrics: ${policy.metrics.join(", ")}.`;
  document.querySelector("#promotion-rule").textContent = `PF above ${policy.promotion_rules.min_profit_factor.toFixed(2)} · at least ${policy.promotion_rules.min_trades_per_day.toFixed(2)} trades/day`;
  const candidates = data.testing.strategies; const tested = candidates.filter(item => ["passed_goal", "failed_goal"].includes(item.status)).length;
  const running = candidates.filter(item => item.status === "running").length; const ready = candidates.filter(item => item.status === "ready_for_comparison").length;
  document.querySelector("#pipeline-counts").textContent = `${data.testing.awaiting_adapter} Adapter drafts missing runnable code · ${ready} ready to test · ${running} running · ${tested} tested`;
  document.querySelector("#test-count").textContent = `${candidates.length} runnable strategies · ${tested} tested`;
  const job = data.testing.jobs[0];
  if (job) { document.querySelector("#job-title").textContent = `${job.strategy} · ${job.status}`; document.querySelector("#job-message").textContent = job.message; document.querySelector("#job-output").textContent = job.lines?.join("\n") || "No Freqtrade output yet."; }
  const strategies = document.querySelector("#strategies"); strategies.replaceChildren(); const ascending = sortBy === "max_drawdown";
  candidates.sort((a, b) => number(a.metrics?.[sortBy], !ascending) - number(b.metrics?.[sortBy], !ascending));
  if (!candidates.length) { const row = document.createElement("tr"); const blank = document.createElement("td"); blank.colSpan = 10; blank.textContent = "No runnable strategies yet. Complete Adapter code will appear here automatically."; row.append(blank); strategies.append(row); }
  for (const strategy of candidates) {
    const row = document.createElement("tr"); const metrics = strategy.metrics || {};
    const resultLabel = strategy.status === "passed_goal" ? `Passes goal · best of ${strategy.comparison_timeframes.join(", ")}` : strategy.status === "failed_goal" ? `Fails PF/TPD goal · best diagnostic` : `${strategy.completed_timeframes}/${strategy.comparison_timeframes.length} tested`;
    cell(row, strategy.name); cell(row, strategy.kind); cell(row, strategy.timeframe); cell(row, resultLabel); cell(row, metrics.score); cell(row, metrics.pf); cell(row, metrics.cagr); cell(row, metrics.max_drawdown); cell(row, metrics.trades_per_day);
    const action = document.createElement("td"); const button = document.createElement("button"); button.className = "test-button"; const readyToTest = strategy.status === "ready_for_comparison";
    button.textContent = readyToTest ? "Compare frames" : (strategy.status === "running" ? "Testing…" : "Tested"); button.disabled = !readyToTest; button.onclick = () => startTest(strategy.code_name); action.append(button); row.append(action); strategies.append(row);
  }
}
for (const heading of document.querySelectorAll(".sortable")) { heading.addEventListener("click", () => { sortBy = heading.dataset.sort; loadTesting(); }); }
loadTesting();
setInterval(loadTesting, 2000);
