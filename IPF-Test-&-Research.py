#######################################################################################################################################################################
#User Dependent Variables
County_Value = "Bonneville-Idaho"
Number_of_CSV_Files = 1
State = "Idaho"
County = "Bonneville"
Down_Payment_Percentage = 0.20
Mortgage_Rate = 0.04
Term_of_Loan_Years = 30
Bedroom_Unit_Fair_Rent_0 = 730
Bedroom_Unit_Fair_Rent_1 = 870
Bedroom_Unit_Fair_Rent_2 = 1070
Bedroom_Unit_Fair_Rent_3 = 1520
Bedroom_Unit_Fair_Rent_4 = 1820
Property_Tax_Rate = 0.0079
Market_Rent_Rate = 1.15




#######################################################################################################################################################################
from reportlab.pdfgen import canvas
from datetime import date
import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np

USA = {
    "Idaho": {
        "Bonneville": ['83401', '83402', '83404', '83406', '83236', '83454', '83444', '83443', '83427', '83120', '83285', '83449', '83428', '83403', '83405', '83415'],
        "Ada":['83646','83642','83709','83704','83687','83706','83616','83634','83713','83705','83714','83702','83716','83703','83669','83712','83641','83721','83733','83730','83727','83624','83757','83720','83724','83731','83680','83701','83708','83707','83711','83715','83717','83719','83722','83725','83726','83729','83728','83732','83756','83735','83799'],
        "County221":[],
                
    },
    "Alaska": {
        "County331":[],
        "County332":[],
                
    },
    "Alabama": {
        "County441":[],
        "County442":[],
    }
}

#Key format for dictionary
'''if Zip in USA["Idaho"]["Bonneville"]:'''
'''
    1SALE TYPE
    2SOLD DATE
    3PROPERTY TYPE
    4ADDRESS
    5CITY
    6STATE OR PROVINCE
    7ZIP OR POSTAL CODE
    8PRICE
    90BEDS
    10BATHS
    11LOCATION
    12SQUARE FEET
    13LOT SIZE
    14YEAR BUILT
    15DAYS ON MARKET
    16$/SQUARE FEET
    17HOA/MONTH
    18STATUS
    19NEXT OPEN HOUSE START TIME
    20NEXT OPEN HOUSE END TIME
    21URL
    22SOURCE
    23MLS Number
'''

Date = date.today()
Date = str(Date)

Number_of_CSV_Files = int(Number_of_CSV_Files)
Number_of_CSV_Files = Number_of_CSV_Files + 1

