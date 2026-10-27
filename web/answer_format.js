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
      if (block.type === "table") {
        const width=block.columns.length, rows=[];
        for(let i=0;i<block.claims.length;i+=width) rows.push('<tr>'+block.claims.slice(i,i+width).map(c=>'<td>'+claimHTML(c)+'</td>').join('')+'</tr>');
        return '<div class="answer-table-scroll" role="region" aria-label="Evidence comparison" tabindex="0"><table class="answer-table"><thead><tr>'+block.columns.map(c=>'<th scope="col">'+esc(c)+'</th>').join('')+'</tr></thead><tbody>'+rows.join('')+'</tbody></table></div>';
      }
      if (block.type === "bullets" || block.type === "steps") {
        const tag = block.type === "steps" ? "ol" : "ul";
        return '<'+tag+' class="answer-list">'+block.claims.map(c=>'<li>'+claimHTML(c)+'</li>').join("")+'</'+tag+'>';
      }
      return '<p class="answer-paragraph">'+block.claims.map(claimHTML).join(" ")+'</p>';
    }).join("");
    const checked = result.claims?.length && result.claims.every(c=>c.support_status === "automated_supported");
    return rendered+(checked ? '<p class="support-label">Automated support checks passed for the displayed claims. Evidence check details are available below.</p>' : "");
  }
  function toMarkdown(result) {
    const claim = c => md(c.text)+" ["+c.sources.map(md).join(", ")+"]";
    return blocks(result).map(b=>{
      if(b.type==='table') {
        const width=b.columns.length, rows=['| '+b.columns.map(md).join(' | ')+' |','| '+b.columns.map(()=>'---').join(' | ')+' |'];
        for(let i=0;i<b.claims.length;i+=width)rows.push('| '+b.claims.slice(i,i+width).map(claim).join(' | ')+' |');
        return rows.join('\n');
      }
      return b.type === "paragraph" ? b.claims.map(claim).join(" ") : b.claims.map((c,i)=>(b.type === "steps" ? (i+1)+". " : "- ")+claim(c)).join("\n");
    }).join("\n\n");
  }
  const api = {renderHTML,toMarkdown};
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.AnswerFormat = api;
})(typeof window !== "undefined" ? window : this);
