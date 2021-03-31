
import cPickle as pickle    # cPickle is 1000 times faster than pickle. Also, cPickle does not store data in ASCII format while pickle does.
import os
import random
import math

class bank:
    def __init__(self):
        self.s_b_a=20       # Default Value for Business Loan Interest
        self.pers_loan=30   # Default Value for Personal Loan Interest
        self.debit_card=2000    #Default Value for Maximum value that can be withdrawn at a time
    def bank_details(self): # Function to input bank pre-requisits - For Administrator
        self.s_b_a=input('Enter the INTEREST for Business loan =')
        self.pers_loan=input('Enter the INTEREST for Personal loan =')
        self.debit_card=input('Enter the MAXIMUM amount that be withdrawn per day =')
class customer(bank):
    def __init__(self):
        self.cust_id=1
        self.cust_name=''
        self.cust_balance=0
        self.cust_dep=0
        self.cust_withdraw=0
        self.cust_transfer=0
        self.cust_loan=0
        self.cust_debit=[None,None]
    def customer_details(self,j):   # Method to input/modify customer details
        if j==0:    #j=0 implies user is entering details while registrering
            self.cust_id=random.randint(100000,1000000)
            while True:
                self.cust_name=raw_input('Enter the customer name -')
                if self.cust_name.isalpha():
                    break
                else:
                    print self.cust_name, "is not a name!"
                    print "Please enter a valid name!"
            self.cust_email=raw_input('Enter the customer email-id =')
            print'Your ID is -',self.cust_id
        if j==1:    #j=1 implies user is modifying details after registrering
            while True:
                self.cust_name=raw_input('Enter the customer name -')
                if self.cust_name.isalpha():
                    break
                else:
                    print self.cust_name, "is not a name!"
                    print "Please enter a valid name!"
            self.cust_email=raw_input('Enter the customer email =')
    def customer_deposit(self):     # Method to deposit money in bank account
        amt=input('Enter the amount to be deposited (without commas)=')
        self.balance+=amt
    def customer_withdraw(self):    # Method to withdraw money from bank account
        amt=input('Enter the amount to be withdrawn (without commas)=')
        if self.balance<amt:
            print "Insuffecient Balance !"
        else:
            self.balance-=amt
    def customer_transfer(self,account2):   # Method to transfer money
        amt=input('Enter the amount to be transfered =')
        if self.balance<amt:
            print "Insuffecient Balance !"
        else:
            self.balance-=amt

