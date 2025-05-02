<script>
  import Home from './pages/Home.svelte';
  import Admin from './pages/Admin.svelte';
  import NewArticle from './pages/NewArticle.svelte';
  import EditArticle from './pages/EditArticle.svelte';
  
  let articles = [];
  let page = 'home';
  let editId = null;
  const API = import.meta.env.VITE_API_BASE_URL;

  async function loadArticles() {
    const res = await fetch(`${API}/api/articles`);
    articles = await res.json();
  }

  loadArticles();
</script>

<style>
  main {
    max-width: 720px;
    margin: 3rem auto;
    padding: 2rem;
    font-family: 'Georgia', serif;
    background-color: #f9f9f9;
    color: #222;
    border-radius: 10px;
    box-shadow: 0 0 24px rgba(0, 0, 0, 0.06);
  }

  h1 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 2rem;
    color: #444;
  }

  article {
    margin-bottom: 3rem;
    padding: 1rem 1.5rem;
    background: #ffffff;
    border-left: 5px solid #005f73;
    border-radius: 6px;
    box-shadow: 0 0 10px rgba(0,0,0,0.04);
  }

  h2 {
    font-size: 1.6rem;
    margin-bottom: 0.5rem;
    color: #005f73;
  }

  p {
    white-space: pre-wrap;
    line-height: 1.7;
    font-size: 1.05rem;
    color: #333;
    margin: 1rem 0;
  }

  small {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.85rem;
    color: #888;
    text-align: right;
  }

  nav {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
  }

  button {
    margin: 0 1rem;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #005f73;
    color: white;
  }

  button.active {
    background-color: #003f5c;
  }

  button:hover {
    background-color: #003f5c;
  }
</style>

<nav>
  <button class:active={page === 'home'} on:click={() => page = 'home'}>Home</button>
  <button class:active={page === 'admin'} on:click={() => page = 'admin'}>Admin</button>
  <button class:active={page === 'new'} on:click={() => page = 'new'}>New</button>
</nav>

{#if page === 'home'}
  <Home {articles} />
{:else if page === 'admin'}
  <Admin on:edit={(e) => { editId = e.detail; page = 'edit'; }} />
{:else if page === 'new'}
  <NewArticle on:articleCreated={() => { page = 'admin'; loadArticles(); }} />
{:else if page === 'edit'}
  <EditArticle {editId} on:articleUpdated={() => { page = 'admin'; loadArticles(); }} />
{/if}
