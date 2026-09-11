const http=require('http'),fs=require('fs'),path=require('path');
const ROOT=path.join(__dirname,'istore-dakar');
const T={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8',
 '.js':'text/javascript; charset=utf-8','.png':'image/png','.webp':'image/webp',
 '.jpg':'image/jpeg','.jpeg':'image/jpeg','.svg':'image/svg+xml','.mp4':'video/mp4',
 '.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
http.createServer((req,res)=>{
  let u=decodeURIComponent(req.url.split('?')[0]);
  if(u==='/')u='/index.html';
  const f=path.join(ROOT,u);
  if(!f.startsWith(ROOT)){res.writeHead(403);res.end('403');return}
  fs.readFile(f,(e,d)=>{
    if(e){res.writeHead(404,{'Content-Type':'text/plain'});res.end('404 '+u);return}
    res.writeHead(200,{'Content-Type':T[path.extname(f).toLowerCase()]||'application/octet-stream',
      'Content-Length':d.length,'Cache-Control':'no-store'});
    res.end(d);
  });
}).listen(4173,()=>console.log('http://localhost:4173'));
