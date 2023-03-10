#PAWAN NIHURE-UCID:30160898, RUTVI BRAHMBHATT  L11-03 Block-11
#ENDG 233 Final Project

class years:
    '''A class used to create years object.'''
    
    def __init__(self, year, population_increase):
        self.year = year
        self.population_increase = population_increase

    def print_all_data(self):
        '''A function that prints the name and code of the school instance'''
        print("Year: {0}, Growth in Population: {1}".format(self.year, self.population_increase))


import numpy as np                          #import numpy and matplotlib respectively
import matplotlib.pyplot as plt

def array_1():
    """returns array for 1st_csv_file.csv file"""
    dataset_1 = np.genfromtxt('1st_csv_file.csv', delimiter = ',', skip_header = True)
    return dataset_1
   
def array_2():
    """returns array for 2nd_csv_file_age_specific_birth_rate.csv file"""
    dataset_2 = np.genfromtxt('2nd_csv_file_age_specific_birth_rate.csv', delimiter = ',', skip_header = True)
    return dataset_2
    
def array_3():
    """returns array for 3rd_csv_file.csv file"""
    dataset_3 = np.genfromtxt('3rd_csv_file.csv', delimiter = ',', skip_header = True)
    return dataset_3

def list_year():
    '''Function that return list of years.'''
    list_1 = ['1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
    return list_1
def list_birth():
    '''Function that returns list of number of births.'''
    list_2 = [62052,64458,63216,60729,59334,56640,55104,54180,51030,52278,50541,50793,49938,50475,51636,51798,52821,55254,57546,58092,60153,59913,59166,58782,57321,57672,57282,57603,55350,57051,56604,55800,54021,56136,58074,57744,59193,64044,64341,62541,63897,61404,61179,58719,57243,10348,59430,59610,58020,59637,57573]
    return list_2
def list_popn_inc():
    '''Function that returns list of number of population increase.'''
    list_3 = [37212,40149,38415,35418,34071,31527,29646,28221,26361,26940,23865,25641,24405,24483,26256,24318,25776,27837,30138,31050,33621,33522,32049,31680,30369,29859,29028,30132,29145,28929,29943,27975,25956,28125,29655,30711,30948,35523,35154,33579,35460,31323,31080,29151,26181,29430,28251,26271,24795,25377,24960]
    return list_3


#main function.
def main():

    print('ENDG 233 FINAL PROJECT')
    print()
    list_of_year = list_year()               
    list_of_total_birth = list_birth()         #call all lists functions and store in respective variables
    list_of_popn_inc = list_popn_inc()
   
    create_dict1 = dict(zip(list_of_year,list_of_popn_inc))           #create a dictionary from list of years and population increase
    create_dict2 = dict(zip(list_of_year,list_of_total_birth))
    print('Dictionary for the Years and respective Birth numbers:')
    print(create_dict2)
    print()
    while True:
        input_year = input( 'Please enter the year:\n') #ask the user to input year
        input_birth = int(input('Please enter the no. of births in the particular year:\n'))
        if input_year in list_of_year:
            if input_birth in list_of_total_birth:                #check whether the inputted data is in the list
                year_1 = input_year                               #store the value for the year in a new variable 
                print("\n***Requested Year Statistics***\n")
                year_popn = years( input_year,create_dict1[input_year])        #assign respective objects to the class
                year_popn.print_all_data()                                     #call the print print_all_data function
                print()
                break
            else:
                print('Please enter the correct total birth number.')       #print an error message if the condition is not satisfied
                continue
        
        else:
            print('Data is not available for the following year. Please re-enter.')          # Display an message if the if condition is not satisfied
            continue            #continue the loop again

    p_year_1=list_of_year.index(year_1)         #index the location of value in the array
    data_1 = array_1()
    data_2 = array_2()                          #call all array functions and store in respective variables
    data_3 = array_3()
    birth_death_ratio = data_1[p_year_1][1] / data_1[p_year_1][2]                                      #calculate birth to death ratio
    print('Total Birth to Death ratio for the year',(input_year),f'is : {birth_death_ratio:.1f}')     #print the calculated value 

    data_2_array =np.array([data_2[p_year_1][1],data_2[p_year_1][2],data_2[p_year_1][3],data_2[p_year_1][4],data_2[p_year_1][5]]) #create an array from the data of sepcific row from the inputted year in data_2 
    data_2_max = data_2_array.max()    #find the maximum value in the array
    data_2_min = data_2_array.min()    #find the maximum value in the array
    data_2_list1 = list(data_2[:,1])   #create a ist from the second column in data_2
    data_2_list2 = list(data_2[:,2])   #create a list from the third column in data_2
    data_2_list3 = list(data_2[:,3])   #create a list from the fourth column in data_2
    data_2_list4 = list(data_2[:,4])   #create a list from the fifth column in data_2
    data_2_list5 = list(data_2[:,5])   #create a list from the sixth column in data_2

    if data_2_max in data_2_list1:
        print('Age category with the highest Age Specific Birth rate : 15-19 years')

    if data_2_max in data_2_list2:
        print('Age category with the highest Age Specific Birth rate : 20-24 years')

    if data_2_max in data_2_list3:                                                  ##check in which columns list does the max value lie 
        print('Age category with the highest Age Specific Birth rate : 25-29 years')    ##print a message accordingly if True

    if data_2_max in data_2_list4:
        print('Age category with the highest Age Specific Birth rate : 30-34 years')

    if data_2_max in data_2_list5:
        print('Age category with the highest Age Specific Birth rate : 35-39 years')

    if data_2_min in data_2_list1:
        print('Age category with the lowest Age Specific Birth rate : 15-19 years')

    if data_2_min in data_2_list2:                                                  ##check in which columns list does the min value lie
        print('Age category with the lowest Age Specific Birth rate : 20-24 years')     ##print a message accordingly if True

    if data_2_min in data_2_list3:
        print('Age category with the lowest Age Specific Birth rate : 25-29 years')

    if data_2_min in data_2_list4:
        print('Age category with the lowest Age Specific Birth rate : 30-34 years')

    if data_2_min in data_2_list5:
        print('Age category with the lowest Age Specific Birth rate : 35-39 years')


    avg_as_birthrate = (data_2[p_year_1][2] + data_2[p_year_1][3]) / 2                 #calculate the average age-specific birth rate
    print('Average Age specific Birth rate at healthy maternal age category(20-29yrs) :',(avg_as_birthrate))      #print the calculated value

    percent_vaccinated = (data_3[p_year_1][2] / 30) * 100                              #calculate the percentage of vaccinated infants
    print ('Percentage of Vaccinated Infant out of 30 : ',(percent_vaccinated),'%')   #print the calculated value


    def first_graph(i):
        '''Function to generate the first output graph'''
        index = list_of_year.index(input_year)     #index the lcation of value in the array
        plt.figure(1)             # #create figure object 1                      
        plt.subplot(4,1,1)        #assign the location for the sub-plot
        x = ['15-19 age','20-24 age','25-29 age','30-34 age','35-39 age']    #create a list to store the points on x-axis
        y1 = [data_2[index][1],data_2[index][2],data_2[index][3],data_2[index][4],data_2[index][5]]  #create a list to store the points in y-axis
        plt.plot(x, y1, '--', color = 'red', label = 'Birth Rate Line')       #use matplotlib to plot the points x and y stored above and also mention the color and design of the sub-plot with its label name
        plt.title('Age Specific Birth rate graph')                           #assign the title to the sub-plot
        plt.ylabel('Average no. of women', fontsize=8)                       #assign the name for y-axis with a suitable font size 
        plt.xlabel('Age groups')                                             #assign the name for x-axis
        plt.xticks(x)                                                        #set the tick locations on x-axis
        plt.legend()                                                         
        
        plt.subplot(4,1,2)                                    #assign location for the sub-plot 
        x = [1970,1995,2020]                                  #create a list for the points on x-axis
        i1 = list_of_year.index('1970')                       #index the particular year from list_of_year
        i2 = list_of_year.index('1995')                       #index the particular year from list_of_year
        i3 = list_of_year.index('2020')                       #index the particular year from list_of_year

        y2 = [data_2[i1][1],data_2[i2][1],data_2[i3][1]]      #create a list for points on y-axis
        plt.plot(x, y2, '--', color = 'blue', label = 'for age 15-19')   #use matplotlib to plot the points x and y stored above and also mention the color and design of the sub-plot with its label name
        plt.ylabel('Average no. of women', fontsize=8)                  #assign the name for y-axis with suitable font size
        plt.xlabel('Years',fontsize=10)                                 #assign the name for x-axis with suitable font size 
        plt.xticks(x)                                                   #set the tick locations on x-axis
        plt.legend()                                                    #assign legend for the plot

        plt.subplot(4,1,3)                                    #assign the location for the sub-plot
        x = [1970,1995,2020]                                  #create a list for the points on x-axis
        y3 = [data_2[i1][3],data_2[i2][3],data_2[i3][3]]      #creaet a list for the points on y-axis
        plt.plot(x, y3, '--', color = 'magenta', label = 'for age 25-29')      #use matplotlib to plot the points x and y stored above and also mention the color and design of the plot with its label name
        plt.ylabel('Average no. of women', fontsize=8)                         #assign the name for y-axis with suitable font size
        plt.xlabel('Years',fontsize=10)                                        #assign the name for x-axis with suitable font size
        plt.xticks(x)                                          #set the tick locations on x-axis
        plt.legend()                                            #assign legend for the plot


        plt.subplot(4,1,4)                                      #assign the location for the sub-plot
        x = [1970,1995,2020]                                    #create a list for the points on x-axis
        y4 = [data_2[i1][5],data_2[i2][5],data_2[i3][5]]        #creaet a list for the points on y-axis
        plt.plot(x, y4, '--', color = 'green', label = 'for age 35-39')    #use matplotlib to plot the points x and y stored above and also mention the color and design of the plot with its label name
        plt.ylabel('Average no. of women', fontsize=8)                     #assign the name for y-axis with suitable font size
        plt.xlabel('Years',fontsize=10)                                    #assign the name for x-axis with suitable font size
        plt.xticks(x)                                                      #set the tick locations on x-axis
        plt.legend()                                                       #assign legend for the plot
     
        plt.tight_layout()                                                 #adjust sub-plot's parameters
        plt.show()                                                         #display the plot

    def second_graph(input_year):
        '''Function to generate second output graph'''
        plt.figure(2)                                            #create figure object 2
        i1 = list_of_year.index(input_year)                      #index the location of value from list_of_year
        x = np.arange(1)                                         #ensure equally spaced array elements
        y1 = [data_1[i1][1],data_1[i1][1],data_1[i1][1]]         #create a list for the points on y-axis for the first graph
        y2 = [data_1[i1][2],data_1[i1][2],data_1[i1][2]]         #create a list for the points on y-axis for the second graph
        y3 = [data_1[i1][3],data_1[i1][3],data_1[i1][3]]         #create a list for the points on y-axis for the second graph
        width = 0.2                                          #store a value for the width
        plt.bar(i1-0.2, y1, width, color = 'cyan')           #use matplotlib to plot the first bar with a sepcific width and color
        plt.bar(i1, y2, width, color = 'orange')             #use matplotlib to plot the second bar with a sepcific width and color
        plt.bar(i1+0.2, y3, width, color = 'blue')           #use matplotlib to plot the third bar with a sepcific width and color
        plt.title('Live Birth Vs Death')                     #assign the plot title
        plt.xticks(x,[input_year])                           #assign the tick locations on x-axis
        plt.xlabel("Year")                                   #assign the name for x-axis
        plt.ylabel("Numbers of babies")                      #assign the name for y-axis
        plt.legend(['Live birth', 'Death', 'Population Growth'])  #assign legend for the plot
        plt.show()                                            #display the plot

    def third_graph(input_year):
        plt.figure(3)                                        #create figure object 3
        x = ['1970','1980','1990','2000','2010','2020']      #create a list for the points on x-aaxis
        i1 = list_of_year.index('1970')                      #index the location of the specific year from list_of_year
        i2 = list_of_year.index('1980')                      #index the location of the specific year from list_of_year
        i3 = list_of_year.index('1990')                      #index the location of the specific year from list_of_year
        i4 = list_of_year.index('2000')                      #index the location of the specific year from list_of_year
        i5 = list_of_year.index('2010')                      #index the location of the specific year from list_of_year
        i6 = list_of_year.index('2020')                      #index the location of the specific year from list_of_year
        
        y1 = [data_3[i1][1],data_3[i2][1],data_3[i3][1],data_3[i4][1],data_3[i5][1],data_3[i6][1]]         #create a list for the points on y-axis
        plt.plot(x, y1, '--g*', label = 'Unvaccinated babies')        #use matplotlib to plot the points x and y stored above and also mention design of the plot with its label name
                
        y2 = [data_3[i1][2],data_3[i2][2],data_3[i3][2],data_3[i4][2],data_3[i5][2],data_3[i6][2]]          #create a second list for the points on y-axis
        plt.plot(x, y2, '--r*', label = 'Vaccinated babies')           #use matplotlib to plot the points x and y stored above and also mention the color and design of the plot with its label name

        plt.title('Unvaccinated Vs Vaccinated babies out of 30')     #assign the title for the plot
        plt.xlabel('Years')                                          #assign the name for x-axis
        plt.ylabel('Number of babies')                               #assign the name for y-axis
        plt.xticks(x)                                                #assign the tick locations on x-axis
        plt.legend()                                                 #assign legend for the plot
        plt.show()                                                   #display the plot

    first_graph(input_year)                           #call the function fist_graph
    second_graph(input_year)                          #call the function second_graph
    third_graph(input_year)                           #call the function third_graph


if __name__ == '__main__':
    main()                                            #call the main function