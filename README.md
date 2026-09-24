<p align="center">
  <a href="https://portfolio-milan-omega.vercel.app">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="./assets/header-light.svg">
      <img alt="Misael — developer and code security reviewer" src="./assets/header-light.svg" width="100%">
    </picture>
  </a>
</p>

<p align="center">
  I build web, mobile and AI applications, and I review source code looking for what breaks before someone else finds it.<br>
  Systems Engineering student (4th year) · based in Colombia, originally from Spain.
</p>

<p align="center">
  <a href="https://portfolio-milan-omega.vercel.app">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/misael-gallo/">LinkedIn</a> ·
  <a href="mailto:misaelgallo19@hotmail.com">misaelgallo19@hotmail.com</a>
</p>

## Selected work

| Project | What it is | Evidence |
|---|---|---|
| **[MEDI-IA](https://github.com/Milan32555/medi-ia-medical-agent)** | Differential-diagnosis agent over 14 medical textbooks. Hybrid retrieval (BM25 + FAISS, fused with RRF), cross-encoder reranking, ReAct agent on Qwen2.5-7B. Flask, Docker. | **97.1%** Recall@1 on 40 annotated queries · **185** tests |
| **[AnimalVision](https://github.com/Milan32555/AnimalVision-AI-Image-Classification-System)** | Image classifier served as a full-stack web app, transfer learning on MobileNetV2. [Live demo](https://animal-cnn-classifier.onrender.com) | **93.4%** test accuracy (5 classes) · **~0.8 s** per image |
| **[Real-time chat](https://github.com/Milan32555/Chat-socket-mongodb)** | WebSocket chat with live presence and persistent history. Socket.IO, Express 5, MongoDB. | User input escaped before rendering (XSS) |
| **[Safe Transfer AI](https://github.com/Milan32555/safe-transfer-ai)** | Fraud-risk simulator for bank transfers. Android, Kotlin and Jetpack Compose. | **7** weighted risk signals · **8** unit tests |
| **[Library system](https://github.com/Milan32555/Full-stack-library-management-system-with-Vue.js-frontend-and-Node.js-backend)** | Catalog and admin panel with Clean Architecture. Vue.js and Node.js. [Live demo](https://full-stack-library-management-syste-eight.vercel.app) | Swapping the database touched **1** file |
| **[portfolio-milan](https://github.com/Milan32555/portfolio-milan)** | My site: Next.js 16 and a Three.js hero with custom shaders. [Live](https://portfolio-milan-omega.vercel.app) | Lighthouse accessibility **96–100** · **0** axe violations |

## Recently shipped

<!-- recent starts -->
- **[portfolio-milan](https://github.com/Milan32555/portfolio-milan)** — docs: sincronizar el spec maestro con /servicios y los arreglos del hero en movil (#17) <sub>2026-09-24</sub>
- **[medi-ia-medical-agent](https://github.com/Milan32555/medi-ia-medical-agent)** — docs: unificar el conteo de tests (185 tests, no aserciones) <sub>2026-09-22</sub>
- **[Full-stack-library-management-system-with-Vue.js-frontend-and-Node.js-backend](https://github.com/Milan32555/Full-stack-library-management-system-with-Vue.js-frontend-and-Node.js-backend)** — docs: agregar URL de la demo en vivo y aclarar migracion <sub>2026-09-21</sub>
- **[VUE-KardexAPP](https://github.com/Milan32555/VUE-KardexAPP)** — docs: actualizar README sin emojis y con seccion de tests <sub>2026-09-18</sub>
- **[safe-transfer-ai](https://github.com/Milan32555/safe-transfer-ai)** — docs: reescribir README con descripcion honesta del proyecto <sub>2026-09-18</sub>
<!-- recent ends -->

<sub>Updated daily by a [GitHub Action](./.github/workflows/update-readme.yml) running [a small Python script](./scripts/update_readme.py).</sub>

## Now

- Shipping **Base**, a Flutter app for a private client (in app-store review, September 2026).
- Preparing a SOC Analyst certification.

## What I offer

- **Development** — websites and landing pages, full-stack web apps, mobile apps, custom business systems.
- **Code review** — source-code security review with prioritized findings (XSS, SQL injection, exposed secrets, CSRF, broken access control). Code only; no penetration testing.

## Stack

<p>
  <img src="https://skillicons.dev/icons?i=ts,nextjs,react,vue,threejs,nodejs,express,mongodb,mysql,python,flask&perline=11" alt="TypeScript, Next.js, React, Vue, Three.js, Node.js, Express, MongoDB, MySQL, Python, Flask" height="40">
  <br>
  <img src="https://skillicons.dev/icons?i=kotlin,androidstudio,flutter,dart,java,docker,linux,aws,gcp,git&perline=10" alt="Kotlin, Android Studio, Flutter, Dart, Java, Docker, Linux, AWS, Google Cloud, Git" height="40">
</p>

Also: WebSockets (Socket.IO) · RAG and AI agents (FAISS, BM25, rerankers) · Jetpack Compose · Pinia · OWASP Top 10 · Red Hat · Cisco networking
