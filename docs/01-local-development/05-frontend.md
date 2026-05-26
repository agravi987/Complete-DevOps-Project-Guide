# Phase 5: Frontend

Goal: create a simple React frontend that calls the services through one API base URL.

In early local development you can call services directly. After Nginx is added, the frontend will call the gateway instead.

## Create The React App

Run from project root:

```powershell
cd frontend
npm create vite@latest . -- --template react
npm install
```

## Add Environment File

Create `frontend/.env`:

```powershell
New-Item .env
```

Add:

```env
VITE_API_BASE_URL=http://localhost:8080/api
```

This value points to the Nginx gateway that you will add later.

## Replace App.jsx

Replace `frontend/src/App.jsx`:

```jsx
import { useEffect, useState } from "react";
import "./App.css";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || "http://localhost:8080/api";

function App() {
  const [products, setProducts] = useState([]);
  const [status, setStatus] = useState("Loading");

  useEffect(() => {
    async function loadProducts() {
      try {
        const response = await fetch(`${apiBaseUrl}/products`);
        const data = await response.json();
        setProducts(data);
        setStatus("Connected");
      } catch (error) {
        setStatus("Gateway not running yet");
      }
    }

    loadProducts();
  }, []);

  return (
    <main className="app-shell">
      <section className="toolbar">
        <div>
          <p className="eyebrow">Microservices Project</p>
          <h1>DevOps Store</h1>
        </div>
        <span className="status">{status}</span>
      </section>

      <section className="product-grid">
        {products.map((product) => (
          <article className="product-card" key={product.id}>
            <h2>{product.name}</h2>
            <p>Price: Rs. {product.price}</p>
          </article>
        ))}
      </section>
    </main>
  );
}

export default App;
```

## Replace App.css

Replace `frontend/src/App.css`:

```css
:root {
  color: #172033;
  background: #f5f7fb;
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
}

.app-shell {
  width: min(1100px, calc(100% - 32px));
  margin: 0 auto;
  padding: 32px 0;
}

.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
}

.eyebrow {
  margin: 0 0 4px;
  color: #52627a;
  font-size: 14px;
}

h1 {
  margin: 0;
  font-size: 32px;
}

.status {
  border: 1px solid #cfd7e6;
  border-radius: 6px;
  padding: 8px 12px;
  background: #ffffff;
  color: #2f5f4f;
  font-weight: 600;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}

.product-card {
  border: 1px solid #d8deea;
  border-radius: 8px;
  padding: 18px;
  background: #ffffff;
}

.product-card h2 {
  margin: 0 0 8px;
  font-size: 20px;
}

.product-card p {
  margin: 0;
  color: #52627a;
}
```

## Run Frontend

```powershell
npm run dev -- --host 0.0.0.0
```

Open the URL Vite prints, usually:

```text
http://localhost:5173
```

At this point the frontend may show `Gateway not running yet`. That is fine. The gateway is added in the container phase.

## Commit

Run from project root:

```powershell
git add .
git commit -m "feat: add react frontend"
```

## Checkpoint

You are ready when:

- The React app starts on port `5173`.
- The page loads in your browser.
- It is okay if product loading waits for the gateway phase.
