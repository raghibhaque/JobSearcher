# ☀️ JobSearcher — my 2024 automation project

Back in **January 2024**, I spent a few weeks experimenting with web automation and APIs — mainly just tinkering and learning how different Python tools worked together.  
While cleaning my old laptop recently, I found this small side project called **JobSearcher**, and decided it deserved a proper spot on GitHub. Granted, its super basic and VERY messy (was going off a couple youtube tutorials, and the fact I gave up on python shortly thereafter.)

It’s a simple idea:  
> “What if I could search for jobs on LinkedIn, get AI summaries of each posting, and automatically save them to my GitHub?”

That’s exactly what this does.

---

## 🧠 What It Does
- 🔍 Uses **Selenium** to automatically scrape job listings from LinkedIn.  
- 🧩 Summarises each job description using the **Hugging Face AI API** (BART model).  
- 💾 Saves everything to local files (`jobs.json` + `job_log.md`).  
- ☁️ Uploads the summaries directly to a GitHub repo using the **GitHub API** — like a personal job-tracker that updates itself.

---

## 🚀 How It Works
When you run the script:
1. You’re asked for a job title (for example: `Software Engineer Intern`)
2. Selenium searches LinkedIn and grabs a few recent listings.
3. Each listing gets summarised through Hugging Face.
4. The results are saved locally **and pushed to your GitHub repo** automatically.

It was my first real attempt at connecting multiple APIs and automating something useful — and it actually worked surprisingly well.

---

## ⚙️ Setup & Running

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

---

### 2️⃣ Create a `.env` file in the root folder
```bash
HUGGINGFACE_API_KEY=your_huggingface_token
GITHUB_TOKEN=your_github_token
GITHUB_REPO=your_username/your_repo
```
---

Example output

| Purpose      | Technology                                 |
| ------------ | ------------------------------------------ |
| Web scraping | Selenium + BeautifulSoup                   |
| AI summaries | Hugging Face API (facebook/bart-large-cnn) |
| Automation   | Python (requests, dotenv)                  |
| Uploads      | PyGithub + GitHub REST API                 |

---

🧾 License

MIT License — free to use, remix, or learn from.

---

coded in 2024 with coffee, found it in 2025... with coffee <3