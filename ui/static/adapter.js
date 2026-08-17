function node(tag, className, text) { const item = document.createElement(tag); if (className) item.className = className; if (text) item.textContent = text; return item; }
async function load() {
  const response = await fetch("/api/dashboard"); const data = await response.json(); const drafts = data.adapters;
  document.querySelector("#count").textContent = `${drafts.length} adapter drafts`;
  const queue = data.adapter.queue; document.querySelector("#queue-count").textContent = `${queue.items.length} waiting`;
  const queueBox=document.querySelector("#queue"); if(!queue.items.length) queueBox.append(node("p","empty","No sources queued."));
  for(const item of queue.items){const card=node("article","card");card.append(node("p","label",item.status));card.append(node("h3","",item.title));card.append(node("p","small",`Target: ${item.target}`));queueBox.append(card);}
  const container = document.querySelector("#drafts");
  if (!drafts.length) { container.append(node("p", "empty", "No adapter drafts yet. Create one from a saved source on the dashboard.")); return; }
  for (const draft of drafts) {
    const card = node("article", "card"); card.append(node("p", "label", draft.status)); card.append(node("h3", "", draft.title)); card.append(node("p", "small", `Source market: ${draft.source_market}`)); card.append(node("p", "small", `Target: ${draft.target}`)); card.append(node("p", "small", `File: ${draft.file}`));
    if (draft.source_link) { const link = node("a", "source-link", "Open original source"); link.href = draft.source_link; link.target = "_blank"; link.rel = "noreferrer"; card.append(link); }
    container.append(card);
  }
}
load();
