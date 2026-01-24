const CACHE_VERSION = 'v1'
const IMAGE_CACHE = `chartcoach-eval-ui-images-${CACHE_VERSION}`

function isCrossOriginImageRequest(request) {
  try {
    const url = new URL(request.url)
    if (url.origin === self.location.origin) return false

    if (request.destination === 'image') return true
    return /\.(png|jpe?g|gif|webp|svg)$/i.test(url.pathname)
  } catch {
    return false
  }
}

async function cacheFirst(request) {
  const cache = await caches.open(IMAGE_CACHE)
  const cached = await cache.match(request)
  if (cached) return cached

  const response = await fetch(request)
  if (response && (response.ok || response.type === 'opaque')) {
    await cache.put(request, response.clone())
  }
  return response
}

self.addEventListener('install', (event) => {
  event.waitUntil(self.skipWaiting())
})

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter((key) => key.startsWith('chartcoach-eval-ui-images-') && key !== IMAGE_CACHE)
            .map((key) => caches.delete(key)),
        ),
      )
      .then(() => self.clients.claim()),
  )
})

self.addEventListener('fetch', (event) => {
  const request = event.request
  if (request.method !== 'GET') return
  if (!isCrossOriginImageRequest(request)) return

  event.respondWith(
    cacheFirst(request).catch(() => caches.open(IMAGE_CACHE).then((cache) => cache.match(request))),
  )
})

