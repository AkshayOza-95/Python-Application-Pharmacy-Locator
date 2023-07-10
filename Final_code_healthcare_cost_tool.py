from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)

options = Options()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-encoding': 'gzip, deflate, br',
    'Accept-language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Referer': 'http://www.google.com/'
}
options.add_argument(f'headers')
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\14124\Desktop\chromedriver.exe')
driver1 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\14124\Desktop\chromedriver.exe')

def getdrugName(): #asks the user to enter the drug name
    name=input("Enter the name of the drug/medicine you want to buy: ")
    return name
def getUserAddress(): #asks the user to enter their address
    city=input("Enter your address (for example- 623, Bellefonte street, Pittsburgh):  ")
    return city
def getRadius(): #asks the user to enter the radius within which they want to check the drug prices
    radius= input("Enter preferred distance of the pharmacy from 1/ 5/ 10/ 20 miles: ")
    return radius
def extract_genric_prices(name, address, radius): #scrapes the data for three pharmacies with lowest price for the generic drug user entered and returns the dataframe with pharmacy name and other details
    try:
        url = 'https://www.americaspharmacy.com/drug/' + name + '/' + address
        driver.get(url)
        radius_drop = Select(driver.find_element_by_id("edit-radius"))
        radius_drop.select_by_value(str(radius))
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        p0_name = soup.find_all(id="pharmacyDirection_0")
        p1_name = soup.find_all(id="pharmacyDirection_1")
        p2_name = soup.find_all(id="pharmacyDirection_2")
        p_address_contact = soup.find_all('span', class_='location d-none d-md-block')

        pharm0_details = list()
        for i in p0_name:
            pharm0_details.append(i.get_text())
        pharm0 = pharm0_details[0].split(".")

        pharm1_details = list()
        for i in p1_name:
            pharm1_details.append(i.get_text())
        pharm1 = pharm1_details[0].split(".")

        pharm2_details = list()
        for i in p2_name:
            pharm2_details.append(i.get_text())
        pharm2 = pharm2_details[0].split(".")

        address = list()
        for a in p_address_contact:
            address.append(a.get_text())
        address0 = address[0]
        phone0 = address[1]
        address1 = address[2]
        phone1 = address[3]
        address2 = address[4]
        phone2 = address[5]

        gen_prices = soup.find_all('p', class_="price-only")
        prices = list()
        for i in gen_prices:
            prices.append(i.get_text())
        price_0 = prices[0].split("$")
        price_1 = prices[1].split("$")
        price_2 = prices[2].split("$")

        return_pharm_list = [pharm0[1], pharm1[1], pharm2[1]]
        return_price_list = [float(price_0[1]), float(price_1[1]), float(price_2[1])]
        return_address_list = [address0.upper(), address1.upper(), address2.upper()]
        return_contact_list = [phone0, phone1, phone2]

        output_DF = pd.DataFrame()
        output_DF['Pharmacy'] = return_pharm_list
        output_DF['Price'] = return_price_list
        output_DF['Address'] = return_address_list
        output_DF['Contact'] = return_contact_list

        return output_DF


    except Exception as ex:
        print("Sorry we did not find the medicine")
def extract_brand_prices(name, address, radius): #scrapes the data for three pharmacies with lowest price for the brand version of drug user entered and returns the dataframe with pharmacy name and other details
    try:
        url1 = 'https://www.americaspharmacy.com/drug/' + name + '/' + address
        driver1.get(url1)
        med_drop = Select(driver1.find_element_by_id("edit-bdrugnamefilter"))
        med_drop.select_by_value("B_" + name.upper())
        radius_drop = Select(driver1.find_element_by_id("edit-radius"))
        radius_drop.select_by_value(str(radius))
        html1 = driver1.page_source

        soup = BeautifulSoup(html1, 'html.parser')
        p0_name = soup.find_all(id="pharmacyDirection_0")
        p1_name = soup.find_all(id="pharmacyDirection_1")
        p2_name = soup.find_all(id="pharmacyDirection_2")
        p_address_contact = soup.find_all('span', class_='location d-none d-md-block')

        pharm0_details = list()
        for i in p0_name:
            pharm0_details.append(i.get_text())
        pharm0 = pharm0_details[0].split(".")

        pharm1_details = list()
        for i in p1_name:
            pharm1_details.append(i.get_text())
        pharm1 = pharm1_details[0].split(".")

        pharm2_details = list()
        for i in p2_name:
            pharm2_details.append(i.get_text())
        pharm2 = pharm2_details[0].split(".")

        address = list()
        for a in p_address_contact:
            address.append(a.get_text())
        address0 = address[0]
        phone0 = address[1]
        address1 = address[2]
        phone1 = address[3]
        address2 = address[4]
        phone2 = address[5]

        gen_prices = soup.find_all('p', class_="price-only")
        prices = list()
        for i in gen_prices:
            prices.append(i.get_text())
        price_0 = prices[0].split("$")
        price_1 = prices[1].split("$")
        price_2 = prices[2].split("$")

        return_pharm_list = [pharm0[1], pharm1[1], pharm2[1]]
        return_price_list = [float(price_0[1]), float(price_1[1]), float(price_2[1])]
        return_address_list = [address0.upper(), address1.upper(), address2.upper()]
        return_contact_list = [phone0, phone1, phone2]

        output_DF_brand = pd.DataFrame()
        output_DF_brand['Pharmacy'] = return_pharm_list
        output_DF_brand['Price'] = return_price_list
        output_DF_brand['Address'] = return_address_list
        output_DF_brand['Contact'] = return_contact_list

        return output_DF_brand

    except Exception as ex:
        print("Sorry we did not find the medicine/brand version")

