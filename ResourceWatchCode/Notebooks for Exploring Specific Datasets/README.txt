These files each deal with a specific dataset relevant to the Resource
Watch platform.

They are helpers for viewing the particular data. Something like these
could be distributed whenever users download the related datasets from the RW
API in order to give a headstart to user's exploration of the data.

CDIAC Data:
* Convert CSVs of CDIAC emissions data into dataframes, use these to compute
change over time

AQUASTAT_reformat:
* Turn a series of sheets in an excel doc into a single spreadsheet of
crop calendars

GCAM Widget:
* Investigate economic and regulatory scenario models to see what would be
needed to achieve certain global climate targets

GDELT Play:
* Filter the GDELT data by some tags and explore the distribution over an area

EORA Exploration:
* Load EORA trade tables into a set of pandas dataframes, use these to show
change over time

World Bank data from RW API:
* Concatenate several world bank datasets stored on the RW API for use in a D3
visualization

IPUMS Data Reader:
* Convert the .dat files that IPUMS provides data in to pandas dataframes,
attach this data to shapefiles at admin level 2 level

Downscaling National Trade data with Census data:
* Experimental - use the IPUMS jobs data and the EORA trade and emissions data
to model where in a country (in this case China) emissions have occured for
various industries
