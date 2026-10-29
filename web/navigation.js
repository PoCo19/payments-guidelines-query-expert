"use strict";
// One navigation contract for research, saved answers and change summaries.
function productNavigation(workbench=false) {
  const view=(id,label)=>workbench?`<a class="nav" href="/?view=${id}">${label}</a>`:`<button class="nav" data-view="${id}">${label}</button>`;
  return `<a class="brand" href="/" aria-label="Payments Guidelines Query Expert home"><span class="brand-mark">pg<span>•</span></span><span>Payments Guidelines<br>Query Expert</span></a>
  <div class="workspace-label">YOUR WORKSPACE</div><nav aria-label="Main navigation">
  ${view('explore','Ask a question')}
  <a class="nav" data-area="impact" href="/work?kind=impact">Understand a change</a>
  <a class="nav" data-area="saved" href="/work">Saved work</a>
  ${view('library','Document library')}
  <details class="tools-menu"><summary>Manage library &amp; tools</summary>
  ${view('intake','Add documents')}${view('review','Source review')}${view('experiments','Retrieval checks')}</details>
  ${view('about','About this project')}</nav>
  <div class="sidebar-bottom"><div class="local"><i></i> Runs on your computer</div><p>Answers and changes, with evidence</p></div>`;
}
if(typeof document!=="undefined")document.getElementById('product-navigation').innerHTML=productNavigation(document.body.classList.contains('workbench'));
if(typeof module!=="undefined")module.exports={productNavigation};
