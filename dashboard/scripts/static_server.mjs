import { createReadStream, existsSync } from 'node:fs'
import { createServer } from 'node:http'
import { extname, join, normalize, resolve } from 'node:path'

const root = resolve(process.argv[2] || 'dist')
const port = Number(process.env.PORT || 4173)
const types = { '.css': 'text/css; charset=utf-8', '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png', '.ico': 'image/x-icon' }

createServer((request, response) => {
  const path = new URL(request.url || '/', 'http://localhost').pathname
  const relative = path === '/' ? 'index.html' : normalize(path).replace(/^[/\\]+/, '')
  const file = resolve(join(root, relative))
  if (!file.startsWith(`${root}/`) || !existsSync(file)) {
    response.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' })
    response.end('Not found')
    return
  }
  response.writeHead(200, { 'Content-Type': types[extname(file)] || 'application/octet-stream', 'Cache-Control': 'no-cache' })
  createReadStream(file).pipe(response)
}).listen(port, '0.0.0.0', () => console.log(`GitHub Radar static server listening on ${port}`))