for x in range(1,Number_of_CSV_Files):
    x = str(x)
    df_ZILLOWA = pandas.read_csv(D:\Execute Program\County_Value + '-' + x + '.csv')
    df_ZILLOW = df_ZILLOWA.fillna(0) 
    CSV_Length = len(df_ZILLOW)
    CSV_Length = int(CSV_Length)
    for i in range(0,CSV_Length):
        print(i)
        #Set variables from .csv
        Address = df_ZILLOW.iat[0 + i,3]
        Address = str(Address)
        Length = len(Address)

        Property_Type = df_ZILLOW.iat[0 + i,2]
        Property_Type = str(Property_Type)

        Square_Footage_Cost = df_ZILLOW.iat[0 + i,15]
        Square_Footage_Cost = str(Square_Footage_Cost)

        Year_Built = df_ZILLOW.iat[0 + i,13]
        Year_Built = str(Year_Built)

        Days_On_Market = df_ZILLOW.iat[0 + i,14]
        Days_On_Market = str(Days_On_Market)

        Zip = df_ZILLOW.iat[0 + i,6]
        Zip = str(Zip)
        
        Property_Listing_Cost = df_ZILLOW.iat[0 + i,7]
        Property_Listing_Cost = int(Property_Listing_Cost)
        
        HOA_Yearly = df_ZILLOW.iat[0 + i,16]
        HOA = int(HOA_Yearly)
        HOA_Yearly = HOA*12
        
        Square_Feet = df_ZILLOW.iat[0 + i,11]
        
        Lot_Size = df_ZILLOW.iat[0 + i,12]
        
        Bedroom = df_ZILLOW.iat[0 + i,8]
        
        Bath = df_ZILLOW.iat[0 + i,9]

        if Zip in USA["Idaho"]["Bonneville"]:
            State = "Idaho"
            County = "Bonneville"
            Property_Taxes = 0.82*Property_Listing_Cost
        if Zip in USA["Idaho"]["Ada"]:
            State = "Idaho"
            County = "Ada"
        
        
    #Home Insurance Cost
        Property_Listing_Cost_Coverage = 0.8*Property_Listing_Cost
        if Property_Listing_Cost_Coverage <= 199000:
            Insurance = 946
        elif Property_Listing_Cost_Coverage <= 299000:
            Insurance = 1442
        elif Property_Listing_Cost_Coverage <= 399000:
            Insurance = 1899
        elif Property_Listing_Cost_Coverage <= 499000:
            Insurance = 2481
        elif Property_Listing_Cost_Coverage <= 599000:
            Insurance = 3263
        else:
            continue
        Insurance_Yearly = Insurance

        if Bedroom == 0:
            Unit_Fair_Rent_Original = Bedroom_Unit_Fair_Rent_0 
        elif Bedroom == 1:
            Unit_Fair_Rent_Original = Bedroom_Unit_Fair_Rent_1
        elif Bedroom == 2:
            Unit_Fair_Rent_Original = Bedroom_Unit_Fair_Rent_2 
        elif Bedroom == 3:
            Unit_Fair_Rent_Original = Bedroom_Unit_Fair_Rent_3
        elif Bedroom == 4:
            Unit_Fair_Rent_Original = Bedroom_Unit_Fair_Rent_4
        else:
            continue
        
        if Bedroom == 0:
            Unit_Fair_Rent = Bedroom_Unit_Fair_Rent_0 * Market_Rent_Rate
        elif Bedroom == 1:
            Unit_Fair_Rent = Bedroom_Unit_Fair_Rent_1 * Market_Rent_Rate
        elif Bedroom == 2:
            Unit_Fair_Rent = Bedroom_Unit_Fair_Rent_2 * Market_Rent_Rate
        elif Bedroom == 3:
            Unit_Fair_Rent = Bedroom_Unit_Fair_Rent_3 * Market_Rent_Rate
        elif Bedroom == 4:
            Unit_Fair_Rent = Bedroom_Unit_Fair_Rent_4 * Market_Rent_Rate
        else:
            continue


    #Property Management
        Property_Management = (0.10 * Unit_Fair_Rent)*12

    #Down Payment
        Down_Payment = Down_Payment_Percentage*Property_Listing_Cost

    #Property mortgaged after down and closing
        Property_After_Down1 = Down_Payment - Property_Listing_Cost
        Closing_Cost = 0.03*Property_After_Down1
        Property_After_Down = Closing_Cost - Property_After_Down1
        
        r = Mortgage_Rate/12
        P = Property_After_Down
        n = Term_of_Loan_Years*12
        Monthly_Mortgage = P*(r*((1 + r)**n)/((1 + r)**n -1))
        Yearly_Mortgage = Monthly_Mortgage*12
        
    #Other Expenses
        #Property Taxes
        Property_Taxes = Property_Tax_Rate*Property_Listing_Cost
        #Capital Expenditures
        Capital_Expenditures = 0.01 * Property_Listing_Cost
        #Vacency
        Vacancy = 0.005 * Property_Listing_Cost
        #Maintenance
        Maintenance = 0.01 * Property_Listing_Cost
    #Cash on Cash Return
        Total_Cash_Invested = Down_Payment + Closing_Cost
        Total_Income = Unit_Fair_Rent*12
        
        Total_Expenses = Property_Taxes + HOA_Yearly + Yearly_Mortgage + Insurance + Capital_Expenditures + Vacancy + Maintenance
        
        CoC = ((Total_Income-Total_Expenses)/Total_Cash_Invested)*100
        
    #Cost of acquisition
        Closing_Cost_Max = Property_Listing_Cost * 0.06
        Cost_of_Acquisition_Max = Down_Payment + Closing_Cost_Max
        Closing_Cost_Min = Property_Listing_Cost * 0.03
        Cost_of_Acquisition_Min = Down_Payment + Closing_Cost_Min

        Cost_of_Acquisition_Min = round(Cost_of_Acquisition_Min)
        Cost_of_Acquisition_Max = round(Cost_of_Acquisition_Max)
        Cost_of_Acquisition_Min = str(Cost_of_Acquisition_Min)
        Cost_of_Acquisition_Max = str(Cost_of_Acquisition_Max)
    #NOI = Income - Expenses
        NOI1 = round(Total_Income-Total_Expenses)
        NOI2 = round((Total_Income*1.005)-Total_Expenses)
        NOI3 = round((Total_Income*1.010)-Total_Expenses)
        NOI4 = round((Total_Income*1.015)-Total_Expenses)
        NOI5 = round((Total_Income*1.020)-Total_Expenses)
        NOI10 = round((Total_Income*1.040)-Total_Expenses)
        NOI15 = round((Total_Income*1.060)-Total_Expenses)
        NOI20 = round((Total_Income*1.080)-Total_Expenses)
        NOI30 = round(((Total_Income*1.120)-Total_Expenses)+Yearly_Mortgage)

        NOI1 = int(NOI1)
        
        i = str(i)
        if NOI1 >= 500:
            NOI1 = str(NOI1)
            #Remaining Balance
            principal = Property_After_Down  # the initial amount borrowed
            interest_rate = Mortgage_Rate  # 5% interest rate
            loan_term = Term_of_Loan_Years  # the loan term in years
            num_payments_made = 1  # number of payments made so far
            payment_per_year = 12  # number of payments made per year
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance1 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance1 = int(remaining_balance1)
            round(remaining_balance1)
            
            num_payments_made = 2
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance2 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance2 = int(remaining_balance2)
            round(remaining_balance2)

            num_payments_made = 3
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance3 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance3 = int(remaining_balance3)
            round(remaining_balance3)

            num_payments_made = 4
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance4 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance4 = int(remaining_balance4)
            round(remaining_balance4)

            num_payments_made = 5
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance5 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance5 = int(remaining_balance5)
            round(remaining_balance5)

            num_payments_made = 10
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance10 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance10 = int(remaining_balance10)
            round(remaining_balance10)

            num_payments_made = 15
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance15 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance15 = int(remaining_balance15)
            round(remaining_balance15)

            num_payments_made = 20
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance20 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance20 = int(remaining_balance20)
            round(remaining_balance20)

            num_payments_made = 30
            num_payments = num_payments_made * payment_per_year
            monthly_interest_rate = interest_rate / payment_per_year
            total_payments = loan_term * payment_per_year
            mortgage_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
            remaining_balance30 = principal * ((1 + monthly_interest_rate)**num_payments) - (mortgage_payment / monthly_interest_rate) * ((1 + monthly_interest_rate)**num_payments - 1)
            remaining_balance30 = int(remaining_balance30)
            round(remaining_balance30)

            #Yearly Apreiciation
            Year1PropertyValue = Property_Listing_Cost
            Year2PropertyValue = round(Year1PropertyValue * 1.02)
            Year3PropertyValue = round(Year2PropertyValue * 1.02)
            Year4PropertyValue = round(Year3PropertyValue * 1.02)
            Year5PropertyValue = round(Year4PropertyValue * 1.02)
            Year6PropertyValue = round(Year5PropertyValue * 1.02)
            Year7PropertyValue = round(Year6PropertyValue * 1.02)
            Year8PropertyValue = round(Year7PropertyValue * 1.02)
            Year9PropertyValue = round(Year8PropertyValue * 1.02)
            Year10PropertyValue = round(Year9PropertyValue * 1.02)
            
            Year11PropertyValue = round(Year10PropertyValue * 1.02)
            Year12PropertyValue = round(Year11PropertyValue * 1.02)
            Year13PropertyValue = round(Year12PropertyValue * 1.02)
            Year14PropertyValue = round(Year13PropertyValue * 1.02)
            Year15PropertyValue = round(Year14PropertyValue * 1.02)
            Year16PropertyValue = round(Year15PropertyValue * 1.02)
            Year17PropertyValue = round(Year16PropertyValue * 1.02)
            Year18PropertyValue = round(Year17PropertyValue * 1.02)
            Year19PropertyValue = round(Year18PropertyValue * 1.02)
            Year20PropertyValue = round(Year19PropertyValue * 1.02)
            
            Year21PropertyValue = round(Year20PropertyValue * 1.02)
            Year22PropertyValue = round(Year21PropertyValue * 1.02)
            Year23PropertyValue = round(Year22PropertyValue * 1.02)
            Year24PropertyValue = round(Year23PropertyValue * 1.02)
            Year25PropertyValue = round(Year24PropertyValue * 1.02)
            Year26PropertyValue = round(Year25PropertyValue * 1.02)
            Year27PropertyValue = round(Year26PropertyValue * 1.02)
            Year28PropertyValue = round(Year27PropertyValue * 1.02)
            Year29PropertyValue = round(Year28PropertyValue * 1.02)
            Year30PropertyValue = round(Year29PropertyValue * 1.02)
            
    #Loan Balance
            Loan_Balance1 = round((Yearly_Mortgage*1)-Property_After_Down)
            Loan_Balance2 = round((Yearly_Mortgage*2)-Property_After_Down)
            Loan_Balance3 = round((Yearly_Mortgage*3)-Property_After_Down)
            Loan_Balance4 = round((Yearly_Mortgage*4)-Property_After_Down)
            Loan_Balance5 = round((Yearly_Mortgage*5)-Property_After_Down)
            Loan_Balance10 = round((Yearly_Mortgage*10)-Property_After_Down)
            Loan_Balance15 = round((Yearly_Mortgage*15)-Property_After_Down)
            Loan_Balance20 = round((Yearly_Mortgage*20)-Property_After_Down)
            Loan_Balance30 = round((Yearly_Mortgage*30)-Property_After_Down)
            
    #equity over 30 years
            Equity1 = Year1PropertyValue - remaining_balance1
            Equity2 = Year2PropertyValue - remaining_balance2 
            Equity3 = Year3PropertyValue - remaining_balance3 
            Equity4 = Year4PropertyValue - remaining_balance4 
            Equity5 = Year5PropertyValue - remaining_balance5 
            Equity10 = Year10PropertyValue - remaining_balance10 
            Equity15 = Year15PropertyValue - remaining_balance15 
            Equity20 = Year20PropertyValue - remaining_balance20 
            Equity30 = Year30PropertyValue - remaining_balance30

    #Profit
            Profit1 = round(Equity1 - Total_Cash_Invested)
            Profit2 = round(Equity2 - Total_Cash_Invested)
            Profit3 = round(Equity3 - Total_Cash_Invested)
            Profit4 = round(Equity4 - Total_Cash_Invested)
            Profit5 = round(Equity5 - Total_Cash_Invested)
            Profit10 = round(Equity10 - Total_Cash_Invested)
            Profit15 = round(Equity15 - Total_Cash_Invested)
            Profit20 = round(Equity20 - Total_Cash_Invested)
            Profit30 = round(Equity30 - Total_Cash_Invested)


            def amortization_schedule(principal, interest_rate, monthly_payment, months):
                        balance = principal
                        interest_paid = 0
                        principal_paid = 0
                        amortization = []
                        equity = []
                        
                        for month in range(1, months+1):
                            interest = balance * (interest_rate / 12)
                            interest_paid += interest
                            principal_paid = monthly_payment - interest
                            balance -= principal_paid
                            equity_value = principal - balance
                            amortization.append(balance)
                            equity.append(equity_value)
                            
                        return amortization, equity
        
            principal = Property_After_Down
            interest_rate = Mortgage_Rate
            monthly_payment = Monthly_Mortgage
            months = Term_of_Loan_Years * 12


            amortization, equity = amortization_schedule(principal, interest_rate, monthly_payment, months)

            # Group data into 12-month intervals
            amortization_12 = np.add.reduceat(amortization, np.arange(0, len(amortization), 12))
            equity_12 = np.add.reduceat(equity, np.arange(0, len(equity), 12))

            # Create bar chart
            fig, ax = plt.subplots()
            ax.bar(np.arange(1, len(amortization)+1), amortization, width=0.4, label='Balance')
            ax.bar(np.arange(1, len(equity)+1), equity, width=0.4, label='Equity')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount ($)')
            #ax.set_title('Amortization Schedule')
            ax.legend() 
            plt.savefig('amortization_schedule.png', bbox_inches='tight') 
            

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            CoC2 = round(CoC,2)
            CoC2 = str(CoC2)
            Property_Listing_Cost = str(Property_Listing_Cost)
            Bedroom = str(Bedroom)
            Bath = str(Bath)
            Square_Feet = str(Square_Feet)
            Lot_Size = str(Lot_Size)
            Monthly_Mortgage = round(Monthly_Mortgage,2)
            Monthly_Mortgage = str(Monthly_Mortgage)
            Total_Expenses = round(Total_Expenses)
            Total_Income = round(Total_Income)
            Total_Expenses = str(Total_Expenses)
            Total_Income = str(Total_Income)

            Yearly_Mortgage = round(Yearly_Mortgage)
            Property_Taxes = round(Property_Taxes)
            Vacancy = round(Vacancy)
            Capital_Expenditures = round(Capital_Expenditures)
            Insurance = round(Insurance)
            HOA_Yearly = round(HOA_Yearly)
                
            Maintenance = round(Maintenance)
            Property_Management = round(Property_Management)

            
            Yearly_Mortgage = str(Yearly_Mortgage)
            Property_Taxes = str(Property_Taxes)
            Vacancy = str(Vacancy)
            Capital_Expenditures = str(Capital_Expenditures)
            Insurance = str(Insurance)
            HOA_Yearly = str(HOA_Yearly)

            Unit_Fair_Rent_Original = str(Unit_Fair_Rent_Original)
            Unit_Fair_Rent = str(Unit_Fair_Rent)
                
            Maintenance = str(Maintenance)
            Property_Management = str(Property_Management)           
                
            def IPF(c):
                #Images
                #c.drawImage('Map_Idaho.png', 10, 360, width=150, height=260)
                #c.drawImage('Map_Side.png', 70, 560, width=90, height=50)
                #c.drawImage('amortization_schedule.png', 230, 200, width=325, height=190)
                #c.drawImage('Yearly_Overview.png', 350, 415, width=250, height=190)

                c.setFillColorRGB(0.82,0.82,0.82)
                c.rect(10,750,365,20, fill=1)

                c.setFillColorRGB(0.82,0.82,0.82)
                c.rect(10,640,570,20, fill=1)

                c.setFillColorRGB(0.82,0.82,0.82)
                c.rect(10,450,280,20, fill=1)
