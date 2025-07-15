<script>
  let url = '';
  let qr = '';
  let error = '';
  let triedEmpty = false;

  async function generateQR() {
    error = '';
    if (!url.trim()) {
      triedEmpty = true;
      return;
    }
    triedEmpty = false;
    try {
      const res = await fetch('https://qr-code-generator-y4lj.onrender.com/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      });
      const data = await res.json();
      if (data.qr) {
        qr = data.qr;
      } else {
        error = data.error || 'Unknown error';
      }
    } catch (e) {
      error = e.message;
    }
  }

</script>

<div class="center">
  <h1>QR Generator</h1>
  <form on:submit|preventDefault={generateQR} style="width: 100%; max-width: 400px;">
    <div class="input-row">
      <input bind:value={url} placeholder="Enter URL or text" />
      <button type="submit" disabled={!url.trim()}>Generate</button>
    </div>
  </form>


  <div class="qr-box">
    {#if url.trim() && qr}
      <img src={qr} alt="QR Code" />
    {:else}
      <div style="width:256px;height:256px;display:flex;align-items:center;justify-content:center;opacity:1;font-size:1.2rem;color:#a259ff;">
        Enter a link
      </div>
    {/if}
  </div>

  {#if error}
    <div class="error">{error}</div>
  {/if}
</div>