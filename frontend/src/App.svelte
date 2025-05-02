<script>
  import { onMount } from 'svelte';
  let articles = [];
  const API = import.meta.env.VITE_API_BASE_URL;

  onMount(async () => {
    const res = await fetch(`${API}/api/articles`);
    articles = await res.json();
  });
</script>

<style>
  main {
    max-width: 700px;
    margin: 3rem auto;
    padding: 2rem;
    font-family: system-ui, sans-serif;
    background-color: #1e1e1e;
    color: #f0f0f0;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.4);
  }

  h1 {
    font-size: 2.2rem;
    text-align: center;
    margin-bottom: 2rem;
  }

  article {
    margin-bottom: 2.5rem;
    border-left: 4px solid #4ade80;
    padding-left: 1rem;
  }

  h2 {
    margin: 0.2rem 0;
    color: #4ade80;
  }

  p {
    line-height: 1.6;
    margin: 0.5rem 0;
  }

  small {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.85rem;
    color: #aaaaaa;
  }
</style>

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
