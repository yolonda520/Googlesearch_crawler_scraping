# Google Search scraping to extract contact and group emails sending
**This is a simple google search results crawler and scrape the contacts. After scraping emails and saving to .csv file, we can send group emails by that scraping results. Before use this tool, please read these tips below.**

## Requirements
**Need install some packages, I prefer Google: conda forge install <package name>**

## How to Use?
1. SF_research_list.csv is just an example .csv file, you can change any csv file instead of this one.
2. csv_group_email_sending_template.py is a python code template, which you can use this template send group email from .csv file. But this template only send from gmail. If you want use other email domain to group sending, please change smtp_server.
3. Hide_receivers_Input_groupemail_sending_template.py can be used to send group emails, just change receiver_email content(whom you want send). And email receivers will not see addresses that who you send to.
4. show_receiver_groupemail_sending_template.py can be used to send group emails, just change to_addr content(whom you want send). And receivers will see all email addresses that you send to.
5. email_scrape_template.py can be used to scrape email that you want from Google Search results and save to .csv file.

