function cell(row, value) { const td = document.createElement("td"); td.textContent = value || "—"; row.append(td); }
async function findRules(file) {
  const response = await fetch("/api/find-rules", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({file})}); const payload = await response.json();
  document.querySelector("#message").textContent = response.ok ? `Result: ${payload.result}. Sent to Testing Engine.` : payload.error; load();
}
async function findAll() { const button=document.querySelector("#find-all"); button.disabled=true; const response=await fetch("/api/find-all-rules",{method:"POST",headers:{"Content-Type":"application/json"},body:"{}"}); const payload=await response.json(); document.querySelector("#message").textContent=payload.message || payload.error; button.disabled=false; setTimeout(load,1000); }
async function load() {
  const data = await (await fetch("/api/dashboard")).json(); const drafts = data.adapters; const table = document.querySelector("#adapters"); table.replaceChildren();
  document.querySelector("#count").textContent = `${drafts.length} selected sources`;
  if (!drafts.length) { const row=document.createElement("tr"); const blank=document.createElement("td"); blank.colSpan=6; blank.textContent="No sources waiting. Adapted ideas have moved to Testing Engine."; row.append(blank); table.append(row); }
  for (const draft of drafts) {
    const row=document.createElement("tr"); cell(row,draft.title); cell(row,draft.source_market); cell(row,draft.target); cell(row,draft.status); cell(row,"Waiting for rule recovery");
    const action=document.createElement("td"); const button=document.createElement("button"); button.textContent="Find rules"; button.onclick=()=>findRules(draft.file); action.append(button); row.append(action); table.append(row);
  }
  const archived=document.querySelector("#archived"); archived.replaceChildren(); const archivedDrafts=data.archived_adapters; document.querySelector("#archived-count").textContent=`${archivedDrafts.length} archived sources`;
  if (!archivedDrafts.length) { const row=document.createElement("tr"); const blank=document.createElement("td"); blank.colSpan=2; blank.textContent="No archived sources."; row.append(blank); archived.append(row); }
  for (const draft of archivedDrafts) { const row=document.createElement("tr"); cell(row,draft.title); cell(row,draft.note || "Duplicate or incomplete source."); archived.append(row); }
}
document.querySelector("#find-all").addEventListener("click",findAll); load(); setInterval(load,3000);