b=bank()    # Creating object for class bank
def main(): 
    print '''
              WELCOME TO OOHS BANK!
    Welcome to OOHS Bank's banking services.
We are your one-stop solution to all your banking needs.

    '''
    print
    k=1
    while k==1:
        print'\t\t________MAIN MENU________'
        print'\t\tAdministrator-->1'
        print'\t\tCustomer------->2'
        print'\t\tExit----------->3'
        print
        choice=input('Please enter your choice =')
        if choice==1:
            print'\t\tLog in-->1'
            print'\t\tReturn to main menu-->2'
            print
            choice1=input('Please enter your choice =')
            if choice1==1:
                password=input('Please enter your 6-Digit ID =')
                while True:
                    if password==123456789:     # Password for admininstrator is 123456789
                        print
                        print
                        print
                        print'\t\tEnter the bank pre-requisits-->1'
                        print'\t\tView transaction history-->2'
                        print'\t\tLog out-->3'
                        print
                        choice2=input('Please enter your choice =')
                        if choice2==1:
                            global b
                            b=bank()    #another local object created for class bank
                            b.bank_details()    # Allows administrator to enter bank pre-requisits
                            dict_bank=dict()
                            dict_bank[123456789]=[b.s_b_a,b.pers_loan,b.debit_card]# Dictionary is made with key 123456789(administrator password) and value is a list of Business Loan Interest, Personal Loan Interest, and Max. amount that can be withdrawn at a time 
                            try:
                                f=open("bankdetails0.dat","rb")     #bankdetails0.dat is a file containing dictionary with default values of bank pre-requisits
                                m=pickle.load(f)
                                f.close()
                                m.update(dict_bank)     # Updating bank pre-requisits values in dictionary
                                f=open("bankdetails0.dat","wb")
                                pickle.dump(m,f)
                                f.close()
                            except:     
                                f=open("bankdetails0.dat","wb")
                                pickle.dump(dict_bank,f)    # If there are no values entered, dictionary 'dict_bank' will be overwritten
                                f.close()
                        elif choice2==2 and os.path.isfile('transaction.txt')==True:    # transaction.txt - text file containing all bank transactions which took place
                            trans=open("transaction.txt","r")
                            print
                            print"TRANSACTIONS DETAILS.........."
                            print
                            transread=trans.readlines()     # Reads text file line by line
                            try:
                                for i in transread:     # i is each character in string transread of lines
                                    r=i
                                    o=list()  # Empty list created
                                    o.append(r)    # list element value changed to string r
                                    
                                    for j in o: #takes string value r
                                        h=j.split('#')
                                        for c in h:
                                            if c[1]=='D' or c[1]=='d':
                                                print
                                                print
                                                '_________________________________________________________________'
                                            print c
                            except IndexError:
                                pass
                            print
                            trans.close()
                        elif choice2==3:
                            break
                        else:
                            print'Your request could not be satisfied. Please check the following and try once again!'
                            print "1. Check if the range if the choice entered is 1-3"
                            print "2. Make sure if any bank transaction has taken place"
                            print "\n\n"
                    else:
                        print'Wrong Administrator Password!'
                        password=input('Please enter your 6-Digit ID =')
            elif choice1==2:
                pass
            else:
                print "Invalid Choice! Please try again!"
        elif choice==2: # For customer
            print
            print'\t\tLogin-->1'
            print'\t\tRegister--2>'
            print'\t\tReturn to main menu-->3'
            print
            choice3=input('Please enter your choice =')
            if choice3==1 and os.path.isfile('customer0.dat')==True:    # customer0.dat - file which has customer id, name and email dumped into it
                f=open("customer0.dat","rb")
                detail=pickle.load(f)
                f.close()
                id1=input('Please enter your 6-Digit ID =')
                print
                q=1
                while q==1:
                    if detail.has_key(id1)==True:   # To check is bank account with user entered id exists
                        status=1
                        print
                        print
                        print'\t\t__________________________MENU________________________________'
                        print'\t\tMODIFY ACCOUNT DETAILS -->1'
                        print'\t\tSEARCH ACCOUNT DETAILS -->2'
                        print'\t\tDELETE ACCOUNT DETAILS -->3'
                        print'\t\tTRANSFER MONEY -->4'
                        print'\t\tDEPOSIT MONEY -->5'
                        print'\t\tWITHDRAW MONEY -->6'
                        print'\t\tTAKE LOAN -->7'
                        print'\t\tISSUE CREDIT CARD -->8'
                        print'\t\tLOG OUT -->9'
                        print
                        choice4=input('Please enter your choice =')
                        print
                        q=1
                        if choice4==1:
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            global p
                            p=customer()    # Local object for class customer created
                            p.customer_details(1)   # Customer enters details. Argument '1' refers to modifying details after creating account
                            dict1[id1]=[p.cust_name,p.cust_email,p.cust_balance,p.cust_dep,p.cust_withdraw,p.cust_loan,p.cust_debit] # Dictionary with user details created
                            f=open("customer0.dat","wb")
                            pickle.dump(dict1,f)
                            f.close()
                            print
                            print'======YOUR DEATILS HAS BEEN MODIFIED======='
                            print
                        elif choice4==2:
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            print'\t====DETAILS===='
                            print'ID=',id1
                            print'Name-->',dict1[id1][0]
                            print'E-mail-->',dict1[id1][1]
                            print'Balance-->',dict1[id1][2]
                            print'Pending loan-->',dict1[id1][5]
                            print'Credit card number-->',dict1[id1][6][0],'Pincode-->',dict1[id1][6][1]
                            print
                        elif choice4==3:
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            f=open("customer0.dat","wb")
                            del dict1[id1]  # Deletes dictionary key with paarticular user's details
                            pickle.dump(dict1,f)
                            f.close()
                            print'========YOUR ACCOUNT HAS BEEN SUCCESSFULLY DELETED========'
                        elif choice4==4:
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            id2=input('Enter the account to which money has to be transferred =')
                            if dict1.has_key(id2)==True:    # Check is the other account exists
                                transfer=input('Enter the amount needed to be transferred =')
                                if dict1[id1][2]>=transfer:
                                    dict1[id2][2]+=transfer
                                    dict1[id1][2]-=transfer
                                    print'========MONEY HAS BEEN TRANSFERRED========'
                                    ft=open("transaction.txt","a")
                                    lt=range(3)
                                    lt[0]='Transferrer\'s ID-'+str(id1)+'#' # Enters transferers ID into file transaction.txt
                                    lt[1]='Reciever\'s ID-'+str(id2)+'#'    # Enters recievers ID into file transaction.txt
                                    lt[2]='Money transfered-'+str(transfer)+'$$'    # Enters amount transfered into file transaction.txt
                                    ft.writelines(lt)
                                    ft.close()
                                    print'==================RECIEPT=========================='
                                    print'ID OF TRANSFERRER -',id1
                                    print'ID OF RECIEVER -',id2
                                    print'NAME OF TRANSFERRER -',dict1[id1][0]
                                    print'NAME OF RECIEVER -',dict1[id2][0]
                                    print'AMOUNT TRANSFERRED =',transfer
                                    print'ACCOUNT BALANCE OF TRANSFERRER =',dict1[id1][2]
                                    print
                                    f=open("customer0.dat","wb")
                                    pickle.dump(dict1,f)    # Updates original dictionary
                                    f.close()
                                else:
                                    print'INSUFFICIENT BALANCE'
                            else:
                                print'THE ACCOUNT DOESNT EXIST'
                                f=open("customer0.dat","wb")
                                pickle.dump(dict1,f)    # overwites already existing data
                                f.close()
                            print
                        elif choice4==5:
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            dep=input('Enter the amount to be deposited =')
                            ft=open("transaction.txt","a")
                            lt=range(2) # Creates list
                            lt[0]='id-'+str(id1)+'#'    # Changes 1ist element 1(index=0) to 'id-ID#'
                            lt[1]='Amount deposited-'+str(dep)+'$'  # Changes 1ist element 2(index=1) to 'Amount deposited-AMOUNT$'
                            ft.writelines(lt)   # Updates file 'transaction.txt'
                            ft.close()
                            dict1[id1][2]+=dep    # Updates account balance in original dictionary
                            print
                            print'\t-THE AMOUNT HAS BEEN DEPOSITED-'
                            print'\t==========RECIEPT============'
                            print'\tID ==============>',id1
                            print'\tNAME ============>',dict1[id1][0]
                            print'\tAMOUNT BALANCE ==>',dict1[id1][2]
                            print
                            f=open("customer0.dat","wb")
                            pickle.dump(dict1,f)    # Updates original dictionary
                            f.close()
                            print
                        elif choice4==6:
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            withdraw=input('Enter the amount needed to be withdrawn =')
                            if withdraw<=dict1[id1][2] and withdraw<=b.debit_card:                                              
                                ft=open("transaction.txt","a")
                                lt=range(2) # Creates list
                                lt[0]='id-'+str(id1)+'#'    # Changes 1ist element 1(index=0) to 'id-ID#'
                                lt[1]='Amount withdrawn='+str(withdraw)+'$$'    # Changes 1ist element 2(index=1) to 'Amount deposited-AMOUNT$'
                                ft.writelines(lt)   # Updates file 'transaction.txt'
                                ft.close()
                                dict1[id1][2]-=withdraw    # Updates account balance in original dictionary
                                print'\t-------MONEY WITHDRAWN-------'
                                print'\t==========RECIEPT============'
                                print'\tID-->',id1
                                print'\tNAME-->',dict1[id1][0]
                                print'\tAMOUNT BALANCE OF TRANSFERRER-->',dict1[id1][2]
                                print
                                f=open("customer0.dat","wb")
                                pickle.dump(dict1,f)    # Updates original dictionary
                                f.close()
                                print
                        
                            else:   # clause in case error while withdrawing money occurs
                                print 'Withdrawal of amount', withdraw, "could not be possible. Please check the following and try again:- "
                                print "1. Check if withdrawal amount not is greater than account balance"
                                print "2. Check if withdrawal amount not is greater than maximum withdrawal amount at a time (if you don't know the  maximum withdrawal amount at a time, please ask an administrator)"
                            print
                        elif choice4==7:    # Loan
                            f1=open("bankdetails0.dat","wb")
                            try:
                                
                                bank1=pickle.load(f1)
                            except:
                                f1.close()
                            print
                            print'\t\t________________________LOAN MENU_______________________________'
                            print'\t\tBusiness Loan-->1'
                            print'\t\tPersonal Loan-->2'
                            print
                            choice5=input('Please enter your choice =')
                            if choice5==1:
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                f.close()
                                print
                                tem=b.s_b_a     # b.s_b_a is loan interest for Business Loans
                                
                                print'Interest will be compounded yearly at',tem,'rate.'
                                
                                print'Per annum for a minimum time period of one year .Do you agreee.(y/n)'
                                choice66=raw_input('Please enter your choice =')
                                print
                                if choice66.lower()=='y':
                                    amount=input("Enter the amount =")  # amount refers the Principle Amount P
                                    time=input('Enter the time period(IN YEARS) =')     # time refers the Time Period T
                                    print'YOUR LOAN HAS BEEN GRANTED'
                                    print
                                    print'Amount to be repaid =',(amount)+(amount*(float(b.s_b_a)/100)**(time))     # Compound Interest Formula
                                    dict1[id1][5]+=(amount)+(amount*(float((b.s_b_a))/100)**(time))     # Updates account balance in original dictionary
                                    ft=open("transaction0.dat","a")
                                    lt=range(3) # Creates List  
                                    lt[0]='id-'+str(id1)+'#'    # Changes 1ist element 1(index=0) to 'id-ID#'
                                    lt[0]='Type of loan - SMALL BUSINESS LOAN'+'$$'         # Changes 1ist element 2(index=1) to 'Type of loan - SMALL BUSINESS LOAN$$'
                                    ft.writelines(lt[0])
                                    ft.close()
                                    f=open("customer0.dat","wb")
                                    pickle.dump(dict1,f)    # Updates original dictionary
                                    f.close()
                                elif choice66.lower()=='n':
                                    print "Loan Request Cancelled Successfully!"
                                else:
                                    print 'Wrong Input'
                            elif choice5==2:
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                f.close()
                                print
                                tem=b.pers_loan # b.pers_loan is loan interest for Business Loans
                                print'Interest will be compounded quarterly at',tem,'% rate.'
                                print'Per annum for a minimum time period of one year .Do you agreee.(y/n)'
                                choice66=raw_input('Please enter your choice =')
                                print
                                if choice66.lower()=='y':
                                    amount=input('Enter the amount to be borrowed =')   # amount refers the Principle Amount P
                                    time=input('Enter the time (IN YEARS)=')    # time refers the Time Period T
                                    print'YOUR LOAN HAS BEEN GRANTED'
                                    print
                                    print'Amount to be repaid =',(amount)+(amount*(float((b.pers_loan))/100)**(time))   # Compound Interest Formula
                                    dict1[id1][5]+=(amount)+(amount*(float((b.pers_loan))/100)**(time)) # Updates account balance in original dictionary
                                    ft=open("transaction0.dat","a")
                                    lt=range(3)
                                    lt[0]='id-'+str(id1)+'#'    # Changes 1ist element 1(index=0) to 'id-ID#'
                                    lt[0]='Type of loan - PERSONAL LOAN'+'$$'   # Changes 1ist element 2(index=1) to 'Type of loan - PERSONAL LOAN$$'
                                    ft.writelines(lt[0])
                                    ft.close()
                                    f=open("customer0.dat","wb")
                                    pickle.dump(dict1,f)    # Updates original dictionary
                                    f.close()
                                elif choice66.lower()=='n':
                                    print "Loan Request Cancelled Successfully!"
                                else:
                                    print 'Wrong choice'
                            else:
                                print 'Wrong choice'

                        elif choice4==8:    # For issuing credit card
                            f=open("customer0.dat","rb")
                            try:
                                dict1=pickle.load(f)
                            except EOFError:
                                f.close()
                            
                            print "TERMS AND CONDITIONS:-"
                            print   # Printing terms and conditions
                            print """   
                        TERMS AND CONDIDTIONS
                        
You need to read this document and accept the terms and conditions hereto. It sets out specific terms and conditions on which we agree to provide you with credit card
products. You must read it in conjunction with our Customer Terms, the product brochure and any other documents forming our banking agreement included in your Welcome Pack.
The Welcome Pack forms an integral part of this document. To the extent of any inconsistency between the terms set hereunder and our Customer Terms, these terms prevail.

Definitions:-
Defined Words printed in italics and defined words used in our banking agreement shall have the meaning ascribed to them in our Customer Terms unless otherwise defined
herein. Some additional defined words which apply to the products referred to in these terms and conditions hereunder shall have the same meaning ascribed to them at the end
of this document.

1. Choosing the product that is right for you.
We offer a variety of credit card products designed to suit your personal banking needs which you have discussed with us. The particular types of credit cards we offer are set
out in the product brochures. If you need us to explain any of the features of, or the terms applying to, any credit cards, please contact us and we will be happy to give you all the
information that you may need.

2. The credit cards

Issue of credit cards
2.1 We may issue a credit card to you and, if you ask, to each supplementary cardholder.

Collection
2.2 We send the credit card (and any replacement credit card) to your address last notified to us unless you notify us in writing that you want to collect the credit
card from us.

Activation procedures
2.3 Each cardholder must comply with any activation procedures notified from time to time.

Using the credit card
The terms of our banking agreement apply to each use of a credit card. If a cardholder does not agree with those terms, they should not sign the credit card or carry out any transaction.

2.4 You accept the terms of our banking agreement when you first use the credit card.

2.5 You must ensure that only you are using the credit card. Any supplement cards issued for other eligible persons shall be used at your sole liability and will be deemed, if used by such persons, as if used by you personally.
Supplementary cards

2.6 We send any supplementary cards, their PINs/password and all communications relating to them to you.

2.7 Any communication we give to you on any supplementary cardholder shall be delivered to you.

2.8 You shall procure that each supplementary cardholder agree to be bound by the instructions that any of you give us.

Co-brand cards
2.9 We may convert a co-brand card to another type of credit card at our discretion.

2.10 We are not liable for any representations, promotions or obligations made by a business alliance partner.

3. Credit limit
3.1 We notify you of the credit limit when your application has been approved. We may vary the credit limit at any time.

3.2 The credit limit is an overall limit that applies to all credit cards issued to you.

3.3 The credit limit is also dependant on the prevailing local regulations.

Exceeding your credit limit
3.4 It is your responsibility to ensure that the credit limit is not exceeded.

3.5 In calculating whether the credit limit has been exceeded, we may take into account:
• any transaction made usig the credit card but which has not been debited from the account for a credit card; and
• any authorisation we have given to a third party in connection with a proposed transaction using the credit card.

Credit limit exceeded
3.6 If you exceed the credit limit or any temporary credit limit extension has expired, you must immediately pay us that part of the balance owing for the account for
the credit card which exceeds the credit limit in addition to any payment we require.

4. Cash advance
How to obtain a cash advance:
The Cardholder may obtain Cash Advance subject to availability of adequate credit and as may be acceptable to the Bank from time to time at it’s absolute discretion by
the following means

4.1 You may obtain a cash advance using your credit card at one of our branches, other financial institutions displaying the logo of a card association and any
OOHS BANK.

Maximum limit on cash advance
4.2 A cash advance is only available up to the maximum amount the person providing the advance permits. For details of the maximum amount we permit contact us.

5. Balance transfer
5.1 If you ask, we may permit a balance transfer subject to any conditions we specify.

5.2 You should continue to make any required payments to the account from which you transfer a balance until we confirm that the account has been credited. We are not liable for any overdue payment or interest incurred relating to the
account from which you transfer a balance.

5.3 Any payment made on your account for the credit card will first be applied to reduce the balance transfer before any other balance owing.

6. Interest, fees and charges

6.1 Interest, fees and charges (including finance charges, cash advance fees, overlimit fees, annual fees and administrative fees) are set out in the Service & Price Guide.

6.2 Unless otherwise specified, interest is calculated on the basis of a 360 day year and compounded on monthly basis or such other basis we choose.

6.3 Interest is charged until the date the balance owing is paid in full.

6.4 You must pay all costs such as debt collection fees we incur in connection with the credit card on demand.

7. Liability

General
7.1 You are liable for:
• any failure by any cardholder to comply with the terms of our banking agreement;
• all transactions made using a credit card (except for disputed transactions);
• the balance owing for the account for a credit card (including all amounts debited and credited to the account for the credit card by any supplementary cardholder); and
• any transactions where we could otherwise have exercised chargeback rights if you do not notify us of the transactions and provide any further documents or information we require within the time periods required.

Disputes between you and supplementary cardholders
7.2 Our rights and obligations relating to you and each supplementary cardholder are not affected by any dispute or claim you and the supplementary cardholder may have against each other.
Purchase of goods or services

7.3 We are not liable for:
• Any payment terms by instalments or otherwise on the account of the credit card or any other payment arrangement you conclude with third parties with the credit card;
• the refusal of any merchant, financial institution or other person to accept the credit card; and
• any defect or deficiency in goods or services supplied to you by any merchant, financial institution or other person.
You must solely resolve any complaint against any merchant, financial institution or other person without any involvement from us and no claim against any of them may be set off against us.

Additional services offered with credit cards
7.4 Some types of credit cards give you access to services provided and paid for by third parties. For example, if you hold a Visa Gold Card or Visa Platinum Card you may have access to the International Emergency Assistance Service. You are liable for the cost of any medical, legal or other services provided under
these third party services. You acknowledge that the third party service providers do their best to provide the services to cardholders and that the services may not always be available (for example, because of time, distance
or location). Neither we nor the third party service provider or Visa International Service Association is liable to you for any loss in connection with any service
or its unavailability.

7.5 We are also not liable to holders of a credit card with access to Emergency Cash Withdrawal (if available) for any loss they suffer if we are unable to give immediate effect to an Emergency Cash Withdrawal, replacement card or any
other facilities we offer in connection with the credit card. The Customer Terms include additional provisions relating to your liability to us and exclusions or limits on our liability. See, for example, “You indemnify us”
and “Exclusion of liability”.

8. Additional services for your account
8.1 We may offer additional services for your account. These may include reward programmes, balance transfer schemes, payment arrangements, card protection and any other services which you can find out more about by
contacting us at one of our branches or by using phone banking or as we advise you from time to time.

8.2 If you sign up for additional services, you are bound by the terms of the additional services. To the extent of any inconsistency between the terms of the additional services and our banking agreement, our banking agreement
prevails unless the terms of the additional services specify otherwise.

8.3 For details of any bonus point scheme applying to the credit card, please refer to our banking agreement or contact us.

9. Payments

Payment by due date
9.1 On or before the due date set out in the statement we issue for your credit card, you must pay at least the minimum payment due as set out in the statement.
9.2 Your liability to us remains even if, for any reason, you do not receive your periodic statement.
9.3 If an amount is due on a day which is not a banking day, you must pay it on the next banking day.

Calculation of minimum payment
9.4 We calculate the minimum payment in accordance with our usual practice. Please refer to your statement or contact us for further information.

Currency of transactions
9.5 If any transaction made using the credit card is not denominated in the currency of Qatar, we convert the amount of the transaction to the currency of Qatar in accordance with our usual practice and our banking agreement.

How we apply payments
9.6 We may (but need not) apply payments we receive to pay:
• fees, charges, cash advances, interest and other charges shown on the previous statement; then
• fees, charges, cash advances, interest and other charges interest shown on the current statement; then
• any unpaid transactions shown on the previous statement; then
• any unpaid transactions shown on the current statement; then
• fees, charges, cash advances, interest, other charges and other transactions on the account not shown on the current statement.

What happens if you do not pay
9.7 If we do not receive the balance owing for the account for a credit card on or before the due date we may charge and debit from the account for a credit card finance charges as set out in the Service & price Guide or elsewhere in our
banking agreement.

9.8 If we do not receive the minimum payment on or before the due date, then:
• you must pay a late payment charge as set out in the Service & price Guide or elsewhere in our banking agreement;
• you must not use the credit card until the minimum payment has been paid;
• we may suspend your use of the credit card.

Payment in full if we ask
9.9 Despite any other term of our banking agreement, at any time we may demand immediate payment of the total amount of the balance owing for the account for a credit card plus interest and fees.
Refunds to the credit card account

9.10 We only credit a refund to the account for a credit card in connection with:
• a transaction made with the credit card; or
• a payment to the account for the credit card; or
• any other credit owing to you, when we receive the amount to be credited in Qatar and in accordance with our usual practice.

Statement
9.11 If you think there is an error on your statement you must notify us in writing with details of the error within 30 days after the date of the statement. If you do not
do so, we treat the statement as correct.

10. Cancellation and termination

How to terminate
10.1 At any time we may choose to:
• cancel or suspend your right to use the credit card or end the account for a credit card;
• refuse to authorise any transaction for which you want to use the credit card; and
• refuse to re-issue, renew or replace the credit card, without giving you any notice or reason.
10.2 At any time, you may end the account for a credit card by notifying us in writing.

What happens if the account is terminated
10.3 If you or we end the account for a credit card, you must:
• cut the credit card in half; and
• immediately pay the balance owing for the account for the credit card together with any other amounts owing in connection with credit card transactions which have been made before termination but which have not actually been
debited to the account for the credit card.

Termination of use of supplementary credit card by cardholder
10.4 Either you or a supplementary cardholder may end the use of a supplementary credit card by:
• notifying us in writing; and
• cutting the card in half.

11. Variation
11.1 If you are not comfortable with any changes we make to our banking agreement, you may terminate the account for a credit card in accordance with the procedure in clause 10.

11.2 If we notify you of any changes to our banking agreement in accordance with any applicable law and you keep or use the credit card, the account for the credit card or the PIN/password, you will be deemed to have agreed to the
changes.

12. Suspicious transactions
We may not honour suspicious transactions (and need not notify you if this is the case).

13. Payment Protection Insurance
13.1 Application: This Clause shall apply if you have indicated in the Application Form that you want Payment Protection Insurance, but not otherwise.

13.2 Acceptance: We have the right to accept or reject your application for Payment

Protection Insurance at our absolute discretion and without providing reasons for our decision.

13.3 Conditions If you enrol for Payment Protection Insurance

13.3.1 Your obligation to pay certain outstanding amounts under the Credit Card shall be deemed to be discharged in certain events (such as your accidental death, total and permanent disablement or terminal illness) and upon certain
additional conditions being met. The terms and conditions relating to your Payment Protection Insurance are set out in the Payment Protection Insurance Terms & Conditions and these form a part of these Credit Card
Terms and Conditions; and

13.3.2 We shall specify in the (Confirmation or Policy Cover Note), the (nonrefundable-assuming regular premium) Payment Protection Insurance premium (or fee) you shall have to pay to us each month.

14. Meaning of words
You also need to refer to our Customer Terms which also define key words used in these terms. If a word defined in these terms is also defined in our Customer Terms, the
definition in these terms applies for the purposes of accounts for the credit cards. balance transfer means a transaction where we debit an amount you specify from your
credit card and pay the amount to another credit card with us or another financial institution. cash advance means cash issued in any currency obtained by using the credit card.
co-brand card means a card issued by us in conjunction with a business alliance partner. credit limit means, for an account for a credit card, the maximum amount you are entitled
to have outstanding on the account for the credit card. our banking agreement means the agreement between you and us formed when we accept an application from you, the terms of which include our Customer Terms and these
terms. supplementary card means, for an account for a credit card, a credit card issued to a person you authorise as a supplementary cardholder on your account for the credit card.
supplementary cardholder means each person to whom we issue a supplementary card.
"""
                            print "\n\n\n"
                            print'Do you agree to the Terms and Conditions(y/n)'
                            c=raw_input('Please enter your choice =')
                            
                            if c=='y':  # For accepting T&C
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                dict1[id1][6][0]=(random.randint(1000,10000))   # Creates Pin code
                                dict1[id1][6][1]=(random.randint(1000,10000))   # Creates credit card no.
                                print "\nWHICH PACKAGE DO YOU WISH TO CHOOSE?\n"
                                print "1. $50,000,000"
                                print "2. $10,000,000"
                                print "3. $1,000,000"
                                print "4. $500,000"
                                print "5. $100,000"
                                print "6. $50,000"
                                while True:
                                    choice99=input("Enter your choice: ")
                                    if choice99>=1 and choice99<=6:
                                        print'\nCREDIT CARD SUCCESSFULLY ISSUED\n'
                                        break
                                    else:
                                        print "Invalid Choice! Please try again!"
                                    
                                print
                                print'Card number-->',dict1[id1][6][0]
                                print'Pin code-->',dict1[id1][6][1]
                                if choice99==1:
                                    print 'Amount--> $50,000,000'
                                elif choice99==2:
                                    print 'Amount--> $10,000,000'
                                elif choice99==3:
                                    print 'Amount--> $1,000,000'
                                elif choice99==4:
                                    print 'Amount--> $500,000'
                                elif choice99==5:
                                    print 'Amount--> $100,000'
                                elif choice99==6:
                                    print 'Amount--> $50,000'
                                ft=open("transaction.txt","a")
                                lt=range(2) # Creates list
                                lt[0]='id-'+str(id1)+'#'    # Changes list element 1(index=0) to 'id-ID$$'
                                lt[1]='Credit card isssued'+'$$'    # Changes list element 2(index=1) to 'Credit card isssued$$'
                                ft.writelines(lt[1])    # Creates transaction record of credit card issue
                                ft.close()
                                f=open("customer0.dat","wb")
                                pickle.dump(dict1,f)    # Updates original dictionary
                                f.close()
                            else:
                                print'SORRY, YOU ARE NOT ELIGIBLE FOR THE CREDIT CARD'
                        elif choice4==9:
                            print
                            print'========YOU HAVE SUCCESSFULLY LOGGED OUT========'
                            print
                            q=2
                        else:
                            print "Invalid Choice! Please try again!"
                    else:
                        print
                        print'Invalid Choice! Please Try Again!'
                        print
                        id1=input('Please enter your 6-Digit ID =')
                        

            elif choice3==2:    # For customer registration
                s=customer()
                s.customer_details(0)   # invokes customer_details of class customer with j=0 which implies details entering for registration (Refer line 26)
                dict_customer=dict()    # Empty distionary created
                dict_customer[s.cust_id]=[s.cust_name,s.cust_email,s.cust_balance,s.cust_dep,s.cust_withdraw,s.cust_loan,s.cust_debit] # Account created
                try:
                    f=open("customer0.dat","rb")
                    m=pickle.load(f)    # Reads default dictionary
                    f.close()
                    m.update(dict_customer)     # Modifies dictionary
                    f=open("customer0.dat","wb")
                    pickle.dump(m,f)    # New dictionary dumped
                    f.close()
                    
                except: # In case there is no file 'customer0.dat' created
                    f=open("customer0.dat","wb")
                    pickle.dump(dict_customer,f)    #New dictionary dumped
                    f.close()
                    
                print'Thank You for registering'
                print
                print
        elif choice==3:
            print'Exiting OOHS Bank..................................'
            print 'Hope you have enjoyed!'
            print 'Feel free to come back! Have a nice day!'
            exit()
        else:
            print "Invalid Choice! Please try again!"
        

main()
