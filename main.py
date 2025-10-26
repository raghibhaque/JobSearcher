from scraper import scrape_linkedin_jobs
from api_handler import summarize_text
from github_uploader import upload_to_github
import json
import os

def main():
    print("=== 🤖 AutoJobTracker ===")
    keyword = input("🔍 Enter the job title or keyword to search on LinkedIn: ").strip()

    if not keyword:
        print("⚠️ You must enter a valid job title.")
        return

    print(f"\nSearching LinkedIn for '{keyword}' jobs...")
    jobs = scrape_linkedin_jobs(keyword, num_jobs=5)

    if not jobs:
        print("❌ No jobs found. Try another keyword.")
        return

    print(f"Found {len(jobs)} jobs. Summarizing descriptions...")

    for job in jobs:
        summary = summarize_text(f"{job['title']} at {job['company']}")
        job["summary"] = summary
        print(f"✅ {job['title']} → {summary[:80]}...")

    os.makedirs("data", exist_ok=True)

    # Save JSON
    with open("data/jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)

    # Save Markdown summary
    md_path = "data/job_log.md"
    with open(md_path, "w", encoding="utf-8") as log:
        log.write(f"# 🧠 AutoJobTracker Results for '{keyword}'\n\n")
        for job in jobs:
            log.write(f"### {job['title']} @ {job['company']}\n")
            log.write(f"🔗 [View Job]({job['link']})\n\n")
            log.write(f"💬 {job['summary']}\n\n---\n\n")

    upload_to_github(md_path)
    print("\n✅ Done! Results saved in 'data/' and synced to GitHub.")

if __name__ == "__main__":
    main()
