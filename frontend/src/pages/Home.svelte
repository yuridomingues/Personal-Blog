<script>
    export let articles = [];
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
  </script>
  
  <style>
    article {
      margin-bottom: 3rem;
      padding: 1rem 1.5rem;
      background: #ffffff;
      border-left: 5px solid #005f73;
      border-radius: 6px;
      box-shadow: 0 0 10px rgba(0,0,0,0.04);
      cursor: pointer;
      transition: background 0.3s ease;
    }
  
    article:hover {
      background: #f0f8ff;
    }
  
    h2 {
      font-size: 1.6rem;
      margin-bottom: 0.5rem;
      color: #005f73;
    }
  
    p {
      line-height: 1.6;
      font-size: 1rem;
      color: #333;
      margin: 0.5rem 0;
      white-space: pre-wrap;
    }
  
    small {
      display: block;
      font-size: 0.85rem;
      color: #888;
      margin-top: 0.5rem;
      text-align: right;
    }
  </style>
  
  <main>
    <h1>Articles</h1>
  
    {#if articles.length > 0}
      {#each articles as article}
        <article on:click={() => dispatch('view', article.id)}>
          <h2>{article.title}</h2>
          <p>{article.content.slice(0, 200)}{article.content.length > 200 ? '...' : ''}</p>
          <small>{new Date(article.published_at).toLocaleString()}</small>
        </article>
      {/each}
    {:else}
      <p style="text-align: center;">No articles found.</p>
    {/if}
  </main>
  