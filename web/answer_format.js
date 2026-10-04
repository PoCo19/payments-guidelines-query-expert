/* A small shared renderer: only allowlisted structure, never model HTML/Markdown. */
(function (root) {
  "use strict";
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const md = value => String(value ?? "").replace(/\r?\n/g," ").replace(/([\\`*_{}\[\]<>()#!|>+~-])/g,"\\$1").replace(/^(\d+)\. /,"$1\\. ");
  function blocks(result) {
    return result.answer_blocks?.length ? result.answer_blocks : (result.claims?.length ? [{type:"paragraph",claims:result.claims}] : []);
  }
  function claimHTML(claim) {
    return '<span class="answer-claim">'+esc(claim.text)+' <span class="answer-citations">'+claim.sources.map(id => '<button class="citation-button" data-citation="'+esc(id)+'" aria-label="Read source '+esc(id)+'">'+esc(id)+'</button>').join(" ")+'</span></span>';
  }
  function renderHTML(result) {
    const rendered = blocks(result).map(block => {
      if (block.type === "bullets" || block.type === "steps") {
        const tag = block.type === "steps" ? "ol" : "ul";
        return '<'+tag+' class="answer-list">'+block.claims.map(c=>'<li>'+claimHTML(c)+'</li>').join("")+'</'+tag+'>';
      }
      return '<p class="answer-paragraph">'+block.claims.map(claimHTML).join(" ")+'</p>';
    }).join("");
    const checked = result.claims?.length && result.claims.every(c=>c.support_status === "automated_supported");
    return rendered+(checked ? '<p class="support-label">Automated support checks passed for the displayed claims. Review details below.</p>' : "");
  }
  function toMarkdown(result) {
    const claim = c => md(c.text)+" ["+c.sources.map(md).join(", ")+"]";
    return blocks(result).map(b=>b.type === "paragraph" ? b.claims.map(claim).join(" ") : b.claims.map((c,i)=>(b.type === "steps" ? (i+1)+". " : "- ")+claim(c)).join("\n")).join("\n\n");
  }
  const api = {renderHTML,toMarkdown};
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.AnswerFormat = api;
})(typeof window !== "undefined" ? window : this);