def firstPath(): #displays the menu of choices for the user - either to check hospital charges or drug prices or to quit
    print('1. Search drugs prices')
    print('2. Search hospital charges')
    print('0. Quit')
    print('')
    path = int(input('Enter number of selection or 0 to quit: '))
    return path

def drugdata(): # ask the user if they want to see data fro drug prices or return to the main menu
    print('1. To see data a drug ')
    print('0: To return to the main menu')
    drugdata1 =  int(input('Enter choice: '))
    return drugdata1
    
def getData(): #reads the csv file into a pandas dataframe
    import pandas as pd
    df2 = pd.read_csv('hospitals.csv')
    return df2

def getScores(): #returns a series that has details about hospitals and their value based purchasing score
    import pandas as pd
    vbp = pd.read_csv('PA hospital scores.csv')
    vbp_list = vbp['Facility Name'].tolist()
    vbp_score = vbp['Total Performance Score'].tolist()
    vbp_series = pd.Series(vbp_score, index=vbp_list)
    return vbp_series

def firstChoice(): # prompts the user to choose between finding hospital by illness category or compare two hospitals across all categories
    print('1. Find hospital by illness category')
    print('2. Compare two hospitals across categories')
    print('0. Quit')
    print('')
    route = int(input('Enter number of selection or 0 to quit: '))
    return route

def oneMenu(dataframe): #returns details about the hospitals by illness category
    choices = dataframe['drg_field'].tolist()
    choices = list(set(choices))
    counter = 1
    for i in choices:
        print('%d. %s' % (counter, i))
        counter+=1
    value = int(input('Enter number of illness category: '))
    value = choices[value-1]
    return value

def twoMenu(dataframe): #returns details to compare two hospitals across the categories
    hosp = dataframe['provider_name'].tolist()
    hosp = list(set(hosp))
    counter = 1
    for i in hosp:
        print('%d. %s' % (counter, i))
        counter+=1
    hosp1 = int(input('Enter number of first selection: '))
    hosp1 = hosp[hosp1-1]
    hosp2 = int(input('Enter number of second selection: '))
    hosp2 = hosp[hosp2-1]
    return [hosp1, hosp2]

