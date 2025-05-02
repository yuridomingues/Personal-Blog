<script>
    import { createEventDispatcher } from 'svelte';
    import { onMount } from 'svelte';

    const dispatch = createEventDispatcher();

    let articles = [];
    const API = import.meta.env.VITE_API_BASE_URL;
    let username = '';
    let password = '';
    let isLoggedIn = false;

    async function loadArticles() {
      const res = await fetch(`${API}/api/articles`);
      articles = await res.json();
    }

    async function deleteArticle(id) {
      const confirmed = confirm('Delete this article?');
      if (!confirmed) return;

      const res = await fetch(`${API}/api/articles/${id}`, {
        method: 'DELETE',
        headers: {
          Authorization: 'Basic ' + btoa(`${username}:${password}`)
        }
      });

      if (res.ok) {
        articles = articles.filter(a => a.id !== id);
      } else {
        alert('Failed to delete article.');
      }
    }

    function handleLogin(e) {
      e.preventDefault();
      isLoggedIn = true;
      loadArticles();
    }

    onMount(() => {
      if (isLoggedIn) loadArticles();
    });
</script>

<style>
    .admin {
      max-width: 700px;
      margin: 0 auto;
    }

    .admin-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
    }

    .article-list {
      list-style: none;
      padding: 0;
    }

    .article-list li {
      margin-bottom: 1rem;
      border-bottom: 1px solid #ccc;
      padding-bottom: 0.5rem;
    }

    .controls {
      margin-top: 0.5rem;
    }

    button {
      margin-right: 0.5rem;
      padding: 0.3rem 0.7rem;
      font-size: 0.9rem;
      border: none;
      border-radius: 4px;
      background-color: #005f73;
      color: white;
      cursor: pointer;
    }

    button.delete {
      background-color: #bb0000;
    }

    form {
      margin: 2rem 0;
      display: flex;
      gap: 0.5rem;
    }

    input {
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
</style>

<div class="admin">
    {#if !isLoggedIn}
      <form on:submit={handleLogin}>
        <input type="text" bind:value={username} placeholder="Username" />
        <input type="password" bind:value={password} placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    {:else}
      <div class="admin-header">
        <h2>Admin Dashboard</h2>
        <button on:click={() => alert('A funcionalidade de adicionar será implementada!')}>+ Add</button>
      </div>

      {#if articles.length === 0}
        <p>No articles found.</p>
      {:else}
        <ul class="article-list">
          {#each articles as article}
            <li>
              <strong>{article.title}</strong>
              <div class="controls">
                <button on:click={() => dispatch('edit', article.id)}>Edit</button>
                <button class="delete" on:click={() => deleteArticle(article.id)}>Delete</button>
              </div>
            </li>
          {/each}
        </ul>
      {/if}
    {/if}
</div>