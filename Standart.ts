
import { serveDir, serveFile } from "jsr:@std/http/file-server";
Deno.serve((req: Request) => {
  const pathname = new URL(req.url).pathname;
  return serveDir(req, {})

});