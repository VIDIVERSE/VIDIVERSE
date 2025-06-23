
import { serveDir, serveFile } from "jsr:@std/http/file-server";
Deno.serve((req: Request) => {
  const pathname = new URL(req.url).pathname;
   if (pathname==="/Home"){return serveFile(req,"./VIDIVERSE.html")}
  else
   {
   console.log(pathname)
   return serveDir(req, {})}

});
