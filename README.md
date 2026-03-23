<div align="center">

# ⚡ FitLife n8n — AI Workflow Automation Engine

[![n8n](https://img.shields.io/badge/n8n-Self_Hosted-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/)
[![Ollama](https://img.shields.io/badge/Ollama-CPU_Inference-000000?style=for-the-badge)](https://ollama.com/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-Flash_Lite-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![Cloudflare](https://img.shields.io/badge/Cloudflare-Tunnel-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)](https://cloudflare.com/)

**The AI brain behind [FitLife](https://github.com/ANIS151993/Fit-Life) — 6 self-hosted n8n workflows that power food image analysis, diet plan generation, and workout program creation using a dual AI engine.**

[🌐 n8n Dashboard](https://n8n.marcbd.site) · [📊 Project Showcase](https://anis151993.github.io/Fit-Life/) · [🥗 FitLife App](https://fitlife.marcbd.site)

---

<img src="https://img.shields.io/badge/Workflows-6_Active-brightgreen?style=flat-square" alt="Workflows" />
<img src="https://img.shields.io/badge/AI_Models-4-purple?style=flat-square" alt="Models" />
<img src="https://img.shields.io/badge/Uptime-99.9%25-blue?style=flat-square" alt="Uptime" />
<img src="https://img.shields.io/badge/Cost-$0/month-green?style=flat-square" alt="Cost" />

</div>

---

## 🧠 How It Works

FitLife's AI features are powered by **6 n8n webhook workflows** — 3 using Google Gemini (fast, cloud) and 3 using Ollama (free, self-hosted). Every feature has two AI options so users can choose speed vs. privacy.

### Workflow Architecture

```
                        ┌─────────────────────────────┐
                        │      FITLIFE FRONTEND        │
                        │    fitlife.marcbd.site       │
                        └──────────┬──────────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
            ┌──────────┐   ┌──────────┐   ┌──────────┐
            │  FOOD    │   │   DIET   │   │ WORKOUT  │
            │ ANALYSIS │   │   PLAN   │   │   PLAN   │
            └────┬─────┘   └────┬─────┘   └────┬─────┘
                 │              │              │
           ┌─────┴─────┐  ┌────┴────┐   ┌─────┴─────┐
           ▼           ▼  ▼         ▼   ▼           ▼
      ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
      │ WF 1   │ │ WF 4   │ │ WF 2   │ │ WF 5   │ │ WF 3   │ │ WF 6   │
      │Gemini  │ │Ollama  │ │Gemini  │ │Ollama  │ │Gemini  │ │Ollama  │
      │Fast ⚡ │ │Free 🌿 │ │Fast ⚡ │ │Free 🌿 │ │Fast ⚡ │ │Free 🌿 │
      └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘
          │          │          │          │          │          │
          ▼          ▼          ▼          ▼          ▼          ▼
   ┌──────────┐ ┌──────────┐                                        
   │ Gemini   │ │ Ollama   │  Gemini    Ollama    Gemini     Ollama
   │ Flash    │ │ llava:7b │  Flash     phi3:     Flash      phi3:
   │ Lite API │ │ (Vision) │  Lite      mini      Lite       mini
   └──────────┘ └──────────┘
                    │                         │
                    ▼                         ▼
              ┌──────────┐              ┌──────────┐
              │ KV STORE │              │ KV STORE │
              │ jobId →  │              │ jobId →  │
              │ result   │              │ result   │
              └──────────┘              └──────────┘
```

---

## 📋 The 6 Workflows

### 🍕 Food Image Analysis

| | Gemini (WF 1) | Ollama (WF 4) |
|---|---|---|
| **Endpoint** | `/webhook/fitlife/analyze-food-fast` | `/webhook/fitlife/analyze-food` |
| **AI Model** | `gemini-2.5-flash-lite` | `llava:7b` (7B vision model) |
| **Input** | Base64 image + userId + mealType | Same |
| **Speed** | ~10-20 seconds | ~1-3 minutes |
| **Output** | Calories, macros, vitamins, allergens, quality score | Same |

**What the AI returns:**
```json
{
  "food_items": [
    { "name": "Grilled Chicken Breast", "quantity_g": 200, "calories": 330, "protein_g": 62 }
  ],
  "totals": { "calories": 485, "protein_g": 68, "carbs_g": 32, "fat_g": 12 },
  "vitamins_minerals": { "vitamin_b12_mcg": 1.2, "iron_mg": 3.5, "calcium_mg": 45 },
  "meal_quality_score": 8,
  "allergens": [],
  "health_notes": "Excellent high-protein meal"
}
```

### 🥑 Diet Plan Generation

| | Gemini (WF 2) | Ollama (WF 5) |
|---|---|---|
| **Endpoint** | `/webhook/fitlife/generate-diet-fast` | `/webhook/fitlife/generate-diet-free` |
| **AI Model** | `gemini-2.5-flash-lite` | `phi3:mini` (3.8B text) |
| **Input** | Age, gender, weight, goals, restrictions | Same |
| **Speed** | ~30-60 seconds | ~3-5 minutes |
| **Output** | 7-day meal plan with recipes + daily targets | 3-day plan |

### 💪 Workout Plan Generation

| | Gemini (WF 3) | Ollama (WF 6) |
|---|---|---|
| **Endpoint** | `/webhook/fitlife/generate-workout-fast` | `/webhook/fitlife/generate-workout-free` |
| **AI Model** | `gemini-2.5-flash-lite` | `phi3:mini` (3.8B text) |
| **Input** | Goals, fitness level, equipment, days/week | Same |
| **Speed** | ~30-60 seconds | ~3-5 minutes |
| **Output** | 7-day program with exercises, form tips, warmup/cooldown | Same |

---

## ⚙️ Async Job System

All workflows use an **async polling pattern** to handle long-running AI inference:

```
1. Client POST → /webhook/fitlife/analyze-food
   Body: { imageBase64, userId, mealType, jobId: "uuid-xxx" }

2. n8n returns 200 immediately (non-blocking)

3. n8n processes AI request in background:
   - Sends image/text to Gemini API or Ollama
   - Parses JSON response
   - Stores result in KV Store: kvstore:3456/set?key=uuid-xxx

4. Client polls → GET /webhook/fitlife/food-result?jobId=uuid-xxx
   - Returns { status: "processing" } while working
   - Returns { status: "done", analysis: {...} } when complete

5. KV Store auto-cleans entries after 30 minutes
```

### KV Store

A lightweight Python HTTP key-value store running in Docker alongside n8n:

```yaml
kvstore:
  image: python:3.11-slim
  command: python /app/server.py
  ports: ["3456:3456"]
  # GET  /get?key=xxx     → { value } or { status: "processing" }
  # POST /set?key=xxx     → stores JSON body
  # Auto-cleanup: entries older than 30 min are purged
```

---

## 🏗️ Infrastructure

```
PROXMOX SERVER-1 (172.16.185.23)
├── VM 100 │ 172.16.184.60  │ Ollama + Docker
│   ├── ollama container (port 11434)
│   ├── Models: llava:7b (4.7GB), phi3:mini (2.3GB)
│   └── Cloudflare Tunnel → ollama.marcbd.site
│
└── VM 101 │ 172.16.184.111 │ n8n + Docker
    ├── n8n container (port 5678)
    ├── kvstore container (port 3456)
    ├── 6 active workflows
    └── Cloudflare Tunnel → n8n.marcbd.site

PROXMOX SERVER-2 (172.16.184.208)
└── VM 200 │ 172.16.184.217 │ Next.js Dev
    └── FitLife app source code
```

### Network Flow
- **n8n ↔ Ollama**: Direct LAN connection (`172.16.184.60:11434`) — no internet hop
- **n8n ↔ Gemini**: HTTPS to `generativelanguage.googleapis.com`
- **Frontend ↔ n8n**: Via Cloudflare Tunnel (`n8n.marcbd.site`)
- **Frontend ↔ Firebase**: Direct HTTPS

---

## 🚀 Deployment

```bash
# On VM 101
cd /opt/n8n

# Start all services
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f n8n

# Backup workflows
docker exec n8n n8n export:workflow --all --output=/backup/workflows.json
```

### Environment Variables
| Variable | Purpose |
|----------|---------|
| `N8N_BASIC_AUTH_USER` | n8n login username |
| `N8N_BASIC_AUTH_PASSWORD` | n8n login password |
| `WEBHOOK_URL` | Public webhook base URL |
| `N8N_ENCRYPTION_KEY` | Credential encryption |
| `OLLAMA_BASE_URL` | LAN URL to Ollama server |
| `N8N_RUNNERS_TASK_TIMEOUT` | 600s for long Ollama inference |

---

## 🔧 Key Technical Decisions

1. **Dual AI Engine** — Users choose between fast (Gemini) and free (Ollama) for every feature
2. **Async Polling** — Long-running AI tasks don't block HTTP connections (Ollama can take 3-5 min on CPU)
3. **KV Store** — Simple Python HTTP server instead of Redis — lighter, zero dependencies
4. **LAN Communication** — n8n talks to Ollama over local network (172.16.x.x), no internet roundtrip
5. **Cloudflare Tunnels** — No open ports, no port forwarding, no firewall holes
6. **Task Runner Timeout** — Set to 600s to handle slow CPU inference without dropping connections

---

## 📜 License & Copyright

**© 2024-2026 [Md Anisur Rahman Chowdhury](https://marcbd.site), Gannon University**

---

<div align="center">

**Built with ❤️ by [Md Anisur Rahman Chowdhury](https://marcbd.site)**

*Gannon University*

[![Portfolio](https://img.shields.io/badge/Portfolio-marcbd.site-10b981?style=for-the-badge&logo=google-chrome&logoColor=white)](https://marcbd.site)
[![GitHub](https://img.shields.io/badge/GitHub-ANIS151993-181717?style=for-the-badge&logo=github)](https://github.com/ANIS151993)

</div>
