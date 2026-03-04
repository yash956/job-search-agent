from scrapers.company_scraper import scrape_jobs
import pandas as pd


jobs = scrape_jobs()

# convert jobs list to dataframe
df = pd.DataFrame(jobs)

# save to csv
df.to_csv("data/jobs.csv", index=False)

print("Jobs saved to data/jobs.csv")

print(df)