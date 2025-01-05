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

      .. container:: subtitle

         ブログなど

      .. postlist:: 5
         :date: %Y/%m/%d
         :format: {date} : {title}

      .. container:: subtitle

         ショートカット

      * :doc:`「何をやっているか」を知りたい時 </works/index>`
      * :doc:`「何を考えているか」を知りたい時 </notes/index>`
      * `GitHubでの主要活動を知りたい時 <https://github.com/attakei>`_
      * `Xでの活動などを知りたい時 <https://x.com/attakei>`_

   .. container:: column

      .. figure:: /_static/images/icon-attakei.jpg

      .. figure:: https://api.githubtrends.io/user/svg/attakei/repos?time_range=one_year&include_private=True&loc_metric=changed&theme=classic
         :alt: Most contiribution repositories on GitHub

         Most contiribution repositories on GitHub.
         Powered by `GitHub Trends <https://www.githubtrends.io/>`_.

SNSを眺める
===========

.. container:: columns

   .. container:: column is-half is-offset-3

      .. raw:: html

         <link rel="stylesheet" href="https://embedbsky.com/embedbsky.com-master-min.css" />
         <div id="embedbsky-com-timeline-embed"></div>
         <script>let containerHeight=600;const getHtml=async t=>{const e=await fetch(t);return 200!==e.status?'<p><strong>No feed data could be located</p></strong>':e.text()};document.addEventListener('DOMContentLoaded',(async()=>{const t=(new Date).toISOString(),e=document.getElementById('embedbsky-com-timeline-embed');e.style.width="100%",e.style.height=`${containerHeight}px`;const n=await getHtml(`https://embedbsky.com/feeds/bdac985419da2452d311f77ffa3876f86f2ffe51cb05b1249ff301e8e49b8fb0.html?v=${t}`);e.innerHTML=n}));</script>
