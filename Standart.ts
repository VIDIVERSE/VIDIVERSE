
import { serveDir, serveFile } from "jsr:@std/http/file-server";
Deno.serve((req: Request) => {
  const pathname = new URL(req.url).pathname;

  if (pathname === "/LogIn") {return serveFile(req, "./login.html");}
  else if (pathname === "/Home") return serveFile(req, "./VIDIVERSE.html");
  else if (pathname === "/Passwort-Recovery") return serveFile(req, "./forgot-passwort.html")
  else if (pathname === "/Next-Recovery") return serveFile(req, "./Passwort_recovery_site.html")
  else if (pathname === "/Aha") return serveFile(req, "./Hidden_Vidiverse.html")
  else if (pathname === "/LoggedIn") return serveFile(req, "./Geheim.html")
  else {
    return serveDir(req, {});
  }
});
