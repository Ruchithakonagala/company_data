import csv #importing ths csv module to work with CSV files
Stocks=[] #empty list to store all company data

with open("company_data.csv","r") as file:  #opening the company data file in read mode 'with' automatically closes the file 
    reader=csv.DictReader(file) #reads each row as a dictionaru(key-value pairs)
    Stocks=[]
#loop through each row in csv
    for row in reader:
        Stocks.append(row) #ass this company rows into the stocks list
#s is variable that is holding data for list of stocks
    for s in Stocks: #loop through all companies to convert string values to numbers
        try:
            s["PriceStart"]=float(s["PriceStart"]) #convert price columns from strings to numbers
            s["PriceEnd"]=float(s["PriceEnd"])
        except ValueError: #if conversion fails print this
            print(f"Invalid data found in {s['Stock']}")
    for s in Stocks:
        s["Return_%"]=(((s["PriceEnd"]-s["PriceStart"])/s["PriceStart"])*100) #calculate return% for each stock
    sort_Stocks=sorted(Stocks,key=lambda x:x["Return_%"], reverse=True)  #sort the companies based on return% in decending order
    print("\nPerforming companies:\n")

    for s in sort_Stocks:
        print(f"{s['Stock']} ({s['Sector']})-{s['Return_%']}%")
     #sort_Stocks=sorted(Stocks,key=lambda x:x["Return_%"], reverse=True)
    print("\nTop 5 companies: \n")
    for s in sort_Stocks[:5]:
        print(f"{s['Stock']} - {s['Return_%']}%")
# create dictionary to store returns that grouped by sector
    Sector_return={}
    Sector_count={} #dictionary count
    for s in sort_Stocks:
        Sector=s["Sector"]
        Sector_return.setdefault(Sector,[]).append(s["Return_%"]) #setdefault() creates an empty list for sector if it doesn't exist
    #adding return% to sectors
    print("\nAverage return per Sector:\n") 
    Sector_count[Sector]=Sector_count.get(Sector,0)+1 #for stocks that belongs to sector
    best_sector=None
    best_avg=float('-inf') 
    for sec, values in Sector_return.items(): #loop through each sector and calculate its average return
        avg=sum(values)/len(values)
        count= Sector_count[Sector]
    print(f"{Sector_return}:{round(avg)}%, Stocks={count}\n")

    with open("performance_report.csv","w",newline="")as f: #now generate a performance report csv file
        columns=["Stock","Sector","PriceStart","PriceEnd","Return_%"]  #column names for new csv filr
        writer=csv.DictWriter(f,fieldnames=columns) #it is for writing dictionaries into csv file
        writer.writeheader() #these for column names(header)
        writer.writerows(sort_Stocks)  #writing all stock data in rows
    print("\nReport generated successfully!")



