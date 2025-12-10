// server.ts
import { serve } from "https://deno.land/std@0.224.0/http/server.ts";

serve(async (req) => {
  if (req.method === "POST" && new URL(req.url).pathname === "/order") {
    try {
      const orderData = await req.json();

      // Python-Skript starten
      const process = new Deno.Command("python3", {
        args: ["save_order.py"],
        stdin: "piped",
        stdout: "piped",
        stderr: "piped",
      }).spawn();

      // JSON an Python senden
      const writer = process.stdin.getWriter();
      await writer.write(new TextEncoder().encode(JSON.stringify(orderData)));
      await writer.close();

      // Antwort von Python lesen
      const output = await process.output();
      const resultText = new TextDecoder().decode(output);
      return new Response(resultText, { status: 200, headers: { "Content-Type": "application/json" } });

    } catch (err) {
      return new Response(JSON.stringify({ status: "error", message: err.message }), {
        status: 500,
        headers: { "Content-Type": "application/json" },
      });
    }
  }

  return new Response("Not Found", { status: 404 });
}, { port: 8000 });

console.log("Server läuft auf http://localhost:8000");