def main(): # the main function that compiles all the functions above and run our amazing application.
    path = firstPath()
    print('')
    while path != 0:
        if path == 1:
            drugdata1 = drugdata()
            while drugdata1 !=0:
                drugname = getdrugName()
                print('')
                user_address = getUserAddress()
                print('')
                distance = getRadius()
                print('')
                print("Details for the generic brand of ", drugname)
                print('')
                print(extract_genric_prices(drugname, user_address, distance))
                print('')
                print("Details for the  brand version of ", drugname)
                print('')
                print(extract_brand_prices(drugname, user_address, distance))
                print('')
                drugdata1= drugdata()
                print('')
            path = firstPath()
                
        elif path == 2:
            df2 = getData()
            vbp_series = getScores()
            route = firstChoice()
            while route != 0:
                if route == 1:
                    value = oneMenu(df2)
                    grouped = df2.groupby(['drg_field'])
                    grouped_df = grouped.get_group(value)
                    final_df = grouped_df.groupby(['provider_name'])
                    means = final_df.mean()
                    minlist = means['uncovered_%'].tolist()
                    indexlist = list(means.index.values)
                    graph_df = pd.DataFrame({'Hospital':indexlist, 'Uncovered_%':minlist})
                    graph_df = graph_df.sort_values(by=['Uncovered_%'])
                    graph_df.reset_index(inplace=True, drop=True)
                    # print output
                    
                    print('%s: %2.2f' % (graph_df['Hospital'][0],100*graph_df['Uncovered_%'].min()))
                    print('')
                    print('%s has the lowest average share of total payments remaining after applying medicare coverage when treating %s.' % (graph_df['Hospital'][0],value))
                    print('')
                    print('This facility has an overall value-based purchasing performance score of %2.2f' % vbp_series.loc[graph_df['Hospital'][0]])
                    print('')
                    print('The average value-based purchasing performance score in the state is %2.2f' % vbp_series.mean())
                    # print chart
                    plt.title('Share of total payment left uncovered by medicare')
                    plt.xticks(rotation=90)
                    sns.barplot('Hospital','Uncovered_%',data=graph_df)
                    plt.show()
                    # find overcharge max
                    maxlist = means['overcharge_%'].tolist()
                    maxindex = list(means.index.values)
                    max_df = pd.DataFrame({'Hospital':maxindex, 'Overcharge_%':maxlist})
                    max_df = max_df.sort_values(by=['Overcharge_%'], ascending=False)
                    max_df.reset_index(inplace=True, drop=True)
                    # print output
                    
                    print('%s: %2.2f' % (max_df['Hospital'][0],100*max_df['Overcharge_%'].max()))
                    print('')
                    print('%s has the largest gap in its initial charges compared to actual payments when treating %s.' % (max_df['Hospital'][0],value))
                    print('')
                    print('This facility as an overall value-based purchasing performance score of %2.2f' % vbp_series.loc[max_df['Hospital'][0]])
                    print('')
                    print('The average value-based purchasing performance score in the state is %2.2f' % vbp_series.mean())
                    #print chart
                    plt.title('Share of total charges not paid in actual total payments')
                    plt.xticks(rotation=90)
                    sns.barplot('Hospital','Overcharge_%',data=max_df)
                    plt.show()
                    
                else:
                    h = twoMenu(df2)
                    hosp1 = h[0]
                    hosp2 = h[1]
                    choices = df2['drg_field'].tolist()
                    choices = list(set(choices))
                    grouped_prov = df2.groupby(['provider_name'])
                    prov_df = grouped_prov.get_group(hosp1)
                    hosp1_df = prov_df.groupby(['drg_field'])
                    hosp1_means = hosp1_df.mean()
                    grouped_prov2 = df2.groupby(['provider_name'])
                    prov_df2 = grouped_prov2.get_group(hosp2)
                    hosp2_df = prov_df2.groupby(['drg_field'])
                    hosp2_means = hosp2_df.mean()
                    # uncovered %
                    h1 = round(hosp1_means['uncovered_%'],3)
                    h2 = round(hosp2_means['uncovered_%'],3)
                    h2.rename(columns={'uncovered_%':0}, inplace=True)
                    comp_df = pd.concat([h1, h2],axis=1, sort=True)
                    comp_df['Difference']=comp_df['uncovered_%'] - comp_df[0]
                    comp_df.rename(columns={'uncovered_%':hosp1, 0:hosp2},inplace=True)
                    # print output
                    pd.set_option('display.max_columns', None)
                    pd.set_option('expand_frame_repr', False)
                    print('Comparison of % of total payments that remain uncovered after medicare payments')
                    print('-------------------------------------------------------------------------------')
                    print(comp_df)
                    print('')
                    print('Value-based purchasing total performance scores:')
                    print('%s: %2.2f' % (hosp1, vbp_series.loc[hosp1]))
                    print('%s: %2.2f' % (hosp2, vbp_series.loc[hosp2]))
                    # print chart
                    if len(comp_df[hosp1]) > len(comp_df[hosp2]):
                        xaxis = len(comp_df[hosp1])
                    else:
                        xaxis = len(comp_df[hosp2])
                    plt.xticks(rotation=90)
                    ypos=np.arange(xaxis)
                    plt.bar(ypos-0.2, comp_df[hosp1], width=0.4, label=hosp1, color='red')
                    plt.bar(ypos+0.2, comp_df[hosp2], width=0.4, label=hosp2, color='blue')
                    plt.title('Share of total payments remaining after medicare payments')
                    plt.xticks(ypos,choices)
                    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                    plt.show()
                    # overcharge %
                    h1_over = round(hosp1_means['overcharge_%'],3)
                    h2_over = round(hosp2_means['overcharge_%'],3)
                    h2_over.rename(columns={'uncovered_%':0}, inplace=True)
                    comp_df2 = pd.concat([h1_over, h2_over],axis=1, sort=True)
                    comp_df2['Difference']=comp_df2['overcharge_%'] - comp_df2[0]
                    comp_df2.rename(columns={'overcharge_%':hosp1, 0:hosp2},inplace=True)
                    # print output
                    pd.set_option('display.max_columns', None)
                    pd.set_option('expand_frame_repr', False)
                    print('Comparison of % gap in total hospital charges compared to actual total payments')
                    print('-------------------------------------------------------------------------------')
                    print(comp_df2)
                    print('')
                    print('Value-based purchasing total performance scores:')
                    print('%s: %2.2f' % (hosp1, vbp_series.loc[hosp1]))
                    print('%s: %2.2f' % (hosp2, vbp_series.loc[hosp2]))
                    # print chart
                    if len(comp_df2[hosp1]) > len(comp_df2[hosp2]):
                        xaxis = len(comp_df[hosp1])
                    else:
                        xaxis = len(comp_df2[hosp2])
                    plt.xticks(rotation=90)
                    ypos=np.arange(xaxis)
                    plt.bar(ypos-0.2, comp_df2[hosp1], width=0.4, label=hosp1, color='red')
                    plt.bar(ypos+0.2, comp_df2[hosp2], width=0.4, label=hosp2, color='blue')
                    plt.title('Share of total payments remaining after medicare payments')
                    plt.xticks(ypos,choices)
                    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                    plt.show()
                route = firstChoice()
            path = firstPath()
            
            
if __name__ == '__main__':
    main()