#
                c.setFillColorRGB(0.82,0.82,0.82)
                c.rect(300,450,280,20, fill=1)

                c.setFillColorRGB(0.82,0.82,0.82)
                c.rect(300,320,280,20, fill=1)
#
                c.setFillColorRGB(0.82,0.82,0.82)
                c.rect(10,180,570,20, fill=1)

                #Investment Overview
                c.setFillColorRGB(0,0,0)
                c.setFont("Courier", 14)
                c.drawString(14,755,"Investment Overview")
                
                c.setFont("Courier", 12)
                c.drawString(14,735,"Acquisition Cost")
                c.drawString(14,715,"Net Operating Income")
                c.drawString(14,695,"Total Income")
                c.drawString(14,675,"Total Expense")

                c.drawString(250,735,Cost_of_Acquisition_Min + ' - ' +Cost_of_Acquisition_Max)
                c.drawString(250,715,NOI1)
                c.drawString(250,695,Total_Income)
                c.drawString(250,675,Total_Expenses)
                
                c.line(10, 770, 375, 770)
                c.line(10, 750, 375, 750)
                c.line(10, 730, 375, 730)
                c.line(10, 710, 375, 710)
                c.line(10, 690, 375, 690)
                c.line(10, 670, 375, 670)
                
                c.line(10, 770, 10, 670)
                c.line(375, 770, 375, 670)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #Property Info
                c.setFont("Courier", 14)
                c.drawString(14,645,"Property Info")
                
                c.setFont("Courier", 12)
                c.drawString(14,625,"Property Cost")
                c.drawString(14,605,"Address")
                c.drawString(14,585,"Bedroom & Bath")
                c.drawString(14,565,"Square Footage")
                c.drawString(14,545,"Square Footage Cost")
                c.drawString(14,525,"Property Type")
                c.drawString(14,505,"Built")
                c.drawString(14,485,"Days on Market")

                c.drawString(300,625,'$'+Property_Listing_Cost)
                c.drawString(300,605,Address)
                c.drawString(300,585,Bedroom+' Bedroom(s)'+' & '+Bath+' Bathroom(s)')
                c.drawString(300,565,Square_Feet)
                c.drawString(300,545,Square_Footage_Cost)
                c.drawString(300,525,Property_Type)
                c.drawString(300,505,Year_Built)
                c.drawString(300,485,Days_On_Market)
                
                c.line(10, 660, 580, 660)
                c.line(10, 640, 580, 640)
                c.line(10, 620, 580, 620)
                c.line(10, 600, 580, 600)
                c.line(10, 580, 580, 580)
                c.line(10, 560, 580, 560)
                c.line(10, 540, 580, 540)
                c.line(10, 520, 580, 520)
                c.line(10, 500, 580, 500)
                c.line(10, 480, 580, 480)
                
                c.line(10, 660, 10, 480)
                c.line(580, 660, 580, 480)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #Yearly Expense
                c.setFont("Courier", 14)
                c.drawString(14,455,"Yearly Expenses")
                c.setFont("Courier", 12)
                c.drawString(14,435,"Mortgage")
                c.drawString(14,415,"Property Tax")
                c.drawString(14,395,"Vacancy")
                c.drawString(14,375,"Capital Expenditures")
                c.drawString(14,355,"Insurance")
                c.drawString(14,335,"HOA")
                c.drawString(14,315,"Maintenance")
                c.drawString(14,295,"*Property Management")
                c.drawString(14,275,"Total Expense")
                c.drawString(14,255,"* Not included in final metrics")

                c.drawString(220,435,Yearly_Mortgage)
                c.drawString(220,415,Property_Taxes)
                c.drawString(220,395,Vacancy)
                c.drawString(220,375,Capital_Expenditures)
                c.drawString(220,355,Insurance)
                c.drawString(220,335,HOA_Yearly)
                c.drawString(220,315,Maintenance)
                c.drawString(220,295,Property_Management)
                c.drawString(220,275,Total_Expenses)
                
                
                
                c.line(10, 470, 290, 470)
                c.line(10, 450, 290, 450)
                c.line(10, 430, 290, 430)
                c.line(10, 410, 290, 410)
                c.line(10, 390, 290, 390)
                c.line(10, 370, 290, 370)
                c.line(10, 350, 290, 350)
                c.line(10, 330, 290, 330)
                c.line(10, 310, 290, 310)
                c.line(10, 290, 290, 290)
                c.line(10, 270, 290, 270)
                
            
                c.line(10, 470, 10, 270)
                c.line(290, 470, 290, 270)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #Loction Overview
                c.setFont("Courier", 14)
                c.drawString(304,455,"Location Analysis")
                c.setFont("Courier", 12)
                c.drawString(304,435,"Population")
                c.drawString(304,415,"Economic Activity")
                c.drawString(304,395,"Crime")
                c.drawString(304,375,"Amount of Rentals")
                c.drawString(304,355,"Ideal Bed & Bath")

                c.drawString(494,435,"0000.00")
                c.drawString(494,415,"0000.00")
                c.drawString(494,395,"0000.00")
                c.drawString(494,375,"0000.00")
                c.drawString(494,355,"0000.00")
                
                
                c.line(300, 470, 580, 470)
                c.line(300, 450, 580, 450)
                c.line(300, 430, 580, 430)
                c.line(300, 410, 580, 410)
                c.line(300, 390, 580, 390)
                c.line(300, 370, 580, 370)
                c.line(300, 350, 580, 350)
                
                
                c.line(580, 470, 580, 350)
                c.line(300, 470, 300, 350)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #Tenant Overview
                c.setFont("Courier", 14)
                c.drawString(304,325,"Market Data")
                c.setFont("Courier", 12)
                c.drawString(304,305,"Fair Rent")
                c.drawString(304,285,"Market Rent")
                c.drawString(304,265,"Affordable Rent")
                c.drawString(304,245,"Tenant Income")
                c.drawString(304,225,"Total Income")

                c.drawString(494,305,Unit_Fair_Rent_Original)
                c.drawString(494,285,Unit_Fair_Rent)
                c.drawString(494,265,"0000.00")
                c.drawString(494,245,"0000.00")
                c.drawString(494,225,Total_Income)
                
                
                c.line(300, 340, 580, 340)
                c.line(300, 320, 580, 320)
                c.line(300, 300, 580, 300)
                c.line(300, 280, 580, 280)
                c.line(300, 260, 580, 260)
                c.line(300, 240, 580, 240)
                c.line(300, 220, 580, 220)
                
                
                c.line(580, 340, 580, 220)
                c.line(300, 340, 300, 220)
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #30 Year Overview
                #Vertical
                c.line(10, 40, 10, 200)
                c.line(130, 40, 130, 180)
                c.line(180, 40, 180, 180)
                c.line(230, 40, 230, 180)
                c.line(280, 40, 280, 180)
                c.line(330, 40, 330, 180)
                c.line(380, 40, 380, 180)
                c.line(430, 40, 430, 180)
                c.line(480, 40, 480, 180)
                c.line(530, 40, 530, 180)
                c.line(580, 40, 580, 200)

                #Horizontal
                c.line(10, 40, 580, 40)
                c.line(10, 60, 580, 60)
                c.line(10, 80, 580, 80)
                c.line(10, 100, 580, 100)
                c.line(10, 120, 580, 120)
                c.line(10, 140, 580, 140)
                c.line(10, 160, 580, 160)
                c.line(10, 180, 580, 180)
                c.line(10, 200, 580, 200)
                #Overview Text
                c.setFont("Courier", 10)
                c.drawString(12,45,"Profit if Sold")
                c.drawString(12,65,"NOI")
                c.drawString(12,85,"Mortgage Payment")
                c.drawString(12,105,"Loan Balance")
                c.drawString(12,125,"Equity")
                c.drawString(12,145,"Property Value")
                
                c.setFont("Courier", 10)
                c.drawString(132,165,"Year 1")
                c.drawString(182,165,"Year 2")
                c.drawString(232,165,"Year 3")
                c.drawString(282,165,"Year 4")
                c.drawString(332,165,"Year 5")
                c.drawString(382,165,"Year 10")
                c.drawString(432,165,"Year 15")
                c.drawString(482,165,"Year 20")
                c.drawString(532,165,"Year 30")

                c.drawString(132,145,'$'+str(Year1PropertyValue))
                c.drawString(182,145,'$'+str(Year2PropertyValue))
                c.drawString(232,145,'$'+str(Year3PropertyValue))
                c.drawString(282,145,'$'+str(Year4PropertyValue))
                c.drawString(332,145,'$'+str(Year5PropertyValue))
                c.drawString(382,145,'$'+str(Year10PropertyValue))
                c.drawString(432,145,'$'+str(Year15PropertyValue))
                c.drawString(482,145,'$'+str(Year20PropertyValue))
                c.drawString(532,145,'$'+str(Year30PropertyValue))

                c.drawString(132,105,'$'+str(remaining_balance1))
                c.drawString(182,105,'$'+str(remaining_balance2))
                c.drawString(232,105,'$'+str(remaining_balance3))
                c.drawString(282,105,'$'+str(remaining_balance4))
                c.drawString(332,105,'$'+str(remaining_balance5))
                c.drawString(382,105,'$'+str(remaining_balance10))
                c.drawString(432,105,'$'+str(remaining_balance15))
                c.drawString(482,105,'$'+str(remaining_balance20))
                c.drawString(532,105,'$'+str(remaining_balance30))

                c.drawString(132,125,'$'+str(Equity1))
                c.drawString(182,125,'$'+str(Equity2))
                c.drawString(232,125,'$'+str(Equity3))
                c.drawString(282,125,'$'+str(Equity4))
                c.drawString(332,125,'$'+str(Equity5))
                c.drawString(382,125,'$'+str(Equity10))
                c.drawString(432,125,'$'+str(Equity15))
                c.drawString(482,125,'$'+str(Equity20))
                c.drawString(532,125,'$'+str(Equity30))

                c.drawString(132,85,'$'+Monthly_Mortgage)
                c.drawString(182,85,'$'+Monthly_Mortgage)
                c.drawString(232,85,'$'+Monthly_Mortgage)
                c.drawString(282,85,'$'+Monthly_Mortgage)
                c.drawString(332,85,'$'+Monthly_Mortgage)
                c.drawString(382,85,'$'+Monthly_Mortgage)
                c.drawString(432,85,'$'+Monthly_Mortgage)
                c.drawString(482,85,'$'+Monthly_Mortgage)
                c.drawString(532,85,'$'+"0")

                c.drawString(132,65,'$'+str(NOI1))
                c.drawString(182,65,'$'+str(NOI2))
                c.drawString(232,65,'$'+str(NOI3))
                c.drawString(282,65,'$'+str(NOI4))
                c.drawString(332,65,'$'+str(NOI5))
                c.drawString(382,65,'$'+str(NOI10))
                c.drawString(432,65,'$'+str(NOI15))
                c.drawString(482,65,'$'+str(NOI20))
                c.drawString(532,65,'$'+str(NOI30))

                c.drawString(132,45,'$'+str(Profit1))
                c.drawString(182,45,'$'+str(Profit2))
                c.drawString(232,45,'$'+str(Profit3))
                c.drawString(282,45,'$'+str(Profit4))
                c.drawString(332,45,'$'+str(Profit5))
                c.drawString(382,45,'$'+str(Profit10))
                c.drawString(432,45,'$'+str(Profit15))
                c.drawString(482,45,'$'+str(Profit20))
                c.drawString(532,45,'$'+str(Profit30))
                
                #rgb values R/256 G/256 B/256
                #c.setFillColorRGB(0,0,0.5)
                #c.rect(0,790,600,50, fill=1)
                #c.setFillColorRGB(0,0,0.5)
                #c.rect(0,0,600,20, fill=1)

                c.setFillColorRGB(0,0,0)
                c.drawString(520,25,Date)
                
                
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #Titles
                c.setFillColorRGB(0,0,0)
                c.setFont("Courier", 45)
                c.drawString(20,790,'IPF'+'-'+i+'-'+x)
                c.setFillColorRGB(0,0,0)
                c.setFont("Courier", 14)
                #c.drawString(23,345,"Acquisition")
                #c.drawString(218,585,"Ongoing Costs")
                c.drawString(14,185,"30 Year Overview")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            def IPF1(c):
                #Images
                #c.drawImage('Map_Idaho.png', 10, 360, width=150, height=260)
                #c.drawImage('Map_Side.png', 70, 560, width=90, height=50)
                #c.drawImage('Yearly_Overview.png', 350, 415, width=250, height=190)

                c.setFillColorRGB(0.82,0.82,0.82)
                c.rect(10,750,365,20, fill=1)

                c.setFillColorRGB(0,0,0)
                c.setFont("Courier", 14)
                c.drawString(14,755,"Amortization Schedule")
                c.drawImage('amortization_schedule.png', 12, 530, width=325, height=190)


            
                #Horizontal
                c.line(10, 770, 375, 770)
                c.line(10, 670, 375, 670)

                #Vertical
                c.line(10, 770, 10, 670)
                c.line(375, 770, 375, 670)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                c.setFillColorRGB(0,0,0)
                c.drawString(520,25,Date)              
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #Titles
                c.setFillColorRGB(0,0,0)
                c.setFont("Courier", 45)
                c.drawString(20,790,'IPF'+'-'+i+'-'+x)
                c.setFillColorRGB(0,0,0)
                c.setFont("Courier", 14)
                
                
            c = canvas.Canvas('IPF'+ i + '-'+ x +'.pdf')
            IPF(c)
            c.showPage()
            IPF1(c)
            c.showPage()
            c.save()
            import os
            #os.remove('Yearly_Overview.png')
            os.remove('amortization_schedule.png')
            print("##########FOUND##########FOUND##########FOUND##########FOUND##########")
