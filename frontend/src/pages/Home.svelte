<script>
    export let articles = [];
  </script>
  
  <main>
    <h1>Articles</h1>
    {#if articles.length > 0}
      {#each articles as article}
        <article>
          <h2>{article.title}</h2>
          <p>{article.content}</p>
          <small>{new Date(article.published_at).toLocaleString()}</small>
        </article>
      {/each}
    {:else}
      <p style="text-align: center;">No articles found.</p>
    {/if}
  </main>
  