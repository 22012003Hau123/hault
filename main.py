from scraper import scrape_articles
from uploader import vector_store, openai_uploader,create_assistant


def main():
    scraped_files = scrape_articles()
    vt = vector_store()
    openai_uploader(scraped_files, vt)
    create_assistant(vt.id)

if __name__ == "__main__":
    main()