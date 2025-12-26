async function fetchStock() {
  const symbol = document.getElementById("symbol").value;
  const loader = document.getElementById("loader");
  const result = document.getElementById("result");
  const button = document.querySelector("button");

  if (!symbol) {
    alert("Please enter a stock symbol");
    return;
  }

  // UI state: loading
  loader.classList.remove("hidden");
  result.classList.add("hidden");
  button.disabled = true;

  const url = `http://127.0.0.1:8000/explain-stock?symbol=${symbol}&company=${symbol}`;

  try {
    const res = await fetch(url);
    const data = await res.json();

    if (data.error) {
      alert(data.error);
      return;
    }

    document.getElementById("stockName").innerText = data.stock_data.symbol;
    document.getElementById("price").innerText = data.stock_data.current_price;
    document.getElementById("change").innerText = data.stock_data.percent_change;
    document.getElementById("explanation").innerText = data.ai_explanation;

    result.classList.remove("hidden");

  } catch (err) {
    alert("Failed to fetch data");
    console.error(err);
  } finally {
    // UI state: done
    loader.classList.add("hidden");
    button.disabled = false;
  }
}
