async function loadEngineNav() {
  const response = await fetch("/api/dashboard");
  const data = await response.json();
  const nav = document.querySelector("#engine-nav");
  if (!nav) return;
  nav.innerHTML = `
    <a class="engine active engine-link" href="/"><p class="label">01 · RESEARCH ENGINE</p><h2>${data.research.unique_sources} source ideas</h2><p>Find public strategy sources.</p><span class="badge">Ready</span></a>
    <a class="engine active engine-link" href="/adapter.html"><p class="label">02 · STRATEGY ADAPTER</p><h2>${data.adapter.drafts} adapter drafts</h2><p>Adapt a source to crypto spot or futures.</p><span class="badge">Ready</span></a>
    <a class="engine engine-link" href="/testing.html"><p class="label">03 · TESTING ENGINE</p><h2>${data.testing.reports} test runs</h2><p>Not built yet. It cannot run strategies.</p><span class="badge muted">Locked</span></a>
    <a class="engine engine-link" href="/bot.html"><p class="label">04 · BOT ENGINE</p><h2>0 live strategies</h2><p>Not built yet. No exchange connection.</p><span class="badge muted">Locked</span></a>`;
}
loadEngineNav();
