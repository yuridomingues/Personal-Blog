<script>
    import { onMount, createEventDispatcher } from 'svelte';
    export let articleId;
    let title = '';
    let content = '';
    let username = '';
    let password = '';
    let error = '';
    const API = import.meta.env.VITE_API_BASE_URL;
    const dispatch = createEventDispatcher();
  
    onMount(async () => {
      const res = await fetch(`${API}/api/articles/${articleId}`);
      if (res.ok) {
        const article = await res.json();
        title = article.title;
        content = article.content;
      } else {
        error = 'Failed to load article';
      }
    });
  
    async function submitUpdate() {
      if (!title || !content || !username || !password) {
        error = 'Fill in all fields';
        return;
      }
  
      const res = await fetch(`${API}/api/articles/${articleId}`, {
        method: 'PUT',
        headers: {
          'Authorization': 'Basic ' + btoa(`${username}:${password}`),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, content })
      });
  
      if (res.ok) {
        alert('Article updated!');
        dispatch('articleUpdated');
      } else {
        error = 'Update failed';
      }
    }
  </script>
  
  <style>
    form {
      display: flex;
      flex-direction: column;
      max-width: 700px;
      margin: 2rem auto;
      gap: 1rem;
      font-family: Georgia, serif;
    }
  
    input, textarea {
      padding: 0.75rem;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 6px;
    }
  
    button {
      padding: 0.6rem;
      font-size: 1rem;
      background-color: #0077b6;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }
  
    .error {
      color: red;
      text-align: center;
    }
  </style>
  
  <form on:submit|preventDefault={submitUpdate}>
    <input type="text" bind:value={title} placeholder="Title" />
    <textarea rows="10" bind:value={content} placeholder="Content"></textarea>
    <input type="text" bind:value={username} placeholder="Username" />
    <input type="password" bind:value={password} placeholder="Password" />
    <button type="submit">Update Article</button>
  
    {#if error}
      <p class="error">{error}</p>
    {/if}
  </form>
  