print("Done")


'''                #Tenant Overview
                c.setFont("Courier", 14)
                c.drawString(304,455,"Tenant Data")
                c.setFont("Courier", 12)
                c.drawString(304,435,"Age")
                c.drawString(304,415,"Marital Status")
                c.drawString(304,395,"Income")
                c.drawString(304,375,"Affordable Rent")
                c.drawString(304,355,"Market Rent")
                
                
                c.line(300, 470, 580, 470)
                c.line(300, 450, 580, 450)
                c.line(300, 430, 580, 430)
                c.line(300, 410, 580, 410)
                c.line(300, 390, 580, 390)
                c.line(300, 370, 580, 370)
                c.line(300, 350, 580, 350)
                
                
                c.line(580, 470, 580, 350)
                c.line(300, 470, 300, 350)
                '''
'''
                c.setFont("Courier", 12)
                c.drawString(22,755,Address)
                c.drawString(22,735,'$'+Property_Listing_Cost)
                c.drawString(22,715, Bedroom+' Bedroom(s)'+' & '+Bath+' Bathroom(s)')
                c.drawString(22,695,'Total Square Footage '+Square_Feet)
                c.drawString(22,675,'Lot Size '+Lot_Size)
                '''
'''    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Yearly_Overview = np.array([Yearly_Mortgage, HOA_Yearly, Insurance_Yearly, Property_Taxes, Capital_Expenditures, Vacancy, Maintenance])
            mylabels = ["Mortgage", "HOA", "Insurance", "Property Taxes", "Capital Expenditures", "Vacency", "Maintenace"]

            mycolors = ["DeepSkyBlue", "DodgerBlue", "CornflowerBlue", "Blue", "royalblue", "mediumturquoise", "turquoise"]

            def absolute_value(val):
                a = np.round(val/100.*Yearly_Overview.sum(), 0)
                return a

            plt.pie(Yearly_Overview, labels = mylabels, colors = mycolors, autopct=absolute_value)
            plt.savefig("Yearly_Overview.png")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            def amortization_schedule(principal, interest_rate, monthly_payment, months):
                balance = principal
                interest_paid = 0
                principal_paid = 0
                amortization = []
                equity = []
                
                for month in range(1, months+1):
                    interest = balance * (interest_rate / 12)
                    interest_paid += interest
                    principal_paid = monthly_payment - interest
                    balance -= principal_paid
                    equity_value = principal - balance
                    amortization.append(balance)
                    equity.append(equity_value)
                    
                return amortization, equity
        
            principal = Property_After_Down
            interest_rate = Mortgage_Rate
            monthly_payment = Monthly_Mortgage
            months = Term_of_Loan_Years * 12


            amortization, equity = amortization_schedule(principal, interest_rate, monthly_payment, months)

            # Group data into 12-month intervals
            amortization_12 = np.add.reduceat(amortization, np.arange(0, len(amortization), 12))
            equity_12 = np.add.reduceat(equity, np.arange(0, len(equity), 12))

            # Create bar chart
            fig, ax = plt.subplots()
            ax.bar(np.arange(1, len(amortization)+1), amortization, width=0.4, label='Balance')
            ax.bar(np.arange(1, len(equity)+1), equity, width=0.4, label='Equity')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount ($)')
            ax.set_title('Amortization Schedule')
            ax.legend() 
            plt.savefig('amortization_schedule.png', bbox_inches='tight')
'''
'''def amortization_schedule(principal, interest_rate, monthly_payment, months):
            balance = principal
            interest_paid = 0
            principal_paid = 0
            amortization = []
            equity = []
            
            for month in range(1, months+1):
                interest = balance * (interest_rate / 12)
                interest_paid += interest
                principal_paid = monthly_payment - interest
                balance -= principal_paid
                equity_value = principal - balance
                amortization.append(balance)
                equity.append(equity_value)
                
            return amortization, equity
    
        principal = Property_After_Down
        interest_rate = Mortgage_Rate
        monthly_payment = Monthly_Mortgage
        months = Term_of_Loan_Years * 12


        amortization, equity = amortization_schedule(principal, interest_rate, monthly_payment, months)

        # Group data into 12-month intervals
        amortization_12 = np.add.reduceat(amortization, np.arange(0, len(amortization), 12))
        equity_12 = np.add.reduceat(equity, np.arange(0, len(equity), 12))

        # Create bar chart
        fig, ax = plt.subplots()
        ax.bar(np.arange(1, len(amortization)+1), amortization, width=0.4, label='Balance')
        ax.bar(np.arange(1, len(equity)+1), equity, width=0.4, label='Equity')
        ax.set_xlabel('Month')
        ax.set_ylabel('Amount ($)')
        ax.set_title('Amortization Schedule')
        ax.legend() 
        plt.savefig('amortization_schedule.png', bbox_inches='tight')
'''
'''
            #Ongoing
            #Vertival Lines - Ongoing
            c.line(215, 580, 215, 440)
            c.line(360, 580, 360, 440)
            c.line(410, 580, 410, 440)
            c.line(530, 580, 530, 440)
            #^vertical>Down Horizontal
            c.line(215, 440, 530, 440)
            c.line(215, 460, 530, 460)
            c.line(215, 480, 530, 480)
            c.line(215, 500, 530, 500)
            c.line(215, 520, 530, 520)
            c.line(215, 540, 530, 540)
            c.line(215, 560, 530, 560)
            c.line(215, 580, 530, 580)
            c.drawString(218,445,"Property Management")
            c.drawString(218,465,"HOA")
            c.drawString(218,485,"Vacancy")
            c.drawString(218,505,"Property Taxes")
            c.drawString(218,525,"Bills/Utility")
            c.drawString(218,545,"Insurance")
            c.drawString(218,565,"Mortgage")
            c.drawString(362,565, Monthly_Mortgage)
'''
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Aquizition
            c.drawString(22,220,"Total Cost")
            c.drawString(22,240,"*Remodel")
            c.drawString(22,260,"*Earnest Money")
            c.drawString(22,280,"Down Payment")
            c.drawString(22,300,"Escrow")
            c.drawString(22,320,"Closing Cost")
            c.line(20, 215, 205, 215)
            c.line(20, 235, 205, 235)
            c.line(20, 255, 205, 255)
            c.line(20, 275, 205, 275)
            c.line(20, 295, 205, 295)
            c.line(20, 315, 205, 315)
            c.line(20, 335, 205, 335)
'''
