====
Home
====

.. raw:: html

   <style>
      h1 { display: none; }
   </style>

.. toctree::
   :hidden:
   :includehidden:
   :titlesonly:

   about
   works/index
   notes/index
   blog/index

"attakei pages"は、H/N attakeiが主にWeb上を中心に活動する際のコンテンツ置き場の起点となる個人サイトです。

.. container:: columns

   .. container:: column

      .. container:: title

         ブログなど

      .. postlist:: 5
         :date: %Y/%m/%d
         :format: {date} : {title}

   .. container:: column

      .. figure:: /_static/images/icon-attakei.jpg

      :doc:`「何をやっているか」を知る時 </works/index>`
      /
      :doc:`「何を考えているか」を知る時 </notes/index>`


SNSを眺める
===========

.. container:: columns

   .. container:: column

      .. raw:: html

         <a class="twitter-timeline" href="https://twitter.com/attakei?ref_src=twsrc%5Etfw">Tweets by attakei</a>
         <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

   .. container:: column

      .. raw:: html

         <link rel="stylesheet" href="https://embedbsky.com/embedbsky.com-master-min.css" />
         <div id="embedbsky-com-timeline-embed"></div>
         <script>let containerHeight=600;const getHtml=async t=>{const e=await fetch(t);return 200!==e.status?'<p><strong>No feed data could be located</p></strong>':e.text()};document.addEventListener('DOMContentLoaded',(async()=>{const t=(new Date).toISOString(),e=document.getElementById('embedbsky-com-timeline-embed');e.style.width="100%",e.style.height=`${containerHeight}px`;const n=await getHtml(`https://embedbsky.com/feeds/bdac985419da2452d311f77ffa3876f86f2ffe51cb05b1249ff301e8e49b8fb0.html?v=${t}`);e.innerHTML=n}));</script>
