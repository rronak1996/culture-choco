import { defineConfig } from 'vite'

export default defineConfig({
    base: '/culture-choco/',
    build: {
        outDir: 'dist',
        assetsDir: 'assets',
        emptyOutDir: true,
    }
})
