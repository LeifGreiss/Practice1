import scraperwiki
import lxml.html
# scrape_table function: gets passed an individual page to scrape
# where is root coming from?
def scrape_table(root):
    rows = root.cssselect("TABLE TR")
    #rows = root.cssselect("table.Trolley.table tr")  # selects all <p> blocks within <p class="ex1">
    for row in rows: # where do rows come from? 
        # Set up our data record 
        record = {}
        table_cells = row.cssselect("TD") #In the row use cssselect to select for TD
        if table_cells: 
            record['Racecourse'] = table_cells[0].text
            record['Address and Phone Number'] = table_cells[1].text
            # Print out the data we've gathered
            print record, '------------'
            # Save the record to the data store with Hospital as the unique key.
            scraperwiki.sqlite.save(["Racecourse"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    scrape_table(root)
starting_url = 'http://www.ukjockey.com/racecourses.html'
scrape_and_look_for_next_link(starting_url)
